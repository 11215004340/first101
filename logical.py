# Example 1
x = 5
print(x > 3 and x > 10) 
 
# Example 2
y = 12
print(y > 10 and y % 5 ==0)

#or operator
# Example 3
x = 5
print(x < 3 or x > 10)

# Example 4
y = 12
print(y < 10 or y % 2 == 0)

#Not operator
# Example 5
x = 5
print(not(x > 3 and x < 10))  #false because the condition inside the not is true

# Example 6
y = 12
print(not(y > 10 and y % 5 == 0)) #true becaouse the condition inside the not is false

#checking self 
# Example 1 ("AND")
x=11
print(x>8 and x<12)

# Example 2 ("or")
x=100
print(x<111 or x>99)

# Exaample 3 ("Not")
y=55
print(not(y<12 and y%5==11))
