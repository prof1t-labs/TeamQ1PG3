import sys

def enterClassroom2016(state):
    if not state["visited"]["classroom2016"]:
        state["visited"]["classroom2016"] = True
        print(f"You awake in a room, the area is completely dark, with only a light illuminating a room.\n"
          f"Having overslept, you are in a daze as to how any faculity staff could of let this happen.\n"
          f"For now, you should probably look around to see what to do.")
    elif state["visited"]["classroom2016"]:
        print("The room is still in the same state that it was when you originally left it, still dark, empty seats, empty tables\n"
              "whiteboard with signs of use and still no staff present. Best that you leave this place.")


    #Change this
    def handle_look():
        #Dialogue tree for looking around.
        print("You see praticually nothing in the room, empty seats, tables with nothing on them, a white board with remants\n"
              "of something being erased, and still no staff in sight. Maybe it is best to leave this room.")
        print("- Possible exits: corridor")
        print("- Your current inventory:", state["inventory"])

    def handle_help():
        print("\nAvailable commands:")
        print("- look around         : Examine the room and its contents.\n"
              "- go corridor         : Leave the room and return to the corridor.\n"
              "- ?                   : Show this help message.\n"
              "- quit                : Quit the game entirely.")

    def handle_go(destination):
        if destination in ["corridor"]:
            print("🚪 You open the door and step into the corridor.")
            return "corridor"
        else:
            print(f"❌ You can't go to '{destination}' from here.")
            return None

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


        elif command == "quit":
            print("👋 You drop your backpack, leave the maze behind, and step back into the real world.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")