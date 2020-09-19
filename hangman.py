import random

def hangman():
    word_list = ['Python', 'Java', 'computer', 'hacker', 'painter']
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ['','_____     ','|         ','|    |    ','|    o    ','|   /|\   ','|   / \   ']
    remaining_letters = list(word)
    letter_board = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ！')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input('1文字を予想してね')
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '_' not in letter_board:
            print('あなたの勝ち！ The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses+1]))
        print('あなたの負け！正解は {}'.format(word))

hangman()
