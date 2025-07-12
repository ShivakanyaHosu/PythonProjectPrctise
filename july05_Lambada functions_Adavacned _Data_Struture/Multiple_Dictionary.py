student_info3 = {
    "Name": " Shiva",
    "Age": 26,
    "Address": {
        "State": "Karnataka",
        "City": "Benglore"
    }
}

student_info4 = {
    "Name": " Shivani",
    "Age": 27,
    "Address": {
        "State": "Karnataka",
        "City": "Belaganvi"
    }
}
student_list = [student_info3, student_info4]
print(student_list)
print(student_list[0])
print(student_list[1])
print(student_list[1]["Age"])
print(student_list[1]["Address"]["City"])
print(student_list[1]["Address"])

# without list we can access by using dictionary also
print(student_info4["Address"])
print(student_info4["Address"]["State"])
