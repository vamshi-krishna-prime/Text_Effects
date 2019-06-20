import time

def spin(string):
    for _ in range(10):
        for ch in '-\\|/':
            print(ch, end='', flush=True)
            print(string + ch, end='', flush=True)
            time.sleep(0.1)
            print('\b\b\b\b\b\b\b\b\b\b\b\b\b\b', end='', flush=True)


if __name__ == '__main__':
    spin(" Game start ")
