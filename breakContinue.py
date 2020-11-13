# Break Statement
#The break statement ends the current loop and jumps to the statement immediately following the loop. It is like a loop test that can happpen anywhere in the body of the loop

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

#Continue
#The continue statement ends the current iteration and jumps to the top ooof the loop and starts the next iteration.

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
