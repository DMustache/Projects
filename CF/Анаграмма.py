lenght, requests = map(int, input().split())
mainword = input()
answerlist = []
#sdlpoadkaowdjioadjii
for i in range(requests):
    checker = input()
    if sorted(mainword) == sorted(checker):
        answerlist.append("YES")
    else:
        answerlist.append("NO")
for i in answerlist:
    print(i)