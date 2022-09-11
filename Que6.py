s=str(input("Enter a string:"))
s.string()
match s:
    case s if ' ' in s:
        print("Multiword Sting")
    case s if ' ' not in s:
        print("Single Word String")
