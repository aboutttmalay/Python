marks = {
    "Malay" : 100,
    "vasu" : 67,
    "somo" : 78,
    23: "Moti"
}

print(marks.items())
print()
print(marks.keys())
print()
print(marks.values())
print()


marks.update({"Malay" : 99, "Motu": 89})
print(marks)
print()
# print(marks.get("Malay56")) # It's show none
# print(marks["Harry"]) # It's show as returns an error


# print(marks.pop("Malay"))
# print(marks)

print(marks.popitem())