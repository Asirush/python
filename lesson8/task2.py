def oddNumbers(num1, num2):
    a = num1
    while(a < num2):
        if a %2 != 0:
            print(a)
            a = a+1
        else:
            a=a+1
            
if "___main____" == __name__:
    num1 = int(input())
    num2 = int(input())
    oddNumbers(num1, num2)