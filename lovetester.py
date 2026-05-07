import random

def love_calculator():
    name1 = input("Enter first name: ").strip().lower()
    name2 = input("Enter second name: ").strip().lower()

    combined = name1 + name2
    score_seed = sum(ord(char) for char in combined)

    random.seed(score_seed)
    love_percentage = random.randint(0, 100)

    print(f"\n💖 Love result for {name1.title()} and {name2.title()}: {love_percentage}% 💖")

    if love_percentage > 80:
        print("Amazing match!")
    elif love_percentage > 50:
        print("Pretty good compatibility!")
    elif love_percentage > 30:
        print("There might be something there...")
    else:
        print("Maybe better as friends 😅")

love_calculator()