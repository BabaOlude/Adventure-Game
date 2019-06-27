import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)
    random.choice("make_choice")


def intro():
    print_pause("You wake up from a nap in a tucked "
                "away part of the airport expecting\n"
                "that it would be time "
                "for your flight to board.")
    print_pause("You walk towards the gate and the "
                "airport is empty.")
    print_pause("You walk throughout the terminal "
                "and don't see anyone.")
    print_pause("Then you hear a crash!")
    print_pause("You start to hear peaple walking, "
                "and feel relieved, but as the people get\n"
                "closer and closer you realize they're "
                "not people...")
    print_pause("They're zombies!")
    print_pause("How are you going to get out of there!")


def motorcycle_exit(items):
    print_pause("You decide to exit through the parking garage.")
    print_pause("You see that there are a bunch of rental cars, "
                "but they've all been locked.")
    print_pause("You see a motorcycle, as long as you can "
                "find the key, you'll take it!")
    if "keys" in items:
        print_pause("You search behind that desk of a rental "
                    "car company but there are no more "
                    "available\n "
                    "keys, so you must try something else.")
    else:
        print_pause("You search behind the desk of a rental car "
                    "company\n"
                    "but there is nothing that can help you, "
                    "although you do find a tire iron.")
        items.append("keys")
    print_pause("You go back the way you came.")
    make_choice(items)


def airplane_exit(items):
    print_pause("You decide to exit onto the tarmac.")
    print_pause("You see a a bunch of aircraft hangers "
                "and wonder which ones contain aircraft.")
    print_pause("You have a pilots license, so you just "
                "need a plane!")
    if "map_of_the_hangars" in items:
        print_pause("The only planes on the tarmac are "
                    "commercial jetliners.")
        print_pause("There is no place to hide and no way "
                    "to get out, but "
                    "you do find, a fireman's axe.")
    else:
        print_pause("You see an open runway.")
        if "keys" in items:
            print_pause("You can't find an inventory map of "
                        "the hangars, but you do find\n"
                        "a long metal wrench.")
            items.append("map_of_the_hangars")
        else:
            print_pause("You think maybe you'll be able to "
                        "find a map of the hangers\n"
                        "if you find the keys to open the "
                        "airport administrative offices, ")
            print_pause("You need to keep searching, "
                        "but you do find a backpack with "
                        "protective gear.")
    print_pause("You go back the way you came.")
    make_choice(items)


def run_exit(items):
    print_pause("You decide to make a run for it on foot\n"
                "through the "
                "airport exit past baggage claim.")
    print_pause("You're outside!")
    print_pause("After a few minutes you get tired, so you "
                "look around\n"
                "and see that you're near a highway "
                "where some cars "
                "are still driving by.")
    print_pause("You flag down one of the cars and they pick "
                "you up!")
    print_pause("They ask you where you're going, and you say "
                "anywhere "
                "but the airport!")
    print_pause("The driver is a pilot and had been driving "
                "to the airport "
                "to see if\n"
                "he can take a plane to get out of the "
                "quaranteened zone.")
    print_pause("it would be great if he had a map of where "
                "the small aircraft are.")
    if "keys" in items:
        print_pause("You use the keys you found to open the "
                    "door to the airport administrative\n"
                    "office.")
        print_pause("You find the exact locations, makes, "
                    "and models of the aircraft in the airport\n"
                    "You and the driver find a plane, but the "
                    "hanger has been overrun by zombies.")
        if "map_of_the_hangars" in items:
            print_pause("Luckily you have something that can "
                        "help!")
            print_pause("You both drive to the tarmack "
                        "and take one of the small aircraft\n"
                        "he is the pilot, you are the co-pilot "
                        "and you escape.")
            play_again()
        else:
            print_pause("You can't start any of the vehicles,\n "
                        "because you don't have the keys, "
                        "but you do find a hammer.")
            print_pause("You go back the way you came.")
            make_choice(items)
    else:
        print_pause("By the time you get back to the airfield "
                    "it is completely overrun by zombies.")
        print_pause("There is nothing available "
                    "that can get you to safety, "
                    "but you do find a knife.")
        print_pause("You go back the way you came.")
        make_choice(items)
        random.choice("exit")


def make_choice(items):
    print_pause("Please enter 1 - for the parking garage,"
                "2 - for the tarmac,\n3 - for baggage claim: "
                "Then press Enter")
    exit = input("1. Parking garage\n"
                 "2. Tarmac\n"
                 "3. Baggage claim\n")

    if exit == '1':
        motorcycle_exit(items)
    elif exit == '2':
        airplane_exit(items)
    elif exit == '3':
        run_exit(items)
    else:
        print("Sorry, there is no other way to escape.")


def play_again():
    print_pause("Would you like to play again?")
    user_input = input()
    if "n" in user_input or "no" in user_input:
        print_pause("OK, No worries, Goodbye!")
        SystemExit()
    elif "y" in user_input or "yes" in user_input:
        print_pause("I see you're a thrill seeker, let's play")
        play_game()
    else:
        play_again()


def play_game():
    items = []
    intro()
    make_choice(items)


play_game()
