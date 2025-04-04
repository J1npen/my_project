print("Enter your answers below. Type 'done' to finish.")

answers = []
while True:
  answer = input(f"{len(answers) + 1}. ")
  if answer.lower() == 'done':
    break
  answers.append(answer)

print("Your answers:\n")
for i, answer in enumerate(answers):
  print(f"{i + 1}. {answer}")

print("All answers in one line:", " ".join(answers))