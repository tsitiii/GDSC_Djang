dic={}
def basic_operation(num1, num2):
    try:
            add=num1+num2
            sub=num1-num2
            mult=num1*num2
            div=num1/num2
            dic[sub]={"Addition":add,"Subtraction":sub,"Multiplication":mult,"Division":div}
            return dic
    except ZeroDivisionError:
        print("Division by zero is not allowed")



def power_operation(base, exponent, **kwargs):
    try:
            result=base**exponent
            if "arg" in kwargs:
                arg=kwargs['arg']
                result= result%arg
            return result
    except:
            print(ZeroDivisionError)

def apply_operation(operation_list):
        results = list(map(lambda operation: operation[0](*operation[1:]), operation_list))
        return results
def add(a,b):
        return a+b
def mult(a,b):
        return a*b
