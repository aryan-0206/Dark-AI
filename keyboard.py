from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

def volumeup():
    """
    Increase system volume
    """
    try:
        for i in range(5):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            sleep(0.1)
    except Exception as e:
        print(f"Error adjusting volume: {e}")

def volumedown():
    """
    Decrease system volume
    """
    try:
        for i in range(5):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            sleep(0.1)
    except Exception as e:
        print(f"Error adjusting volume: {e}")

def mute():
    """
    Mute/unmute system volume
    """
    try:
        keyboard.press(Key.media_volume_mute)
        keyboard.release(Key.media_volume_mute)
    except Exception as e:
        print(f"Error muting: {e}")

# Test function
if __name__ == "__main__":
    print("Keyboard module loaded successfully")
    print("Available functions: volumeup(), volumedown(), mute()")
