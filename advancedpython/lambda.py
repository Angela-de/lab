#filter,map,lambda

# returning only even numbers..another way using lambda
print("\n")
numbers = [1,56,234,87,4,76,24,69,90,135]
new = filter ((lambda x: x%2==0), numbers)
print (list(new))

# returning only even numbers..another way using lambda
print("\n")
numbers = [1,56,234,87,4,76,24,69,90,135]
new = map ((lambda x: x%2==0), numbers)
print (list(new))

#combinations..adding not to produce odd numbers
print("\n")
numbers = [1,56,234,87,4,76,24,69,90,135]
newlist = [n for n in numbers if not n%2==0]
print (newlist) 


