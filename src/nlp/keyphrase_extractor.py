import pke
import string
from nltk.corpus import stopwords

def position_rank(content):
	pos = {'NOUN'}
	grammar = "NP: {<NOUN>+}"
	extractor = pke.unsupervised.PositionRank()
	extractor.load_document(input=content,
	                    language='en',
	                    normalization=None)
	extractor.candidate_selection(grammar=grammar,
	                          maximum_word_number=5)
	extractor.candidate_weighting(window=10,
	                          pos=pos)
	keyphrases = extractor.get_n_best(n=20)
	return keyphrases

def topic_rank(content):

	# 1. create a TopicRank extractor.
	extractor = pke.unsupervised.TopicRank()

	# 2. load the content of the document.
	extractor.load_document(input=content)

	# 3. select the longest sequences of nouns and adjectives, that do
	#    not contain punctuation marks or stopwords as candidates.
	pos = {'NOUN', 'PROPN' }
	stoplist = list(string.punctuation)
	stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
	stoplist += stopwords.words('english')
	extractor.candidate_selection(pos=pos, stoplist=stoplist)

	# 4. build topics by grouping candidates with HAC (average linkage,
	#    threshold of 1/4 of shared stems). Weight the topics using random
	#    walk, and select the first occuring candidate from each topic.
	extractor.candidate_weighting(threshold=0.74, method='average')

	# 5. get the 10-highest scored candidates as keyphrases
	keyphrases = extractor.get_n_best(n=20)
	return keyphrases

def text_rank(content):

	# define the set of valid Part-of-Speeches
	pos = {'NOUN', 'PROPN'}

	# 1. create a TextRank extractor.
	extractor = pke.unsupervised.TextRank()

	# 2. load the content of the document.
	extractor.load_document(input=content,
	                        language='en',
	                        normalization=None)

	# 3. build the graph representation of the document and rank the words.
	#    Keyphrase candidates are composed from the 33-percent
	#    highest-ranked words.
	extractor.candidate_weighting(window=2,
	                              pos=pos,
	                              top_percent=0.33)

	# 4. get the 10-highest scored candidates as keyphrases
	keyphrases = extractor.get_n_best(n=20)
	return keyphrases