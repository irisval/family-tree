from collections import defaultdict, OrderedDict
import json
import copy
from graph import Person, Graph 



def loadJSON():
	with open('windsors.json', 'r') as f:
	 	data = json.load(f, object_pairs_hook=OrderedDict)

	global graph, people
	graph = Graph()
	people = []

	family = data['Windsors']
	relations = ['spouse', 'ex_spouse', 'mother', 'father', 'children']


	for member in family:
		person = Person(member, family[member]["id"], family[member]["spouse"], family[member]["ex_spouse"], family[member]["father"], family[member]["mother"], family[member]["children"])
		people.append(person)

	for person in people:
		for relation in person.relationships:
			if relation is not None:
				if isinstance(person.relationships[relation], list):
					for otherMemberId in person.relationships[relation]:
						graph.addRelationship(person, people[otherMemberId])
				else:
					otherMemberId = person.relationships[relation]
					if otherMemberId is not None:
						graph.addRelationship(person, people[otherMemberId])

def main():
	loadJSON()
	link = [[0,21],[0,1],[8,47],[46, 43],[3,24],[10,15],[20,23],[5,40],[9,17],[6,28]]
	connections = []

	for num in link:
		connections = graph.findRelationship(people[num[0]], people[num[1]])
		print("\nThe most direct line of relation between " + str(people[num[0]]) + " and " + str(people[num[1]]) + " is:")
		for person in connections:
			print("\t--> " + str(person))
	


main()
