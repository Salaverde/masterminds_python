
def medir_largos(iterable, *args, sumatot=False):
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        if sumatot:
            largos = sum(largos)
        return largos
    return len(iterable)


def main():
    print(medir_largos("hola"))
    print(medir_largos("hola", "bernat", "com", "estas", sumatot=True))

if __name__ == "__main__":
    main()