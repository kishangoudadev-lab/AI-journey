print("Hello world!")
name = "XYZ"
number = 1
print(f"{number} {name}")

def name_and_batch_funtion(name, batch,age):
    print(f"{name} {batch}")

    print(f"{name}'s age is {age}")
    return name.capitalize()


name_and_batch_funtion("Jhon", 25 ,30)
name_and_batch_funtion("Doe", 26 , 28)
x = name_and_batch_funtion("Smith", 27 , 56)

def add(a, b):
    return a+b

result = add(18 , 89)
print(f"{result}")
print(x)

lst = [1,2,3,4] 
st = {1,2,3,2,4}
tupple = (1,2,3,4)
dict = {"name" : "Jhon", "age" : 20 , "batch" : 25}

print(lst)      
print(st)
print(tupple)
print(dict)