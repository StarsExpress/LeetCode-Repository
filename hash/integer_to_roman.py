
ints2romans = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
    90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
    9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }


def convert_int_to_roman(num: int) -> str:
    roman_num = ""
    for int_unit, roman_str in ints2romans.items():
        if num >= int_unit:
            quotient = num // int_unit
            roman_num += roman_str * quotient
            
            num %= int_unit
    
    return roman_num
