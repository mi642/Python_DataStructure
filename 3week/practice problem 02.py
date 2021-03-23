print("원문")

str = "나 보기가 역겨워 가실 때에는 말없이 고이 보내 드리오리다\n영변에 약산 진달래꽃 아름 따다 가실 길에 뿌리오리다\n가시는 걸음 걸음 놓인 그 꽃을 사뿐히 즈려 밟고 가시옵소서\n나 보기가 역겨워 가실 때에는 죽어도 아니 눈물 흘리오리다"
print(str, "\n")

set_str = set(str)
set_str.remove(' ')
set_str.remove('\n')
list_str = list(set_str)

print("--------------------\n문자 빈도수(4회 이상)")
print("--------------------")

for i in range(0, len(list_str)):
    count = str.count(list_str[i])
    if count >= 4:
        print(list_str[i], "-->", count)