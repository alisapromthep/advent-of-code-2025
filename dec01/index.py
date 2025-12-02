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
def create_info_list(string_list):
    new_list = []
    for s in string_list:
        info = []
        info.append(s[0])
        distance = int(s.replace(s[0],"",1))
        info.append(distance)
        new_list.append(info)
    
    return new_list
    
example_data = create_info_list(example_list)
print(example_data)
#print(example_list)
input_list = input_string.split()

#dial starts at 50 
#dial is a circle 
#dial left from 0 goes to 99 
#dial right from 99 goes to 0