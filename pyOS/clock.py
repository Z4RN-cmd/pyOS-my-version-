import time
import os
import sys
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def time_now():
    try:
        while True:
            clear()
            print("=== TIME NOW ===")
            print(time.strftime("%H:%M:%S"))
            print("\nPress CTRL+C to return")
            time.sleep(1)
    except KeyboardInterrupt:
        pass


def stopwatch():
    input("Press ENTER to start stopwatch")
    start = time.time()

    try:
        while True:
            clear()
            now = time.time() - start
            print("=== STOPWATCH ===")
            print(round(now, 2), "seconds")
            print("\nPress CTRL+C to return")
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass


def timer():
    seconds = int(input("Set timer (seconds): "))

    while seconds > 0:
        clear()
        print("=== TIMER ===")
        print("Remaining:", seconds, "seconds")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")
    input("Press ENTER to return")


print("=== pyOS CLOCK ===")

while True:
    clear()
    print("=== pyOS CLOCK ===")
    print("1. Time Now")
    print("2. Stopwatch")
    print("3. Timer")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        time_now()

    elif choice == "2":
        stopwatch()

    elif choice == "3":
        timer()

    elif choice == "4":
        sys.exit