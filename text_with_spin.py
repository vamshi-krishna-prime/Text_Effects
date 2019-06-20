import time

class text():
    def spin(self, string, num):
        self.clear = "\b"*(4 + len(string))
        for _ in range(num):
            for ch in '-\\|/':
                print(ch + ch + string + ch + ch, end='', flush=True)
                time.sleep(0.1)
                print(self.clear, end='', flush=True)
                # example of print statement for string = " Game start "
                # print('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b', end='', flush=True)


def print_spin(message, num):
    fido = text()
    fido.spin(message, num)

if __name__ == '__main__':
    string = input("Enter the text > ")
    num = int(input("No.of times to spin > "))
    # fido = text.spin(string, num) also works
    
    # /////////////    
    # fido = text()
    # fido.spin(string, num) also works
    print_spin(string, num)
