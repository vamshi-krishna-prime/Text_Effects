import time

def spin(string):
    for _ in range(10):
        for ch in '-\\|/':
            # print(f"{ch} { string } {ch}", end='', flush=True)
            print(ch, end='', flush=True)
            time.sleep(0.1)
            print('\b', end='', flush=True)
            print(string, end='', flush=True)
            time.sleep(0.1)
            print('\b\b\b\b\b\b\b\b\b\b\b', end='', flush=True)
            print(f"           {ch}", end='', flush=True)
            time.sleep(0.1)
            print('\b\b\b\b\b\b\b\b\b\b\b\b', end='', flush=True)

if __name__ == '__main__':
    spin(" Game start")
    # print(f"{spin()} Game start {spin()}")
