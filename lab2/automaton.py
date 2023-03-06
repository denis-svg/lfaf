import grammar

class FiniteAutomaton:
    def __init__(self, states, inputs, start_states, final_states, transitions):
        self.states = states
        self.inputs = inputs
        self.start_states = start_states
        self.final_states = final_states
        self.transitions = transitions

    
    def isAccepted(self, input_string):
        current_state = self.start_states[0]

        for symbol in input_string:
            if (current_state, symbol) not in self.transitions:
                return False
            current_state = self.transitions[(current_state, symbol)][0]

        return current_state in self.final_states
    
    def toGrammar(self):
        p = {}
        for key in self.transitions.keys():
            if key[0] not in p:
                p[key[0]] = []
            for comb in self.transitions[key]:
                p[key[0]].append(key[1] + comb)
        return grammar.Grammar(self.states, self.inputs, p)
    
    def isNfa(self):
        # every state cannot got though other states with same input
        for key in self.transitions.keys():
            if len(self.transitions[key]) > 1:
                return True

        # every state must go through every input once
        occcurences = {}
        for key in self.transitions.keys():
            if key[0] not in occcurences:
                occcurences[key[0]] = set()
            occcurences[key[0]].add(key[1])
        
        inputs_set = set(self.inputs)
        for key in occcurences.keys():
            if inputs_set != occcurences[key]:
                return True

        return False
    
    def nfa_to_dfa(self):
        queue = [{'q0'}]
        dfa = {}
        conv = {}
        dfa_fin_states = []
        it = 0

        while queue:
            state = queue.pop(0)
            for inp in self.inputs:
                for st in state:
                    if (st, inp) in self.transitions:
                        # print((st, inp), self.transitions[(st, inp)])
                        if ('q' + str(it), inp) not in dfa:
                            dfa[('q' + str(it), inp)] = []
                            conv['q' + str(it)] = state
                        for st2 in self.transitions[(st, inp)]:
                            if st2 not in dfa[('q' + str(it), inp)]:
                                dfa[('q' + str(it), inp)].append(st2)

            for key in dfa:
                if set(dfa[key]) not in conv.values():
                    queue.append(set(dfa[key]))
                    if self.final_states[0] in dfa[key]:
                        dfa_fin_states.append(dfa[key])
            
            it += 1
        
        for key in dfa:
            for key2 in conv:
                if conv[key2] == set(dfa[key]):
                    dfa[key] = [key2]
        
        converted_dfa_fin_states = []
        for st in dfa_fin_states:
            for key2 in conv:
                if conv[key2] == set(st):
                    converted_dfa_fin_states.append(key2)
        return FiniteAutomaton(list(conv.keys()), self.inputs, self.start_states, converted_dfa_fin_states, dfa)

        
        


