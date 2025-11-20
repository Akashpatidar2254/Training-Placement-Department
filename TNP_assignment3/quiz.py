import question_bank as qb

score = 0


def start_quiz(cate):
    global score
    score = 0
    total_questions = len(cate)
    print("--- Quiz Starting ---")
    for q in cate:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"]):
            print(f"  {i + 1}. {option}")

        user_choice = input("write your answer (1, 2, 3, or 4): ")
        user_answer_text = ""
        if user_choice == "1":
            user_answer_text = q["options"][0]
        elif user_choice == "2":
            user_answer_text = q["options"][1]
        elif user_choice == "3":
            user_answer_text = q["options"][2]
        elif user_choice == "4":
            user_answer_text = q["options"][3]

        if user_answer_text == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was: {q['answer']}")

    print("\n--- Quiz Finished ---")
    print(f"Your final score is: {score} out of {total_questions}")