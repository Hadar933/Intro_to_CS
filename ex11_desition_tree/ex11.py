import sys
from collections import *
import copy
import itertools


class Node:
	"""
	class for node objects.
	"""
	def __init__(self, data, pos = None, neg = None):
		self.data = data
		self.positive_child = pos
		self.negative_child = neg


class Record:
	"""
	class for record objects
	"""
	def __init__(self, illness, symptoms):
		self.illness = illness
		self.symptoms = symptoms
	
			
def parse_data(filepath):
	"""
	this function reads the file path and returns the data as records
	"""
	with open(filepath) as data_file:
		records = []
		for line in data_file:
			words = line.strip().split()
			records.append(Record(words[0], words[1:]))
		return records
		
		
class Diagnoser:
	"""
	Class that is responsible for diagnosers objects.
	"""
	def __init__(self, root):
		self.root = root
		
	def diagnose(self, symptoms):
		"""
		this function tells what is the plausible illness according to
		a list of provided symptoms, by running over a decision tree.
		:param symptoms: list of given symptoms
		:return: self.root.data - the illness in the last node
		"""
		if self.root.positive_child is None or\
				self.root.negative_child is None: # reached bottom
			return self.root.data
		if self.root.data in symptoms: # going down positive child
			new_pos_root = Diagnoser(self.root.positive_child)
			return new_pos_root.diagnose(symptoms)
		else:
			if self.root.data not in symptoms: # going down negative child
				new_neg_root = Diagnoser(self.root.negative_child)
				return new_neg_root.diagnose(symptoms)

	def calculate_success_rate(self, records):
		"""
		this function calculates the ratio between the successful
		diagnoses of the tree to the entire length of the records.
		:param records: list of records
		:return: success rate in percentage
		"""
		count = 0
		for record in records:
			illness = self.diagnose(record.symptoms)
			if record.illness == illness:
				count += 1
		final_result = count/len(records)
		return final_result

	def all_illnesses(self):
		"""
		returns all the illnesses that are kept in the leafs data
		in a list according to occurrences
		:return: lst of ordered illnesses
		"""
		lst_of_ills = []
		self.all_illnesses_helper(lst_of_ills)
		new_lst = self.illnesses_sort(lst_of_ills)
		return new_lst

	def all_illnesses_helper(self,lst):
		"""
		this function adds the data of all leafs to a list
		in an unordered fashion.
		:param lst: empty lst to which illnesses will be added
		"""
		if self.root.positive_child is None or\
				self.root.negative_child is None: # reached last node
			lst.append(self.root.data)
			return
		# recursive run over the positive nods #
		new_pos_root = Diagnoser(self.root.positive_child)
		new_pos_root.all_illnesses_helper(lst)
		# recursive run over the negative nods #
		new_neg_root = Diagnoser(self.root.negative_child)
		new_neg_root.all_illnesses_helper(lst)

	def illnesses_sort(self,lst):
		"""
		converts the list that has been made im all_illnesses_helper
		to an ordered list that shows each illness once.
		:param lst: unordered list
		:return: ordered list
		"""
		sorted_lst = (sorted(lst, key=Counter(lst).get, reverse=True))
		no_repetition = list(OrderedDict.fromkeys(sorted_lst))
		return no_repetition

	def most_rare_illness(self, records):
		"""
		the function will provide the illness that is the rarest
		among all of the illness. rarest means that it was a result
		of a decision tree the least amount of times
		:param records: list of records
		:return: rarest illness
		"""
		all_ills = self.all_illnesses()
		record_ills = []
		for record in records:
			illness = self.diagnose(record.symptoms)
			record_ills.append(illness)
		new_lst = self.illnesses_sort(record_ills)
		for item in all_ills: # item hasn't been shown at all(0 times)
			if item not in record_ills:
				return item
		return new_lst[-1] # last item in that list will be the rarest

	def paths_to_illness(self, illness):
		"""
		runs on all possible routes and returns the route that suits
		the given illness to the node reached.
		:param illness: an illness in string format
		:return: lst of all paths
		"""
		final_lst = []
		path_lst = []
		self.paths_to_illness_helper(illness,path_lst,final_lst)
		return final_lst

	def paths_to_illness_helper(self,illness,path_lst,final_lst):
		"""
		performs the recursive runs aiding the main function paths to illness
		:param illness: illness: an illness in string format
		:param path_lst: list that will represent a single path
		:param final_lst: lst of the final path
		"""
		if self.root.positive_child is None or \
				self.root.negative_child is None: # base case
			if self.root.data == illness:
				final_lst.append(copy.copy(path_lst))
		else:
			# recursive run over the positive nods #
			if self.root.positive_child:
				path_lst.append(True)
				new_pos_root = Diagnoser(self.root.positive_child)
				new_pos_root.paths_to_illness_helper(
					illness,path_lst,final_lst)
				path_lst.pop()
			# recursive run over the negative nods #
			if self.root.negative_child:
				path_lst.append(False)
				new_neg_root = Diagnoser(self.root.negative_child)
				new_neg_root.paths_to_illness_helper(
					illness,path_lst,final_lst)
				path_lst.pop()


def build_tree(records,symptoms):
	"""
	builds a tree according to the symptoms provided
	:param records: list of objects from Records class
	:param symptoms: list of symptoms in string format
	:return: root of the created tree
	"""
	bools = [True, False]
	sym_copy = copy.copy(symptoms)
	route = []
	return tree_helper(records,symptoms,bools,route,sym_copy)


def tree_helper(records,symptoms,bools,route,sym_copy):
	"""
	a function that performs the recursive runs, helping the main function
	build tree.
	:param records: list of objects from Records class
	:param symptoms: list of symptoms in string format
	:param bools: list of two boolean value true and false
	:param route: a route that is represented as a list of boolean values
	:param sym_copy: copy of symptoms
	:return: leaf and node
	"""
	if len(symptoms) == 0: # reached last node - a leaf
		leaf_data = sorting_helper(sym_copy,records,route)
		leaf = Node(leaf_data)
		return leaf
	my_node = Node(symptoms[0]) # creating the first node
	for bool in bools:
		if bool: # positive child recursive runs
			route.append(True)
			my_node.positive_child = \
				tree_helper(records,symptoms[1:],bools,route,sym_copy)
		else:
			route.append(False) # negative child recursive runs
			my_node.negative_child =\
				tree_helper(records,symptoms[1:],bools,route,sym_copy)
		route.pop()
	return my_node


def sorting_helper(syms,recs,route):
	"""
	converts the route list to a list representing a route to a leaf
	:param recs: list of objects from Records class
	:param syms: list of symptoms in string format
	:param route: a route that is represented as a list of boolean values
	:return: first value of the converted list
	"""
	bad_lst = []
	recs_copy = copy.copy(recs)
	for rec in recs_copy: # removing all symptoms that are irrelevant
		for i in range(len(route)):
			if route[i]:
				if syms[i] not in rec.symptoms:
					bad_lst.append(rec)
					break
			else:
				if syms[i] in rec.symptoms:
					bad_lst.append(rec)
					break
	for item in bad_lst: # performing the final removal
		recs_copy.remove(item)
	if not recs_copy:
		return bad_lst[0].illness # random illness if lst is empty
	ills_lst = illness_lst(recs_copy)
	sorted_ills = Counter(ills_lst).most_common(1) # getting most common
	return sorted_ills[0][0]


def illness_lst(recs_copy):
	"""
	converts a list of records to a list of illnesses
	:param recs_copy:
	:return:
	"""
	ills_lst = []
	for rec in recs_copy:
		ills_lst.append(rec.illness)
	return ills_lst


def optimal_tree(records, symptoms, depth):
	"""
	returns the tree with the highest success rate
	:param records: list of objects from Records class
	:param symptoms: list of symptoms in string format
	:param depth: length of subset
	:return: tree with the highest success rate
	"""
	lst_of_trees = []
	lst_of_rates = []
	syms_subsets = itertools.combinations(symptoms,depth)
	for subset in syms_subsets:
		tree = build_tree(records,subset)
		lst_of_trees.append(tree)
		diag = Diagnoser(tree)
		suc_rate = diag.calculate_success_rate(records)
		lst_of_rates.append(suc_rate)
	idx_of_max = lst_of_rates.index(max(lst_of_rates))
	return lst_of_trees[idx_of_max]


if __name__ == "__main__":


		# Manually build a simple tree.
		#                cough
		#          Yes /       \ No
		#        fever           healthy
		#   Yes /     \ No
		# influenza   cold


		flu_leaf = Node("influenza", None, None)
		cold_leaf = Node("cold", None, None)
		inner_vertex = Node("fever", flu_leaf, cold_leaf)
		healthy_leaf = Node("healthy", None, None)
		root = Node("cough", inner_vertex, healthy_leaf)

		diagnoser = Diagnoser(root)

		# Simple test
		diagnosis = diagnoser.diagnose(["cough"])
		if diagnosis == "cold":
			print("Test 1 passed")
		else:
			print("Test 1 failed. Should have printed cold, printed: ", diagnosis)


		# second test - calculate_success_rate

		influenza_leaf = Node("influenza", None, None)
		cold_leaf = Node("cold", None, None)
		mono_leaf = Node("mono", None, None)
		healthy_leaf = Node("healthy", None, None)
		strep_leaf = Node("strep", None, None)
		meningitis_leaf = Node("meningitis", None, None)
		empty_leaf = Node("empty", None, None)
		inner_vertex_11 = Node("rigidity", meningitis_leaf, empty_leaf)
		inner_vertex_10 = Node("irritability", inner_vertex_11, empty_leaf)
		inner_vertex_9 = Node("fever", inner_vertex_10, empty_leaf)
		inner_vertex_8 = Node("fever", strep_leaf, empty_leaf)
		inner_vertex_7 = Node("headache", mono_leaf, empty_leaf)
		inner_vertex_6 = Node("headache", inner_vertex_9, healthy_leaf)
		inner_vertex_5 = Node("fatigue", inner_vertex_7, inner_vertex_8)
		inner_vertex_4 = Node("sore_throat", inner_vertex_5, inner_vertex_6)
		inner_vertex_3 = Node("nausea", influenza_leaf, empty_leaf)
		inner_vertex_2 = Node("fatigue", inner_vertex_3, cold_leaf)
		inner_vertex = Node("headache", inner_vertex_2, empty_leaf)
		root_2 = Node("cough", inner_vertex, inner_vertex_4)

		diagnoser_2 = Diagnoser(root_2)

		records = parse_data(sys.argv[1])

		result = diagnoser_2.calculate_success_rate(records)

		if result == 1.0:
			print("Test 2 passed")
		else:
			print("Test 2 failed. Should have printed 1.0, printed: ", result)


		# third test - all_illnesses

		result = diagnoser_2.all_illnesses()
		if len(result) == 7:
			print("Test 3 passed")
		else:
			print("length is", len(result), "because results contains",result, "instead of 7, therfore Test 3 failed")


		# forth test - most_rare_illness
		records = parse_data(sys.argv[2])

		result = diagnoser_2.most_rare_illness(records)

		if result == 'meningitis' or 'mono' or 'influenza':
			print("Test 4 passed")
		else:
			print("Test 4 failed")

		
		# fifth test - paths_to_illness
		leaf_4 = Node("influenza", None, None)
		leaf_3 = Node("cold", None, None)
		inner_vertex_4 = Node("headache", leaf_4, leaf_3)
		leaf_2 = Node("cold", None, None)
		leaf_1 = Node("healthy", None, None)
		inner_vertex_1 = Node("headache", leaf_2, leaf_1)
		root_3 = Node("cough", inner_vertex_4, inner_vertex_1)

		illness = 'cold'
		empty_illness = 'strep'

		diagnoser_3 = Diagnoser(root_3)

		result = diagnoser_3.paths_to_illness(illness)
		result_2 = diagnoser_3.paths_to_illness(empty_illness)

		if result == [[True, False], [False, True]] and result_2 == []:
			print("Test 5 passed")
		else:
			print("Test 5 failed")


		# sixes test - build_tree
		records = parse_data(sys.argv[2])
		build_tree(records, ['fatigue', 'nausea', 'sore_throat', 'muscle_ache'])

		
		# seventh  test - optimal_tree
		record1 = Record('influenza', ['cough', 'fever'])
		record2 = Record('cold', ['cough'])
		records = [record1, record2]
		root_1 = build_tree(records, ['fever'])
		root_2 = optimal_tree(records, ['cough', 'fever'], 1)
		if root_1.data == root_2.data and \
				root_1.positive_child.data == root_2.positive_child.data and \
				root_1.negative_child.data == root_2.negative_child.data:
			print("Test 7 passed")
		else:
			print("Test 7 failed")

		records = parse_data(sys.argv[2])
		symptoms = []
		for record in records:
			for symptom in record.symptoms:
				if symptom not in symptoms:
					symptoms.append(symptom)
		print(symptoms)
		root = optimal_tree(records, symptoms, 3)

