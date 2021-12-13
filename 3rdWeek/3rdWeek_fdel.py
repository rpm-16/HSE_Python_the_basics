str = str(input())
str = "In the hole in the ground there lived a hobbit"

if str.find("h") != -1:
    print(str.find("f"))
if str.find("h", -1) != -1:
    print(str.find("f", -1))
