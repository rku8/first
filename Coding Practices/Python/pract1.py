
string = "My lucky number is %d, what is yours?" % 7
print(string)

s = 'Hello, Hi how are you Vivek. I came to you because I have heard that Vivek was a good person.'
s = s.replace('Vivek', 'Ravi') # Replace all 
print(s)

s = 'Today, I ate mango, and mango very sweet.'
s = s.replace('mango', 'papaya', 1) # Replace one
print(s)

print(s.find('ate')) # Index of first character of text 

if 'I' in s:
    print(True)

