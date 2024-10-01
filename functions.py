import time  # Import the time module
from IPython.display import Image, display

#### define rooms and items

#ROOMS:

game_room = {
    "name": "game room",
    "type": "room",
    "image": 'https://i.postimg.cc/bwj8Vk60/8a5a7c33-5306-4d3b-ab19-9df4d4e1ce00.jpg',
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
    "image": 'https://i.postimg.cc/sD34PDSn/image-1.png',
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
    "image": 'https://i.postimg.cc/6QpPMfvm/image.png',
}

living_room = {
    "name": "living room",
    "type": "room",
    "image": "https://i.postimg.cc/Gmr1rDWc/image-3.png",
}

wardrobe = {
  "name": "wardrobe",
  "type": "room",
  "image": "https://i.postimg.cc/SKHhBPqP/image-5.png",
}

outside = {
  "name": "outside",
  "type": "room",
  "image": "https://i.postimg.cc/D0HfwNdR/5ec9757e-e57b-4d33-9850-ca858a65bd30.jpg",
}

#DOORS:

door_a = {
    "name": "door a",
    "type": "door",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d = {
    "name": "door d",
    "type": "door",
}

door_e = {
    "name": "door e",
    "type": "door",
}


#FURNITURE:

couch = {
    "name": "couch",
    "type": "furniture",
}

piano = {
    "name": "piano",
    "type": "furniture",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

dining_table = {
    "name": "dinning table",
    "type": "furniture",
}

safebox = {
    "name": "safebox",
    "type": "furniture",
}

jacket = {
    "name": "jacket",
    "type": "furniture",
}

clue = {
    "name": "a paper with random numbers: 1, 3, 2, 4",
    "type": "furniture",
}

#KEYS:

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}


key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "wardrobe key",
    "type": "key",
    "target": door_d,
}

key_e = {
    "name": "key for door e",
    "type": "key",
    "target": door_e,
}


#list of rooms and doors:

all_rooms = [game_room, bedroom_1, bedroom_2, living_room, wardrobe, outside]

all_doors = [door_a, door_b, door_c, door_d, door_e]

# define which items/rooms are related

object_relations = {
    ### ROOMS
    "game room": [couch, piano, door_a],
    "bedroom 1": [queen_bed, door_a, door_b, door_c],
    "bedroom 2": [double_bed, dresser, door_b],
    "living room": [dining_table, safebox, door_c, door_d, door_e],
    "wardrobe": [jacket, door_d],
    "outside": [door_e],
    ### DOORS
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [wardrobe, living_room],
    "door e": [living_room, outside],
    ### FURNITURE
    "piano": [key_a],
    "queen bed": [key_b],
    "double bed": [key_c],
    "dresser": [clue],
    "safebox": [key_d],
    "jacket": [key_e]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("""        You wake up on a couch and find yourself in a strange house with no windows which you have never been to before.
        You don't remember why you are here and what had happened before. 
        You feel some unknown danger is approaching and you must get out of the house, NOW!""")
    check_time()
    show_image(game_state["current_room"]["image"])
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """

    game_state["current_room"] = room

    if game_state["current_room"] == game_state["target_room"]:
        print("Congrats! You escaped the room!")
    else:
        print("You are now in " + room["name"])
        # show_image(room["image"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        print(intended_action)
        if intended_action == "explore":
            explore_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)

        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    current_room = room
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))
    play_room(current_room)

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    #for room in connected_rooms:
    #    if(not current_room == room):
    #        return room

    next_room = next(room for room in connected_rooms if room != current_room)

    # Ana:
    # sin next no funciona
    # otra opción sería
    # next_room = [room for room in object_relations[door["name"]] if room != current_room][0]
    # Crea una lista de todas las salas conectadas que no son la sala actual
    # y accede al primer elemento de esa lista usando [0]
    # Como la lista sólo va a tener un elemento, siempre va a ser el primero.

    return next_room
#Otra forma de hacer la compresión de lista para esa función
    #"""def get_next_room_of_door(door, current_room):
    #"""
    #From object_relations, find the two rooms connected to the given door.
    #Return the room that is not the current_room.
    #"""
    #connected_rooms = object_relations[door["name"]]
    #for room in connected_rooms:
    #    if(not current_room == room):
    #        return room

    #next_room = next(room for room in connected_rooms if room != current_room)
    #return next_room
    #connected_rooms = object_relations.get(door["name"], [])
    #next_room = [room for room in connected_rooms if room != current_room]
    #return next_room[0]"""

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            #Si el objeto es igual puerta
            if(item["type"] == "door"):
                # Si es concretamente la puerta "door a"
                if item_name == "door a":
                    show_image('https://st2.depositphotos.com/3259223/5494/v/450/depositphotos_54949487-stock-illustration-spooky-ghost.jpg')
                    print("""A ghost appears and says: HAHAHAHAHA I see you've woken up.
                          If you want to open the door, you have to guess the number I am thinking of.
                          As a clue, I will tell you that it is a number between 1 and 5""")
                    secret_number = 4
                    attempts = 3
                    #Le damos 3 intentos al usuario
                    while attempts > 0:
                        try:
                          guess = int(input(f"Attempt {4 - attempts}/3: Enter a number between 1 and 5: "))
                          if guess == secret_number:
                            print("The ghost smiles and says: 'Correct! You may open the door.'")
                            break
                          else:
                            attempts -= 1
                            if attempts > 0:
                                print(f"Wrong! Try again. You have {attempts} attempts left.")
                            else:
                                print("The ghost frowns: 'You failed. You cannot open this door now.'")
                                return play_room(current_room)
                        except ValueError:
                          attempts -= 1
                          print(f"Invalid input! You have {attempts} attempts left. Please enter a valid number between 1 and 5.")
                          if attempts == 0:
                            print("The ghost frowns: 'You failed. You cannot open this door now.'")
                            return play_room(current_room)

                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if item["name"] == "safebox":
                    print("You find a safe box. It has a number lock.")
                    correct_code = "1324"
                    code_attempt = input("Enter the code (4 numbers code): ").strip()
                    if code_attempt == correct_code:
                        print("The safebox opens! Inside, you find a door to a secret wardrobe.")
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "You find " + item_found["name"] + "."
                        #next_room = wardrobe  # el armario
                    else:
                        print("The code is incorrect.")
                elif(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    output += "You find " + item_found["name"] + "."
                    if item_found["type"] == "key":
                        game_state["keys_collected"].append(item_found)
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break
    if(output is None):
        print("The item you requested is not found in the current room.")
    if(next_room and input("Do you want to go to the next room? Type 'yes' or 'no'").strip() == 'yes'):
      #check_time()
      if check_time() == True:
          show_image(next_room["image"])
          play_room(next_room)

    else:
        play_room(current_room)

# Set the total time limit in seconds (e.g., 5 minutes = 300 seconds)
total_time = 600

# Store the start time when the game starts
start_time = time.time()
#print (start_time)

def check_time():

    """Check if the player still has time left."""
    elapsed_time = time.time() - start_time  # Calculate time passed
    # print (elapsed_time)
    remaining_time = total_time - elapsed_time  # Calculate remaining time
    # print (remaining_time)

    if remaining_time <= 0:
        #print("Time's up! You failed to escape in time.")
        #print("Exiting the game...")  # Handle the exit gracefully without raising an error
        print("Time's up! You failed to escape in time. Exiting the game...")
        return False  # Return False to indicate the time is up
    else:
        minutes, seconds = divmod(remaining_time, 60)
        print(f"Time left: {int(minutes)} minutes and {int(seconds)} seconds\n")
        return True  # Continue the game if time remains
    
def show_image(image_url, width=400, height=300):
  img = Image(url=image_url, width=width, height=height)
  display(img)
  time.sleep(1)

#show_image('https://st2.depositphotos.com/3259223/5494/v/450/depositphotos_54949487-stock-illustration-spooky-ghost.jpg')
#print("A ghost appears!")

game_state = INIT_GAME_STATE.copy()





