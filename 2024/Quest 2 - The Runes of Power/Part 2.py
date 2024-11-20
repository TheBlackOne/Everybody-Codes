input = """WORDS:THE,OWE,MES,ROD,HER,QAQ

AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
THE FLAME SHIELDED THE HEART OF THE KINGS
POWE PO WER P OWE R
THERE IS THE END
QAQAQ"""

words, phrase = input.split('\n\n')
_, words = words.split(':')

word_count = 0

for line in phrase.split('\n'):
    tracking_string = "".zfill(len(line))
    tracking_list = list(tracking_string)

    for word in words.split(','):
        for symbol in [word, word[::-1]]:
            for i in [i for i in range(len(line)) if line.startswith(symbol, i)]:
                for n in range(i, i + len(symbol)):                
                    tracking_list[n] = '1'

    tracking_string = ''.join(tracking_list)
    word_count += tracking_string.count('1')

print(word_count)