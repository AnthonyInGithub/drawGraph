#This program is intended to draw the graph according to the formula you entered.
#IMPORTANT: NEED MATPLOTLIB AND NUMPY INSTALLED IN ORDER TO RUN
#NOTE: This program does not support the decimal power of nagative number, because the Numpy does not support it.
import matplotlib.pyplot as plt
import numpy as np 
import re
import warnings
warnings.filterwarnings('error')

history = []


def defineGraph(formula, start_point, end_point):
    coefficient = re.match("^[0-9\.\+-]*[a-zA-Z]", formula)
    if(coefficient == None): #if user inputs a constant
        coefficient = 0
    elif(re.search("^[^a-z^A-Z]+", coefficient.group()) == None):# if the input is x(no coefficient enter)
        coefficient = 1
    else:
        coefficient = re.search(
            "^[0-9\.\+-]+", coefficient.group()).group()

    temp_ex = re.search("\^[+,-]?[0-9\.]*[+,-]?", formula)
    if(temp_ex == None):# if user only enter x(no exponential entered)
        exponential = 1
    else:
        exponential = temp_ex.group().strip("+").strip("-").replace("^", "")

    k = re.search("[1-9a-zA-Z]?[+,-]?[0-9\.]+$", formula)
    if(k == None):
        k = 0
    else:
        if(k.group()[1:2] == "+" or k.group()[1:2] == '-'):#check whether it has P/N sign
            k = float(k.group()[1:])
        else:
            k = float(k.group())
    try:
        debug = re.search("\^[0-9\.]+$", formula).group()#check for the special case where input is "x^2"
        k = 0
    except:
        pass

    print("coefficient: "+str(coefficient))
    print("exponential: "+str(exponential))
    print("constant: "+ str(k))
    
    x = np.linspace(int(start_point), int(end_point), 100)
    try:
        y = float(coefficient)*(x**float(exponential)) + float(k)
    except Warning as e:
        print("This program does not support frictional power of negative num, because Numpy does not allow it to do so.")

    return x, y

def main():
    index = ""
    while True:
        start_point = input("enter the start point of x: ")
        end_point = input("enter the end point of x: ")

        if index == "":
            formula = input("enter your formula(bx^n+k)(enter \"exit\" to exit): ")
        else:
            formula = history[int(index)-1]
            print("Your formula is: "+formula)
            history.pop()

        if(formula == "exit"):
            break

        try:
            x, y = defineGraph(formula, start_point,end_point)
        except:
            print("wrong input, try again")
            print("---------------")
            continue
        history.append(formula)
        plt.plot(x, y)#plot the function
        plt.show()
        
        print("Formulas you have entered: "+str(history))
        index = input("Enter the index of any former formula you want to reuse(start by 1)(press enter to skip): ")
        if index != "":#user get formula from history
            try:
                index = re.search("^[0-9]*$",index).group()
                if int(index)> history.__len__() or int(index)<1:
                    print("your index is out of the range, enter your formula by hand please")
                    index = ""
            except:
                print("wrong input, enter your formula by hand please")
                index = ""
        else:
            print("skip")
        print("---------------")



#[-+]?([0-9]*\.?[0-9]+)?(x(\\^[+-]?[0-9]+)?)?

main()
