import time


def blink(string1, string2):
    for _ in range(10):
        print(string1, end='', flush=True)
        time.sleep(0.1)
        print('\b\b\b\b\b\b\b\b\b\b\b\b', end='', flush=True)
        print(string2, end='', flush=True)
        time.sleep(0.1)
        print('\b\b\b\b\b\b\b\b\b\b\b\b', end='', flush=True)
    print(string1)
if __name__ == '__main__':
    blink(" Game start ", "            ")
