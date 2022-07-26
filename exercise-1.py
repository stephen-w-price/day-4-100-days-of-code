import random

heads_or_tails = random.random() * 10
print(heads_or_tails)
if heads_or_tails > 5:
    heads_or_tails = 'heads'
else:
    heads_or_tails= 'tails'

print(heads_or_tails)