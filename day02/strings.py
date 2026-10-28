print("----------------Indexing-----------------")
name = 'Python'

print(len(name))            # 6

print(name[0])              # P

print(name[len(name) - 1])  # n

print(name[-1])             # n

print(name[-2])             # o

print("----------------Slicing String-----------------")
# Slicing returns new String
s = 'Java Programming Language'

s2 = s[5:16]
print(s2)

# Beginning and ending indexes are optional
s3 = s[:4]
print(s3)

# Slice and reverse using (extra :)
s4 = s[::-1]
print(s4)

s5 = 'Python Programming'

s6 = s5[7:]

print(s6)

# Reverse constructor
#s5 = reversed(s)

print(type(s5)) #reversed

# s5 = str(reversed(s))

# print(s5)


s7 = 'CYDEO SCHOOL'
#str(reversed(s7))

print('-------------------- Str methods ----------------------')
# print(help(str))

print(':Capitalized:')
# First char only
s = 'pytho programming language'
s = s.capitalize()
print(s)

# Cap first char in every word
s = s.title()
print(s)
print(':Strip:')
# Strip = java.trim
s = "           Python        "
# s = s.rstrip()
# s = s.lstrip()
s = s.strip()
print(s)

print(':Index number:')
s = 'JAVA ABA'
print(s.index('A'))

print(s.rindex('A'))

print(':Replace:')
s ='Java Java'
# s = s.replace('Java','Python') # replace all
print(s)
s = s.replace('Java','Python',1) # replace based on count
print(s)

s = 'C# C# Python'
s = s.replace(' C#',' Java')
print(s)

print(':Count:')
s = 'Java Java JAVA Java java Python Python'
count_java = s.lower().count('java')
count_python = s.count('Python')
print(count_java)
print(count_python)

print(':Comparing:')
s1 = 'java'
s2 = 'JAVA'

print(s1 == s2)
print(s1.lower() == s2.lower())
# to ignore case sensitivity

# verify first char is upper or lower
s = 'Java'
print(s[0].islower())
print(s[0].isupper())

#verify type
s = 'a'
print(s.isalpha())
s = '1'
print(s.isdigit())

s = 'Cydeo School'
print(s.istitle())


