## list

#### 🔥 예제 5-6 

> 리스트 요소 수정

```python
flowers = ['a','b']
print(flowers)

flowers[1] = 'bbb'
print(flowers)
```

#### 🔥 예제5-8

>빈 리스트에 요소 추가
```python
scores=[]
while True:
    score=int(input("성적을 입력하세요(종료:-1):"))
    if score==-1:
        break
    else:
        scores.append(score)
print(scores)
```


#### 🔥 예제 5-9
> insert() 메소드로 요소 삽입하기
```py
fruits=["apple","orange","banana","cherry"]
print(fruits)
fruits.insert(1,"melon")
print(fruits)
fruits.insert(2,"strawberry")
print(fruits)
```

#### 🔥 예제 5-10
> index() 메소드로 요소의 인덱스 구하기
```py
number=[5,20,13,7,8,22,7,17]
print(number)
idx = number.index(7)
print(idx)
```

### 🔥 예제 5-11 
> remove() 메소드로 리스트의 요소 삭제
```py
member=["홍지웅",20,"경기도 김포시","jiwoong@naver.com","010-1234-5678"]
print(member)
member.remove(20)
print(member)
```

### 🔥 예제 5-12
> pop() 메소드로 리스트의 요소 삭제
data = [10,20,30,40,50,60,70,80]
print(data)
x=data.pop(2)
print(x)
print(data)


### 🔥 예제 5-13
> 리스트의 모든 요소 삭제
data=[3,12,7,-3,-9]
print(data)
data.clear()
print(data)


 ### 🔥 문제 c5-1
> 1~20의 양의 정수 리스트를 생성해라
data=list(range(1,21))
for i in range(0,len(data)):
    print("%d"%data[i],end=" ")


### 🔥 문제 c5-2
> c5-1에서 짝수번째 요소를 출력하라
data=list(range(1,21))
for i in range(0,len(data)):
  if(1+i)%2==0:
    print("%d"%data[i],end=" ")
