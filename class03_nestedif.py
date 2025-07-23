# username = input("username: ")
# password = input("Password: ")

# if username == "admin":
#     if password == "admin123":
#         print("You're admin")
#     else:
#         print("worng")
# elif username == "user":
#     if password == "user123" :
#         print("You're user")
#     else:print("worng")
# else:
#     print("Not found")

# x = 10
# x += 10
# x = x + 10
# print(x)

# x = "ตะแน่ว"
# x += "เดอะมอลล์บางกะปิ"
# print(x)

x = input("meme : ")
word = ""
b = "the mall bangkae"
t = "the mall thapra"
p = "the mall bangkapi"

if x == "ตะแน่ว" :
    word = input("branch : ")
    if word == p :
        print(x+p)
    elif word == t :
        print(x+t)
    elif word == b :
        print(x+b)
    else :
        print("Not Found")
elif x == "tung tung" :
    word = input("branch : ")
    if word == p :
        print(x+p)
    elif word == t :
        print(x+t)
    elif word == b :
        print(x+b)
    else :
        print("Not Found")
else:
    print("Not found")