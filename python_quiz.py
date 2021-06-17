import math
#Given list x = [100,110,120,130,140,150], use list comprehension to create another list containing each number in the list multiplied by 5.  

x=[100,110,120,130,140,150]
newList=[]
for mult in  x:
    mult*=5

    newList.append(mult)   
    print(newList)

#Write a function named divisible_by_three that accepts a number n and prints all numbers from 1 to n that are divisible by 3. 
    def divisible_by_three(n):
        
        for x in range (n):
            if x%3==0:
                print(x)


    divisible_by_three(9)       

    #Given the nested list x = [[1,2],[3,4],[5,6]], write a function that flattens the list and returns it as [1,2,3,4,5,6]     

    def join():
        
        x=[[1,2],[3,4],[5,6]]
        flat=[]
        for i in x:
            for j in i:
                flat.append(j)
            print (flat)
    join()   

    #Write a Python function named smallest that accepts a list of unsorted integers and returns the smallest number in the list. Example:
    #smallest([3,6,8,2,4,1,5,7]) returns 1     
    def smallest(x):
        x=[]
        for i in x:
            x.sort(reverse=True)
            print (x. index[1])
    smallest([1,2,3,5])        


#Write a function that accepts list x below and uses a set to remove the duplicate letters and returns the list without duplicates

    def dupicates():
     x = ['a','b','a','e','d','b','c','e','f','g','h']
     v=set(x)
     print (v)
     newList=list(v)
     print(newList)
    dupicates() 


#Write a function named divisible_by_seven that; using the range function and a for loop returns a list containing all the numbers between 100 and 200 that are divisible by 7.


    def divisible_by_seven():
        
        for t in range(100,200):
            if t%7==0:
                print (t)
    divisible_by_seven()

#Given this list of students containing age and name,  students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}], write a function that greets each student and tells them the year they were born. e.g Hello Eunice, you were born in the year 2002.    

    #





#Create a Class Rectangle with the following Attributes and Methods
#Attributes: The class has attributes width and length that represent the two sides of a rectangle 
#Methods:
# Add a method named area which returns the area (A) of the rectangle using the formula A=width*length
#Add a method named perimeter which returns the perimeter (P) of the rectangle using the formula P=2(length+width)
class Rectsangle:
    
    def __init__(self,width,length):
        self.width=width
        self.length=length

    def area( self ,length,width):
        area= length*width
        return f" {area} is the area given length{length} and width {width}"
    def perimeter( self ,length,width):
        perimeter= 2(length+width)
        return f" {perimeter} is the area given length{length} and width {width}"    
