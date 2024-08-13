import time

def long_running_process():
    while True:
        print("Doing something...")
        time.sleep(1)

try:
    long_running_process()
except KeyboardInterrupt:
    print("KeyboardInterrupt: Program interrupted by user.")
except Exception as err:
    print(f"Error: {err}")