#multiplication table
num = int(input("Enter the number: "))
print(f"Multiplication of {num}: ")
for i in range(0,13):
    print(f"{num} x {i} = {int(num)*i}")