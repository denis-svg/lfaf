from enum import Enum

class TokenType(Enum):
    NUMBER = 1
    PLUS = 2
    MINUS = 3
    DIV = 4
    LPAREN = 5
    RPAREN = 6
    ASSIGMENT = 10
    FUNDEF = 11
    ENDOFLINE = 12
    COMMA = 13
    SEMICOL = 14
    STRING = 17
    NAME = 19
    BOOL = 20
    START = 21
    END = 22
    IF = 23
    ARGSTART = 24
    ARGEND = 25
    MULT = 26
    LOGICOP = 28

DIGITS = "0123456789"
WHITESPACE = ' \n\t'
SPECIAL = '!@#$%^&*()-+=;?,."{ }'

class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return f'{self.type}:{self.value}'
    
class Lexer:
    def __init__(self, source) -> None:
        self.source = iter(source)
        self.current_char = None
        self.tokens = []

    def advance(self):
        try:
            self.current_char = next(self.source)
        except:
            self.current_char = None
    
    def getTokens(self):
        # current_char is None at the begining so it is needed to advance
        self.advance()
        i = 0
        while self.current_char != None:
            if self.current_char == ';':
                self.tokens.append(Token(TokenType.ENDOFLINE ,self.current_char))
                self.advance()
            if self.current_char == '=':
                self.tokens.append(Token(TokenType.ASSIGMENT ,self.current_char))
                self.advance()
            elif self.current_char == '{':
                self.tokens.append(Token(TokenType.START ,self.current_char))
                self.advance()
            elif self.current_char == '}':
                self.tokens.append(Token(TokenType.END ,self.current_char))
                self.advance()

            elif self.current_char in WHITESPACE:
                self.advance()
            
            elif self.current_char in '+-*/':
                if self.current_char == '+':
                    self.tokens.append(Token(TokenType.PLUS ,self.current_char))
                if self.current_char == '-':
                    self.tokens.append(Token(TokenType.MINUS ,self.current_char))
                if self.current_char == '*':
                    self.tokens.append(Token(TokenType.MULT ,self.current_char))
                if self.current_char == '/':
                    self.tokens.append(Token(TokenType.DIV ,self.current_char))
                self.advance()

            elif self.current_char == '"':
                self.tokens.append(Token(TokenType.STRING ,self.getString()))
                self.advance()
            
            elif self.current_char == '(':
                self.tokens.append(Token(TokenType.LPAREN ,self.current_char))
                self.advance()
            elif self.current_char == ')':
                self.tokens.append(Token(TokenType.RPAREN ,self.current_char))
                self.advance()
            elif self.current_char == ',':
                self.tokens.append(Token(TokenType.COMMA ,self.current_char))
                self.advance()

            elif self.current_char in DIGITS:
                self.tokens.append(Token(TokenType.NUMBER ,self.getNumber()))
            elif self.current_char.isalpha():
                name = self.getWord()
                if name == 'def':
                    self.tokens.append(Token(TokenType.FUNDEF ,name))
                elif name == 'True' or name == 'False':
                    self.tokens.append(Token(TokenType.BOOL ,name))
                elif name == 'and' or name == 'or' or name == 'not':
                    self.tokens.append(Token(TokenType.LOGICOP ,name))
                elif name == 'if':
                    self.tokens.append(Token(TokenType.IF ,name))
                else:
                    self.tokens.append(Token(TokenType.NAME , name))

            else:
                self.advance()       

    def getString(self):
        string = ''
        self.advance()
        while self.current_char != '"':
            string += self.current_char
            self.advance()
        return string

    def getWord(self):
        word = ''
        while (self.current_char not in WHITESPACE) and (self.current_char not in SPECIAL) and (self.current_char != None):
            word += self.current_char
            self.advance()
        return word

    def getNumber(self):
        num = ''
        while (self.current_char in DIGITS) or (self.current_char in '.'):
            num += self.current_char
            self.advance()
        return num
    
    def print(self):
        for token in self.tokens:
            if token.type not in [TokenType.ENDOFLINE, TokenType.START, TokenType.END]:
                print(token, end=', ')
            else:
                print(token)


if __name__ == "__main__":
    f = open("myfile.pcc", "r")
    content = f.read()
    f.close()
    l = Lexer(content)
    l.getTokens()
    l.print()

