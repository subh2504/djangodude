import json

json_data = json.loads(input())[0]
aws=[]
for j in json_data["question"]:
    ans = 1
    if int(j["answer"]) > 1:
        ans = ""
    else:
        ans = j["answer"]

    print()
    # print("++++++++++++++++++++++++++++++++++++++++\n")
    # print(q)
    # AliveQuestions.objects.get_or_create(qid=j["questionid"],ans=j["answer"])
    if (int(j["answer"]) > 1):
        an = 0
        opt = ""
        if (j["question"].lower() == j["relatedinfo"].lower() or j["relatedinfo"] == "True"):
            ans=1
        else:
            ans=0
    print(j["question"])
    print(j["relatedinfo"])
    print(str(ans))
    aws.append(ans)

print("******************************************************************")

print(*aws)
