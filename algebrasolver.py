from sympy import symbols, Eq, solve

x = symbols('x')

left = input('Left Side: ')
right = input('Right Side: ')

eq = Eq(eval(left), eval(right))

answer = solve(eq, x)

print(answer[0].evalf())