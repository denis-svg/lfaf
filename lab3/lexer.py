from enum import Enum, auto

class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    DIV = auto()
    LPAREN = auto()
    RPAREN = auto()
    ASSIGMENT = auto()
    FUNDEF = auto()
    ENDOFLINE = auto()
    COMMA = auto()
    SEMICOL = auto()
    STRING = auto()
    NAME = auto()
    BOOL = auto()
    START = auto()
    END = auto()
    IF = auto()
    MULT = auto()
    LOGICOP = auto()
    COMPARISONOP = auto()

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
                self.advance()
                if self.current_char == '=':
                    self.tokens.append(Token(TokenType.COMPARISONOP , '=='))
                else:
                    self.tokens.append(Token(TokenType.ASSIGMENT ,self.current_char))
            elif self.current_char == '{':
                self.tokens.append(Token(TokenType.START ,self.current_char))
                self.advance()
            elif self.current_char == '}':
                self.tokens.append(Token(TokenType.END ,self.current_char))
                self.advance()
            elif self.current_char in "<>!":
                previous_char = self.current_char
                self.advance()
                if self.current_char in "=":
                    self.tokens.append(Token(TokenType.COMPARISONOP , previous_char + self.current_char))
                else:
                    self.tokens.append(Token(TokenType.COMPARISONOP , previous_char))

            elif self.current_char.isspace():
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

            elif self.current_char.isdigit():
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
        while (not self.current_char.isspace()) and (self.current_char not in SPECIAL) and (self.current_char != None):
            word += self.current_char
            self.advance()
        return word

    def getNumber(self):
        num = ''
        while (self.current_char.isdigit()) or (self.current_char in '.'):
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

