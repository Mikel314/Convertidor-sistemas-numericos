from math import floor

def de_bi_conversion(number, decimals):
    #Declaration of variables
    bi = []
    fracc = round(number % 1, decimals)
    fracc_part = []
    
    #Dividing the number by 2 and adding the reminder to a list
    while number != 0:
        re = number % 2
        re = floor(re)
        if re > 1:
            re = 1
        elif re < 0:
            re = 0

        number /= 2
        number = floor(number)
        if number < 2 and number > 1:
            number = 1
        elif number < 1:
            number = 0
        bi.append(int(re))

    #Dealing with the decimal part, multiplying the decimal by 2, with a precision of 4 decimal numbers by default
    for i in range(decimals):
        fracc *= 2
        fracc_part.append(int(fracc))
        fracc = round(fracc % 1, decimals)
    
    bi.reverse()
    return bi, fracc_part


def de_hex_conversion(number, decimals):
    #Declaration of variables
    hex = []
    hex_range = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hex_frac = round(number % 1, decimals)
    hex_fraclist = []

    #Dividing the number by 16 and adding the reminder to a list, also checking for the correct letter to use given de hex_range dict
    while number != 0:
        hex_re = number % 16
        hex_re = floor(hex_re)

        number /= 16
        number = floor(number)
        if number < 1:
            number = 0
        
        if hex_re > 9:
            hex_re = hex_range[hex_re]
        if hex_re == type(float):
            hex.append(int(hex_re))
        else:
            hex.append(hex_re)

    #Dealing with the decimal part, multiplying the decimal by 16, with a precision of 4 decimal numbers by default
    for i in range(decimals):
        hex_frac *= 16
        if int(hex_frac) > 9:
            tmp = hex_range[int(hex_frac)]
            hex_fraclist.append(tmp)
        elif int(hex_frac) < 9:
            hex_fraclist.append(int(hex_frac))
        hex_frac = round(hex_frac % 1, decimals)
    
    
    hex.reverse()
    return hex, hex_fraclist

def de_o_conversion(number, decimals):
    #Declaration of variables
    oc = []
    dec_part = round(number % 1, decimals)
    dec_partlist = []

    #Dividing the number by 8 and adding the reminder to a list
    while number != 0:
        re = number % 8
        re = floor(re)
        if re < 0:
            re = 0

        number /= 8
        number = floor(number)
        if number < 1:
            number = 0
        oc.append(int(re))
    
    #Dealing with the decimal part, multiplying the decimal by 8, with a precision of 4 decimal numbers by default
    for i in range(decimals):
        dec_part /= 8
        dec_partlist.append(int(dec_part))
        dec_part = round(dec_part % 1, decimals)
    
    oc.reverse()
    return oc, dec_partlist

#Not finished
def bin_dec_conversion(number, decimals):
    fracc_part = round(number % 1, decimals)
    decimal_number = 0
    tmp = []
    final = 0
    number = str(number)

    if fracc_part == 0.0:
        number = int(number, 2)

    return number, decimal_number    

#Self explanatory 
def isBinary(number):
    p = set(str(number))
 
    s = {'0', '1'}

    if s == p or p == {'0'} or p == {'1'}:
        return True
    else:
        return False

#Function to deal with input
def getInput():
    #print("Number: ", end="")
    result = input("Number: ")

    if "." in result:
        result = float(result)
    else:
        try:
            result = int(result)
        except ValueError:
            return ValueError
    
    return result