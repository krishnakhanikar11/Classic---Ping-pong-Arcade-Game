from turtle import Turtle

class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.A_score = 0
        self.B_score = 0
        self.increaseA()

    def increaseA(self):
        self.write(self.A_score, align='center' , font=("Courier" , 80, 'normal'))


    def increaseB(self):
        self.write(self.B_score, align='center', font=("Courier", 80, 'normal'))

    def update_A(self):
        self.A_score += 1
        self.clear()
        self.increaseA()

    def update_B(self):
        self.B_score += 1
        self.clear()
        self.increaseB()




