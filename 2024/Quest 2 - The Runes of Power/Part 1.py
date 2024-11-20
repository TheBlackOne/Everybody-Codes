input = """WORDS:THE,OWE,MES,ROD,HER

AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE"""

words, phrase = input.split('\n\n')
_, words = words.split(':')

word_count = 0

for word in words.split(','):
    word_count += phrase.count(word)

print(word_count)