st = input("Введите строку: ")

print (" В строке содержится" , len(st))

print(st.lower())
print(st.upper())
print(st.capitalize())

print(st.split())
print(st.split("."))
print(st.rstrip())

for s in st:
    print(s, end=" ")
