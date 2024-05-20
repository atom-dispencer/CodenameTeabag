#
# Codename Teabag Programming Tutorial
# Copyright (C) 2024 Adam Spencer
#
# This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

print("Greetings, Adventurer!")

print("What do they call you?")
name = input("> ")

# TODO When do I introduce fstrings?
print("Greetings to you, " + name + "!")
print("Welcome to the Forgotten Lands!")

position = 0
has_key = False
while (True):
    print("")
    action = input("What do you want to do? (try HELP) > ")
    match (action.upper()):
        case "EAST":
            position = position + 1
        case "WEST":
            position = position - 1
        case "HELP":
            print("EAST: Move east")
            print("WEST: Move west")
            print("HELP: Show this message")
            continue
        case _:
            print("Unknown action: " + action + " - try HELP.")
            continue

    if position == 0:
        print("You are standing on a path that leads east and west.")
    elif position == 1:
        print("The path continues through a forest.")
        print("You can hear the birds singing in the trees.")
    elif position == 2:
        if not has_key:
            print("You see a small golden key on the ground.")
            pick_up_key = input("Do you want to pick it up? > ")
            match (pick_up_key.upper()):
                case "YES":
                    print("You put the key in your pocket.")
                    has_key = True
                case "NO":
                    print("You set the key down.")
    elif position == -1:
        print("The path widens into a wide road.")
        print("'I wonder where this goes', you think.")
        print("'These lands haven't been inhabited in years...'")
    elif position == -2:
        print("You are standing in front of an enormous door.")
        print("You can see a very small keyhole at its base.")
        if has_key:
            insert_key = input("Do you want to go through the door? > ")
            match (insert_key.upper()):
                case "YES":
                    print("You insert your key and the door swings open...")
                    print("A voice booms from above...")
                case "NO":
                    print("You hold your key in your hand...")
                    print("'Another time', you think...")
        else:
            print("'If only I had a key...', you think...")

    # INFO I could do an 'else' here, but instead I use an invertion
    if position < -2 or position > 2:
        print("You find a cliff and walk to the edge.")
        print("You cannot see the bottom.")
        step_away = input("Do you want to step away from the edge? > ")
        match(step_away.upper()):
            case "YES":
                print("You walk away from the cliff.")
                if position > 2:
                    position = 2
                elif position < -2:
                    position = -2
            case "NO":
                print("As you ponder the view, the cliff crumbles.")
                print("The sunset looks beautiful as you fall...")
                exit()
