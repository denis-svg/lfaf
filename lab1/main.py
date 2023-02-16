"""Variant 19"""
from grammar import Grammar

VN = ["S", "A", "B", "C"]
VT = ["a", "b"]
P = {
    "S":["aA"],
    "A":["bS", "aB"],
    "B":["bC"],
    "C":["aA", "b"]
}

if __name__ == "__main__":
    g = Grammar(VN, VT, P)
    automaton = g.getAutomaton()
    N = 10
    for i in range(1, N + 1):
        string = g.generateString(i)
        print(f"""{string}:{automaton.isAccepted(string)}""")




