# Author: Daniel Flores
# Date: 2024/3/7


import random
import assets




global unknown_word_char_list
medal = assets.medal
loose = assets.loose
banner = assets.banner
word_list = assets.word_list
state_dic = assets.state_dic

def main():
    
    print(banner)
    
    unknown_word = word_list[random.randint(0,len(word_list) - 1)]
    double_letters = set()
    error_counter = 0
    playing = True
    win = False
    guessed_letters = "".join(len(unknown_word)*"_")
    
    
    while playing:
        unknown_word_char_list = list(unknown_word)
        new_letter = input("Write a letter in order to guess the word ===>    ").capitalize()
        if check_initial_conditions(new_letter, double_letters):
            if new_letter in unknown_word_char_list:
                guessed_letters = compute_guess_bar(new_letter, unknown_word, guessed_letters)
                print_state(error_counter, state_dic)
                print(f"{new_letter} ===> Correct!!          {guessed_letters}",)
                double_letters.add(new_letter)
                print(f"Used letters: \n{double_letters}")
                playing, win = check_final_conditions(error_counter, unknown_word, guessed_letters)
            else:
                error_counter += 1
                print_state(error_counter, state_dic)
                print(f"{new_letter} ===> Does not belong to the word!!          {guessed_letters}")
                double_letters.add(new_letter)
                print(f"Used letters: \n{double_letters}")
                playing, win = check_final_conditions(error_counter, unknown_word, guessed_letters)
    if win:
        print(medal)
        print(f'The word was {unknown_word}')
    else:
        print(loose)
        print(f'The unknown word was {unknown_word}')


def compute_guess_bar(new_letter, unknown_word, guessed_letters):
    indexes = []
    for i in range(0,len(unknown_word)):
        if unknown_word[i] == new_letter:
           indexes.append(i)
    guessed_letters_list = list(guessed_letters)
    for char in guessed_letters_list:
        if char == "_":
            for index in indexes:
                guessed_letters_list[index] = new_letter
    return "".join(guessed_letters_list)



def check_initial_conditions(new_letter, double_letters):
    if new_letter in double_letters:
        print(f'You have already typed {new_letter}')
        return False
    if len(new_letter) != 1:
        print("Write only one letter")
        return False
    return True

def check_final_conditions(error_counter, unknown_word, guessed_letters):
    if error_counter == 6 and unknown_word != guessed_letters:
        return False, False
    elif error_counter == 6 and unknown_word == guessed_letters:
        return False, True
    elif unknown_word == guessed_letters:
        return False, True
    else:
        return True, False
    

def print_state(error_counter, state_dic):
    print(state_dic.get(error_counter))

main()
 