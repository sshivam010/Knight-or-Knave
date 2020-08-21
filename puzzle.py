from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

rules = And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave))
)
print(' Puzzle 0')
print(' A says "I am both a knight and a knave."', end='\n\n')
knowledge0 = And(
    rules,
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

print(' Puzzle 1')
print(' A says "We are both knaves."', end='\n\n')
# B says nothing.
knowledge1 = And(
    rules,
    Biconditional(AKnight, And(AKnave, BKnave))
)

print(' Puzzle 2')
print(' A says "We are the same kind."')
print(' B says "We are of different kinds."', end='\n\n')
knowledge2 = And(
    rules,
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)

print(' Puzzle 3')
print(' A says either "I am a knight." or "I am a knave.", but you don\'t know which.')
print(' B says "A said \'I am a knave\'."')
print(' B says "C is a knave."')
print(' C says "A is a knight."', end='\n')
knowledge3 = And(
    rules,
    Biconditional(BKnight, And(AKnight, AKnave)),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight)
)

print('\nSolutions:\n')
def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
