year=int(input("Enter year number:"))
match year:
    case year if year%100!=0 and year%4==0:
        print("Non Century Leap Year")
    case year if year%400==0:
        print("Century Leap Year")
    case year if year%100!=0 and year%4!=0:
        print("Non Century Non Leap Year")
    case year if year%400!=0:
        print("Century Non Leap Year")