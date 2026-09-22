import sys


OWL_ART = """
              --                        --
          -==========              -=========-
         ==================- =================-
        -==========-================-===========
        -=======------============----=-========
        -======--------==========---------======
        -====------------======-------------====
        -===--------------------------------====
        -===-::-------------------------:.:--===
        -===-:..:+++=--------------=+*+:..:--===
      -=====-:..:*###*.:--------:.*###+:..:--=====
    ========--...-*#*-..---::---..-*#*-...---=======
  ==========-----:....:----------:...::-----==========
 ============-------:----=--====-----------============
================------=============-----================
========================================================
 ======================================================
  ===================================================-
    ================================================
      ============================================
        ========================================
        -==================--===================
          -  ==============================  -
              -===========================
             ===============================
             ===============================
             -=======-             =======-
"""


# ---------- Commands ----------

def show_help():
    print("--- 🧭 Command List ---")
    print("  /help or ?  = show this list")
    print("  /dict       = show the dictionary")
    print("  /quit       = quit (you lose your streak!)")
    print("-----------------------")


def show_dictionary():
    print("--- 📖 Duolingo Dictionary 📖 ---")
    print("ik = I            boterham = sandwich")
    print("ben = am          een = a/an")
    print("jij = you         jongen = boy")
    print("bent = are        meisje = girl")
    print("spreek = talk     Nederlands = Dutch")
    print("hallo = hi        ja = yes")
    print("doei = bye        nee = no")
    print("water = water     brood = bread")
    print("drink = drink     eet = eat")
    print("hij = he          vrouw = woman")
    print("-----------------------------------")


def ask(prompt):
    """
    Works like input(), but understands the room commands.
    ? and /help show the help menu.
    /dict shows the dictionary.
    /quit exits the entire game.
    """

    while True:
        text = input(prompt).strip().lower()

        if not text.startswith("/") and text != "?":
            return text

        if text == "?" or text == "/help":
            show_help()

        elif text == "/dict":
            show_dictionary()

        elif text == "/quit":
            print("You have lost your streak🔥... Doei!")
            raise SystemExit

        else:
            print("Unknown command. Type /help to see the list.")


def enterRoom6(state):

    if state["visited"]["room6"]:
        print()
        print("The Duolingo ghost looks at you again... 🦉👻")
        print("You've already completed your lesson here.")
        print("There doesn't seem to be anything else for you.")
        return "corridor"

    state["visited"]["room6"] = True

    print("")
    print("")
    print("                       --.")
    print("                    ---------")
    print("                   -------------")
    print("        ---       -----------------------------")
    print("       --------   -----    ---------------------")
    print("       --------------    .   --------------------")
    print("        -------------  ))))  --------     ------.")
    print("        ----------------))) -------   ))   -----")
    print("         --------------------....-- ))))   ----")
    print("           ------------------***--- ((*--.--------------")
    print("             .---------------***------------------------")
    print("              -----------------------------------------")
    print("              ----------------------------------------")
    print("               ------------------------------------")
    print("         ---    -----------------------------.")
    print("         ----    -------------------------")
    print("          ----     ---------------------")
    print("                      ---------------")
    print("                            ...         --")
    print("                                     ------")
    print("                                     ---.")

    print("")
    print("(Duolingo ghost appears🦉👻)")

    ask(
        "You haven't done your lesson today... \n"
        "What do you have to say in your defense?🤨:"
    )

    print("")
    print("")
    print("")

    print("                    .)))((/*        .-----..")
    print("                   ##))((((//*-///***----......")
    print("                  ###))((((((((///**----........")
    print("                  ###))(((((((////**----.........")
    print("                  ###))(((((((////**---...........")
    print("                  ###)))((((((////**----..........")
    print("                  ###))))((((((///**----....###. .")
    print("                  ####))))(((((///**---........  ...")
    print("                  (((()))))((((///**---...........*")
    print("               ((/--..())(*...-//**----...........")
    print("             )((/*---(((*---..-***-------.........")
    print("            ))(//***(((/////***-------***-.....*..")
    print("            ))(/////((////***---------****-...-..")
    print("            #))((//((((//***-----------***--.--..")
    print("             #))(((()((///***----------***---...*.")
    print("              #)))((())((//*****-------***----**-..")
    print("                 ))))))))(((///////*************-")
    print("")

    attempts = 0

    wrong_replies = [
        "I couldn't quite understand you, could you repeat?😅",
        "Hablo Espanol?🫩",
        "Sprechen Sie Deutsch?🫩",
        "Parli italiano?",
        "Parles-tu francais?",
        "We don't have time for this tom foolery",
    ]

    while True:

        if attempts == 0:
            prompt = (
                "Excuses, excuses. Let's work on your Dutch shall we👀? "
                "\n(Y/N):"
            )
        else:
            prompt = (
                wrong_replies[
                    min(attempts - 1, len(wrong_replies) - 1)
                ]
                + "\n(Y/N):"
            )

        choice = ask(prompt)

        if choice == "y":

            if attempts >= 2:
                print("Too bad, we are doing Dutch today💩!")

            break

        elif choice == "n":

            print()
            print(
                "You have lost your streak🔥... \nof the days you've "
                "been walking this earth😈\n"
                "GAME OVER."
            )

            raise SystemExit

        else:
            attempts += 1

    show_dictionary()

    correct = 0
    wrong = 0


    q1 = False

    while not q1:

        print(
            "---First Task: How will you say "
            "'I am a sandwich' in Dutch?---"
        )

        print("  A) Ik ben een boterham")
        print("  B) Jij bent een boterham")
        print("  C) Ik eet en boterham")

        answer = ask("Your answer \n(A/B/C):")

        if answer == "a":

            print("Juist🦉!")

            correct += 1
            q1 = True

        else:

            wrong += 1

            print(OWL_ART)
            print("Fout, Try again lil bro😕")

    q2 = False

    while not q2:

        print(
            "---Second Task: Fill in the missing word: "
            "'Jij ____ een jongen'---"
        )

        answer = ask("Your answer:")

        if answer == "bent":

            print("Goed zo!🦉")

            correct += 1
            q2 = True

        else:

            wrong += 1

            print(OWL_ART)
            print("Probeer je het zelfs?😠")


    q3 = False

    while not q3:

        print(
            "---Third Task: How will you say "
            "'He drinks water' in Dutch?---"
        )

        print("  A) Ik eet water")
        print("  B) Jij drinkt water")
        print("  C) Hij drinkt water")

        answer = ask("Your answer \n(A/B/C):")

        if answer == "c":

            print("Juist (Correct)")

            correct += 1
            q3 = True

        else:

            wrong += 1

            print("Ik heb je beter geleerd dan dit...🙈")

    q4 = False

    while not q4:

        print(
            "---Fourth Task: Fill the missing word: "
            "'Ik ____ brood' (I eat bread)---"
        )

        answer = ask("Write the missing word:")

        if answer == "eet":

            print("Hoo hoo, great job🦉")

            correct += 1
            q4 = True

        else:

            wrong += 1

            print("Zo slecht🫩")

    q5 = False

    while not q5:

        print(
            "---Fifth Task: How will you say "
            "'I speak Dutch' in Dutch?---"
        )

        print("  A) Ik bent Nederlands")
        print("  B) Ik spreek Nederlands")
        print("  C) Jij bent Nederlands")

        answer = ask("Your answer \n(A/B/C):")

        if answer == "b":

            print("Perfect👻🎶")

            correct += 1
            q5 = True

        else:

            wrong += 1

            print("Je zou Duolingo premie moeten krijgen🦉")

    q6 = False

    while not q6:

        print(
            "---Sixth Task: Fill the missing words: "
            "'___ bent een ___' (You are a woman)---"
        )

        answer = ask("Your answer:")

        if answer == "jij vrouw":

            print(
                "Correcto, you have done a great job today🎊"
            )

            correct += 1
            q6 = True

        else:

            wrong += 1

            print("It's almost over, you can do it🦉")

    print()
    print(f"Lesson complete! Correct: {correct} | Wrong: {wrong}")
    print("The Duolingo ghost lets you leave... for now. 🦉👻")
    print()

    return "corridor"
