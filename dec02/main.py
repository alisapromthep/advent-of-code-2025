from input import example_input, input

#The ranges are separated by commas (,);
#each range gives its first ID and last ID separated by a dash (-). 

#preparing the input 
#1.split the input into ranges by , 
#2.create a list, with [0] containing the first number 
#3.find the size of the range, add into the list as [1]
#4. store the last number in the range [2] (for debugging)

example_list = example_input.split(",")
#print(example_list)


def create_range_list(str):
    return str.split("-")


example_ranges = []
for ranges in example_list:
    list_range = create_range_list(ranges)
    example_ranges.append(list_range)

#print(example_ranges)

#invild IDS are sequence of repeating digits, i.e. 55,6464, 123123
#no numbers have leading zeros 
#odd number of digits are all VALID 

#checking valid ids 
#steps 
#00. loop through the prepare list, [firstnum, range size, last num]
#0.in each range, loop through each number
#1.count number of digits 
#2.ODD = valid, EVEN = must check further 
#3.divide digit number by 2
#4.split the number by digit number above(splitting it in half)
#5.use loop to check if the digit matches 

def check_valid_id(id):
    id_str = str(id)
    id_length = len(id_str)
    num_digits = id_length
    is_even = num_digits % 2
    if is_even != 0:
        return True
    else:
        #find the middle
        mid = num_digits//2
        #compare the digits 
        i = 0
        j = mid - 1 
        while j < id_length - 1:
            if id_str[i] == id_str[j]:
                return False
            else: 
                i += 1
                j += 1 
        return True

example_result = []
for a in example_ranges:
    r = range(int(a[0]),int(a[1]))
    for id in r:
        id_valid = check_valid_id(id)
        if id_valid == False:
            print("result",id,id_valid)
            example_result.append(id)

print(example_result)







