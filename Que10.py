s1=input("What is your favourite colour?")
l1=["yellow","blue","orange","white","black","red"]
for colour in l1:
    if colour in s1:
        c=colour
        break
    else:
        c="other"
match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "white":
        print("Friday")
    case "black":
        print("Saturday")
    case "other":
        print("Sunday")
print()
