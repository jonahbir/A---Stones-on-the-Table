n=int(input())
colors=input()
Remove=0
for index in range(n-1):
    if colors[index]==colors[index+1]:
        Remove+=1
print(Remove)


