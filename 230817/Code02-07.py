import turtle
import random

## 함수 선언 부분 ##
# 들여쓰기
def  screenLeftClick(x, y):
    # 거북이 색상
    # turtle.color('red')

    # global 전역, static과 비슷
    global r, g, b
    # turtle 인스턴스 초기화는 아래에서 진행 했을 것임
    # pencolor = 매개변수 rgb 값을 받아서, 선색
    r = random.random()
    g = random.random()
    b = random.random()
    
    turtle.pencolor((r, g, b))
    # pendown = 선을 그리겠다 의미
    turtle.pendown()

    # 크기 변경하기
    tSize = random.randrange(1, 10)
    # shapesize = 모양 크기
    turtle.shapesize(tSize)

    # 거북이 모양 도장찍기
    turtle.stamp()

    # 거북이 색상 랜덤
    turtle.color(r, g, b)

    # goto = 매개변수 좌표값으로 이동
    turtle.goto(x, y)

    # 거북이 회전, left, right
    turtle.left(random.randrange(1, 360))

# 우클릭시 기능
def  screenRightClick(x, y):
    # penup = 선을 안그리고
    turtle.penup()
    # 해당 좌표로 이동 x,y
    turtle.goto(x, y)

# 휠 클릭시
def  screenMidClick(x, y):
    # 전역으로 설정된 rgb 색깔 선언부분
    global r, g, b
    # 1~9 까지 랜덤한 정수 선택
    tSize = random.randrange(1, 10)
    # shapesize = 모양 크기
    turtle.shapesize(tSize)
    # 색상 랜덤을 이용해서 할당. rgb 0~255 사이의 값을 할당
    r = random.random()
    g = random.random()
    b = random.random()
    print(f"랜덤한 색상의 값 조회: 0~255, r : {r}, g : {g}, b : {b}")

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

# 이벤트 핸들러 역할 onscreenclick
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
