import json

json_data = json.loads(input())[0]
aws=[]
for j in json_data["question"]:
    ans = 1
    ans = j["campid"]

    for i in j["option"]:
        if i["campid"]=="1":
            opt=i["option"]
            break
    print(j["question"])
    print(str(ans))
    print(opt)
    aws.append(ans)

print("******************************************************************")

print(*aws)
