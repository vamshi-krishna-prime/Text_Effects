import time

class text():
    def blink(self, string, num):
        self.blank_list = []

        for letter in message:
            self.blank_list.append(" ")
            self.blank_string = "".join(self.blank_list)

        for _ in range(num):
            self.clear = "\b" * len(string)
            print(string, end='', flush=True)
            time.sleep(0.1)
            print(self.clear, end='', flush=True)
            print(self.blank_string, end='', flush=True)
            time.sleep(0.1)
            print(self.clear, end='', flush=True)
        print(string)


def print_blink(message, num):
    fido = text()
    fido.blink(message, num)


if __name__ == '__main__':
    message = input("Enter the text > ")
    num = int(input("No.of times to blink > "))
    print_blink(message, num)
