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
    return [multi_room,
            multi_room_enemy,
            multi_room_chest,
            side_choice,
            side_choice_chest,
            side_choice_enemy]


all_rooms = rooms()
print(all_rooms[5])
