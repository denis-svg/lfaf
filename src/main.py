"""Variant 19"""
from grammar import Grammar

"""Variant 19"""
VN = ["S", "A", "B", "C", "E"]
VT = ["a", "d"]
P = {
    "S" : [["d", "B"], ["B"]],
    "A" : [["d"], ["d", "S"], ["a", "A", "d", "C", "B"]],
    "B" : [["a", "C"], ["b", "A"], ["A", 'C']],
    "C" : [[]],
    "E" : ["A", 'S']
}

if __name__ == "__main__":
    g = Grammar(VN, VT, P)
    g = g.convert_to_chomsky_normal_form()

    print(g.VN)
    print(g.VT)
    print(g.P)
    

