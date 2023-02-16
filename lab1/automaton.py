class FiniteAutomaton:
    def __init__(self, grammar):
        self.states = grammar.VN
        self.inputs = grammar.VT
        self.start_states = ["S"]
        self.final_states = self.findFinalStates(grammar.P)
        self.transitions = self.findTransitions(grammar.P)

    def findFinalStates(self, P):
        res = []
        for state in P.keys():
            for input in P[state]:
                flag = True
                for char in input:
                    if char in self.states:
                        flag = False
                        break
                if flag:
                    res.append(state)
                    break
        return res

    def findTransitions(self, P):
        res = {}
        for state in P.keys():
            for input in P[state]:
                inp = None
                toState = None
                for char in input:
                    if char in self.states:
                        toState = char
                    else:
                        inp = char
                if toState is None:
                    toState = state
                if (state, inp) not in res:
                    res[(state, inp)] = [toState]
                else:
                    res[(state, inp)].append(toState)
        print(res)
        return res
    
    def isAccepted(self, input_string):
        current_state = self.start_states[0]

        for symbol in input_string:
            if (current_state, symbol) not in self.transitions:
                return False
            current_state = self.transitions[(current_state, symbol)][0]

        return current_state in self.final_states

