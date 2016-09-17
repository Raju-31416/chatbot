qry_categories = dict()
from nltk.corpus import wordnet as wn

query="tell me the details about places to visit in Rajasthan"
#pos tag query, to extract relevant terms, hence prepare below list

list_of_terms = query.split(" ");

# append synsets
for term in list_of_terms:
	for i in wn.synsets(term):
		key=wn.morphy(term)
                for j in i.lemmas():  # Iterating through lemmas for each synset.
			# append synonyms
			syn = str(j.name())
			if key in qry_categories:
    				qry_categories[key].append(syn)
			else:
        			# create a new array in this slot
        			qry_categories[key] = [syn]
			

for c in qry_categories:
	qry_categories[c] = list(set(qry_categories[c]))
	#print c, ':', qry_categories[c]
print qry_categories
