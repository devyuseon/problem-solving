open_bracket = ["(", "["]
close_bracket = [")", "]"]
bracket_match_dic = {"(": ")", "[": "]"}
bracket_value_dic = {")": 2, "]": 3}

brackets = " ".join(input()).split() # 괄호 문자열
stack = []
result = 0

# 첫번째 괄호 닫힌것이면 유효X
if brackets[0] not in open_bracket:
    print(0)
    exit()

for b in brackets:
    if b in open_bracket:
        stack.append(b)
    elif b in close_bracket:
        tmp = 0
        while stack:
            poped = stack.pop()
            if poped in open_bracket:
                if bracket_match_dic[poped] == b:
                    if tmp == 0:
                        stack.append(bracket_value_dic[b])
                    else:
                        stack.append(bracket_value_dic[b] * tmp)
                    break
                else:
                    print(0)
                    exit()
            else: # 숫자일 경우
                if tmp == 0:
                    tmp = poped
                else:
                    tmp += poped
                    
# for문 끝났는데 스택에 괄호 남아있으면 유효X
for i in stack:
    if i in open_bracket:
        print(0)
        exit()
    else:
        result += i

print(result)