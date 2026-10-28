print(':break:')
for i in range(1, 6):
    print(i)
    if i == 3:
        break # Exists loop

print(':continue:')
for i in range(1, 6):
    if i == 3 or i == 4:
        continue # Skips loop
    print(i)

print(':pass:')
for i in range(1, 6):
    if i == 3 or i == 4:
        pass # placeholder [abstraction] can only be used in body
    print(i)

# pass can be used in the following
def function():
    pass

if True:
    pass

class Class:
    def method(self):
        pass
    pass