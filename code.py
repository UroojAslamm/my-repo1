

user_input= float(input("enter a number: "))
user_input2= float(input("enter your second number: "))

def add(user_input, user_input2):
    
    """
    Description:
    function num will add the two numbers and return them

    Params: 
    user_input this is the first number
    user_input2 this is the second number

    return:
    sum type float will give the summation of the two numbers 
    """
    sum=user_input+user_input2
    return sum




def subtract(x,y):
        """
    Description:
    function num will subtract the two numbers and return them

    Params: 
    user_input this is the first number
    user_input2 this is the second number

    return:
    subtract type float will give the subtraction of the two numbers 
    """
subtract=x-y
return subtract


subtract = subtract(user_input,user_input2)
print(subtract)

def divide(a,b):

    """
    Description:
    function divide will divide the two numbers and return them

    Params: 
    user_input this is the first number
    user_input2 this is the second number

    return:
    divide type float will give the quotient of the two numbers 
    """

  
   result= a//b
   return result




def main():

    user_input= float(input("enter a number: "))
    user_input2= float(input("enter your second number: "))

    addition = add(user_input, user_input2)
    print(addition)

    divide1 = divide(user_input,user_input2)
    print (divide1)

  
    subtract = subtract(user_input,user_input2)
    print(subtract)

  
 
main()



