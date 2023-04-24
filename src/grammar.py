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
    
    def findFinalStates(self):
        res = []
        for state in self.P.keys():
            for input in self.P[state]:
                flag = True
                for char in input:
                    if char in self.VN:
                        flag = False
                        break
                if flag:
                    res.append(state)
                    break
        return res

    def findTransitions(self):
        res = {}
        for state in self.P.keys():
            for input in self.P[state]:
                inp = None
                toState = None
                for char in input:
                    if char in self.VN:
                        toState = char
                    else:
                        inp = char
                if toState is None:
                    toState = state
                if (state, inp) not in res:
                    res[(state, inp)] = [toState]
                else:
                    res[(state, inp)].append(toState)
        return res

    def getAutomaton(self):
        return FiniteAutomaton(self.VN, self.VT, ["S"], self.findFinalStates(), self.findTransitions())
    
    def convert_to_chomsky_normal_form(self):
        # Step 1: Eliminate all productions with epsilon
        for v in self.VN:
            if [] in self.P[v]:
                self.P[v].remove([])

        # Step 2: Replace all unit productions A -> B with A -> C, where C -> B is a production
        unit_productions = set()
        for v in self.VN:
            for p in self.P[v]:
                if len(p) == 1 and p[0] in self.VN:
                    unit_productions.add((v, p[0]))

        for (v, u) in unit_productions:
            for p in self.P[u]:
                if p != [] and p not in self.P[v]:
                    self.P[v].append(p)

        # Step 3: Replace all non-unit productions A -> w with A -> BC, where B -> x and C -> y are productions
        new_productions = []
        for v in self.VN:
            for p in self.P[v]:
                if len(p) > 1:
                    for i in range(len(p)):
                        if p[i] in self.VT:
                            new_productions.append((p[i], [], [p[i]]))
                            p[i] = new_productions[-1][0]

                    while len(p) > 2:
                        B = p.pop(-1)
                        C = p.pop(-1)
                        new_variable = "X" + str(len(self.VN) + len(new_productions) + 1)
                        self.VN.append(new_variable)
                        self.P[new_variable] = [[C, B]]
                        new_productions.append((new_variable, [C, B], []))
                        p.append(new_variable)

        # Step 4: Eliminate any remaining unit productions
        unit_productions = set()
        for v in self.VN:
            for p in self.P[v]:
                if len(p) == 1 and p[0] in self.VN:
                    unit_productions.add((v, p[0]))

        while unit_productions:
            (v, u) = unit_productions.pop()
            for p in self.P[u]:
                if p != [] and p not in self.P[v]:
                    self.P[v].append(p)

                    if len(p) == 1 and p[0] in self.VN:
                        unit_productions.add((v, p[0]))

        return self

    