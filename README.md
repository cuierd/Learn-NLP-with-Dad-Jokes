
# Exercise 1
Hand in until **March 8th 2022 at 23:59**.

## Introduction

In this first exercise, you will implement the module ```processing.py``` to process natural language data, namely dad jokes. The processing involves sentence splitting, tokenizing, filtering profanity and printing out readable output. To work on it, write your code using Test Driven Development (TDD) as you've seen in the lectures.

Please use modules from Python’s standard library only, unless it is stated otherwise in the exercise description.

### Unit Tests
To make sure your code catches corner cases, too, writing unit tests is common practise. For tasks 1 to 3 you need to write own test assertions into the existing file ```test_processing.py```. Think of cases that need testing instead of just adding random tests. For inspiration, have a look at the tests we provided you with.


### GitLab

To submit your code, use GitLab. Make sure your account is set up and ready to work with. Have a look at the instructions on ```OLAT > Material > Tutorial > instructions.pdf``` if you're unsure how to submit your work.


### To Submit
* ```processing.py``` with all your implemented functions
* ```test_processing.py``` with your own assertions added
* ```task_5.txt``` with your answers to task 5 and your feedback

It is **mandatory** to work in pairs. If you have no partner, please contact us so we can set you up with someone. Before submitting, make sure all your code runs and your repository contains all the files you need to hand in.


## Task 1
In this first task, you split the jokes into its sentences, how it is often done in NLP. Implement the function ```split_into_sentences(str) -> List[str]```, which takes a string and returns a list of sentences of type string. Think about how you can split sentences as accurately as possible. Note that since the dataset are posts from the internet, formatting and content is not consistent. Can you find ways, to make your function as generally applicable as possible? For example, remove any non-standard characters, like emojis, and keep the formatting like it is in the original post. Linebreaks (\n) count as a separate sentence.

### Example
```
split_into_sentences('Want to hear a construction joke?\nI'm working on it.🏗') -> ['Want to hear a construction joke?', '\n', 'I'm working on it.']
```

### Outcome
* Implemented function ```split_into_sentences(post_str: str) -> List[str]```
* 2 own test assertions


## Task 2
To work with text in NLP, it is very common to tokenize it first things first. Implement the function ```tokenize(sentences_str: List) -> List[List[str]]```. It takes the list of the split sentences and returns a list of lists containing all its tokens. Find the best way to tokenize the sentences.

### Example
```
tokenize(['Want to hear a construction joke?', '\n', 'I'm working on it.']) -> [['Want', 'to', 'hear', 'a', 'construction', 'joke', '?'], ['\n'], ['I'm', 'working', 'on', 'it', '.']]
```

### Outcome
* Implemented function ```tokenize(sentences_str: List) -> List[List[str]]```
* 2 own test assertions


## Task 3
Since you're working with dad jokes, chances are high that those jokes will be seen by kids. Implement a profanity filter that censors all profanities. The function ```filter_profanity(tokenized: List[List[str]], filename: str) -> Tuple[List[List[str]], int]``` takes the tokenized sentences as input. The output is a tuple containing a list of lists of tokens and censored profanities and an integer representing the profanity-count. Censor the words, which can be found in the file ```profanities.txt```, using a placeholder of the profanity's length consisting of hashtags (#). Additionally, count the profanities per post. Note that the file ```profanities.txt``` contains mostly words in their lemma form. Make sure to catch words like 'pissing' or 'fucks', too.

### Example
```
filter_profanity([['Why', 'are', 'men', 'so', 'calm', 'and', 'relaxed', 'after', 'making', 'love', '?'], ['They', 'just', 'ran', 'out', 'of', 'fucks', 'to', 'give', '.']]) ->([['Why', 'are', 'men', 'so', 'calm', 'and', 'relaxed', 'after', 'making', 'love', '?'], ['They', 'just', 'ran', 'out', 'of', '#####', 'to', 'give', '.']], 1)
```

### Outcome
* Implemented function ```filter_profanity(tokenized: List[List[str]], filename: str) -> Tuple[List[List[str]], int]```
* 2 own test assertions


## Task 4
Implement the function ```pretty_print(processed: List[List[str]]) -> None``` which returns the jokes in a readable way. Think of a format that makes most sense to you. You don't need to write any test assertions for this function.


### Outcome
* Implemented function ```pretty_print(processed: List[List[str]]) -> None``` 


## Task 5
a) List three advantages or disadvantages of Test Driven Development. In addition, describe an example where TDD has affected the way you have implemented a function.

b) What did you test in your unit tests? Please list at least three different test criteria.

c) Please give us a short feedback about the exercise. How long did it take you to solve the tasks? Where did you have difficulties? What was easy to handle? Did you gain any new knowledge by solving the exercise?

### Outcome
* Your answers to a-c written in a separate textfile named ```task_5.txt```.

## Data Sources
```dadjokes_samples.txt```: https://www.kaggle.com/oktayozturk010/reddit-dad-jokes

```profanities.txt```: https://www.freewebheaders.com/full-list-of-bad-words-banned-by-google/
