words={"꽃":"flower","나비":"butterfly","학교":"school","자동차":"car","비행기":"airplane"}
print("<영어단어 맞추기 퀴즈>")
for a in words:
    input_word=input("'%s'에 해당되는 영어단어를 입력해주세요:"%a)
    if input_word==words[a]:
        print("정답입니다")
    else:
        print("틀렸습니다")