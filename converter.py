from email.mime import base
import math

def main():

    #Input
    base_sys = input("From (first 3 letters): ").lower().strip()
    desired_sys = input("To (first 3 letters): ").lower().strip()
    numb = input("Number: ")

    if base_sys == "dec" and desired_sys == "bin":
        result = de_bi_conversion(float(numb))
        for i in result:
            print(i, end="")
    elif base_sys == "dec" and desired_sys == "hex":
        h_result = de_hex_conversion(float(numb))
        for j in h_result:
            print(j, end="")
    elif base_sys == "dec" and desired_sys == "oct":
        o_result = de_o_conversion(float(numb))
        for k in o_result:
            print(k, end="")
    

def de_bi_conversion(number):
    bi = []

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
    
    bi.reverse()
    return bi


def de_hex_conversion(number):
    hex = []
    hex_range = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

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
    
    hex.reverse()
    return hex

def de_o_conversion(number):
    oc = []

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
    
    oc.reverse()
    return oc

if __name__ == "__main__":
    main()