- [Lab 5: Parsers](#org5cfc323)
- [Theory](#org74327b2)
  - [Parser analysis](#org732ae06)
- [Objectives](#org5545cea)
- [Results](#org923194d)
- [Implementation](#orgc2bc5f8)




<a id="org5cfc323"></a>

# Lab 5: Parser & Building an Abstract Syntax Tree

Course
: Formal Languages &amp; Finite Automata

Author
: Prodan Denis


<a id="org74327b2"></a>

# Theory


<a id="org732ae06"></a>

## Chomsky Normal Form

Certainly! The top-down parser is a type of parsing algorithm used in compiler design and natural language processing. It starts with the input string and attempts to construct a parse tree from the top (the start symbol) down to the leaves (the input symbols). The goal of the top-down parser is to find a valid sequence of production rules that generates the input string, following the grammar rules.

Here's a brief explanation of the theory behind the top-down parser:

   Grammar: The parser operates based on a given context-free grammar (CFG). The CFG consists of a set of nonterminal symbols, terminal symbols, a start symbol, and a set of production rules. The production rules define how the nonterminal symbols can be replaced by other symbols (terminal or nonterminal) in the grammar.

   Parse Tree: The parse tree represents the syntactic structure of the input string according to the grammar. It is a hierarchical tree-like structure where the nonterminal symbols are the internal nodes, and the terminal symbols and epsilon are the leaves.

   Recursive Descent Parsing: The top-down parser uses a recursive descent parsing strategy, which means that it starts from the start symbol and recursively expands nonterminal symbols by choosing appropriate production rules based on the current input symbol.

   Predictive Parsing: The top-down parser can be predictive, meaning it can predict the production rule to apply based on the current nonterminal symbol and the next input symbol. This prediction is possible if the grammar is LL(1), where LL stands for Left-to-right, Leftmost derivation and 1 indicates that a single lookahead symbol is sufficient to make a decision.

   Backtracking: If the predictive top-down parser encounters a mismatch between the predicted symbol and the input symbol, it backtracks and explores alternative production rules until it finds a match or exhausts all possibilities.

   Leftmost Derivation: The top-down parser follows a leftmost derivation strategy, which means it expands the leftmost nonterminal symbol in each step. This strategy corresponds to constructing the parse tree from left to right.

Overall, the top-down parser is based on the principles of recursive descent and predictive parsing. It uses the given grammar rules and the input string to construct a parse tree, exploring different production rules until a valid parse is found or determining that the input does not conform to the grammar rules.

<a id="org5545cea"></a>

# Objectives

1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.


<a id="org923194d"></a>

# Results

code
```
a = 4 + (c + 6) / 3.213;
b = 5;
c = 3;
```
output
```
Program:
  [{'Assign': {'Variable': 'a', 'Expression': {'BinaryOp': {'Left': {'Number': '4'}, 'Operator': '+', 'Right': {'BinaryOp': {'Left': {'ParenthesizedExpr': {'BinaryOp': {'Left': {'Variable': 'c'}, 'Operator': '+', 'Right': {'Number': '6'}}}}, 'Operator': '/', 'Right': {'Number': '3.213'}}}}}}}, {'Assign': {'Variable': 'b', 'Expression': {'Number': '5'}}}, {'Assign': {'Variable': 'c', 'Expression': {'Number': '3'}}}]
Program:
  - Assign:
      Variable: a
      Expression:
        BinaryOp:
          Left:
            Number: 4
          Operator: +
          Right:
            BinaryOp:
              Left:
                ParenthesizedExpr:
                  BinaryOp:
                    Left:
                      Variable: c
                    Operator: +
                    Right:
                      Number: 6
              Operator: /
              Right:
                Number: 3.213
  - Assign:
      Variable: b
      Expression:
        Number: 5
  - Assign:
      Variable: c
      Expression:
        Number: 3
```

<a id="orgc2bc5f8"></a>

# Implementation

   1.The code begins by importing the lexer module and the json module, which will be used for printing the parse tree.

   2.The Parser class is defined with an __init__ method that takes a list of tokens as input. It initializes the parser with the tokens and sets the current token to None.

   3.The advance method is defined to move to the next token in the list of tokens. It uses the next function to get the next token from the iterator. If there are no more tokens, it sets the current token to None.

   4.The parse method is the entry point of the parser. It calls the advance method to move to the first token, then calls the program method to start parsing the program. The resulting parse tree is stored in the parse_tree variable, and then the print_parse_tree method is called to print the parse tree.

   5.The program method parses a program by repeatedly calling the statement method to parse individual statements. It collects the parsed statements in a list and returns a dictionary with the key "Program" and the list of statements as the value.

   6.The statement method parses a statement. It checks if the current token is of type TokenType.NAME, which indicates a variable name. If it is, it retrieves the variable name and advances to the next token. If the next token is of type TokenType.ASSIGNMENT, it advances to the next token again and parses the expression using the expression method. It returns a dictionary with the key "Assign" and the variable name and expression as the values. If the next token is not an assignment token, it returns a dictionary with the key "Variable" and the variable name as the value. If the current token is not a variable name token, it returns None.

   7.The expression method parses an expression by repeatedly calling the term method to parse terms and handling addition and subtraction operators. It builds a nested dictionary structure representing the expression and returns it.

   8.The term method parses a term by repeatedly calling the factor method to parse factors and handling multiplication and division operators. It builds a nested dictionary structure representing the term and returns it.

   9.The factor method parses a factor, which can be a number, variable, or a parenthesized expression. It checks the type of the current token and builds the corresponding dictionary structure based on the token type. If the current token is a number or variable, it retrieves the value, advances to the next token, and returns a dictionary with the corresponding key and value. If the current token is a left parenthesis, it advances to the next token, parses the expression recursively using the expression method, and checks if the next token is a right parenthesis. If it is, it advances to the next token and returns a dictionary with the key "ParenthesizedExpr" and the parsed expression as the value. If the current token does not match any of the expected types, it returns a dictionary with the key "InvalidFactor".

   10.The print_parse_tree method is used to print the parse tree in a readable format. It takes the parse tree as input and recursively prints each key-value pair in the tree, indenting the output based on the depth of the tree.

   11.The code then opens a file named "myfile.pcc" and reads its content. It creates a Lexer object with the file content and calls the getTokens method to tokenize the input. It then creates a Parser object with the lexer tokens and calls the
