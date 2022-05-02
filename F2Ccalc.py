print('''
    ███████╗    ████████╗ ██████╗      ██████╗    
    ██╔════╝    ╚══██╔══╝██╔═══██╗    ██╔════╝    
    █████╗         ██║   ██║   ██║    ██║         
    ██╔══╝         ██║   ██║   ██║    ██║         
    ██║            ██║   ╚██████╔╝    ╚██████╗    
    ╚═╝            ╚═╝    ╚═════╝      ╚═════╝    
                                              
          ██████╗ █████╗ ██╗      ██████╗          
         ██╔════╝██╔══██╗██║     ██╔════╝          
         ██║     ███████║██║     ██║               
         ██║     ██╔══██║██║     ██║               
         ╚██████╗██║  ██║███████╗╚██████╗          
           ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝          
                                              
''')

def FtoC(tempF): #defining function FtoC with tempF var
    return (tempF - 32) * (5/9) #function calcs  & returns temp in C

#asks for input,
tempF = input("Enter Temp in Degrees F. Enter Q to quit:")

while tempF != 'q' and tempF != 'Q':
    try:
        tempF = float(tempF)#saves as float var #converts input to float if int
        tempC = FtoC(tempF) #calls on function FtoC
        print('==============================================')
        print(tempF, 'Degrees Fahrenheit') #prints temp in F
        print(round(tempC, 2), "Degrees Celcius") #rounds and prints temp in C
        print('==============================================')
        tempF = input("Enter Temp in Degrees F. Enter Q to quit:")
    except ValueError:
        #if input can't be converted to float
        tempF = input("Please enter a valid temperature:")
        


'''
#Raw F to C with no loop
def FtoC(tempF): #defining function FtoC with tempF var
    print(tempF, 'Degrees Fahrenheit') #prints temp in F
    return (tempF - 32) * (5/9) #function calcs  & returns temp in C
    
tempF = float(input("Enter Temp in Degrees F:"))#asks for input, type to float
tempC = FtoC(tempF) #calls on function FtoC
print(round(tempC, 2), "Degrees Celcius") #rounds and prints temp in C
'''
