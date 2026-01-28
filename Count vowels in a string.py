word=input("enter a word")
vowels=["a","e","i","o","u"]
count=0
for char in word.lower():
    if char in vowels:
        count=count+1
print(count)
