import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
import spacy
parsing = spacy.load('en')
wnlmt = nltk.WordNetLemmatizer().lemmatize
psst = nltk.PorterStemmer().stem

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
			weight = 0.0
			if word in bags_dict[faq]:
				weight = float(user_bags[word] * bags_dict[faq][word]) / sum(bags_dict[faq].values())
			else:
				weight = 0.0
			matched[faq].append(weight)
	return matched

def preprocess(table, bags_dict, regexp, switch_ls):
	# preprocess text file
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
		tokenized1 = [x for x in tokenized if not x in stopwd]
		if switch_ls == 'lemma':
			tokenized1_next = lemmatized(tokenized1)
		else:
			tokenized1_next = stemmed(tokenized1)
		bags_dict[each] = get_bags(tokenized1_next, bags)

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

def print_topten(sorted_key, table, table_weights):
	matched_ten = 0
	for each in sorted_key:
		if matched_ten == 10:
			break
		print "\n" + each + "? " + str(table_weights[each])
		print "" + table[each]
		print "---"
		matched_ten += 1
	print ""

def wn_pos(word_tag):
    if word_tag.startswith('J'):
        return wordnet.ADJ
    elif word_tag.startswith('R'):
        return wordnet.ADV
    elif word_tag.startswith('V'):
        return wordnet.VERB
    else:
        return wordnet.NOUN

def lemmatized(tokenized):
	word_pos_tags = nltk.pos_tag(tokenized)
	lemmatized = []
	for each in word_pos_tags:
		lemmatized.append(wnlmt(each[0], wn_pos(each[1])))
	return lemmatized

def stemmed(tokenized):
	return [psst(each) for each in tokenized]

def tokenize_to_sent(table_sentences, table):
	for each in table:
		question = regexp.sub(' ', each)
		ans = regexp.sub(' ', table[each])
		tmp = question.lower() + " " + ans.lower()
		tokenized = nltk.word_tokenize(tmp)
		tokenized1 = [x for x in tokenized if not x in stopwd]
		table_sentences[each] = tokenized1
	return table_sentences

def get_synset(word, post_tag):
    wn_postag = wn_pos(post_tag)
    try:
        return wordnet.synsets(word, wn_postag)[0]
    except:
        return None

def wordnet_matching(user_input, each_sent):
	wn_res = 0.0
	count = 0
	s1 = nltk.pos_tag(user_input)
	s2 = nltk.pos_tag(each_sent)
	ss1 = [get_synset(each[0], each[1]) for each in s1]
	ss1 = [each for each in ss1 if each is not None]
	ss2 = [get_synset(each[0], each[1]) for each in s2]
	ss2 = [each for each in ss2 if each is not None]
	
	for each1 in ss1:
		max_res = max([each1.path_similarity(ss) for ss in ss2])
		if max_res is not None:
			wn_res += max_res
			count += 1
	return wn_res / count

def dependency_parsing(sent):
	return [each.dep_ for each in sent]

def parsing_matching(user_input, each_sent):
	s1 = parsing(' '.join(user_input).decode('utf-8'))
	s2 = parsing(' '.join(each_sent).decode('utf-8'))
	ss1 = dependency_parsing(s1)
	ss2 = dependency_parsing(s2)
	return s1.similarity(s2)



# Main
regexp = re.compile('[^a-zA-Z]')
table = {}
bags_dict = {} # key = question, value = bags of words {word: count}
stopwd = set(stopwords.words('english'))
preprocess(table, bags_dict, regexp, 'lemma')

user_input  = raw_input("Enter a FAQ related to TOEFL: ")
user_tokenized = regexp.sub(' ', user_input)
user_tokenized1 = nltk.word_tokenize(user_tokenized.lower())
user_tokenized2 = [x for x in user_tokenized1 if not x in stopwd]
user_tokenized3 = lemmatized(user_tokenized2)
user_bow = get_bags(user_tokenized3, {})

matched_weight = matching(bags_dict, user_bow)
matched_weight_next = matching_count(matched_weight, user_bow.keys(), bags_dict)

matched_weight_sorted = sorted(matched_weight_next, key = matched_weight_next.get, reverse = True)
print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "+Top 10 results based on extracted lemmas as features+"
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print_topten(matched_weight_sorted, table, matched_weight_next)

# stemmed words
bags_dict_stem = {}
preprocess({}, bags_dict_stem, regexp, 'stem')

user_tokenized_stem = stemmed(user_tokenized2)
user_tokenized_stem_bow = get_bags(user_tokenized_stem, {})

matched_weight_stem = matching(bags_dict_stem, user_tokenized_stem_bow)
matched_weight_next_stem = matching_count(matched_weight_stem, user_tokenized_stem_bow.keys(), bags_dict_stem)

matched_weight_sorted_stem = sorted(matched_weight_next_stem, key = matched_weight_next_stem.get, reverse = True)
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "+Top 10 results based on extracted stemmed words as features+"
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print_topten(matched_weight_sorted_stem, table, matched_weight_next_stem)

# parsing
table_sentences = tokenize_to_sent({}, table)
table_weight_parse = {}
for each in table_sentences:
	table_weight_parse[each] = parsing_matching(user_bow.keys(), table_sentences[each])

table_weight_parse_sorted = sorted(table_weight_parse, key = table_weight_parse.get, reverse = True)
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "+Top 10 results based on extracted features using dependency parsing+"
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print_topten(table_weight_parse_sorted, table, table_weight_parse)

# wordnet
table_weight_wn = {}
for each in table_sentences:
	table_weight_wn[each] = wordnet_matching(user_bow.keys(), table_sentences[each])

matched_weight_wn_sorted = sorted(table_weight_wn, key = table_weight_wn.get, reverse = True)
print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "+Top 10 results based on extracted features using WordNet+"
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print_topten(matched_weight_wn_sorted, table, table_weight_wn)



