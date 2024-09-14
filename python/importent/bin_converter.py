from termcolor import cprint


try:
    In = input("Enter binary number: ")
    hex_result = (hex(int(In, base= 2))[2:])
    oct_result = (oct(int(In, base= 2))[2:])
    bin_result = (bin(int(In, base= 2))[2:])
    dec_result = ((int(In, base= 2)))

    cprint("Dec:",color= "cyan", on_color= "on_light_green",attrs= ["bold"], end= " ")
    print(dec_result)

    cprint("Hex:",color= "cyan", on_color= "on_light_green",attrs= ["bold"], end= " ")
    print(hex_result)

    cprint("Bin:",color= "cyan", on_color= "on_light_green",attrs= ["bold"], end= " ")
    print(bin_result)

    cprint("Oct:",color= "cyan", on_color= "on_light_green",attrs= ["bold"], end= " ")
    print(oct_result)


except:
    cprint("There is Error", color= "red", attrs= ["bold"], on_color= "on_light_yellow")
    print()
