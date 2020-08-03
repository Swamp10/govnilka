import markovify

with open('text.txt') as f:
    text = f.read()

text_model = markovify.Text(text)

first, second = input().split()[:2]

for i in range(5):
    print(text_model.make_sentence(init_state=(first, second)))
