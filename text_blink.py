import time

#  class to blink the text
class text():
    def blink(self, string, num):
        self.blank_list = []

#         generates a blank text of same length
        for letter in message:
            self.blank_list.append(" ")
            self.blank_string = "".join(self.blank_list)
            
#       cycles 'blank text' and 'input text' for effect 
        for _ in range(num):
            self.clear = "\b" * len(string)
            print(string, end='', flush=True)
            time.sleep(0.1)
            print(self.clear, end='', flush=True)
            print(self.blank_string, end='', flush=True)
            time.sleep(0.1)
            print(self.clear, end='', flush=True)
        print(string)


# calls the text class with 'input text' and 'number of times to blink' as arguments
def print_blink(message, num):
    fido = text()
    fido.blink(message, num)
    

# Runs the program only if executed directly
if __name__ == '__main__':
    message = input("Enter the text > ")
    num = int(input("No.of times to blink > "))
    print_blink(message, num)
