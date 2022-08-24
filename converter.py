from email.mime import base
import math

def main():

    #Input
    base_sys = input("From (first 3 letters): ").lower().strip()
    desired_sys = input("To (first 3 letters): ").lower().strip()
    numb = float(input("Number: "))

    if base_sys == "dec" and desired_sys == "bin":
        int_res, dec_res = de_bi_conversion(numb)
        for i in int_res:
            print(i, end="")
        print(".", end="")
        for j in dec_res:
            print(j, end="")
    elif base_sys == "dec" and desired_sys == "hex":
        h_result, h_decresult = de_hex_conversion(numb)
        for k in h_result:
            print(k, end="")
        print(".", end="")
        for l in h_decresult:
            print(l, end="")
    elif base_sys == "dec" and desired_sys == "oct":
        o_result, o_decresult = de_o_conversion(numb)
        for m in o_result:
            print(m, end="")
        print(".", end="")
        for n in o_decresult:
            print(n, end="")
    

def de_bi_conversion(number):
    bi = []
    fracc = round(number % 1, 2)
    fracc_part = []

    while number != 0:
        re = number % 2
        re = math.floor(re)
        if re > 1:
            re = 1
        elif re < 0:
            re = 0

        number /= 2
        number = math.floor(number)
        if number < 2 and number > 1:
            number = 1
        elif number < 1:
            number = 0
        bi.append(int(re))

    for i in range(4):
        fracc *= 2
        fracc_part.append(int(fracc))
        fracc = round(fracc % 1, 2)
    
    bi.reverse()
    return bi, fracc_part


def de_hex_conversion(number):
    hex = []
    hex_range = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hex_frac = round(number % 1, 2)
    hex_fraclist = []

    while number != 0:
        hex_re = number % 16
        hex_re = math.floor(hex_re)

        number /= 16
        number = math.floor(number)
        if number < 1:
            number = 0
        
        if hex_re > 9:
            hex_re = hex_range[hex_re]
        if hex_re == type(float):
            hex.append(int(hex_re))
        else:
            hex.append(hex_re)

    for i in range(4):
        hex_frac *= 16
        if hex_frac > 9:
            hex_frac = hex_range[hex_frac]
        elif hex_frac < 9:
            hex_fraclist.append(int(hex_frac))
        hex_frac = round(hex_frac % 1, 2)
    
    
    hex.reverse()
    return hex, hex_fraclist

def de_o_conversion(number):
    oc = []
    dec_part = round(number % 1, 2)
    dec_partlist = []

    while number != 0:
        re = number % 8
        re = math.floor(re)
        if re < 0:
            re = 0

        number /= 8
        number = math.floor(number)
        if number < 1:
            number = 0
        oc.append(int(re))
    
    for i in range(4):
        dec_part /= 8
        dec_partlist.append(int(dec_part))
        dec_part = round(dec_part % 1, 2)
    
    oc.reverse()
    return oc, dec_partlist

if __name__ == "__main__":
    main()