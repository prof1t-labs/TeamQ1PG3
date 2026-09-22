# -----------------------------------------------------------------------------
# File: class_ioana.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# -----------------------------------------------------------------------------

import sys


def enterRoom14(state):

    # --- Room entry description ---
    print("\n👻 You enter a dark classroom.")
    print("Three teacher ghosts are waiting inside.")
    if not state["visited"]["room14"]:
        print("Each ghost has a different challenge.")
        print("Choose a ghost and answer its question to escape!")

        print("\nChoose your ghost:")
        print("1. Math Ghost")
        print("2. Coding Ghost")
        print("3. IT Ghost")

        print("\nEnter 1, 2 or 3:")

    elif state["visited"]["room14"]:
        print("You've already been here, disappear.")
        return "corridor"


    # --- Command handlers ---

    def handle_look():
        """Describe the room."""
        print("\nYou look around the classroom.")
        print("There are three ghosts:")
        print("1. Math Ghost")
        print("2. Coding Ghost")
        print("3. IT Ghost")
        print("\nChoose a ghost by typing: choose 1, choose 2 or choose 3")


    def handle_help():
        """List available commands."""
        print("\nAvailable commands:")
        print("- look around        : Look around the classroom.")
        print("- choose 1           : Challenge the Math Ghost.")
        print("- choose 2           : Challenge the Coding Ghost.")
        print("- choose 3           : Challenge the IT Ghost.")
        print("- go corridor        : Return to the corridor.")
        print("- ?                  : Show this help message.")
        print("- quit               : Quit the game.")


    def handle_go(destination):
        """Handle movement out of the room."""
        if destination in ["corridor", "back"]:
            print("You leave the ghosts and return to the corridor.")
            return "corridor"
        else:
            print("❌ You can't go there from this room.")
            return None


    def handle_ghost(choice):
        """Choose a ghost and answer its question."""

        # MATH GHOST
        if choice == "1":
            print("\n👻 The Math Ghost asks:")
            print("What is 5 + 5?")
            print("A. 8")
            print("B. 10")
            print("C. 15")

            while True:
                answer = input("Your answer: ").strip().lower()

                if answer == "b":
                    print("✅ Correct! The Math Ghost lets you escape.")
                    state["visited"]["room14"] = True
                    return "corridor"

                else:
                    print("❌ Wrong answer! Try again.")


        # CODING GHOST
        elif choice == "2":
            print("\n👻 The Coding Ghost asks:")
            print("Which command displays something in Python?")
            print("A. print")
            print("B. show")
            print("C. display")

            while True:
                answer = input("Your answer: ").strip().lower()

                if answer == "a":
                    print("✅ Correct! The Coding Ghost lets you escape.")
                    state["visited"]["room14"] = True
                    return "corridor"

                else:
                    print("❌ Wrong answer! Try again.")


        # IT GHOST
        elif choice == "3":
            print("\n👻 The IT Ghost asks:")
            print("What does CPU stand for?")
            print("A. Central Processing Unit")
            print("B. Computer Personal Unit")
            print("C. Central Program User")

            while True:
                answer = input("Your answer: ").strip().lower()

                if answer == "a":
                    print("✅ Correct! The IT Ghost lets you escape.")
                    state["visited"]["room14"] = True
                    return "corridor"

                else:
                    print("❌ Wrong answer! Try again.")


    # --- Main command loop ---

    while True:

        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == "?":
            handle_help()

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)

            if result:
                return result


        elif command in ["1", "2", "3"]:

            result = handle_ghost(command)

            if result:
                return result

        elif command == "quit":
            print("👋 You leave the haunted classroom. Game over.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")