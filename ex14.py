from sys import argv

script, user_name  = argv
prompt = '>'

print(f"Hi I'm {user_name}, I'm the {script} script")
print("I'd like top ask you few questions. ")

print(f"Do you like me {user_name}")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer you have ?")
computer = input(prompt)

print(f"""
	Alright, so you said {likes} about liking me.
	you live in {lives}. NOT sure where it is.
	And you have a {computer} computer.. Nice.
""")
