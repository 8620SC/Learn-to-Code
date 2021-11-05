def main():
    while True:
        answer_1 = input(
            "1. Who was the president who allowed the public to celebrate his inauguration in the White House?\n")
        if answer_1.lower() == "andrew jackson":
            print("Correct!")
            break
        else:
            print(
                "Incorrect. Hint: He's a president that has a controversial legacy due to his treatment of Native "
                "Americans.")
            print()
            continue
    print()
    while True:
        answer_2 = input("2. Who was the Minister of Aircraft Production for the UK during WWII?\n")
        if answer_2.lower() == "lord beaverbrook":
            print("Correct!")
            break
        else:
            print("Incorrect. Hint: An animal's name is a part of his royal title.")
            print()
            continue
    print()
    while True:
        answer_3 = input(
            "3. Who was Fidel Castro's right hand man who, in 1951, travelled 5000 mi across South America on a "
            "motorcycle?\n")
        if answer_3.lower() == "che guevara":
            print("Correct!")
            break
        else:
            print("Incorrect. Hint: A portrait taken of him, which is one of the most iconic images ever taken, "
                  "shows him wearing a beret.")
            print()
            continue
    print()
    while True:
        answer_4 = input(
            "4. Speaking of communist Cuban leaders, which French existentialist philosopher was a huge fan of "
            "Fidel Castro?\n")

        if answer_4.lower() == "jean paul sartre":
            print("Correct!")
            break

        else:
            print(
                "Incorrect. Hint (but not really): He coined the term \"bad faith\" in his book \"Being and "
                "Nothingness\" to describe self-deception, or when people act a certain way but in reality want to act "
                "another way.")
            print()
            continue
    print()
    while True:
        answer_5 = input(
            "5. No more boring history questions, let's move on to a question pertaining of one of my favorite "
            "sports, motorsports. Which iconic racing driver, who has the nickname \"Drift King\", had a cameo "
            "role in \"Fast and Furious: Tokyo Drift\" as a fisherman?\n")

        if answer_5.lower() == "keiichi tsuchiya":
            print("Correct!")
            break

        else:
            print(
                "Incorrect. Hint: He is often thought to be the inspiration behind Takumi Fujiwara, the main character "
                "of the anime \"Initial D\", because his ride of choice is an ae86 and he used to be a street racer.")
            print()
            continue


main()
