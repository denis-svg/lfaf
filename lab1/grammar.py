import random
from automaton import FiniteAutomaton

class Grammar:
    def __init__(self, VN, VT, P) -> None:
        self.VN = VN
        self.VT = VT
        self.P = P

    def generateString(self, n, non_terminal='S'):
        # Base case: if n == 0, return an empty string
        if n == 0:
            return ''

        # Choose a random production for the current non-terminal symbol
        production = random.choice(self.P[non_terminal])

        # Initialize an empty string to hold the generated word
        word = ''

        # Loop through the symbols in the production
        for symbol in production:
            if symbol in self.VN:
                # If the symbol is a non-terminal, recursively generate a random word from its productions
                word += self.generateString(1, symbol)
            else:
                # If the symbol is a terminal, add it to the word
                word += symbol

        # Recurse with n-1 to generate the rest of the word
        return word + self.generateString(n-1, non_terminal)
    
    def getAutomaton(self):
        return FiniteAutomaton(self)