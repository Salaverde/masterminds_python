def segur(res):
    if res == "si":
        return True
    return False

def main():
    print(segur(input("Estàs segur? (si/no)\n")))

if __name__ == "__main__":
    main()