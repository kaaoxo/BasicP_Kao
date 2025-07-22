x = float(input("enter your distance : "))


if (x>=5 and x<=50) :
    print("ค่าส่ง: 10 บาท",)
elif (x>50 and x<=100) :
    print("ค่าส่ง : 15 บาท ")
elif (x>100 and x<=300) :
    print("ค่าส่ง : 25 บาท")
elif (x>300 and x<=500) :
    print("ค่าส่ง : 35 บาท")
elif (x>500):
    print("ค่าส่ง : 45 บาท")
else :
    print("ค่าส่ง : 0 บาท")