


# pinnacle labs Alarm Clock project




import pygame
import time

def play_alarm_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def set_alarm(alarm_time, sound_file):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time > alarm_time:
            print("The current time is greater than the alarm time, so set the time correctly !!!!")
            break
        if current_time >= alarm_time:
            print("Alarm!")
            play_alarm_sound(sound_file)
            snooze_option = input("Would you like to snooze? (yes/no): ").lower()
            if snooze_option == 'yes':
                snooze_time = time.time() + 300  # Snooze for 5 minutes
                print("Alarm snoozed for 5 minutes.")
                while time.time() < snooze_time:
                    time.sleep(1)
                continue
            else:
                break
        time.sleep(1)

def main():
    print("Welcome to Alarm Clock!")
    alarm_time = input("Enter the time for the alarm (HH:MM:SS format): ")
    sound_file = input("Enter the path to the sound file for the alarm: ")

    try:
        pygame.init()
        set_alarm(alarm_time, sound_file)
    except KeyboardInterrupt:
        print("\nAlarm clock stopped.")

if __name__ == "__main__":
    main()
