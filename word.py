import random


class Player:
    def __init__(self):
        pass


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
        print(f'This is the split word {split_word}')
        print(f'This is the data {data}')
        return word_length, split_word

    def start_game(self, word_args):
        # self.open_file(word_length, split_word, data)
        word_length = word_args[0]
        split_word = word_args[1]

        print("This is a word guessing game.\nYou'll be given a random word, and you have 8 tries to guess that word.\n On each turn, you can guess a letter.\nAre you ready?")

        answer = input('"(Y)es" or "(N)o"?')

        if answer.lower() == "y":

            print(
                f"Great! I've picked a random word for you.\nIt has {word_length} characters. You have 8 guesses.")

            self.guess(split_word)

            # print('this is working')

            # print(random_word)

        elif answer.lower() == "n":

            print("Sorry! Please return when you're ready to take on the world!")
            exit

        else:
            self.start_game(word_length, split_word)

        return word_length, split_word

    def guess(self, split_word):

        self.split_word = split_word
        '''
        check if input is letter
        '''

        letter = input('Please guess by choosing a letter: ')
        letter = letter.lower()
        if len(letter) > 1:
            print("Please only guess one letter per turn!")
        if not letter.isalpha:
            print("There are no numbers in the word; please guess again.")

        if letter.isalpha and len(letter) == 1:
            if letter in split_word:

                print(f'Yes! The word contains a {letter}!')


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
