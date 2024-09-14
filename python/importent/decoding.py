def ASCII_dict():
    ASCII = {}
    for i in range(128):
        bin = "{:08b}".format(i)
        char = chr(i)
        ASCII[str(bin)] = str(char)
    return ASCII

def main():
    ASCII = ASCII_dict()
    msg = input(">> ")
    listmsg = msg.split(" ")

    for bin in listmsg:
        print(ASCII[bin], end= "")

if __name__ == '__main__':
    main()