import funct
from getch import pause

def main():

    #Input
    base_sys = input("From (first 3 letters): ").lower().strip()
    desired_sys = input("To (first 3 letters): ").lower().strip()
    try:
        inp = funct.getInput()
    except ValueError:
        print("That's not a number")
        return main()
    
    if funct.isBinary(inp) == False and base_sys == "bin":
        print("That's not a binary!")
        return main()

    precision = 4
    try:
        if inp % 1 != 0:
            precision = int(input("How many decimals places do you want?: "))
    except TypeError or ValueError:
        print("That's not a correct input!")
        return main()

    #Checking for the desired operation
    #Decimal to binary
    if base_sys == "dec" and desired_sys == "bin":
        int_res, dec_res = funct.de_bi_conversion(inp, precision)
        for i in int_res:
            print(i, end="")
        print(".", end="")
        for j in dec_res:
            print(j, end="")
    #Decimal to hexadecimal
    elif base_sys == "dec" and desired_sys == "hex":
        h_result, h_decresult = funct.de_hex_conversion(inp, precision)
        for k in h_result:
            print(k, end="")
        print(".", end="")
        for l in h_decresult:
            print(l, end="")
    #Decimal to octal
    elif base_sys == "dec" and desired_sys == "oct":
        o_result, o_decresult = funct.de_o_conversion(inp, precision)
        for m in o_result:
            print(m, end="")
        print(".", end="")
        for n in o_decresult:
            print(n, end="")

    #Any system to decimal
    if base_sys == "bin" and desired_sys == "dec" and funct.isBinary(inp) == True:
        number, dec_number = funct.bin_dec_conversion(inp, precision)
        print(number, end=".")
        print(dec_number, end="")
    if base_sys == "hex" and desired_sys == "dec":
        de_res, point_res = funct.hex_dec_conversion(inp, precision)
        print(de_res, end=".")
        print(point_res, end="") 
    

    print("")
    pause("Press any key to continue ")
    main()
    #main()

if __name__ == "__main__":
    main()