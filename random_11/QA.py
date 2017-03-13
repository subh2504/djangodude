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
        for ri in j["option"]:
            a = j["relatedinfo"]
            opt = opt + "\n" + ri["id"] + "  " + ri["option"]
            if (ri["option"].lower() in a.lower()):
                an = int(ri["id"])
        if(an==0):
            print(j["question"])
            print(opt)
            print(j["relatedinfo"])
            an = input()
        ans=an
    print(j["question"])
    print(str(ans))
    aws.append(ans)

print("******************************************************************")

print(*aws)
