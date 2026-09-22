# -----------------------------------------------------------------------------
# File: room16.py
# ACS School Project - Simple Maze Example
# Your own room: Project Room 16
# -----------------------------------------------------------------------------

import sys
from .utils import chooseNextRoom

def enterRoom16(state):
    # --- Room entry description ---
    print("You enter Project Room 16.")
    print("Something must have gone down here, where is everyone and what is this mess?")

    # --- Command handlers ---

    def handle_look():
        """Describe the room and give clues."""
        print("\nYour eyes scan the room.")
        print("Several tables are fallen on the ground, pens, papers and even laptops are scattered all over the floor")
        print("But one thing caught your eye... The whiteboard is covered with a piece of cloth")

        if not state["visited"]["room16"]:
            print("You push it away and get left speechless. Looks like a game of hangman.\n")
            print("    ┌─────┐        ┌─────┐        ┌─────┐         ┌─────┐         ┌─────┐"  )
            print("    │     │        │     │        │     │         │     │         │     │"  )
            print("    │              │     ○        │     ○         │     ○         │     ○"  )
            print("    │              │              │     │         │    /│         │    /|\\")
            print("    │              │              │               │               │       " )
            print("    │              │              │               │               │"        )
            print("   ═╧═            ═╧═            ═╧═             ═╧═             ═╧═"       )
            print("_ _ _ _ _ _   _ _ _ _ _ l     _ _ h _ _ l     _ _ h _ _ l     s _ h _ _ l\n"  )

            lives = 2
            tried = ["s", "h", "l"]
            c_guessed = False
            o_guessed = False

            while True:
                guess = input("What letter are you choosing next? ").lower()

                if guess in tried:
                    print("You already tried that letter.\n")
                    continue

                tried.append(guess)

                if guess == "c" or guess == "o":

                    if guess == "c" and o_guessed == False:
                        c_guessed = True
                        print("NICE, let's continue     s c h _ _ l \n")
                    elif guess == "o" and c_guessed == False:
                        o_guessed = True
                        print("NICE, let's continue     s _ h o o l \n")

                    if guess == "c" and o_guessed == True:
                        print("YOU WIN     s c h o o l")
                        print("Now get out of my sight")
                        state["visited"]["room16"] = True
                        state["previous_room"] = "room16"
                        return "corridor"

                    elif guess == "o" and c_guessed == True:
                        print("YOU WIN     s c h o o l")
                        print("Now get out of my sight.")
                        state["visited"]["room16"] = True
                        state["previous_room"] = "room16"
                        return "corridor"

                else:
                    lives -= 1
                    if lives > 0:
                        print("WRONG, your only try left \n")

                if lives == 0:
                    print("YOU LOSE")
                    return "corridor"

        else:
            print("The challenge is already solved. Now escape while you still can.")
            print("- Possible exits: corridor")
            print("- Your current inventory:", state["inventory"])

    def handle_help():
        """List available commands."""
        print("\nAvailable commands:")
        print("- look around         : Examine the room for clues and start the hangman game.")
        print("- go corridor / back  : Leave the room and return to the corridor.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game completely.")

    def handle_go(destination):
        """Handle movement out of the room."""
        if destination in ["corridor", "back"]:
            print("You step away from the room and return to the corridor.")
            return "corridor"
        else:
            print(f"❌ You can't go to '{destination}' from here.")
            return None

    # --- Main command loop ---
    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            result = handle_look()
            if result:
                return result

        elif command == "?":
            handle_help()

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command == "quit":
            print("👋 You close your notebook and leave the project behind. Game over.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")