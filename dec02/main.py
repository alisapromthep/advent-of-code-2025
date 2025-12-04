from input import example_input, input

#The ranges are separated by commas (,);
#each range gives its first ID and last ID separated by a dash (-). 

#preparing the input 
#1.split the input into ranges by , 
#2.create a list, with [0] containing the first number 
#3.find the size of the range, add into the list as [1]
#4. store the last number in the range [2] (for debugging)

example_list = example_input.split(",")
print(example_list)

def create_range_list(str):
    range_list = str.split("-")
    for s in range_list:
        s.replace(s,int(s),1)
    return range_list
        

for r in example_list:
    print(create_range_list(r))



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

