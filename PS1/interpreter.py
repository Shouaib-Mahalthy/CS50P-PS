inp = input("Expression: ").strip()
x,y,z = inp.split(" ")
x = int(x)
z = int(z)
res = 0.0
match y:
    case '+':
        res = x+z
    case '-':
        res = x-z
    case '*':
        res = x*z
    case '/':
        res = x/z
    case '%':
        res = x%z
print(f"{res:.1f}")
