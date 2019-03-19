def street_fighter_selection(fighters, initial_position, moves):
    [x, y] = initial_position
    UP = "up"
    DOWN = "down"
    RIGHT = "right"
    LEFT = "left"
    charactersHovered = []
    
    for move in moves:
        if move == UP and y > 0:
            y -= 1
        elif move == DOWN and y < len(fighters) - 1:
            y += 1
        elif move == RIGHT:
            x += 1
        elif move == LEFT:
            x -= 1
        
        if abs(x) >= len(fighters[0]):
            if x < 0:
                x = (abs(x) % len(fighters)) * -1
            else:
                x = abs(x) % len(fighters)
        
        charactersHovered.append(fighters[y][x])
    return charactersHovered
    
fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
opts = ["up", "down", "right", "left"]
moves = ["up"]+["left"]*6+["down"]+["right"]*6
print(street_fighter_selection(fighters, (0, 0), moves))