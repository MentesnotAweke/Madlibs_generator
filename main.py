with open("story.txt", "r") as f:
    story = f.read()
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i  # changed from 1 to i to fix syntax logic

    if char == target_end and start_of_word != -1:
        word = story[start_of_word:i + 1]
        words.add(word)
        start_of_word = -1  # was just '-' before, now valid
       
answers = {}
for word in words:
    answer = input(f"Please enter a word for {word}: ")
    answers[word] = answer
print(answers)

for word in words:
    story = story.replace(word, answers[word])
print(story)