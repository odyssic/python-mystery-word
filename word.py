import random

VOWELS = ["a", "e", "i", "o"]

# class Player:

#     def __init__(self):
#         pass
#         guess_count = 0
#         guesses = []
#         guess_count = self.guess_count


# def count_guesses(self, guesses, guess_count):

#     pass
#     if Game.guess_wrong:
#         self.guess_count = self.guess_count - 1


class Game():

    def __init__(self):  # constructor
        # self.player = Player()
        # self.open_file()
        # self.random_word(self.open_file())
        self.open_file()
        # Player()
        self.split_word = []
        self.game_word = []
        self.playing = True
        self.letter_list = []
        self.hidden_word = []
        # self.word_list = word_list

    def open_file(self):

        with open('words.txt', 'r') as file:
            data = file.read()
        self.random_word(data)
        return data

    def random_word(self, data):

        word_list = [word for word in data.split()]
        random_word = random.choice(word_list)
        word_length = len(random_word)
        print(f'This is the random word {random_word}')
        split_word = list(random_word)
        hidden_word = ['_' * word_length]
        guess_count = 8

        print(
            f"I've picked a random word for you.\nIt has {word_length} characters.")

        print(hidden_word)

        self.validate_input(split_word, guess_count, hidden_word)
        return hidden_word, split_word, guess_count

    def validate_input(self, split_word, guess_count, hidden_word):
        print(f'You have  {guess_count} guesses remaining.')
        letter = input('Please choose a letter: ')

        letter = letter.lower().strip()

        if len(letter) > 1:
            print("Please only guess one letter per turn!")
        if not letter.isalpha:
            print("There are only letters in the word; please guess again.")

        if letter.isalpha and len(letter) == 1:

            if letter in split_word:
                self.guess_right(letter, split_word, guess_count, hidden_word)
            else:
                self.guess_wrong(letter, split_word, guess_count, hidden_word)

        return letter

    def guess_right(self, letter, split_word, guess_count, hidden_word):
        if letter in VOWELS:
            print(f'Yes! There is an {letter} in the word!')
        else:
            print(f'Yes! There is a {letter} in the word!')

        self.alter_hidden_word(letter, split_word, guess_count, hidden_word)

    def alter_hidden_word(self, letter, split_word, guess_count, hidden_word):

        for letter in split_word:
            i = split_word.index(letter)
            hidden_word = hidden_word[i].replace('_', letter)
        print('alter hidden split word:', split_word)
        print('alter_hidden: ', hidden_word)
        print('index of letter in alter hidden:', i)

        self.validate_input(split_word, guess_count, hidden_word)

        return hidden_word

    def guess_wrong(self, letter, split_word, guess_count, hidden_word):
        guess_count = guess_count - 1

        if letter in VOWELS:
            print(f'Sorry, the word does not have a {letter}!')
        else:
            print(f'Sorry, the word does not have a {letter}!')

        self.validate_input(split_word, guess_count, hidden_word)

        return guess_count

    # def won_game(self):
    #     pass
    #     # you won the game!
    #     #

    # def lost_game(self, split_word, word_length):
    #     pass

    #     print("You lost this time! would you like to play again? ")
    #     answer = input('"(Y)es" or "(N)o"?')

    #     if answer.lower() == "y":

    #         print(
    #             f"Great! I've picked a random word for you.\nIt has {word_length} characters. You have  guesses remaining.")

    #         print(self.game_word)

    #         self.validate_input(split_word, hidden_word)

    #         # print('this is working')

    #         # print(random_word)

    #     elif answer.lower() == "n":

    #         print("Thank you for playing. We'll see you again soon! Goodbye!")
    #         exit()

    #     return word_length, split_word

    #     pass
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
