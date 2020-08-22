def move():
    direction = "W"
    key = input(">> ").upper()
    if key not in 'WASD':
        print("Invalid Input\n")
        while True:
            key = input(">> ").upper()

            if key in 'WASD':
                break
    direction = key

    return direction
