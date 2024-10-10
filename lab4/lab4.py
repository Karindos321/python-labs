def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)


input_file = 'input.txt'
output_file = 'output.txt'
shift = 3 

text = read_file(input_file)
encrypted_text = caesar_cipher(text, shift)
write_file(output_file, encrypted_text)


