import time
timer = int(input("Enter time for your timer: "))
for i in range(timer, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("Time's UP!")

