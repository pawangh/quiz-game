import pgzrun

WIDTH=800
HEIGHT=600
TITLE="quiz"

marqueebox=Rect(0,0,800,70)
question_box=Rect(20,80,600,180)
answer_box1=Rect(20,280,230,90)
answer_box2=Rect(330,280,230,90)
answer_box3=Rect(20,380,230,90)
answer_box4=Rect(330,380,230,90)
skip=Rect(650,280,100,300)
timer=Rect(650,100,100,100)

allquestions=[]
totalquestions=11
question=[]
questionnumber=0
score=0
gameover=False


def draw():
    screen.fill("black")
    screen.draw.filled_rect(marqueebox,"black")
    screen.draw.filled_rect(question_box,"blue")
    screen.draw.filled_rect(answer_box1,"yellow")
    screen.draw.filled_rect(answer_box2,"yellow")
    screen.draw.filled_rect(answer_box3,"yellow")
    screen.draw.filled_rect(answer_box4,"yellow")
    screen.draw.filled_rect(skip,"yellow")
    screen.draw.filled_rect(timer,"yellow")

    screen.draw.textbox("welcome to the quiz",marqueebox,color="white")
    screen.draw.textbox(question[0],question_box,color="white")
    screen.draw.textbox(question[1],answer_box1,color="white")
    screen.draw.textbox(question[2],answer_box2,color="white")
    screen.draw.textbox(question[3],answer_box3,color="white")
    screen.draw.textbox(question[4],answer_box4,color="white")
    screen.draw.textbox("skip",skip,color="white")
    screen.draw.textbox("0",timer,color="white")
def read_question_file():
    global allquestions,totalquestions
    file=open("questions.txt","r")
    allquestions=file.readlines()
    totalquestions=len(allquestions)
    file.close()
read_question_file()
def readnextque():
    global question
    question=allquestions[questionnumber].split(",")
readnextque()
def update():
    marqueebox.x=marqueebox.x-5
    if marqueebox.x<-800:
        marqueebox.x=800
def on_mouse_down(pos):
    optionno=1
    if answer_box1.collidepoint(pos):
        if optionno==question[5]:
            pass



pgzrun.go()