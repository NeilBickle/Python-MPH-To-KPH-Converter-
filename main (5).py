print("Welcome To The KPH To MPH Converter In Python")
print("1. MPH To KPH");
print("2. KPH To MPH");
Answer = int(input("Enter Your Choice: "));
if (Answer>=1 and Answer<=2):
    print("Enter A Number: ");
    NumOne = int (input());
    if Answer == 1:
        resource = NumOne * 1.609;
        print("Result = ", resource);
        input('Press the ENTER key to continue')
        exit();
    elif Answer == 2:
        resource = NumOne / 1.609;
        print("Result = ", resource);
        input('Press the ENTER key to continue')
        exit();
else:
    print("What You Have Inputed Is Incorrect");
