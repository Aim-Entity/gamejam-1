def move():
    direction = "W"  # The default is always forwards
    key = input(">> ").upper()
    if key not in 'WASD':  # If the entered key is not W A S D
        print("Invalid Input\n")
        while True:
            key = input(">> ").upper()

            if key in 'WASD':
                break
    direction = key  # Updating this var if key is valid

    return direction
