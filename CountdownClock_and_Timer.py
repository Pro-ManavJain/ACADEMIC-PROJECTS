#countdown clock
import time

time_as = int(input("Enter time to start: "))

def countdown_clock(seconds):
    print("countdown has started")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")  # overwrite the line
        time.sleep(1)  # wait for 1 second
        seconds -= 1
    print("00:00")
    print("Time's up!")

print(countdown_clock(time_as))

#timer
import time

times = int(input("Enter time to begin: "))

def start_timer(duration):
    print("Timer has started")
    start_time = time.time()  # Record start time
    while True:
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        mins, secs = divmod(int(elapsed_time), 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")  # overwrite the line
        time.sleep(1)
        if elapsed_time >= duration:
            print(f"Timer finished after {duration} seconds!")
            break

print(start_timer(times))