# x = ["Sun","Tik"]
# print(x)

# x[1] = "Vava"
# print(x)

# x.append("Ton")
# print(x)

# x = ["Sun","Tik"]
# x.pop(0)
# print(x)

# x = ["Sun","Tik","Ton","Vava","Gap"]
# # print(len(x)) หาความยาวในlist #นับตำแหน่งมาบอก
# for i in range(len(x)):
#     print(x[i])

# for speaker in x:
#     print(speaker) 
#     #ปริ้นต์ค่าข้างในเรียงมา

# score = [99,10,23,50]
# sum = 0
# for i in range(len(score)):
#     print(sum)
#     sum += score[i]
# print("total :",sum)

# num = [1,2,3,4,5,6,7,8,9,10]
# for number in num:
#     if (number % 2 == 0):
#         print("even:",number)
#     else:
#         print("odd:",number)

# x = {"name":"Sun",
#       "sid":671305}
# print(x["name"],x["sid"])

# x["score"] = 100
# print(x)
# x["name"] = "Tik"
# print(x)

# students = [
#     {"name":"Sun","sid":671305,"score":100},
#     {"name":"Tik","sid":671305,"score":53}
# ]

# #print(students[0]["name"])
# # for student in students:
# #     print(student["name"],student["score"])

# for student in students:
#     if (student["score"] >= 90):
#         student["score"] = "A"
#     elif (student["score"] >= 80 and student["score"] < 90 ):
#         student["score"] = "B"
#     elif (student["score"] >= 70 and student["score"] < 80):
#         student["score"] = "C"
#     else:
#         student["score"] = "F"
#     print(student)