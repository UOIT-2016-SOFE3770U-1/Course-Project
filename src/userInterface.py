

functionList=[
    "1.   High Conditioned Elliptic Function",
    "2.   Bent cigar Function",
    "3.   Discus Function",
    "4.   Rosenbrock's Function",
    "5.   Ackley's Function",
    "6.   Weierstrass Function",
    "7.   Griewank's Function",
    "8.   Rastrigin's Function",
    "9.   Katsuura Function"
]
for i in functionList:
    print(
    i
    )

print("Choose a function from the list above.\n"
      "Please enter a number form 1 to 9")

user_choice = input("\n")
print("You choose:\n", functionList[int(user_choice)-1])