import time

class text():
    def blink(string1, string2, num):
        for _ in range(num):
            print(string1, end='', flush=True)
            time.sleep(0.1)
            print('\b\b\b\b\b\b\b\b\b\b\b\b', end='', flush=True)
            print(string2, end='', flush=True)
            time.sleep(0.1)
            print('\b\b\b\b\b\b\b\b\b\b\b\b', end='', flush=True)
        print(string1)


if __name__ == '__main__':
    message = input("Enter the text > ")
    blank_list = []
    for letter in message:
        blank_list.append(" ")
        blank_string = "".join(blank_list)

    num = int(input("No.of times to blink > "))
    fido = text.blink(message, blank_string, num)
