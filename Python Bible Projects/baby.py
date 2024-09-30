from random import choice
questions = ["Why do we have hands?", "Why is the sky blue", "Why can't I fly?"]

question =choice(questions)
answer = input(question+": ").strip().lower()
while answer != "just because":
    answer = input("why?: ".strip().lower())
print("Oh... ok")