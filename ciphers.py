class CaesarCipher:
    """Дескриптор для шифра Цезаря"""
    def __init__(self, shift: int):
        self.shift = shift

    def _transform(self, text: str, decrypt: bool = False) -> str:
        result = ''
        direction = -1 if decrypt else 1
        for char in text:
            if 'a' <= char <= 'z':
                base = ord('a')
                offset = (ord(char) - base + self.shift * direction) % 26
                result += chr(base + offset)
            elif 'A' <= char <= 'Z':
                base = ord('A')
                offset = (ord(char) - base + self.shift * direction) % 26
                result += chr(base + offset)
            else:
                result += char
        return result

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        encrypted = getattr(obj, '_caesar_encrypted', '')
        return self._transform(encrypted, decrypt=True)

    def __set__(self, obj, value: str):
        obj._caesar_encrypted = self._transform(value, decrypt=False)


class AtbashCipher:
    """Дескриптор для шифра Атбаш"""
    def __init__(self):
        self._encode_table = str.maketrans(
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
            'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
        )

    def _transform(self, text: str) -> str:
        return text.translate(self._encode_table)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        encrypted = getattr(obj, '_atbash_encrypted', '')
        return self._transform(encrypted)

    def __set__(self, obj, value: str):
        obj._atbash_encrypted = self._transform(value)


class SecureMessage:
    caesar = CaesarCipher(shift=3)
    atbash = AtbashCipher()




if __name__ == "__main__":
    msg = SecureMessage()
    msg.caesar = "Hello, World!"
    msg.atbash = "Hello, World!"

    print("Расшифрованный текст (Caesar):", msg.caesar)
    print("Расшифрованный текст (Atbash):", msg.atbash)
    print("Зашифрованный Caesar:", msg._caesar_encrypted)
    print("Зашифрованный Atbash:", msg._atbash_encrypted)