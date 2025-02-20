import random
import time

def plot_ascii_chart(numbers):
    max_val = max(numbers)  # Find the maximum value for scaling
    for num in numbers:
        bar = '#' * (num * 40 // max_val)  # Scale to fit max width of 40
        print(f"{num:2d} | {bar}")
input("press enter to start:")
while True:
    nums = [random.randint(1, 50) for _ in range(20)]  # Generate new data
    for i in range(10): print( )
    plot_ascii_chart(nums)  # Plot chart
    time.sleep(0.1)  # Delay for smooth updates
