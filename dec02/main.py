from input import example_input, input

#The ranges are separated by commas (,);
#each range gives its first ID and last ID separated by a dash (-). 

#invild IDS are sequence of repeating digits, i.e. 55,6464, 123123
#no numbers have leading zeros 
#odd number of digits are all VALID 

#steps 
#0.in each range, loop through each number
#1.count number of digits 
#2.ODD = valid, EVEN = must check further 
#3.divide digit number by 2
#4.split the number by digit number above(splitting it in half)
#5.use loop to check if the digit matches 


