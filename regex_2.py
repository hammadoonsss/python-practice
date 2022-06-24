import re

start_regex = "^[aeiouAEIOU][a-zA-Z0-9_]*"

def check(string):
    
    value = re.search(start_regex, string)
    
    if value:
        print("Word start with Vowel:", string)
    
    else:
        print("Not Start with vowel!!")
        
if __name__ == "__main__":
    
    string="ankit"
    check(string)
    
    string="geeks"
    check(string)
    
    string="Orange"
    check(string)
    
    string="Dog"
    check(string)
    
    string="Unique"
    check(string)
    
    string="e_at"
    check(string)
    