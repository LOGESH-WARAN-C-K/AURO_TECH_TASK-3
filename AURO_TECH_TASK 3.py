import time

class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.is_running = False

    def start_stopwatch(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            print("Stopwatch started.")
        else:
            print("Stopwatch is already running.")

    def stop_stopwatch(self):
        if self.is_running:
            self.end_time = time.time()
            elapsed_time = self.end_time - self.start_time
            self.is_running = False
            print(f"Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds.")
        else:
            print("Stopwatch is not running.")

    def start_countdown(self, duration):
        print(f"Countdown started for {duration} seconds.")
        time.sleep(duration)
        print("Countdown finished.")

class UserInterface:
    def __init__(self, timer):
        self.timer = timer

    def display_menu(self):
        print("\nTimer Menu:")
        print("1. Start Stopwatch")
        print("2. Stop Stopwatch")
        print("3. Start Countdown")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ")

            if choice == '1':
                self.timer.start_stopwatch()
            elif choice == '2':
                self.timer.stop_stopwatch()
            elif choice == '3':
                duration = int(input("Enter countdown duration in seconds: "))
                self.timer.start_countdown(duration)
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    timer = Timer()
    ui = UserInterface(timer)
    ui.run()
