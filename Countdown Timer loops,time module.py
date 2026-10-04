import time

def countdown_timer(total_seconds):
    # The loop runs as long as there are seconds remaining
    while total_seconds > 0:
        # divmod divides total_seconds by 60 and returns (minutes, seconds)
        mins, secs = divmod(total_seconds, 60)
        
        # Format the numbers to always show two digits (e.g., 05:09)
        timer_format = f"{mins:02d}:{secs:02d}"
        
        # Print the timer on the exact same line using \r (carriage return)
        print(timer_format, end="\r")
        
        # Pause the program for exactly 1 second
        time.sleep(1)
        
        # Decrement the countdown pool
        total_seconds -= 1
        
    print("Time's up! 🎉")

# Get input from the user and convert it to an integer
try:
    user_time = int(input("Enter countdown time in seconds: "))
    countdown_timer(user_time)
except ValueError:
    print("Please enter a valid whole number.")