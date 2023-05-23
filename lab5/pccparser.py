from lexer import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.current_token = None
    
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
    
    def parse(self):
        self.advance()
        parse_tree = self.program()
        self.print_parse_tree(parse_tree)
    
    def program(self):
        statements = []
        statement = self.statement()
        if statement:
            statements.append(statement)
        while self.current_token and self.current_token.type == TokenType.ENDOFLINE:
            self.advance()
            statement = self.statement()
            if statement:
                statements.append(statement)
        return {"Program": statements}
    
    def statement(self):
        if self.current_token and self.current_token.type == TokenType.NAME:
            variable_name = self.current_token.value
            self.advance()
            if self.current_token and self.current_token.type == TokenType.ASSIGMENT:
                self.advance()
                expr = self.expression()
                return {"Assign": {"Variable": variable_name, "Expression": expr}}
            else:
                return {"Variable": variable_name}
        else:
            return None
    
    def expression(self):
        expr = self.term()
        while self.current_token and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token.value
            self.advance()
            term = self.term()
            expr = {"BinaryOp": {"Left": expr, "Operator": op, "Right": term}}
        return expr
    
    def term(self):
        term = self.factor()
        while self.current_token and self.current_token.type in (TokenType.MULT, TokenType.DIV):
            op = self.current_token.value
            self.advance()
            factor = self.factor()
            term = {"BinaryOp": {"Left": term, "Operator": op, "Right": factor}}
        return term
    
    def factor(self):
        if self.current_token and self.current_token.type == TokenType.NUMBER:
            value = self.current_token.value
            self.advance()
            return {"Number": value}
        elif self.current_token and self.current_token.type == TokenType.NAME:
            name = self.current_token.value
            self.advance()
            return {"Variable": name}
        elif self.current_token and self.current_token.type == TokenType.LPAREN:
            self.advance()
            expr = self.expression()
            if self.current_token and self.current_token.type == TokenType.RPAREN:
                self.advance()
                return {"ParenthesizedExpr": expr}
            else:
                return {"InvalidExpression"}
        else:
            return {"InvalidFactor"}

    def print_parse_tree(self, parse_tree, indent=""):
        for key, value in parse_tree.items():
            print(indent + key + ":")
            if isinstance(value, dict):
                self.print_parse_tree(value, indent + "  ")
            else:
                print(indent + "  " + str(value))

# Usage example
lexer = Lexer("a = 4 + (c + 6) / 3.213;")
lexer.getTokens()
parser = Parser(lexer.tokens)
parser.parse()
