"""
Author - bhakti suryawanshi
Docstring - this file gives information about how to calculate area.
Date - 18 nov 2022
"""

"""
#doc string
"""


try:
    while(True):
        
        _title = ("Calculate area of shape")
        print(_title.center(50,'*'))


        print("******List Of Shapes******")
        print("1]Traingle")
        print("2]Circle")
        print("3]Square")
        print("4]Exit")
        choice = int(input("Enter Your Choice [1/2/3/4] = "))
        if choice in [1,2,3,4]:
            if choice == 1:
                #for calculation of area of traingle
                print("**********Calculate Area of Traingle********")
                a = float(input('Enter first side: '))
                b = float(input('Enter second side: '))
                c = float(input('Enter third side: '))

                _semi_perimeter = (a + b + c) / 2
                area = (_semi_perimeter*(_semi_perimeter-a)*(_semi_perimeter-b)*(_semi_perimeter-c)) ** 0.5
                print('The area of the triangle is %0.2f' %area)

            elif choice == 2:
                #for area of circle
                print("******Claculate Area Of Circle******")

                π = 3.14  
                Radius = float (input ("Please enter the radius of the given circle: "))  
                area_of_the_circle = π * Radius * Radius  
                print (" The area of the given circle is: ", area_of_the_circle)  

            elif choice == 3 :
                #for calculation of area of square
                print("*******Area Of Square********")

                _side = float(input("Please enter the side of square : "))
                area_square=_side*_side  
                print("Area of the square="+str(area_square))
                
            elif choice == 4:
                print("*********EXIT*********")
            
            else:
                print("Please Enter Valid No.")
            break
            
except BaseException as ex:
    print(ex)
    



