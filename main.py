from collections import defaultdict, OrderedDict
import json
import copy
from graph import Person, Graph 



def main():
	with open('windsors.json', 'r') as f:
	 	data = json.load(f, object_pairs_hook=OrderedDict)

	graph = Graph()
	family = data['Windsors']
	relations = ['spouse', 'ex_spouse', 'mother', 'father', 'children']
	people = []

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


	connection = graph.findRelationship(people[0], people[21])

	statement = "The most direct line of relation between " + str(people[0]) + " and " + str(people[21]) + " is:"
	for person in connection:
		statement += "\n\t--> " + str(person)
	print(statement)

main()
