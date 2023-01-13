def suma(*numeros):
    res = 0
    for a in numeros:
        res += a
    return res

def main ():
    print(suma(1, 2, 3, 4, 5, 6, 7, 8))

if __name__ == "__main__":
    main()