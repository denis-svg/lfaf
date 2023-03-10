"""Variant 19"""
from grammar import Grammar
from automaton import FiniteAutomaton

states = ["q0", "q1", "q2"]
inputs = ["a", "b"]
start_states = ['q0']
final_states = ['q2']
Sigma = {
    ('q0', 'a') : ['q1', 'q0'],
    ('q1', 'b') : ['q2', 'q1'],
    ('q0', 'b') : ['q0'],
    ('q2', 'b') : ['q2']

}

if __name__ == "__main__":
    fa = FiniteAutomaton(states, inputs, start_states, final_states, Sigma)
    if fa.isNfa():
        print("Variant19 finate automaton is nfa")
        print("NFA", fa.transitions)
    
    print("\n")
    print('converting to dfa')
    print("\n")
    converted_fa = fa.nfa_to_dfa()
    if converted_fa.isNfa():
        print("Converted finate automaton is nfa")
    else:
        print("Converted finate automaton is dfa")
        print("DFA ", converted_fa.transitions)

    print("\n")
    print("Production rules of DFA to Grammar ", converted_fa.toGrammar().P)
    

