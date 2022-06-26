#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test_processing.py

# University of Zurich
# Department of Computational Linguistics

# Authors: # Cui Ding(olatname: cding)
# Matriculation Numbers: # 21-718-945
# 			Mia Tatjana Egli (olatname: miaegl)
# Matriculation Numbers: 21-700-406


# Test Units for dad_jokes Analyzer Engine
# Module for functional and non functional testing of dad_jokes_processor module

# Import Statements
from unittest import TestCase, main
import processing
from os import path


class LpTest(TestCase):
    """
    dad_jokes_processor non functional tests
    """

    def test_output_split_into_sentences_function(self):
        dad_jokes = "Want to hear a construction joke?\nI'm working on it."
        result = processing.split_into_sentences(dad_jokes)
        self.assertIsInstance(result, list, "Required type of output is list")
        self.assertEqual(len(result), 3)
        self.assertIn('?', result[0])


    def test_output_tokenize_function(self):
        split_dad_jokes = ["Want to hear a construction joke?", "\n", "I'm working on it."]
        result = processing.tokenize(split_dad_jokes)
        target = [["Want", "to", "hear", "a", "construction", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]]
        self.assertEqual(result, target)
        self.assertIsInstance(result[0], list)
        self.assertEqual(len(result[2]),5)


    def test_output_filter_profanity_function(self):
        tokenized_dad_jokes = [["Want", "to", "fuck", "a", "construction", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]]
        result = processing.filter_profanity(tokenized_dad_jokes, "profanities.txt")
        target = ([["Want", "to", "####", "a", "construction", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]], 1)
        self.assertEqual(result, target)
        self.assertEqual(result[1], 1)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result[0][0][2]), len(tokenized_dad_jokes[0][2]))
        
        tokenized_dad_jokes_2 = [['You', 'peed', 'all', 'over', 'the', 'crap', 'office', 'floor', '.'], ['\n'], ['Urine', 'pissing', 'serious', 'trouble', 'now', '.']]
        result_2 = processing.filter_profanity(tokenized_dad_jokes_2, "profanities.txt")
        target_2 = ([['You', 'peed', 'all', 'over', 'the', '####', 'office', 'floor', '.'], ['\n'], ['Urine', '#######', 'serious', 'trouble', 'now', '.']], 2)
        self.assertEqual(result_2, target_2)
        self.assertEqual(result_2[0][2][1], "#######")
        

if __name__ == '__main__':
    main()
