from input import input_string


example = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

#change the string into a list 

example_list = example.split();


#function that change string DirectionDistance into [direction, distance]
def create_rotation_list(string_list):
    new_list = []
    for s in string_list:
        info = []
        info.append(s[0])
        distance = int(s.replace(s[0],"",1))
        info.append(distance)
        new_list.append(info)
    
    return new_list
    
example_rotation = create_rotation_list(example_list)
#print(example_list)
input_list = input_string.split()
puzzle_list = create_rotation_list(input_list)

#dial starts at 50 
#dial is a circle 
#dial left from 0 goes to 99 
#dial right from 99 goes to 0

result = [50] 

def calculate_new_dial(start,data):
    #data = [letter,distance]
    direction = data[0]
    distance = data[1]
    newStart = 0
    if direction == "L":
        newStart = start - distance
    else:
        newStart = start + distance
    if newStart < 0:
        newStart = newStart + 100 
    elif newStart > 100:
        newStart = newStart - 100
    elif newStart == 100:
        newStart = 0
    else:
        pass
    return newStart

#start at 50 
#input rotation info, get new number
#push new number into result list 
#use the new number as new start 

def calculate_result(result,rotations_list):
    num_of_zeros = 0;
    for i in range(len(rotations_list)):
        #print('result',result)
        next_dial = calculate_new_dial(result[i],rotations_list[i])
        result.append(next_dial)
        if next_dial == 0:
            num_of_zeros += 1
    return num_of_zeros;

example_result = calculate_result(result,example_rotation)
print(example_result)

puzzle_result = calculate_result(result,puzzle_list)
print(puzzle_result)




