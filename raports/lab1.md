# The title of the work

### Course: Formal Languages & Finite Automata
### Author: Prodan Denis FAF-211

----

## Theory
&ensp;&ensp;&ensp; A formal language can be considered to be the media or the format used to convey information from a sender entity to the one that receives it. The usual components of a language are:
- The alphabet: Set of valid characters;
- The vocabulary: Set of valid words;
- The grammar: Set of rules/constraints over the lang.

&ensp;&ensp;&ensp; Now these components can be established in an infinite amount of configurations, which actually means that whenever a language is being created, it's components should be selected in a way to make it as appropriate for it's use case as possible. Of course sometimes it is a matter of preference, that's why we ended up with lots of natural/programming/markup languages which might accomplish the same thing.





## Objectives:

1. Understand what a language is and what it needs to have in order to be considered a formal one.

2. Provide the initial setup for the evolving project that you will work on during this semester. I said project because usually at lab works, I encourage/impose students to treat all the labs like stages of development of a whole project. Basically you need to do the following:

    a. Create a local && remote repository of a VCS hosting service (let us all use Github to avoid unnecessary headaches);

    b. Choose a programming language, and my suggestion would be to choose one that supports all the main paradigms;

    c. Create a separate folder where you will be keeping the report. This semester I wish I won't see reports alongside source code files, fingers crossed;

3. According to your variant number (by universal convention it is register ID), get the grammar definition and do the following tasks:

    a. Implement a type/class for your grammar;

    b. Add one function that would generate 5 valid strings from the language expressed by your given grammar;

    c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;
    
    d. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;





## Implementation description

```
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
```
This code defines a class called Grammar which represents a context-free grammar using its non-terminals (VN), terminals (VT), and production rules (P). It has two methods:

    a. generateString method which generates a string of a specified length by recursively applying production rules to non-terminal b. b. symbols until the desired length is reached.
    c. getAutomaton method which returns a finite automaton object constructed from the grammar.



```
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
```

This code defines a class called FiniteAutomaton which represents a finite automaton. It takes a Grammar object as an argument in its constructor and initializes its states, inputs, start states, final states, and transitions based on the given grammar.

The findFinalStates method finds the final states of the automaton by iterating through the production rules and checking which non-terminal symbols lead to only terminal symbols.

The findTransitions method finds the transitions between the states of the automaton by iterating through the production rules and creating a dictionary of the form (state, input) -> [next_state].

The isAccepted method determines whether a given input string is accepted by the automaton by iterating through the symbols of the input string and checking the corresponding transitions in the automaton until it reaches a final state. If the final state is reached, the input string is accepted; otherwise, it is rejected


## Conclusions / Screenshots / Results

Completing these objectives demonstrates an understanding of formal languages, grammars, and automata, and provides practical experience in implementing these concepts in a programming language. This can be useful for building language processors, compilers, and other applications that involve working with formal languages.

# Output after running the main file.
'''
ababababaabb:True
ababaabaabaabbababaabaabb:True
aabbababaabaabbaabaabb:True
abaababaabbaabaabbaabbabaabb:True
aabaabaabaabaabbaabbaabbaabaabaabababaabbaabb:True
ababaabaabbaabbababaababaabbaabbaababaabaabbaabaabb:True
aabbaabaabbabaabbababababaabbabababaabbaabbabaabaabaabb:True
aabbabaabbabaabaabaabbaababaababaabababaabbabaabaabaababaabbabaabbaabaabbabaabaabb:True
abaabbabababaabaabbababaabbababaabbabaabbaabaababaabbaabaababaabbabaabbabababababaababaababaababababaabaabb:True
ababababaababaabaabbaabababababaabaabaabababaabaababaababaabbabaabbabababababaabaabababaabbaabababaabbaabbaabbaabbaabaabaabbabaabaabb:True
'''