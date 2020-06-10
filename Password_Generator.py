import random
import string

while True:
    size = int(input(">>>"))

    def password(size):
        pw = ''

        for i in range(size):
            a = random.randint(0, 93)
            pw += string.printable[a]
        return pw


    print(password(size))

