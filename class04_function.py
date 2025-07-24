# def hello(name):
#     print("ค่าที่รับเข้ามาแสดงจาก function: ",name) #สร้างเฉยๆ


# name = input("ค่าที่รับ: ")
# hello(name)

# def sum(a,b):
#     result = a + b
#     print("ผลรวม: ",result)

# num1 = int(input("กรอกเลข1: "))
# num2 = int(input("กรอกเลข2: "))
# sum(num1,num2)

# def sum(a,b):
#     result = a + b
#     return result

# num1 = int(input("กรอกเลข1: "))
# num2 = int(input("กรอกเลข2: "))
# result = sum(num1,num2)
# print(result)

def add(num1,num2):
    result = num1 + num2
    return result

def minus(num1,num2):
    result = num1 - num2
    return result

def muntiple(num1,num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    if num1 < num2:
        print("ไม่สามารถหาค่าได้")
    result = int(num1/num2)
    return result

def is_even(num):
    result = num % 2
    if result == 0:
        return("is even number")
    elif result == 1:
        return(" is odd number")
    
 
def main():
    num1 = int(input("กรอกเลขตัวที่1 : "))
    num2 = int(input("กรอกเลขตัวที่2 : "))
    print(" + - * /  choose one")
    print(" [1] + ")
    print(" [2] - ")
    print(" [3] * ")
    print(" [4]] / ")
    operation = input("choose only one : ")
    if (operation == "1"):
        result = add(num1,num2)
        print("ผลบวกคือ: ",result)
    elif (operation == "2"):
        result = minus(num1,num2)
        print("ผลลบคือ: ",result)
    elif (operation == "3"):
        result = muntiple(num1,num2)
        print("ผลคูณคือ: ",result)
    elif (operation == "4"):
        result = divide(num1,num2)
        print("ผลหารคือ: ",result)

    #เรียก is_even เพื่อเช็กว่าผลลัพธ์ที่ได้เป็นเลขคู่ไหม
    print(is_even(result))
     
main()