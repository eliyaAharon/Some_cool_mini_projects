import random


def pick_twitter():
    twitter_list = [
        {"name": "Eliya Aharon",
         "Followers": 1110,
         "age": 20,
         },
        {
            "name": "Yair kahana",
            "Followers": 128,
            "age": 20,
        }
        ,
        {
            "name": "Beni biton",
            "Followers": 46,
            "age": 20,
        }
        ,
        {
            "name": "Shaul",
            "Followers": 1200,
            "age": 31,
        }
        ,
        {
            "name": "Tali",
            "Followers": 2500,
            "age": 24,
        }
        ,
        {
            "name": "The thinking",
            "Followers": 2000,
            "age": 49,
        }
    ]

    return random.choice(twitter_list)


flag = True
hopes = 0
while flag:

    user_a = pick_twitter()
    user_b = pick_twitter()
    while user_a == user_b:
        user_b = pick_twitter()

    print(f"Compare A: {user_a['name']}, {user_a['age']} yeas old \n")
    print(f"Against B {user_b['name']} , {user_b['age']} years old")
    ans = input("who has more followers? Type 'A' or 'B'")
    if ans == 'A':
        if user_a["Followers"] > user_b["Followers"]:
            hopes = hopes + 1
        else:
            flag = False
    elif ans == 'B':
        if user_b["Followers"] > user_a["Followers"]:
            hopes = hopes + 1
        else:
            flag = False
            break

    print(f"You have {hopes} hopes")
print(f"Oops you failed, you has {hopes} hopes")
