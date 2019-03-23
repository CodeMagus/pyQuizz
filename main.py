from gamedata.game_functions import *
import random
# TODO: Make possible for the player to choose a language or play with OS settings
score = 0
POINTS = 10
all_answers = extract_answers(anime_quiz)
random.shuffle(anime_quiz)

for question in anime_quiz:
    good_answer = question.answer
    bad_answers = remove_answer(good_answer, all_answers)
    answers = new_list(good_answer, bad_answers)
    print("[QUESTION]: {}".format(question.question))
    display(answers)
    is_valid = check_answer(get_player_input(), question, answers)
    if is_valid:
        score += POINTS
        print("+ {} POINTS!\n\n\n".format(POINTS))
    clear_console()

print("{}{}".format(SCORE_DISPLAY_MESSAGE[LANG_CODE], score))
