
def potencia(base, *exponent):
    if exponent:
        return base ** exponent
    return base ** 2


def main():
    print(potencia(10))


if __name__ == "__main__":
    main()
