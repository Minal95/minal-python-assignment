print("Hello guys!")
print("1.Check whether given set of three numbers are length of an isosceles trialgle or not.")
print("2. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not")
print("3. Check whether a given set of three numbers are equilateral triangle or not")
print("Exit")
print("Enter your choice")
#isosceles= two sides same length
#right angle triangle=h**2=p**2 + b**2
#equilateral triangle=3 sides equal
choice=int(input())
match choice:
    case 2:
        print("Enter three numbers:")
        p,b,h=int(input()),int(input()),int(input())
        if h**2==p**2 + b**2:
            print("It's a right angle triangle.")
        else:
            print("Oops! it's not a right angle triangle.")    
    case 1: 
        print("Enter three numbers:")
        a,b,c=int(input()),int(input()),int(input())
        if a==b or a==c or b==c:
            print("It's an isosceles triangle.")
        else:
            print("Oops! It's not an isosceles triangle.")    
    case 3:
        print("Enter three numbers:")
        a,b,c=int(input()),int(input()),int(input())
        if a==b==c:
            print("It's an equilateral triangle.")
        else:
            print("It's not an equilateral triangle.")
    case 4:
        exit()
    case _:
        print("Invalid input")               
        
