from art import logo,vs
from game_data import data
import random
import os

def greater(a,b):
    if a['follower_count']>b['follower_count']:
        return 'A'
    else:
        return 'B'

def game_ui(a_entry,b_entry):
    print(f"Compare A: {a_entry['name']}, a {a_entry['description']}, form {a_entry['country']}")
    print(vs)
    print(f"Compare B: {b_entry['name']}, a {b_entry['description']}, form {b_entry['country']}")

print(logo)
score = 0
a_entry = random.choice(data)
b_entry = random.choice(data)
game_ui(a_entry,b_entry)
ans = greater(a_entry,b_entry)
player_ans = input('Who has more followers? Type "A" or "B": ')
first_entry = b_entry
while player_ans == ans:
    os.system('cls')
    print(logo)
    score+=1
    print(f"You're right! Current score: {score}")
    c_entry = random.choice(data)
    game_ui(first_entry,c_entry)
    ans = greater(first_entry,c_entry)
    player_ans = input('Who has more followers? Type "A" or "B": ')
    first_entry = c_entry
print(f"Sorry, that's wrong. Final score: {score}")





