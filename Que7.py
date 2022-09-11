n=int(input("Enter a number:"))
match n:
    case n if n==0:
        print("Zero")
    case n if n<0:
        print("Negative Number")
    case n if n>0:
        print("Positive Number")