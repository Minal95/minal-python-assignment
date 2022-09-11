x=int(input("Enter a number:"))
match x:
    case x if x%2==0:
        print("Saurabh Shukla")
    case x if x%2!=0 and x>0:
        print("Prateek Jain")
    case x if x%2!=0 and x<0:
        print("Aditya Chaudhary")
