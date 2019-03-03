def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
        
    string = ""
    half = int(n/2)
    
    for i in range(1, half * 2, 2):
        whitespaces = n - i
        sides = " " * (int(whitespaces / 2))
        center = "*" * i
        string += sides + center
        if i != (half * 2) - 1:
            string += "\n"
    string += "\n" + "*" * n + "\n"
    for i in range(half * 2 - 1, 0, -2):
        whitespaces = n - i
        sides = " " * (int(whitespaces / 2))
        center = "*" * i
        string += sides + center
        if i != 1:
            string += "\n"
    
    return string + "\n"
    
print(diamond(7))