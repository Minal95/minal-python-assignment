s1=input("Enter first string:")
s2=input("Enter second string:")
match (s1,s2):
    case (s1,s2) if s1==s2:
        print("Identical String")
    case (s1,s2) if s1>s2:
        print(s2,s1)
        #print("{} comes after {}".format(s1,s2))
    case (s1,s2) if s1<s2:
        print(s1,s2)
       # print("{} comes after {}".format(s2,s1))
