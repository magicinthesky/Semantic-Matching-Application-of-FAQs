import nltk
import re
from nltk.corpus import stopwords

# get bag of words with count
def get_bags(tokenized, bags):
	for word in tokenized:
		if word not in bags:
			bags[word] = 1
		else:
			bags[word] += 1
	return bags

def matching(bags_dict, user_bags):
	matched = {}
	for faq in bags_dict:
		matched[faq] = []
		for word in user_bags:
			weight = 0
			if word in bags_dict[faq]:
				weight = float(user_bags[word] * bags_dict[faq][word]) / sum(bags_dict[faq].values())
			else:
				weight = 0.0
			matched[faq].append(weight)
	return matched

def preprocess(table, bags_dict, regexp):
	with open("data.txt") as data:
		for line in data:
			row = []
			row = line.rstrip("\n").split("?")
			table[row[0]] = row[1]

	for each in table:
		bags = {}
		question = regexp.sub(' ', each)
		ans = regexp.sub(' ', table[each])
		tmp = question.lower() + " " + ans.lower()
		tokenized = nltk.word_tokenize(tmp)
		bags_dict[each] = get_bags(tokenized, bags)

def matching_count(matched_weight, user_bow_keys, bags_dict):
	matching_res = {}
	for question in matched_weight:
		tfidf = 0.0
		for i in range(len(user_bow_keys)):
			idf = 0
			for bow in bags_dict.values():
				if user_bow_keys[i] in bow:
					idf += 1
			if idf != 0:
				idf = 50.0 / idf
			tfidf += matched_weight[question][i] * idf
		matching_res[question] = tfidf
	return matching_res

def print_topten(matched_weight_sorted, table):
	matched_ten = 0
	for each in matched_weight_sorted:
		if matched_ten == 10:
			break
		print "\n" + each + "? " + str(matched_weight_next[each])
		print "" + table[each]
		print "---"
		matched_ten += 1



# Main
regexp = re.compile('[^a-zA-Z]')
table = {}
bags_dict = {} # key = question, value = bags of words {word: count}
stopwd = set(stopwords.words('english'))
preprocess(table, bags_dict, regexp)


user_input  = raw_input("Enter a FAQ related to TOEFL: ")
user_tokenized = regexp.sub(' ', user_input)
user_tokenized1 = nltk.word_tokenize(user_tokenized.lower())
user_bow = get_bags(user_tokenized1, {})

matched_weight = matching(bags_dict, user_bow)
matched_weight_next = matching_count(matched_weight, user_bow.keys(), bags_dict)

matched_weight_sorted = sorted(matched_weight_next, key = matched_weight_next.get, reverse = True)
print "\n+++++++++++++++++++++++++++"
print "+Top 10 results for Task 2+"
print "+++++++++++++++++++++++++++"
print_topten(matched_weight_sorted, table)





