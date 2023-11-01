from math import sqrt


def quadraticSolver(a, b, c):
    try:
        mid = sqrt(b**2 - 4 * a * c)
    except ValueError:
        print("your equation do not have real number solutions")
        return 
    x1 = (-b + mid) / 2 * a
    x2 = (-b - mid) / 2 * a

    if x1 % 1 == 0:
        x1 = int(x1)
    if x2 % 1 == 0:
        x2 = int(x2)
    
    
    print(f"your solutions are {x1:.2f}, {x2:.2f}")

    x1_strip = f"+ {abs(x1):.2f}" if x1 < 0 else f"- {abs(x1):.2f}"
    x2_strip = f"+ {abs(x2):.2f}" if x2 < 0 else f"- {abs(x2):.2f}"

    print(f"(x {x1_strip})(x {x2_strip}) = 0")

if __name__=='__main__':
    print("This program will solve quadratic equations")
    print("First please remake your equation as 'ax^2 + bx + c = 0' type")
    print("a, b, c needs to be integers")

    a = int(input("Enter value for 'a': "))
    b = int(input("Enter value for 'b': "))
    c = int(input("Enter value for 'c': "))
    
    quadraticSolver(a, b, c)