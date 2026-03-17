class multipleones():
    def Percentage():
        Sub1 = int(input("Enter the sub1 mark:"))
        Sub2 = int(input("Enter the sub2 mark:"))
        Sub3 = int(input("Enter the sub3 mark:"))
        Sub4 = int(input("Enter the sub4 mark:"))
        Sub5 = int(input("Enter the sub5 mark:"))
        Total = Sub1+Sub2+Sub3+Sub4+Sub5
        print("Total:", Total)
        Avg = Total/5
        print("Percentage:", Avg)
        return Avg
    
    def Triangle():
        Height = int(input("Enter the Height:"))
        Breadth = int(input("Enter the breadth:"))
        Area = (Height * Breadth)/2
        print("Area of Triangle:", Area)
        Height1 =  int(input("Enter the Height1:"))
        Height2 =  int(input("Enter the Height2:"))
        Breadth1 =  int(input("Enter the Breadth1:"))
        Perimeter = Height1 + Height2 + Breadth1
        print("Perimeter of triangle:", Perimeter)

    def Eligiblemarriage():
        Male = int(input("Enter the Male age:"))
        if(Male>=21):
            print("YOUR GENDER: Male")
            print("YOUR AGE:", Male)
            print("Eligible")
        else:
            print("YOUR GENDER: Male")
            print("YOUR AGE:", Male)
            print("Not Eligible")
            print("------")
        Female = int(input("Enter the Female age:"))
        if(Female>=18):
            print("YOUR GENDER: FEMALE")
            print("YOUR AGE:", Female)
            print("Elgible")
        else:
            print("YOUR GENDER: Female")
            print("YOUR AGE:", Female)
            print("Not Eligible")