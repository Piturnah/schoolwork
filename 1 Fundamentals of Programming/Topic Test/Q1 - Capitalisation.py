char = input("Enter lowercase char\n> ")

# ord(): asc()

def get_upper(char):
    return(chr(ord(char)-32))

try: ord(char)
except: print("ERROR: NOT SINGLE CHAR")

if ord(char) > 122 or ord(char) < 97:
    print("ERROR: NON LOWERCASE CHAR")
else: print(get_upper(char))
