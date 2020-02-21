import random

VOWELS = ["a", "e", "i", "o"]


class Player:
    def __init__(self):
        pass

    def count_guesses(self):
        guesses = 0
        guesses + 1


class Game:

    def __init__(self):
        self.player = Player()
        # self.open_file()
        self.start_game(self.open_file())

    def open_file(self):

        with open('words.txt', 'r') as file:
            data = file.read()
        word_list = [word for word in data.split()]
        random_word = random.choice(word_list)
        word_length = len(random_word)
        print(f'This is the random word {random_word}')
        split_word = list(random_word)
        game_word = ['_' * word_length]
        # print(f'This is the split word {split_word}')
        # print(f'This is the data {data}')
        return word_length, split_word, game_word

    def start_game(self, word_args):
        # self, word_length, split_words, guess_count
        # self.open_file(word_length, split_word, data)
        word_length = word_args[0]
        split_word = word_args[1]
        game_word = word_args[2]
        guess_count = 8
        letter_guesses = []

        print("This is a word guessing game.\nYou'll be given a random word, and you have 8 tries to guess that word.\n On each turn, you can guess a letter.\nAre you ready?")

        answer = input('"(Y)es" or "(N)o"?')

        if answer.lower() == "y":

            print(
                f"Great! I've picked a random word for you.\nIt has {word_length} characters. You have {guess_count} guesses remaining.")

            print(game_word)

            self.validate_input(split_word)

            # print('this is working')

            # print(random_word)

        elif answer.lower() == "n":

            print("Sorry! Please return when you're ready to take on the world!")
            exit()

        return word_length, split_word

    def validate_input(self, split_word):

        letter = input('Please choose a letter: ')
        letter = letter.lower()
        if len(letter) > 1:
            print("Please only guess one letter per turn!")
        if not letter.isalpha:
            print("There are only letters in the word; please guess again.")

        if letter.isalpha and len(letter) == 1:

            if letter in split_word:
                self.guess_right(letter, split_word)
            else:
                self.guess_wrong(letter, guess_count)

    def guess_right(self, letter, split_word):
        if letter in VOWELS:
            print(f'Yes! There is an {letter} in the word!')
        else:
            print(f'Yes! There is a {letter} in the word!')

        self.validate_input(split_word)

    def guess_wrong(self, letter, split_word, guess_count):

        if letter in VOWELS:
            print(f'Sorry, the word does not have a {letter}!')
        else:
            print(f'Sorry, the word does not have a {letter}!')

        print(f'Sorry,the word does not have a {letter}')
        guess_count - 1

        self.validate_input(split_word)

        return guess_count

    def won_game(self):
        pass
        # you won the game!
        #

    def lost_game(self):
        pass
        # you lost the game!


Game()


# def open_file(file):
#     with open(file) as file:
#         open_file = file.read()
#         print(type(open_file))

#     return open_file


# def print_word_freq(file):
#     # stores list as a string
#     list = open_file(file)
#     # splits string into iterable list
#     global split_list
#     split_list = list.split(',')
#     # prints list
#     # print(list)

#     return split_list


# print(split_list)


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
