#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# processing.py

# University of Zurich
# Department of Computational Linguistics

# Authors: Cui Ding(olatname: cding)
# Matriculation Numbers: 21-718-945
# 			Mia Tatjana Egli (olatname: miaegl)
# Matriculation Numbers: 21-700-406


from argparse import ArgumentParser, FileType
from typing import List, Tuple

import re


def split_into_sentences(post_str: str) -> List[str]:
	"""
	Split a line into a list of sentences.
	Non-standard characters, like emojis, removed.
	Original format kept. 
	The line split at the punctuations or \n.
	where the punctuations followed by A-Z,0-9,(.
	
	:param post_str: the line to be split.
	"""
	sent = ""
	str_list =[]
	
	# for a string, go through the characters one by one.
	# we set the upper threshold as 8300 to exclude non-standard char
	# but to include the … and the “ in “banana” and so on.
	 
	clean_str = "".join([char for char in post_str if ord(char)< 8300])
	
##solution_1

	# simpler. But solution_2 is more generalizable.
	# Idea: catch the sentence pattern and split from sentence.
	# 		sentences are contained in the resulting list.
	
	str_list = re.split(r'(\n|[A-Z][^.?!"\)…]+. "$|["\(]?[A-Z][^.?!"\)…]+[.?!"\)…]+ )', clean_str)
	str_list = [sent for sent in str_list if sent]

##solution_2

	# Idea: split from punctuations and keep them in the results.
	#		look at the next element in the list: 
	#			starts with A-Z, 0-9, ( -> current element joins the current sentence.
	#									-> next element build new sentence.
	#		include the very last element in by comparing "i+1" and the len of the list 
	   
# 	sentpunct_list = re.split(r'([.\)?!"~;]+ |\n)', clean_str)

# 	for i in range(len(sentpunct_list)-1):
# 		sent += sentpunct_list[i]
# 		if re.match(r"[A-Z0-9(]|\n", sentpunct_list[i+1]):
# 			str_list.append(sent)
# 			sent = ""
# 		if i+1 == len(sentpunct_list)-1:
# 			sent += sentpunct_list[i+1]
# 			str_list.append(sent)
	
	return str_list
	

def tokenize(sentences_str: List) -> List[List[str]]:
	"""
	Take a list of sentences.
	Split sentence into tokens.
	
	:param sentence_str: the list of strings to be tokenized.
	:return: a list of lists containing tokens.
	"""
	token_sents_list = []

	for sents in sentences_str:
		# for tokenize punctuation.
		sents = re.sub(r'([!"#$%&*+,()./:;<=>?@[\]^_`{|}~])', r' \1 ', sents)
		token_in_sents = [token for token in sents.split(' ') if token]
		token_sents_list.append(token_in_sents)
	
	return token_sents_list
	

def filter_profanity(tokenized: List[List[str]], filename: str) -> Tuple[List[List[str]], int]:
	"""
	Given the tokens of the sentences of each post,
	censor the profanities which were listed in a given file.
	
	:param tokenized: list of tokenized sentences.
	:param filename: a file containing profanities. 
	:return: a tuple of a list and an integer, where the elements mean:
			1. A list of tokenized sentences in the form of lists of tokens,
				profanity is replaced by hashtags of the same length.
			2. counts of profanities per post.
	"""
	counter = 0
	filtered_sents_list = []
	
	# get profanities set.
	with open(filename, "r", encoding="utf-8") as infile:
		profanity_set = {line.strip() for line in infile }
	
	for sents in tokenized:
##solution_1
	# shorter but less efficient.	
# 		for profanity_word in profanity_set:
# 			counter += len(["#"*len(token) for token in sents if token.lower().startswith(profanity_word)])
# 			sents = ["#"*len(token) if token.lower().startswith(profanity_word) else token for token in sents]
# 		filtered_sents_list.append(sents)
		
##solution_2	
	# more efficient.		
		filtered_sents = []
		for token in sents:
			for profanity_word in profanity_set:
				if token.lower().startswith(profanity_word):
					counter += 1
					token = "#"*len(token)
			filtered_sents.append(token)			
		filtered_sents_list.append(filtered_sents)

	return filtered_sents_list, counter
				
	
def pretty_print(processed: List[List[str]], counts, i) -> None:
	"""
	Print a list of lists of tokens. 
	Each big list is a post, each inner list is a sentence.
	print to the command line.
	return None.
	
	:param processed: content to be printed.
	:param counts: number of profanities.
	:param i: count the order of a post.
	"""
	if counts in [0, 1]:
		print(f"This is post NO.{i}, with {counts} profanity:")
	else:
		print(f"This is post NO.{i}, with {counts} profanities:")
	# join words into sentences.
	sents = [" ".join(sents) for sents in processed]
	for sentence in sents:
		# for print, ignore the "\n".
		if sentence:
			# make the punctuations stick the the words.
			sentence = re.sub(r'" (.+) "', r'"\1"', sentence)
			sentence = re.sub(r'^([\("]) | (")$| ([!$%&*+,()-./:;<=>?@[\]^_`{|}~]+)', r'\1\2\3', sentence)
			print(f"  {sentence}")
	
	return None
	
	
def main():
	# Parse argument, for the extended use of other txt files to be filtered.
	parser = ArgumentParser(description ="Filter a txt file.")
	parser.add_argument("--file", "-f", default = "dadjokes_samples.txt", type = FileType('r', encoding="utf-8"), help="The file to be filtered.")
	args = parser.parse_args()
	
	# for counting the post. 
	i = 0
	
	for line in args.file:
		i += 1
		origin_str_list = split_into_sentences(line)
# 		print(origin_str_list)
		tokens_list = tokenize(origin_str_list)
#		print(tokens_list)
		filtered_str_list, counts = filter_profanity(tokens_list, "profanities.txt")
#		print(f"{filtered_str_list} --> {counts}")
		pretty_print(filtered_str_list, counts, i)
	

if __name__ == '__main__':
	main()
