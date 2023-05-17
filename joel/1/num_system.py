def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def decimal_to_octal(n):
    return oct(n).replace("0o", "")

def decimal_to_hex(n):
    return hex(n).replace("0x", "")

n = int(input("Enter a decimal number: "))
print("Binary: ", decimal_to_binary(n))
print("Octal: ", decimal_to_octal(n))
print("Hexadecimal: ", decimal_to_hex(n))
