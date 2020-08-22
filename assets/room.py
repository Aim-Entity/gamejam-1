def rooms():
    multi_room = """
        | |
 ---|---| |---|---

 ---|         |---
    |         |
    |---| |---|
        | |
        | |
        | |
        | |
  """

    multi_room_enemy = """
        | |
 ---|---| |---|---
        </>
 ---|         |---
    |         |
    |---| |---|
        | |
        | |
        | |
        | |
  """

    multi_room_chest = """ 
        | |   
 ---|---| |---|---   
       |___|
 ---|         |---
    |         |
    |---| |---|
        | |
        | |
        | |
        | |
  """

    side_choice = """ 
 ---|---------|---

 ---|         |---
    |         |
    |---| |---|
        | |
        | |
        | |
        | |
    """

    side_choice_enemy = """ 
 ---|---------|---
        </>   
 ---|         |---
    |         |
    |---| |---|
        | |
        | |
        | |
        | |
    """

    side_choice_chest = """ 
 ---|---------|---
       |___|
 ---|         |---
    |         |
    |---| |---|
        | |
        | |
        | |
        | |
    """

    right_room = """ 
    |---------|---
    |  |___|
    |         |---
    |         |
    |---| |---|
        | |
        | |
        | |
        | |
    """

    right_chest = """ 
    |---------|---
    |  |___|
    |         |---
    |         |
    |---| |---|
        | |
        | |
        | |
        | |
    """

    right_enemy = """ 
    |---------|---
    |   </>
    |         |---
    |         |
    |---| |---|
        | |
        | |
        | |
        | |
    """

    left_room = """ 
 ---|----------|   
               |
 ---|          |
    |          |
    | ---| |---|
         | |
         | |
         | |
         | |
    """

    left_chest = """ 
 ---|----------|   
        |__|   |
 ---|          |
    |          |
    | ---| |---|
         | |
         | |
         | |
         | |
    """

    left_enemy = """ 
 ---|----------|   
        </>    |
 ---|          |
    |          |
    | ---| |---|
         | |
         | |
         | |
         | |
    """
    return [multi_room,
            multi_room_enemy,
            multi_room_chest,
            side_choice,
            side_choice_chest,
            side_choice_enemy,
            right_room,
            right_chest,
            right_enemy,
            left_room,
            left_chest,
            left_enemy]


all_rooms = rooms()
print(all_rooms[-3])
