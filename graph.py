from collections import defaultdict, OrderedDict
import json
import copy


# directed graph repped thru adjacency list
class Person:
	def __init__(self, name, idNum, spouse=None, ex_spouse=None, father=None, mother=None, children=None):
		self.name = name
		self.idNum = idNum
		self.relationships = {"spouse": spouse, "ex_spouse": ex_spouse, "father": father, "mother": mother, "children": children}


	def __repr__(self):
		return self.name


class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addRelationship(self, u, v):
		if v is not None:
			self.graph[u].append(v)

	def findRelationship(self, u, v):
		queue = [[u]]
		visited = []

		while (len(queue) > 0):
			path = queue.pop(0)
			node = path[-1]
			
			if node not in visited:
				relations = self.graph[node]
				
				for relation in relations:
					new_path = copy.deepcopy(path)
					new_path.append(relation)
					queue.append(new_path)
					
					if relation == v:
						return new_path
				visited.append(node)
		return "Path does not exist."

		
	def __repr__(self):
		return str(self.graph)

