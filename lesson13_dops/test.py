answer = "собака"
guess_answer = "******"
input_letter = "а"
for i in range(len(answer)):
    if input_letter == answer[i]:
        guess_answer = guess_answer[:i] + input_letter + guess_answer[i + 1 :]

print(guess_answer)
