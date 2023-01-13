import random
import re
from io import BytesIO

from requests import ConnectTimeout
from PIL import Image
from speak_and_listen import speak, listen
from requests_html import HTMLSession


def indentify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "me llaman ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            pass
    return name


def listen_and_get_number():
    while True:
        user_guess = listen()
        user_guess = user_guess.replace("€", "")
        try:
            user_guess = float(user_guess)
            return user_guess
        except ValueError:
            print("Lo siento, no te he entendido. Di solamente una cantidad")
            speak("Lo siento, no te he entendido")
        except TypeError:
            print("Lo siento, no te he entendido. Di solamente una cantidad")
            speak("Lo siento, no te he entendido")


def get_product_list(session):
    try:
        product_list = []
        products = []
        main_site = session.get("https://www.coolmod.com/")
        categories = main_site.html.find(".subfamilylist")

        while len(products) == 0:
            category_site = session.get(random.choice(tuple(random.choice(categories).links)))
            products = category_site.html.find(".productflex")
            category_title = re.findall("<title>(.+) \|", category_site.text)

        for product in products[:9]:
            product_detail = product.find(".productName", first=True)
            product_name = product_detail.text
            product_name = product_name.split("\n")[0]
            product_detail = product.find(".pricetotal")
            product_price = product_detail[0].text
            product_price = float(product_price.replace(",", ".").replace(".", ""))
            product_detail = product.find(".productImage", first=True)
            product_image = re.findall('src="(.+)" alt', product_detail.html)[0]
            product_details = [product_name, product_price, product_image]
            product_list.append(product_details)
        return category_title, product_list

    except ConnectTimeout:
        return "Connection problem"

    except ConnectionError:
        return "Connection problem"


def main():
    session = HTMLSession()
    print("Bienvenido al precio justo. Te mostraré algunos productos y tendrás que tratar de adivinar su precio.")
    speak("Bienvenido al precio justo. Te mostraré algunos productos y tendrás que tratar de adivinar su precio.")
    category_title, product_list = get_product_list(session)
    for product in product_list:
        product_image = session.get(product[2])
        image = Image.open(BytesIO(product_image.content))
        print(product[0])
        image.show()
        speak("El nombre del producto es {}. Cuánto crees que vale?".format(product[0]))
        user_guess = listen_and_get_number()
        print("El precio era {}".format(product[1]))
        speak("El precio era {}".format(product[1]))


if __name__ == "__main__":
    main()
