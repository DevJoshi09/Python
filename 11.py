# list comprehension : compact way of writing a list 
# syntax : [expression for x in iterable]
# list properties: ordered , changable and duplicates are allowed .

num = [x for x in range(1,11)]

print(num)


# switch case / match case 

num = 1
bol = num % 2
match bol:
    case 0:
        print("Even Number")
    case 1:
        print("Odd Number")
    case _:
        print("enter valid number")


