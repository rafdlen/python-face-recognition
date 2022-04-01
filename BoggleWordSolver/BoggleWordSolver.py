class Tree:
    def __init__(self, letter=None):
        self.letter = letter
        self.children = {}
        self.leaf = False

    # add word, letter by letter
    def add(self, word):
        if len(word):
            letter = word[0]
            word = word[1:]
            if letter not in self.children:
                self.children[letter] = Tree(letter)
            return self.children[letter].add(word)
        else:
            self.leaf = True
            return self

    # locate letter in the tree
    def search(self, letter):
        if letter not in self.children:
            return None
        return self.children[letter]


# function for the actual word solver
def findWord(board, tree, validated, row, col, path=None, currLetter=None, word=None):
    letter = board[row][col]
    if path is None or currLetter is None or word is None:
        currLetter = tree.search(letter)
        path = [(row, col)]
        word = letter
    else:
        currLetter = currLetter.search(letter)
        path.append((row, col))
        word = word + letter

    # base cases
    if currLetter is None:  # prefix does not exist in dict
        return
    if currLetter.leaf:
        validated.add(word)  # word is valid

    # recurisve call
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < 4 and 0 <= c < 4 and r != row and c != col and (r, c) not in path:
                findWord(board, tree, validated, r, c, path[:], currLetter, word[:])


def main():
    # initialise game board based on user input
    board = []
    for i in range(0, 4):
        # append empty row
        board.append([])
        for j in range(0, 4):
            board[i].append(input().strip().upper())

    # print board
    for i in range(0, 4):
        for j in range(0, 4):
            print(board[i][j], end=" ")
        print()

    # load dictionary
    dictt = open("dictionary-yawl.txt", "r")

    tree = Tree()
    for line in dictt:
        word = line.rstrip().upper()
        tree.add(word)

    # set to store strings match valid found in the dictionary
    validated = set()

    # call the findWords function from each grid
    for row in range(0, 4):
        for col in range(0, 4):
            findWord(board, tree, validated, row, col)

    # print out valid words
    for word in sorted(validated):
        if len(word) > 2:
            print(word)


main()
