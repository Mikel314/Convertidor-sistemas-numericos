import funct

def main():

    #Input
    base_sys = input("From (first 3 letters): ").lower().strip()
    desired_sys = input("To (first 3 letters): ").lower().strip()
    try:
        numb = float(input("Number: "))
    except ValueError:
        print("That's not a number")
        return 1
    
    precision = 4

    if numb % 1 != 0:
        precision = int(input("How many decimals places do you want: "))

    #Checking for the desired operation
    #Decimal to binary
    if base_sys == "dec" and desired_sys == "bin":
        int_res, dec_res = funct.de_bi_conversion(numb, precision)
        for i in int_res:
            print(i, end="")
        print(".", end="")
        for j in dec_res:
            print(j, end="")
    #Decimal to hexadecimal
    elif base_sys == "dec" and desired_sys == "hex":
        h_result, h_decresult = funct.de_hex_conversion(numb, precision)
        for k in h_result:
            print(k, end="")
        print(".", end="")
        for l in h_decresult:
            print(l, end="")
    #Decimal to octal
    elif base_sys == "dec" and desired_sys == "oct":
        o_result, o_decresult = funct.de_o_conversion(numb, precision)
        for m in o_result:
            print(m, end="")
        print(".", end="")
        for n in o_decresult:
            print(n, end="")
        else:
            pseudo = input("Press enter to exit or type again for another operation ")
            if pseudo == "":
                return 1
            elif pseudo == "again":
                main()

    # Any system to decimal
    # if base_sys == "bin" and desired_sys == "dec" and funct.isBinary(numb) == True:
    #     result, b_binresult = funct.bin_dec_conversion(numb, precision)
    #     for e in result:
    #         print(e, end="")
    #     print(".", end="")
    #     for q in b_binresult:
    #         print(q, end="")
    
    print(" ")
    final = input("Press enter to exit or type again for another operation ")
    if final == "":
        return 1
    elif final == "again":
        main()


if __name__ == "__main__":
    main()