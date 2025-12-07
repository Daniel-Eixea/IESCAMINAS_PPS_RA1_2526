import hashlib

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha512(data: bytes) -> str:
    return hashlib.sha512(data).hexdigest()

def md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()

def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()

def caesar(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def menu():
    print("\n===== Elige una opción =====")
    print("1) SHA-256")
    print("2) SHA-512")
    print("3) MD5")
    print("4) SHA-1")
    print("5) Cifrado César")
    print("0) Salir")
    print("============================")

def main():
    while True:
        menu()
        choice = input("Selecciona una opción: ")
        if choice == '0':
            break
        elif choice in {'1', '2', '3', '4'}:
            data = input("Introduce el texto a cifrar: ").encode()
            if choice == '1':
                print("SHA-256:", sha256(data))
            elif choice == '2':
                print("SHA-512:", sha512(data))
            elif choice == '3':
                print("MD5:", md5(data))
            elif choice == '4':
                print("SHA-1:", sha1(data))
        elif choice == '5':
            text = input("Introduce el texto a cifrar/descifrar: ")
            shift = int(input("Introduce el desplazamiento (número entero -> positivo para cifrar, negativo para descifrar): "))
            print("Resultado:", caesar(text, shift))
        else:
            print("Opción no válida.")
    
if __name__ == "__main__":
    main()