# -----------------------------------------------------------------------------
# File: main.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Patrick, Juray
# -----------------------------------------------------------------------------

from rooms import enterCorridor, enterClassroom2016, enterRoom16, enterRoom14, enterRoom6

print("****************************************************************************")
print("*                      Welcome to the School Maze!                         *")
print("*        Your goal is to explore all important rooms in the school.        *")
print("*    You may need to solve challenges to collect items and unlock rooms.   *")
print("*               Once you've visited all rooms, you win!                    *")
print("****************************************************************************")

state = {
    "current_room": "classroom2016",
    "previous_room": "classroom2016",

    "visited": {
        "classroom2016": False,
        "room14": False,
        "room16": False,
        "room6": False
    },

    "inventory": []
}

while True:
    current = state["current_room"]

    if current == "corridor":
        state["current_room"] = enterCorridor(state)

    elif current == "classroom2016":
        state["current_room"] = enterClassroom2016(state)

    elif current == "room16":
        state["current_room"] = enterRoom16(state)

    elif current == "room14":
        state["current_room"] = enterRoom14(state)

    elif current == "room6":
        state["current_room"] = enterRoom6(state)

    else:
        print("Unknown room. Exiting game.")
        break