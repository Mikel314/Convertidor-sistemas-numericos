import sys 
import math

def main():

    #Checking for the right amount of input
    if len(sys.argv) != 4:
        print("Correct use: system from system for number to convert")
        return 1

    sys.argv[2].lower
    sys.argv[1].lower

    if sys.argv[2] == "b" and sys.argv[1] == "d":
        result = de_bi_conversion(float(sys.argv[3]))
        for i in result:
            print(i, end="")
    elif sys.argv[2] == "h" and sys.argv[1] == "d":
        h_result = de_hex_conversion(float(sys.argv[3]))
        for j in h_result:
            print(j, end="")
    elif sys.argv[2] == "o" and sys.argv[1] == "d":
        o_result = de_o_conversion(float(sys.argv[3]))
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