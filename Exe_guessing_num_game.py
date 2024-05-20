def find_first_repeating_character(s):

    #creating an empty dictionary to store character counts
    character_count = {}

    #Iterate through each characterin string
    for character in s:
        if character in character_count:
            print(f"First repeating character: {character}, Memory adress: {id(character)}")
            return character, id(character)
        
        #if the repeating character is found for the first time, add to the dict
        character_count[character] = 1
        
    #if the no repeating character is found then return none
    return None

#exaple usage:
input_string = "hello"
result = find_first_repeating_character(input_string)

#check if a repeating character is found
if result is None:
    print("No repeating character found in the string.")



