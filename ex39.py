states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

cities = {
	'CA' : 'San francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
	}
	
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print('NY state has: ', cities['NY'])
print('OR state has: ', cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print("Michigan's has: ", cities[states['Michigan']])
print("Florida's has: ", cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbrevated {abbrev}")
	
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the {city}")
	
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbrevated {abbrev}")
	print(f"and has city {cities[abbrev]}")


print('-' * 10)
state = states.get('Texas')

if not state:
	print("Sorry, no Texas.")
	

city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}")















