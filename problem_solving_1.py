# write a function count_vowels(text), that counts and returns the number of vowels in the given string, ignore case sensitivity

def count_vowels(text):
    vowels = "aEiOu"

    vowel_counts = 0 
    for char in text.lower():
        if char in vowels.lower(): 
            vowel_counts += 1
    return vowel_counts
    

print(count_vowels("shUborna"))