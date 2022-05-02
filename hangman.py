import random

def lifefunc(life):
    if life == 1:
        print('   ( - )\n')
    elif life ==2:
        print('   ( - )\n'
            '     |   \n'
            ' ----|      \n'
            '/    |        \n'
            '     |       \n'
            '     |        \n')
    elif life == 3:
        print('   ( - )\n'
            '     |   \n'
            ' ----|----   \n'
            '/    |     \ \n'
            '     |       \n'
            '     |        \n')
    elif life ==4:
        print('   ( - )\n'
              '     |   \n'
            ' ----|----   \n'
            '/    |     \ \n'
            '     |       \n'
            '     |        \n'
            '    /         \n'
            '   /           \n'
            '  /             ')
    elif life ==5:
        print('   ( - )\n'
              '     |   \n'
            ' ----|----   \n'
            '/    |     \ \n'
            '     |       \n'
            '     |        \n'
            '    / \        \n'
            '   /   \        \n'
            '  /     \        ')



with open ("words.txt", "r") as file:
    data = file.read()
    words = data.split()
    #Generate a random word from the text
    word_pos = random.randint(0, len(words)-1)
    randomWord = words[word_pos]
    while True:
        if len(randomWord)< 5:
            word_pos = random.randint(0, len(words)-1)
            randomWord = words[word_pos]
        else:
            break

print(randomWord)
life = 0
bword = randomWord
b= list(bword)
a= list(randomWord)

sample_output = random.sample(a,int(len(a)/2))
for x in range(0, len(a)-1):
    if a[x] in sample_output:
        a[x]= ' _ '
print(''.join(a))

while life< 5:
    if ' _ ' in a:
        x = input("Enter any letter of the word: ")
        if x in sample_output:
            for i in range(len(b)-1):
                if b[i]==x:
                    a[i]=x
        else:
            life+=1
            lifefunc(life)
        print(''.join(a))
    else:
        print(f"The answer is : {randomWord}")
        break

if life ==5:
    print(f"The answer is : {randomWord}")