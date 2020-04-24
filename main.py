'''
Funny Friendship calculator: using a simple and funny ranking algorithm
'''

# alphabet without vowel
alphabet_without_vowels = 'bcdghjklmnpqrstvwxyz'

# friendship score
friendship_score = 0

# enter two names with space in btn eg john smith
two_names = input('Enter first name, space and then second name:- ')

# iterate over the char in names and check conditions
for character in two_names:
    if character in 'aeiou':
        friendship_score += 5
    if character in 'friends':
        friendship_score += 10
    if character in alphabet_without_vowels:
        friendship_score += alphabet_without_vowels.find(character)
    else:
        friendship_score += 0

# Grade the score 
if friendship_score > 100:
    print("your frinedship score is: ", friendship_score)
    print("Congratulations! you both are best friends")
else:
    print("Your friendship score is: ", friendship_score)
