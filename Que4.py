age=int(input("Enter age of a person:"))
match age:
    case age if age<10:
        print("Kid")
    case age if 10<=age<20:
        print("Teen")
    case age if 20<=age<40:
        print("Young")
    case age if 40<=age<60:
        print("Experienced")
    case age if age>=60:
        print("Senior Citizen")