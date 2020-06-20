""""
Print out all of the numbers in the following array that are divisible by 3:
[85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
The expected output for the above input is:
27
81
9
27
99
63
42
You may use whatever programming language you wish.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.

"""
## UPER method:
# 1- Create a loop
# 2- To look up each elements in the array
# 3- Check to see if each element are divisible by 3
# 4- If true print the element

def divisible_elements(elements):
    for element in elements:
        if element % 3 == 0: 
            print(element)

divisible_elements([85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14])