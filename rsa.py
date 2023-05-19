from math import gcd
from work_with_file import *


def generate_keys(p, q):
    '''

    :param p: prime number to form a public key
    :param q: prime number to form a public key
    :return: (encryption key, public key), (decryption key, public key)

    '''
    n = p * q
    ph = (p - 1) * (q - 1)
    e = 2
    while e < ph:
        if gcd(e, ph) == 1:
            break
        else:
            e += 1
    d = 2
    while (d * e) % ph != 1:
        d += 1
    return (e, n), (d, n)


def binary_pow(number: int, power):
    if power == 0:
        return 1
    elif power % 2 == 1:
        return binary_pow(number, power - 1) * number
    else:
        return binary_pow(number, power/2) * binary_pow(number, power / 2)


class RSA:
    def __init__(self, information: str, alphabet=None):
        self.information = information
        self.alphabet = alphabet

    def encrypt(self, open_key):
        '''

        :param open_key: (encryption key, public key)
        :return: encrypted message
        '''
        ciphered_txt = ''
        for i in self.information:
            if not i.isalpha():
                ciphered_txt += i + '%-%'
            elif i.isupper():
                ciphered_txt += str(self.ciph_decrypt_by_step(open_key, self.alphabet.index(i))) + '%-%'
            else:
                ciphered_txt += str(self.ciph_decrypt_by_step(open_key, self.alphabet.index(i.upper())) + 10000) + '%-%'
        return ciphered_txt

    def decrypt(self, closed_key):
        '''

        :param closed_key: (decryption key, public key)
        :return: decrypted message
        '''
        inform = self.information.split('%-%')[:-1]
        decryption = ''
        for i in inform:
            if not i.isdigit():
                decryption += i
            elif int(i) < 10000:
                decryption += self.alphabet[self.ciph_decrypt_by_step(closed_key, int(i))]
            else:
                decryption += self.alphabet[self.ciph_decrypt_by_step(closed_key, int(i)-10000)].lower()
        return decryption

    @staticmethod
    def ciph_decrypt_by_step(key, letter):
        txt = binary_pow(letter, key[0])
        return txt % key[1]


class StartAlgorithm:
    def __init__(self, information: str, r_file, key, encrypt=1):
        self.information = information
        self.r_file = r_file
        self.key = key
        self.encrypt = encrypt

    def work(self):
        '''
        function to call the cipher and write the encrypted/decrypted messages to a file
        '''
        if self.information.endswith('.txt'):
            self.information = WorkWithFiles(self.information).read_text()
        alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
        rsa = RSA(self.information, alphabet)
        self.key = tuple(map(int, self.key.split(',')))
        if self.encrypt == 1:
            print(rsa.encrypt(self.key))
            WorkWithFiles(self.r_file).write_txt(rsa.encrypt(self.key))
        else:
            print(rsa.decrypt(self.key))
            WorkWithFiles(self.r_file).write_txt(rsa.decrypt(self.key))

