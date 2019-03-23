import random
import time
import os
from gamedata.game_strings import *
from gamedata.parameters import *
from gamedata.quizzes import *
from gamedata.system_infos import *


def get_all_data():
    """Returns a dictionary containing all quizzes
        Key: Quiz Name
        Value: List of questions"""
    return all_quizzes


def extract_answers(quiz):
    all_answers = []
    for questions in quiz:
        all_answers.append(questions.answer)

    return all_answers


def load_question(quiz, index):
    return quiz[index]


def remove_answer(right_answer, all_answers):
    return [answer for answer in all_answers if answer != right_answer]


def new_list(answer, filtered_answers):
    if ANSWERS_TO_DISPLAY > MAX_ANSWERS_DISPLAYABLE:
        raise Exception("Cannot display so many answers. Go to parameters.py to edit.")
    merged_answers = list()
    merged_answers.append(answer)

    while len(merged_answers) < ANSWERS_TO_DISPLAY:
        answer_to_append = random.choice(filtered_answers)
        merged_answers.append(answer_to_append)
        filtered_answers.remove(answer_to_append)

    random.shuffle(merged_answers)

    return merged_answers


def display(answers):
    for index, answer in enumerate(answers):
        time.sleep(DISPLAY_INTERVAL)
        print("#{}\t\t{}".format(index, answer))


def get_player_input():
    while True:
        choice = input(CHOICE_PROMPT_MESSAGE[LANG_CODE])
        try:
            choice = int(choice)
        except TypeError:
            print(INVALID_NUM_MESSAGE[LANG_CODE])
            continue
        else:
            return choice


def check_answer(player_choice, question, answers):
    selected_answer = answers[player_choice]
    return selected_answer == question.answer


def clear_console():
    os.system("cls")
