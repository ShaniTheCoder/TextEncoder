import pyperclip


class SecretCodeLanguage:
    @staticmethod
    def encode_string(name):
        """Encode the given string."""
        fir = name[0]
        name = list(name)
        name.remove(fir)
        name.append(fir)
        for i in range(len(name)):
            if name[i] == 'a':
                name[i] = '0'
            elif name[i] == 'e':
                name[i] = '*'
            elif name[i] == 'i':
                name[i] = '`'
            elif name[i] == 'o':
                name[i] = ','
            elif name[i] == 'u':
                name[i] = '$'
            elif name[i] == ' ':
                name[i] = '%'
        name.reverse()
        encoded_string = ''.join(name)
        return encoded_string

    @staticmethod
    def decode_string(name):
        """Decode the given string."""
        name = list(name)
        name.reverse()
        fir = name[len(name)-1]
        name.remove(name[len(name)-1])
        name.insert(0, fir)
        for i in range(len(name)):
            if name[i] == '0':
                name[i] = 'a'
            elif name[i] == '*':
                name[i] = 'e'
            elif name[i] == '`':
                name[i] = 'i'
            elif name[i] == ',':
                name[i] = 'o'
            elif name[i] == '$':
                name[i] = 'u'
            elif name[i] == '%':
                name[i] = ' '
        decoded_string = ''.join(name)
        return decoded_string

    @staticmethod
    def scg_prompt():
        """Provide an interactive prompt for encoding and decoding strings."""
        while True:
            option = input(
                "\nDo you want to encode or decode a string? (encode/decode/quit): ")

            if option.lower() == 'encode':
                name = input("Enter the string to encode: ")
                encoded_string = SecretCodeLanguage.encode_string(name)
                print("The encoded string is:", encoded_string)
                pyperclip.copy(encoded_string)
            elif option.lower() == 'decode':
                name = input("Enter the string to decode: ")
                decoded_string = SecretCodeLanguage.decode_string(name)
                print("The decoded string is:", decoded_string)
                pyperclip.copy(decoded_string)
            elif option.lower() == 'quit':
                break
            else:
                print("Invalid input. Please try again.")
# shani i love you but it seems that you don't love me


if __name__ == '__main__':
    SecretCodeLanguage.scg_prompt()
