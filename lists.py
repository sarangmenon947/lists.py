colours = ["red", "orange", "green", "red", "magenta", "green", "magenta", "pink", "violet", "pink", "violet"]
print(colours)
print(len(colours))

print(colours.count("red"))
colours.append("purple")
print(colours)

if "green" in (colours):
    print(True)
if "green" not in (colours):
    print(False)

print(colours[1])
print(colours[8])

print(colours.index("orange"))
print(colours.index("violet"))

print(colours[-1])
print(colours[0:5])
print(colours[4:8])
colours.reverse()
print(colours)

print(colours[::-1])
colours.remove("violet")

print(colours)
colours.pop(5)
print(colours)
colours.pop()
print(colours)
colours[4]="green"
print(colours)