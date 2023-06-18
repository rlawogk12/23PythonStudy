questions=["s_hool","compu_er","deco_ation","windo_","hi_tory"]
answers=["c","t","r","w","s"]
for i in range(1,6):
    q="%s:밑 줄에 들어갈 알파벳은?"%questions[i-1]
    guess=input(q)
    if guess==answers[i-1]:
        print("정답!")
    else:
        print("틀렸어요!")