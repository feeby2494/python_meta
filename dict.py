my_d = {
    1: "Test",
    "Name": "Jim"
}

# print(my_d["Name"])
# # my_d[1] = "Not a test"

# print(my_d[1])
# del my_d[1]

# Only prints out keys
for x in my_d:
    print(x)


# Need both key, value
for key, value in my_d.items():
    print(key, value)

