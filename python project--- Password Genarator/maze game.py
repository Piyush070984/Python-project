def start_game():
    name = input("Hey, type your name: ")
    print(f"Hello {name}, welcome to the adventure game!")

    should_we_play = input("Do you want to play? (yes/no) ").lower()

    if should_we_play == "y" or should_we_play == "yes":
        print("Awesome! Let's begin your adventure!")

        while True:
            direction = input("Do you want to go left or right? (left/right) ").lower()
            if direction == "left":
                print("You went left and encountered a dense, dark forest. The trees seem to whisper... Do you want to:")
                print("1. Explore the forest")
                print("2. Return to the path")
                forest_choice = input("Choose (1/2): ")

                if forest_choice == "1":
                    print("You bravely venture into the forest but get lost. You hear strange noises... It's a wild wolf!")
                    print("Do you want to:")
                    print("1. Fight the wolf")
                    print("2. Run away")
                    wolf_choice = input("Choose (1/2): ")

                    if wolf_choice == "1":
                        print("You fought bravely but the wolf overpowers you. You have perished. Game over.")
                        break
                    elif wolf_choice == "2":
                        print("You managed to escape, but you're back at the start of your journey.")
                        continue
                    else:
                        print("Invalid choice! You stumble and are caught by the wolf. Game over.")
                        break
                elif forest_choice == "2":
                    print("You wisely return to the path and continue your journey.")
                else:
                    print("Invalid choice! You lose your way and perish in the forest. Game over.")
                    break
            elif direction == "right":
                print("You went right and come across a mystical bridge over a river.")
                print("Do you want to:")
                print("1. Cross the bridge")
                print("2. Swim across the river")
                bridge_choice = input("Choose (1/2): ")

                if bridge_choice == "1":
                    print("As you cross the bridge, it creaks ominously. Halfway across, a troll appears!")
                    print("Do you want to:")
                    print("1. Talk to the troll")
                    print("2. Fight the troll")
                    troll_choice = input("Choose (1/2): ")

                    if troll_choice == "1":
                        print("You talk to the troll and offer him some gold. He lets you pass safely. You find a treasure chest and win!")
                        break
                    elif troll_choice == "2":
                        print("You engage the troll in battle, but he's too strong! You lose. Game over.")
                        break
                    else:
                        print("Invalid choice! The troll throws you into the river. Game over.")
                        break
                elif bridge_choice == "2":
                    print("You decide to swim, but the current is too strong, and a lurking alligator finds you. You die. Game over.")
                    break
                else:
                    print("Invalid choice! You stand there indecisively and fall into the river. Game over.")
                    break
            else:
                print("Invalid direction! Please choose 'left' or 'right'.")

    else:
        print("Maybe next time! Goodbye.")

start_game()
