formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("One", "Two", "Three", "Four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"Own text",
	"Maybe a poem",
	"Or a song about fear"
))