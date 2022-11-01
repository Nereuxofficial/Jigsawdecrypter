import argparse
import base64

from Crypto.Cipher import AES


def read_file(input_file):
    in_file = open(input_file, 'rb')
    encrypted_data = in_file.read()
    in_file.close()
    return encrypted_data


def write_file(output_file, decrypted_data):
    out_file = open(output_file, 'wb')
    out_file.write(decrypted_data)
    out_file.close()


def decrypt_file(path):
    input_file = path
    encrypted_data = read_file(input_file)
    return decrypt(encrypted_data)


def decrypt(encrypted_data):
    # Extracted key from Jigsaw Ransomware
    key = 'OoIsAwwF32cICQoLDA0ODe=='
    # Encode key as base64
    key = base64.b64decode(key)
    # Extracted Initialization Vector(iv) from Jigsaw executable
    iv = '\x00\x01\x00\x03\x05\x03\x00\x01\x00\x00\x02\x00\x06\x07\x06\x00'

    # Creating AES object
    obj = AES.new(key, AES.MODE_CBC, iv.encode('utf-8'))
    return obj.decrypt(encrypted_data)


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(description='Decrypts a Jigsaw encrypted file')
    my_parser.add_argument('input',
                           metavar='input_file',
                           type=str,
                           help='the file to decrypt')
    my_parser.add_argument('output',
                           metavar='output_file',
                           type=str,
                           help='the output file')
    args = my_parser.parse_args()

    write_file(args.output, decrypt_file(args.input))
