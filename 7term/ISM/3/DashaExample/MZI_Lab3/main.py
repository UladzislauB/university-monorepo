import rsa.rsa as rsa


def write_to_file(file_name, data):
    with open(file_name, "w") as file:
        file.write(str(data))


def main():

    with open("files/initial.txt", "r") as file:

        data = file.read()

        n, e, d = rsa.make_key_pair(2048)

        print(n, ' ', e, ' ', d)

        encrypted_data = rsa.encrypt(data, e, n)
        write_to_file("files/encrypted.txt", encrypted_data)
        print("\nencrypted data:\n{}".format(encrypted_data))

        decrypted_data = rsa.decrypt(encrypted_data, d, n)
        write_to_file("files/decrypted.txt", decrypted_data)
        print("\ndecrypted data:\n{}".format(decrypted_data))


if __name__ == '__main__':
    main()
