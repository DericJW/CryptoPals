string1 = input("Input first hexstring to XOR: ")
string2 = input("Input second hexstring to XOR: ")

print(hex(int(string1, 16) ^ int(string2, 16))[2:])