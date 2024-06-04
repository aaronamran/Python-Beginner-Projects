import time
from datetime import datetime


def set_alarm():
    while True:
        alarm_time = input("Enter the alarm time in HH:MM format: ")
        try:
            alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
            if 0 <= alarm_hour < 24 and 0 <= alarm_minute < 60:
                return alarm_hour, alarm_minute
            else:
                print("Invalid time format. Please enter a valid time.")
        except ValueError:
            print("Invalid input. Please enter the time in HH:MM format.")


def main():
    print("Welcome to the Python Alarm Clock!")

    # Print the current time
    now = datetime.now()
    print(f"Current time: {now.hour:02}:{now.minute:02}")

    alarm_hour, alarm_minute = set_alarm()
    print(
        f"\nAlarm set for {alarm_hour:02}:{alarm_minute:02}. Waiting for the alarm..."
    )

    while True:
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        print(f"Current time: {current_hour:02}:{current_minute:02}", end='\r')

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("\n\nWake up! It's time!")
            break

        time.sleep(1)  # Check every 1 second


if __name__ == "__main__":
    main()
