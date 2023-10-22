def single_byte_xor(text: bytes, key: int) -> bytes:
    """Given a plain text `text` as bytes and an encryption key `key` as a byte
    in range [0, 256) the function encrypts the text by performing
    XOR of all the bytes and the `key` and returns the resultant.
    """
    return bytes([b ^ key for b in text])

hexstring =  input("Enter hexstring: ")

for i in range(0,255):
    result = single_byte_xor(bytes.fromhex(hexstring), i)
    try:
        result = result.decode("utf-8")
    except:
        pass
    print("Key " + str(i) + ": " + str(result))