def string_mes_llarga(*llista):
    mes_llarga = llista[0]
    for a in llista:
        if len(mes_llarga) < len(a):
            mes_llarga = a
    return mes_llarga

def main():
    print(string_mes_llarga("aaa","aaaaaa","aaaaaaaaa","aaaaaaaaaaaaaaaaaaa","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))

if __name__ == "__main__":
    main()