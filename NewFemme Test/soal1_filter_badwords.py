try:
    import pandas as pd
except ImportError:
    print('[!] You need to install pip')

def load_bad_words():
    badwords_file = pd.read_csv("badwords.csv")
    return badwords_file.bad_word

print('===========================================================\n')
print('================ Filter Text From Bad Word ================\n')
user_input = input("Enter your sentence : ")

badwords = load_bad_words()
badwords = set(badwords)

for key in ['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']:
    sentence = user_input.replace(key, '')

jerk = False
for badword in badwords:
    if badword in sentence:
        print('===========================================================\n')

        print("============ Sorry the word is not allowed 😢 ============")
        print('===========================================================\n')

        jerk = True
        break
    else:
        continue

if (jerk == False):
    print('===========================================================\n')
    print("================== Thanks, to behave 😊 ==================")
    print('===========================================================\n')