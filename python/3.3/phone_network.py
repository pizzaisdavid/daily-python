def phone_network(filename):
	network, calls = parse_input(filename)
	network = create_network(network)
	for call in calls:
		network = place_call(network, call)

def parse_input(filename):
	items = {'network':[], 'calls':[]}
	key = 'network'
	for line in open(filename).readlines():
		item = line.split()
		if item == []:
			key = 'calls'
			continue
		items[key].append(item)
	return items['network'], items['calls']

def create_network(connections):
	dictonary = skeleton_network(connections)
	for start, end, unit in connections:
		unit = int(unit)
		dictonary[end].append((start, unit))
		dictonary[start].append((end, unit)) # allows for two sided web
	return dictonary

def skeleton_network(connections):
	dictonary = {}
	for key, location, _ in connections:
		dictonary[key] = []
		dictonary[location] = [] # allows for two sided web
	return dictonary

def place_call(network, call):
	path = build_call(netowrk, call)

def build_call(network, call):
	start, end = call

phone_network('phone_network.txt')
