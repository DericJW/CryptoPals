import base64

hexstring = input("Enter hexstring here: ")

raw_bytes = bytes.fromhex(hexstring)

print(base64.b64encode(raw_bytes).decode("ascii"))
