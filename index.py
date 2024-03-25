from random import choice, randint
set_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ1234567890" 
amount = int (input())
for _ in range(amount):
    secret_key = ""
    for _ in range(randint(20,30)):
        random_char = choice(set_chars)
        secret_key += random_char
    print(secret_key)
