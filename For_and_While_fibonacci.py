#For and while fibonacci

#For loop
def fibonacci(n):
    first_num = 0
    second_num = 1

    for i in range(n):
        print(first_num)
        next_num = first_num + second_num
        first_num, second_num = second_num, next_num   

fibonacci(11)

#Wile loop
def while_fibonacci(n):

    first_num = 0
    second_num = 1
    while first_num >= n:
        print(first_num)
        next_num = first_num + second_num
        first_num, second_num = second_num, next_num   

while_fibonacci(10)