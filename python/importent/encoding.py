def ASCII_dict():
    ASCII = {}
    for i in range(128):
        bin = "{:08b}".format(i)
        char = chr(i)
        ASCII[str(char)] = str(bin)
    return ASCII

def main():
    ASCII = ASCII_dict()
    msg = input(">> ")
    store = []

    for letter in msg:
        store.append(ASCII[letter])

    print(" ".join(store))

if __name__ == '__main__':
    main()