student_info = {
    "Name": " Shiva",
    "Age": 26,
    "Address": "Karnataka"
}
print(student_info["Age"])
student_info["Age"] = 27
print(student_info)

# Another way to create a dictionary
student_info2 = dict(Name="Shivani", Age=26, Address="Benglore")

# dictionary within the dictionary
student_info3 = {
    "Name": " Shiva",
    "Age": 26,
    "Address": {
        "State": "Karnataka",
        "City": "Benglore"
    }
}

print(student_info3)
