import pyttsx3

def read_text(text):
    # Reads aloud the given text using text-to-speech
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Adjust speed of the reader if needed
    engine.say(text)
    engine.runAndWait()

def screen_reader():
    # Simulates a screen reader by reading user input or text from a file 
    print("\nScreen Reader Simulation")
    print("1. Enter text to read aloud")
    print("2. Read from a file (simulated labeled UI)")  # This simulates the various buttons which can be read allowed and changed
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        text = input("Enter text: ")
        read_text(text)

    elif choice == "2":
        try:
            with open("venmo_labels.txt", "r") as file:
                content = file.read()
                print("\nReading UI Labels...")
                print(content)  # Display text on screen for reference
                read_text(content)
        except FileNotFoundError:
            print("Error: 'venmo_labels.txt' not found. Create the file with sample UI labels.") # If the file has not been created

    else:
        print("Invalid choice. Please restart the script.")

if __name__ == "__main__":
    screen_reader()
