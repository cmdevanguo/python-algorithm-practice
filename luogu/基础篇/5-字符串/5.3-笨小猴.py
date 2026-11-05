word = input()

max_frequency = 0
min_frequency = len(word)

for letter in word:
    frequency = word.count(letter)

    if frequency > max_frequency:
        max_frequency = frequency

    if frequency < min_frequency:
        min_frequency = frequency

difference = max_frequency - min_frequency

is_prime = True

if difference < 2:
    is_prime = False
else:
    for number in range(2, difference):
        if difference % number == 0:
            is_prime = False
            break

if is_prime:
    print("Lucky Word")
    print(difference)
else:
    print("No Answer")
    print(0)