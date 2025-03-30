# range 8-14, upper, lower, digits, special chars, whitespaces
import secrets, string, random
pw=[]
len=random.randint(8, 14)
options=[string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits, " "]
for _ in range(len):
    pw.append(secrets.choice(secrets.choice(options)))
res="".join(pw)
print("Random Password Generator")
print(f"Random Password: {res}")    