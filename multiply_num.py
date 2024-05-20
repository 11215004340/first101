#multiplication table 

num_multiply = int(input ("Enter the number you want to multiply of : "))
limit_num = int(input("Enter the number till where you want to multiply: "))
print(f"The multiplication of {num_multiply} till {limit_num} is: ")
for i in range(0, limit_num+1):
    print(f"{num_multiply} * {i} = {int(num_multiply*i)}")