def phone_network(filename):
	network, calls = parse_input(filename)
	network = create_network(network)
	print network
	print look_up(network, ('C', 'E'))

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
	web = {}
	for connection in connections:
		unit, start, end = sorted(connection)
		if start not in web:
			web[start] = {}
		web[start][end] = int(unit)
	return web

def look_up(network, call):
	start, end = sorted(call)
	return network[start][end]

phone_network('phone_network.txt')
