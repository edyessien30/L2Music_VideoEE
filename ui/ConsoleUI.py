from ui.input_validation import select_item


class ConsoleUI:
    @staticmethod
    def print_menu():
        print("Please select a menu choice.")
        print("'X' to exit menu choice.")

    @classmethod
    def run(cls):
        while True:
            cls.print_menu()
            choice = select_item("Please select an item: ", "Error. Please type in valid menu choice.", ['X'])
            if choice == "X":
                break


if __name__ == "__main__":
    ConsoleUI.run()
