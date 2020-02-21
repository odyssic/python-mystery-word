import secrets


def open_file(file):
    with open(file) as file:
        open_file = file.read()
        print(type(open_file))

    return open_file

    # print(open_file)


def print_word_freq(file):

    list = open_file(file)
    # print(list)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)


class Player:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        self.player = Player()
        self.start_game()

    def start_game(self):
        print("This is a word guessing game.\nYou'll be given a random word, and you have 8 tries to guess that word.\n On each turn, you can guess a letter.\nAre you ready to proceed?")

        answer = input('"(Y)es" or "(N)o"?')

        if answer == "Y":

            print(
                "Great! I've picked a random word for you.\nYou have 8 guesses.\nPLease choose a letter: ")

            print(random_word)

    def guess(self):
        '''
        check if input is letter
        '''

        letter = input('Please guess by typing a letter: ')
        if letter is in string:
            print(f'Yes! The word contains a {Letter}!')

        random_word = secrets.choice(list)

        s = 'a123b'

        for char in s:
        print(char, char.isalpha())


Game()
