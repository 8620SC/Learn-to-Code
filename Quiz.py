def main():
    number_correct: int = 0
    answer_1 = input("1. Who was the president who allowed the public to celebrate his inauguration "
                     "in the White House?\n")
    if answer_1.lower() == "andrew jackson":
        print("Correct!")
        number_correct += 1
    else:
        print("Incorrect. The correct answer is Andrew Jackson, who allowed his supporters to join him in celebrating"
              "his inauguration in the White House. This proved to be a less than astute decision as his supporters"
              "smashed windows and broke several thousand dollars worth of china.")

    print()

    answer_2 = input("2. Who was the Minister of Aircraft Production for the UK during WWII?\n")
    if answer_2.lower() == "lord beaverbrook":
        print("Correct!")
        number_correct += 1
    else:
        print("Incorrect. The answer is Lord Beaverbrook, whose real name was Max Aitken, he was a close friend of "
              "Churchill's, he greatly increased the rate of aircraft production in GB by implementing radical"
              " emergency measures, this led to the Time magazine proclaiming during WWII that \"if [GB wins the war, "
              "it will be [Beaverbrook's] triumph.\" as he left a huge positive impact on GB's war effort.")

    print()

    answer_3 = input(
        "3. Who was Fidel Castro's right hand man who, in 1951, travelled 5000 mi across South America on a "
        "motorcycle?\n")
    if answer_3.lower() == "che guevara":
        print("Correct!")
        number_correct += 1

    else:
        print("Incorrect. The answer is Che Guevara, you probably know him because of a portrait"
              " that was taken of him, which is one of the most iconic images ever taken "
              "that shows him at a memorial service for the victims of an explosion.")

    print()

    answer_4 = input(
        "4. Speaking of communist Cuban leaders, which French existentialist philosopher was a huge fan of "
        "Fidel Castro?\n")

    if answer_4.lower() == "jean paul sartre":
        print("Correct!")
        number_correct += 1

    else:
        print(
            "Incorrect. The answer is Jean Paul Sartre, who is most famous for his book \"Being and "
            "Nothingness\" in which he coined the commonly used term \"bad faith\" to describe self-deception, "
            "or when people act a certain way but in reality want to act another way.")

    print()
    answer_5 = input(
        "5. No more boring history questions, let's move on to a question pertaining of one of my favorite "
        "sports, motorsports. Which iconic racing driver, who has the nickname \"Drift King\", had a cameo "
        "role in \"Fast and Furious: Tokyo Drift\" as a fisherman?\n")

    if answer_5.lower() == "keiichi tsuchiya":
        print("Correct!")
        number_correct += 1
    else:
        print("Incorrect. The answer is Keiichi Tsuchiya, who popularized drifting and is often thought to be the "
              "inspiration behind Takumi Fujiwara, the main character of the anime \"Initial D\", because his ride of "
              "choice is an ae86 and he used to be a street racer.")

    print("You earned a score of", number_correct / 5 * 100, "%")


main()
