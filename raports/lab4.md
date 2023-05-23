- [Lab 4: Chomsky Normal Form](#org5cfc323)
- [Theory](#org74327b2)
  - [Lexical analysis](#org732ae06)
- [Objectives](#org5545cea)
- [Results](#org923194d)
- [Implementation](#orgc2bc5f8)




<a id="org5cfc323"></a>

# Lab 4: Chomsky Normal Form

Course
: Formal Languages &amp; Finite Automata

Author
: Prodan Denis


<a id="org74327b2"></a>

# Theory


<a id="org732ae06"></a>

## Chomsky Normal Form

Chomsky Normal Form (CNF) is a way of representing a context-free grammar (CFG) in a particular form. A grammar is said to be in CNF if all of its productions are of the form:

   A → BC, where A, B, and C are nonterminal symbols
   A → a, where A is a nonterminal symbol and a is a terminal symbol
   S → ε, where S is the start symbol of the grammar and ε represents the empty string.

In other words, each production in a grammar in CNF has either two nonterminal symbols on the right-hand side or a single terminal symbol on the right-hand side.

The conversion of a CFG into Chomsky Normal Form involves a series of steps such as removing epsilon productions, eliminating unit productions, and transforming long productions into shorter ones. This conversion is useful for many parsing algorithms that require a CFG to be in CNF, as it simplifies the parsing process and makes it more efficient.

<a id="org5545cea"></a>

# Objectives

-   [X] Implement a method for normalizing an input grammar by the rules of CNF. 


<a id="org923194d"></a>

# Results

Variant 19
```
VN = ['S', 'A', 'B', 'C', 'E']
VT = ['a', 'd']
Production Rules
S --> [['d', 'B'], ['B']]
A --> [['d'], ['d', 'S'], ['a', 'A', 'd', 'C', 'B']]
B --> [['a', 'C'], ['b', 'A'], ['A', 'C']]
C --> [[]]
E --> ['A', 'S']
```

After applying Chomsky normal form
```
VN = ['S', 'A', 'B', 'C', 'E', 'X11', 'X13', 'X15']
VT = ['a', 'd']

Production Rules
S --> [['d', 'B'], ['B'], ['a', 'C'], ['b', 'A'], ['A', 'C']]
A --> [['d'], ['d', 'S'], ['a', 'X15']]
B --> [['a', 'C'], ['b', 'A'], ['A', 'C']]
C --> []
E --> ['A', 'S', ['d'], ['d', 'S'], ['a', 'X15'], ['d', 'B'], ['B'], ['a', 'C'], ['b', 'A'], ['A', 'C']]
X11 --> [['C', 'B']]
X13 --> [['d', 'X11']]
X15 --> [['A', 'X13']]

```

<a id="orgc2bc5f8"></a>

# Implementation

Step 1: Eliminate all productions with epsilon

In this step, the function removes all epsilon productions from the grammar. An epsilon production is a production of the form A → ε, where A is a nonterminal symbol and ε represents the empty string. The function removes such productions from the grammar by iterating through all nonterminal symbols in the grammar and removing any empty productions that they have.

Step 2: Replace all unit productions A -> B with A -> C, where C -> B is a production

In this step, the function replaces all unit productions of the form A → B, where A and B are nonterminal symbols, with productions of the form A → C, where C is a nonterminal symbol that produces B. The function does this by first identifying all unit productions in the grammar and then replacing them with the corresponding productions that use non-unit productions.

Step 3: Replace all non-unit productions A -> w with A -> BC, where B -> x and C -> y are productions

In this step, the function replaces all non-unit productions of the form A → w, where w is a string of one or more symbols (either terminal or nonterminal), with productions of the form A → BC, where B and C are nonterminal symbols and each symbol in w is either a terminal symbol or a new nonterminal symbol. The function does this by splitting the string w into pairs of symbols (or single symbols if the string has odd length), introducing new nonterminal symbols as necessary to represent each pair, and then replacing the original production with a new set of productions that use the new nonterminal symbols.

Step 4: Eliminate any remaining unit productions

In this step, the function eliminates any remaining unit productions that may have been introduced in Step 2 or Step 3. The function does this by iterating through all nonterminal symbols in the grammar and removing any unit productions that they have. If any new unit productions are created as a result of this removal, the function repeats the process until no more unit productions remain.

After these four steps, the grammar should be in Chomsky Normal Form, with all productions in the required format.


