

import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    hangman game
    """
    ans = random_word()
    guess = ''
    record = ''
    hearts = N_TURNS
    dying = '    ----------\n' \
            '    |        |\n'\
            '    |\n'\
            '    |\n'\
            '    |\n'\
            '    |\n'\
            '    |\n'\
            '    |\n'\
            '    |\n'\
            '---------'
    for i in range(len(ans)):
        guess += '-'
    print('The word like '+guess+'\n'+dying)
    print('You have '+str(hearts)+' wrong guesses left.')
    input_ch = asking()
    while True:
        record = guess
        # record the guess before
        if input_ch in ans:
            guess = ''
            for i in range(len(ans)):
                if input_ch in ans[i]:
                    guess += input_ch
                else:
                    guess += record[i]
            print('You\'r correct!')
        else:
            hearts -= 1
            dying = dying_man(hearts)
            print('There\'s no '+input_ch+' in the word')
        if hearts == 0:
            break
        if guess.isalpha():
            break
        else:
            print('The word like ' + guess+'\n'+dying)
            print('You have ' + str(hearts) + ' wrong guesses left.')
        input_ch = asking()
    if hearts == 0:
        print('You are completely hung :(\n'+dying)
    else:
        print('You win!!')
    print('The word was: ' + ans)


def asking():
    """
    input the guess
    """
    input_ch = input('Your guess: ').upper()
    while not input_ch.isalpha() or len(input_ch) > 1:
        print('Illegal format.')
        input_ch = input('Your guess: ').upper()
    return input_ch


def dying_man(heart):
    if heart == N_TURNS - 1:
        return '    ----------\n' \
               '    |        |\n'\
               '    |       ( )\n'\
               '    |\n'\
               '    |\n'\
               '    |\n'\
               '    |\n'\
               '    |\n'\
               '    |\n'\
               '---------'
    elif heart == N_TURNS - 2:
        return '    ----------\n' \
               '    |        |\n'\
               '    |       ( )\n'\
               '    |        |\n'\
               '    |        |\n'\
               '    |        |\n'\
               '    |\n'\
               '    |\n'\
               '    |\n'\
               '---------'
    elif heart == N_TURNS - 3:
        return '    ----------\n' \
               '    |        |\n'\
               '    |       ( )\n'\
               '    |        |\n'\
               '    |        |\n'\
               '    |        |\n'\
               '    |       /\n'\
               '    |      /\n'\
               '    |\n'\
               '---------'
    elif heart == N_TURNS - 4:
        return '    ----------\n' \
               '    |        |\n'\
               '    |       ( )\n'\
               '    |        |\n'\
               '    |        |\n'\
               '    |        |\n'\
               '    |       / \\\n'\
               '    |\n'\
               '---------'
    elif heart == N_TURNS - 5:
        return '    ----------\n' \
               '    |        |\n' \
               '    |       ( )\n' \
               '    |       /|\n' \
               '    |      / |\n' \
               '    |        |\n' \
               '    |       / \\\n' \
               '    |      /   \\\n' \
               '    |\n' \
               '---------'
    elif heart == N_TURNS - 6:
        return '    ----------\n' \
               '    |        |\n' \
               '    |       ( )\n' \
               '    |       /|\\\n' \
               '    |      / | \\\n' \
               '    |        |\n' \
               '    |       / \\\n' \
               '    |      /   \\\n' \
               '    |\n' \
               '---------'
    elif heart == N_TURNS - 7:
        return '    ----------\n' \
               '    |        |\n' \
               '    |       (xx)\n' \
               '    |       /|\\\n' \
               '    |      / | \\\n' \
               '    |        |\n' \
               '    |       / \\\n' \
               '    |      /   \\\n' \
               '    |\n' \
               '---------'


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()