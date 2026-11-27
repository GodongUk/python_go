import json

class1 = {"국어", "수학", "영어"}
class2 = {"체육", "영어", "과학"}
print("class1 에만 있는 과목")
print(sorted(class1 & class2))
print("전체 class에 있는 과목")
print(sorted(class1 | class2))

dict = {"name":"민수", "subjects":"영어"}
text = json.dumps(dict, ensure_ascii=False)
print(json.loads(text)["name"],json.loads(text)["subjects"])
