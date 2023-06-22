import random
import art
import game_data
import os
def compare(objekt_1,objekt_2):
    if objekt_1['follower_count'] >= objekt_2['follower_count']:
        return 'A'
    else:
        return 'B'
def print_object(object):
    return f"{object['name']}, {object['description']} from {object['country']}"
def run_program():
    run = True
    print(art.logo)
    data = game_data.data
    score = 0
    compare_a = random.choice(data)
    while run:
        print(f"Compare A: " + print_object(compare_a))
        print(art.vs)
        compare_b = random.choice(data)
        if compare_a == compare_b:
            compare_b = random.choice(data)
        print(f"Compare B: " + print_object(compare_b))
        choice = input("Who has more followers? Type 'A' or 'B': ")
        if choice == compare(compare_a,compare_b):
            score += 1
            print(f"You're right! Current score: {score}")
            if choice == 'A':
                compare_a = compare_a
            else:
                compare_a = compare_b
            run = True
            os.system("clear")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            run = False
def main():
    run_program()


main()
