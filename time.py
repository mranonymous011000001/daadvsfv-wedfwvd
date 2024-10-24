import time

# Total hours to wait
total_hours = 5

for hour in range(1, total_hours + 1):
    # Wait for 1 hour (1 hour = 60 * 60 seconds)
    time.sleep(60 * 60)
    # Log after every hour
    print(f"{hour} hour(s) have passed.")
    
print("5 hours have passed in total.")
