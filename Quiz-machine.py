def element():
    Fire = 0
    Earth = 0
    Air = 0
    Water = 0

    print("For each question, type the letter of your answer and hit ENTER.\n")
    q1 = str(input("What is your favorite color?\nA: Red\nB: Blue\nC: Green\nD: White\n")).upper()
    if q1 == 'A':
        Fire += 1
    elif q1 == 'B':
        Water += 1
    elif q1 == 'C':
        Earth += 1
    elif q1 == 'D':
        Air += 1

    q2 = str(input("Where are you going on your ideal vacation?\nA: Beach\nB: Large City\nC: Mountains\nD: Desert\n")).upper()
    if q2 == 'A':
        Water += 1
    elif q2 == 'B':
        Fire += 1
    elif q2 == 'C':
        Air += 1
    elif q2 == 'D':
        Earth += 1

    q3 = str(input("What is your current mood?\nA: Content/Relaxed\nB: Happy\nC: Angry\nD: Energized\n")).upper()
    if q3 == 'A':
        Earth += 1
    elif q3 == 'B':
        Water += 1
    elif q3 == 'C':
        Fire += 1
    elif q3 == 'D':
        Air += 1

    q4 = str(input("Which season were you born in?\nA: Spring\nB: Summer\nC: Autumn\nD: Winter\n")).upper()
    if q4 == 'A':
        Water += 1
    elif q4 == 'B':
        Fire += 1
    elif q4 == 'C':
        Earth += 1
    elif q4 == 'D':
        Air += 1

    q5 = str(input("What is your eye color?\nA: Hazel\nB: Blue\nC: Green\nD: Black\n")).upper()
    if q5 == 'A':
        Fire += 1
    elif q5 == 'B':
        Water += 1
    elif q5 == 'C':
        Earth += 1
    elif q5 == 'D':
        Air += 1

    q6 = str(input("What color is your hair?\nA: Black\nB: Blonde\nC: Brown\nD: Red\n")).upper()
    if q6 == 'A':
        Earth += 1
    elif q6 == 'B':
        Air += 1
    elif q6 == 'C':
        Water += 1
    elif q6 == 'D':
        Fire += 1

    results = {'Fire': Fire, 'Earth': Earth, 'Air': Air, 'Water': Water}
    endResult = max(results, key=results.get)
    print("It looks like you are", str(endResult), "!")

def marvel():
    CapA = 0
    IronM = 0
    HawkE = 0
    Hulk = 0
    BlackW = 0
    Thor = 0

    print("For each question, type the letter of your answer and hit ENTER.\n")
    q1 = str(input("If you had a superpower what would it be?\nA: Flight\nB: Invisibility\nC: Super Strength\nD: Telekinesis\nE: Mind Control\nF: Shapeshifting")).upper()
    if q1 == 'A':
        CapA += 1
    elif q1 == 'B':
        BlackW += 1
    elif q1 == 'C':
        Hulk += 1
    elif q1 == 'D':
        Thor += 1
    elif q1 == 'E':
        IronM += 1
    elif q1 == 'F':
        HawkE += 1

    q2 = str(input("Who is your favorite Marvel Character that is not part of the Original Averger Team?\nA: Spider Man\nB: Dr. Strange\nC: Loki\nD: The Scarlett Witch\nE: Falcon\nF: The Black Panther")).upper()
    if q2 == 'A':
        IronM += 1
    elif q2 == 'B':
        Hulk += 1
    elif q2 == 'C':
        Thor += 1
    elif q2 == 'D':
        BlackW += 1
    elif q2 == 'E':
        CapA += 1
    elif q2 == 'F':
        HawkE += 1

    q3 = str(input("What is your favorite color?\nA: Black\nB: Green\nC: White\nD: Gold\nE: Red\nF: Blue")).upper()
    if q3 == 'A':
        BlackW += 1
    elif q3 == 'B':
        Hulk += 1
    elif q3 == 'C':
        HawkE += 1
    elif q3 == 'D':
        Thor += 1
    elif q3 == 'E':
        IronM += 1
    elif q3 == 'F':
        CapA += 1

    q4 = str(input("Which of the power stones is your favorite one?\nA: Reality\nB: Power\nC: Time\nD: Mind\nE: Soul\nF: Space")).upper()
    if q4 == 'A':
        HawkE += 1
    elif q4 == 'B':
        IronM += 1
    elif q4 == 'C':
        Hulk += 1
    elif q4 == 'D':
        CapA += 1
    elif q4 == 'E':
        BlackW += 1
    elif q4 == 'F':
        Thor += 1

    q5 = str(input("How would you describe yourself?\nA: A Leader\nB: An Intellectual\nC: Brave\nD: Powerful\nE: Loud\nF: Sneaky\n")).upper()
    if q5 == 'A':
        CapA += 1
    elif q5 == 'B':
        Hulk += 1
    elif q5 == 'C':
        BlackW += 1
    elif q5 == 'D':
        Thor += 1
    elif q5 == 'E':
        IronM += 1
    elif q5 == 'F':
        HawkE += 1

    results = {'Captain America': CapA, 'Iron Man': IronM, 'Hawk Eye': HawkE, 'Hulk': Hulk, 'Black Widow': BlackW, 'Thor': Thor}
    endResult = max(results, key=results.get)
    print("It looks like you are", str(endResult), "!")

def color():
    Red = 0
    Orange = 0
    Yellow = 0
    Green = 0
    Blue = 0
    Voilet = 0
    Pink = 0

    print("For each question, type the letter of your answer and hit ENTER.\n")
    q1 = str(input("Which of the following describes your best personality trait?\nA: Intellectual\nB: Ambitious\nC: Loyal\nD: Creative\nE: Optimistic\nF: Compassionate\nG: Generous \n")).upper()
    if q1 == 'A':
        Yellow += 1
    elif q1 == 'B':
        Red += 1
    elif q1 == 'C':
        Blue += 1
    elif q1 == 'D':
        Voilet += 1
    elif q1 == 'E':
        Orange += 1
    elif q1 == 'F':
        Pink += 1
    elif q1 == 'G':
        Green += 1

    q2 = str(input("Which of the following describes your worst personality trait?\nA: Selfish\nB: Impatient\nC: Pessimistic\nD: Conservative\nE: Aggressive\nF: Immature\nG: Emotional\n")).upper()
    if q2 == 'A':
        Green += 1
    elif q2 == 'B':
        Yellow += 1
    elif q2 == 'C':
        Orange += 1
    elif q2 == 'D':
        Blue += 1
    elif q2 == 'E':
        Red += 1
    elif q2 == 'F':
        Voilet += 1
    elif q2 == 'G':
        Pink += 1

    q3 = str(input("What is your favorite color?\nA: Red\nB: Orange\nC: Yellow\nD: Green\nE: Blue\nF: Voilet\nG: Pink\n")).upper()
    if q3 == 'A':
        Red += 1
    elif q3 == 'B':
        Orange += 1
    elif q3 == 'C':
        Yellow += 1
    elif q3 == 'D':
        Green += 1
    elif q3 == 'E':
        Blue += 1
    elif q3 == 'F':
        Voilet += 1
    elif q3 == 'G':
        Pink += 1

    q4 = str(input("What is your least favorite color?\nA: Red\nB: Orange\nC: Yellow\nD: Green\nE: Blue\nF: Voilet\nG: Pink\n")).upper()
    if q4 == 'A':
        Green += 1
    elif q4 == 'B':
        Blue += 1
    elif q4 == 'C':
        Voilet += 1
    elif q4 == 'D':
        Pink += 1
    elif q4 == 'E':
        Red += 1
    elif q4 == 'F':
        Orange += 1
    elif q4 == 'G':
        Yellow += 1

    q5 = str(input("What Indsutry is your dream job in?\nA: Travel/Leisure\nB: Environment/Agriculture\nC: Beauty and Fashion\nD: Philanthropic Work\nE: Food\nF: STEM\nG: Entertainment\n")).upper()
    if q5 == 'A':
        Yellow += 1
    elif q5 == 'B':
        Green += 1
    elif q5 == 'C':
        Pink += 1
    elif q5 == 'D':
        Voilet += 1
    elif q5 == 'E':
        Orange += 1
    elif q5 == 'F':
        Blue += 1
    elif q5 == 'G':
        Red += 1

    q6 = str(input("What is your current mood?\nA: Relaxed\nB: Creative\nC: Sad\nD: Energized\nE: Angry\nF: Excited\nG: Happy\n")).upper()
    if q6 == 'A':
        Green += 1
    elif q6 == 'B':
        Voilet += 1
    elif q6 == 'C':
        Blue += 1
    elif q6 == 'D':
        Pink += 1
    elif q6 == 'E':
        Red += 1
    elif q6 == 'F':
        Orange += 1
    elif q6 == 'G':
        Yellow += 1

    results = {'Red': Red, 'Orange': Orange, 'Yellow': Yellow, 'Green': Green, 'Blue': Blue, 'Voilet': Voilet, 'Pink': Pink}
    endResult = max(results, key=results.get)
    print("It looks like you are", str(endResult), "!")

def main():
    print("Hello and welcome to the quiz machine!")
    name = str(input("Please enter in your name: "))
    print("Okay, ", name, "! Let's get to work.\n")
    selection = int(input("Which quiz would you like to take? (Press the number corresponding to the quiz you want to take + ENTER)\n1. What element are you based off your personality?\n2. What original Avenger character are you?\n3. What color are you based off your personality?"))

    if selection == 1:
        element()
    elif selection == 2:
        marvel()
    elif selection == 3:
        color()
    else:
        print("That does not appear to be a valid selection. Let's try again")

    redo = input(("\nWanna take one again? Just press 'ENTER'! Press any other key + 'ENTER' to exit."))
    if redo == '':
        main()

    else:
        exit()


main()
