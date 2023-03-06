# The title of the work

### Course: Formal Languages & Finite Automata
### Author: Prodan Denis FAF-211

----

## Theory
&ensp;&ensp;&ensp; A finite automaton is a mechanism used to represent processes of different kinds. It can be compared to a state machine as they both have similar structures and purpose as well. The word finite signifies the fact that an automaton comes with a starting and a set of final states. In other words, for process modeled by an automaton has a beginning and an ending.

&ensp;&ensp;&ensp; Based on the structure of an automaton, there are cases in which with one transition multiple states can be reached which causes non determinism to appear. In general, when talking about systems theory the word determinism characterizes how predictable a system is. If there are random variables involved, the system becomes stochastic or non deterministic.

&ensp;&ensp;&ensp; That being said, the automata can be classified as non-/deterministic, and there is in fact a possibility to reach determinism by following algorithms which modify the structure of the automaton.



## Objectives:
1. Understand what an automaton is and what it can be used for.

2. Continuing the work in the same repository and the same project, the following need to be added:
    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.
    
    d. Represent the finite automaton graphically (Optional, and can be considered as a __*bonus point*__):
      
    - You can use external libraries, tools or APIs to generate the figures/diagrams.
        
    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.





## Implementation description

'''
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
'''


This code defines a class called FiniteAutomaton which represents a deterministic or non-deterministic finite automaton. The constructor takes in the states, inputs, start states, final states, and transitions of the automaton. The class has methods to check whether a given input string is accepted by the automaton, to convert the automaton to a grammar, to check whether the automaton is a non-deterministic finite automaton, and to convert a non-deterministic finite automaton to a deterministic finite automaton.

The isAccepted method takes an input string as input and returns True if the automaton accepts the input string, False otherwise.

The toGrammar method returns a grammar object that generates the same language as the finite automaton.

The isNfa method checks if the finite automaton is a non-deterministic finite automaton.

The nfa_to_dfa method converts a non-deterministic finite automaton to a deterministic finite automaton. It returns a new FiniteAutomaton object with the converted DFA.


## Conclusions

In conclusion, the tasks were successfully completed, and the code now includes additional functionality for classifying grammars based on the Chomsky hierarchy, converting finite automata to regular grammars, and converting non-deterministic finite automata to deterministic finite automata. These tasks help to enhance the capabilities of the code for analyzing and modeling complex systems.

# Output after running the main file.
'''
![image](https://user-images.githubusercontent.com/64483300/223067632-6ccc7b2b-4af1-408b-8450-bb15cc9f0088.png)
'''
