import random
from colorama import init, Fore, Style
import debug
from debug import debug_print

# debug.debug_on()


class WordSearchBoard:
    def __init__(self, board_size_x, board_size_y):
        self.letter_positions = []
        self.word_search_board_size = [board_size_x, board_size_y]
        self.board = []
        self.search_words = []
        self.word_positions = []
        self.Color = Fore.BLUE

    def generate_board(self):  # generate a random board
        # list of alphabet to choose from


        line = []  # horizontal line of board
        for x_position in range(self.word_search_board_size[0]):  # add lines until length of board = board size x

            for y_position in range(self.word_search_board_size[1]):  # add letters on a line until line is at board size y
                line.append('-')  # add a - to each position

            self.board.append(line)  # add line to board
            line = []  # reset line to empty list
            debug_print(self.board, debug.Normal)

    def fill_board(self):
        if not self.board:
            self.generate_board()
        temp_board = []

        abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
        for line in self.board:
            temp_line = []
            for letter in line:
                if letter == '-':
                    temp_line.append(abc[random.randint(0, 25)])
                else:
                    temp_line.append(letter)
            temp_board.append(temp_line)
        self.board = temp_board

    def pretty_board(self, cheat_sheet=False):

        y_pos = 0
        pretty_text = ''
        for line in self.board:
            x_pos = 0
            for letter in line:
                axis_xy = {'x': x_pos, 'y': y_pos}
                debug_print(axis_xy, debug.Info)
                pretty_text += ' | '
                if axis_xy in self.letter_positions:  # see if current letter is in list of letter in words
                    debug_print(f'{axis_xy} in letter positions')
                    pretty_text += f'{self.Color}' + letter + f'{Style.RESET_ALL}'
                else:
                    pretty_text += letter
                x_pos += 1
            y_pos += 1
            pretty_text += ' |\n'
        return pretty_text

    def find_words(self):
        self.word_positions = []  # set empty list for positions of words
        self.letter_positions = []
        # create list of backwards words
        backwards_words = []
        for word in self.search_words:
            backwards_word = ''
            for letter in word:
                backwards_word = letter + backwards_word
            backwards_words.append(backwards_word)
        # add all backwards words to list of original words
        for word in backwards_words:
            self.search_words.append(word)

        def find_words_str(string, direction):
            for word in self.search_words:
                word_pos = string.find(word.upper())
                if word_pos > -1:
                    word_pos_dict = {
                        'word': word,
                        'y_pos': y_pos,
                        'x_pos': word_pos,
                        'direction': direction
                    }
                    letter_x = 0
                    while letter_x <= len(word) - 1:
                        letter_pos = {'x': word_pos + letter_x, 'y': y_pos}

                        self.letter_positions.append(letter_pos)
                        letter_x += 1
                    self.word_positions.append(word_pos_dict)

        y_pos = 0
        # Horizontal
        for line in self.board:
            text_line = ''
            debug_print(line)
            for letter in line:
                debug_print(letter)
                text_line += letter.upper()
            find_words_str(text_line, 'h')
            y_pos += 1


        return self.word_positions, self.letter_positions






my_board = [
    ['T', 'E', 'S', 'T', '-', 'W', '-', '-'],
    ['-', '-', '-', '-', '-', 'O', '-', '-'],
    ['-', '-', '-', '-', '-', 'R', '-', '-'],
    ['-', '-', '-', 'H', 'E', 'L', 'L', 'O'],
    ['-', '-', '-', '-', '-', 'D', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', 'B', 'O', 'O', 'N', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-']
]

board = WordSearchBoard(10, 8)
board.generate_board()
print(board.pretty_board())
board.board = my_board
print(board.pretty_board())
board.fill_board()
print(board.pretty_board())
board.search_words = ['hello', 'world', 'noob', 'TEST']
words = board.find_words()

print(board.pretty_board())
print(words)
