def fibonacci_recursiu(n):
    if n <= 1:
        return 1
    return fibonacci_recursiu(n - 1) + fibonacci_recursiu(n - 2)


def main():
    for f in range(99999999999999):
        print(fibonacci_recursiu(f))


if __name__ == "__main__":
    main()