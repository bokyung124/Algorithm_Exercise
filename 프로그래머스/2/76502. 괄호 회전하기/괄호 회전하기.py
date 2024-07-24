def solution(s):
    answer = 0
    n = len(s)
    st = []
    opens = ["(", "{", "["]
    closes = ")}]"
    
    for i in range(n):
        flag = False
        st = []
        for idx, j in enumerate(s):
            find_i = closes.find(j)
            if j in opens:
                st.append(j)
            elif st and st[-1] == opens[find_i]:
                st.pop()
            elif not st:
                flag = True
                break
        s = s[1:] + s[0]
        if flag or st:
            continue
        else:
            answer += 1
        
    return answer