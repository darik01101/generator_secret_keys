from random import choice, randint
with open('secret_keys.txt', 'wt') as new_file:
    set_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 
    amount = int (input())
    for _ in range(amount):
        secret_key = ""
        for _ in range(randint(20,30)):
            random_char = choice(set_chars)
            secret_key += random_char
        print(secret_key, file = new_file)
