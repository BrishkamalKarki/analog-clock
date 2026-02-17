from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QFont, QIcon
from PySide6.QtCore import QTimer, Qt
import math

from clock_styles import get_pens
from clock_engine import get_engine

class clock(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analog Clock")
        self.resize(600,600)
        self.setWindowIcon(QIcon("./images/clock.png"))
        self.engine=get_engine()
        self.pens=get_pens()
        # getting the initial angles for the initial second, minute and hour hand and getting todays day
        self.angles,self.current_day=self.engine.update_time_day()

        # object of the QTimer class
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.seconds)
        self.timer.start(1000)

    def seconds(self):
        # updating the angles for the initial second, minute and hour hand and getting todays day every seconds
        self.angles,self.current_day=self.engine.update_time_day()
        self.update()

    # called immediately and event holds the necessary info by default unless we specify i.e in which region to draw
    def paintEvent(self,event):
        with QPainter(self) as painter:
            # smoothens the quality
            painter.setRenderHint(QPainter.Antialiasing)
            painter.fillRect(self.rect(), Qt.black)
            painter.translate(self.width()/2,self.height()/2) # makes the center of the screen the origin 


            self.draw_face(painter)
            self.draw_hours(painter)
            self.draw_day(painter)
            self.draw_hands(painter)

    def draw_face(self,painter):
        hour_position=[n*5 for n in range(12)]
        painter.save() # this takes the snapshot of the current state i.e where is center, axes or can be refered also as a checkpoint
        for hour in range(60):
            painter.rotate(hour*6) # rotates the axis from x to y i.e clockwise by 6deg every loop
            if hour in hour_position:
                painter.setPen(self.pens['tick_hour']) # pen selection for the hour ticks
                painter.drawLine(0, 103, 0, 111)
            else:
                painter.setPen(self.pens['tick_normal'])
                painter.drawLine(0, 104, 0, 110)
            painter.restore() # after the rotaion we again make the axes to normal state from the saved checkpoint 
            painter.save()

    def draw_hours(self,painter):
        text_hour_list_in_ROMAN=["IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII","I", "II", "III"]
        index=0
        angle=30
        for rotator in range(1,13):
            painter.setPen(self.pens['text'])
            x_coor_txt=89*math.cos(angle*math.pi/180)
            y_coor_txt=89*math.sin(angle*math.pi/180)
            painter.translate(x_coor_txt,y_coor_txt)
            painter.setFont(QFont("Georgia",8))
            painter.drawText(-12, -5, 26, 10, Qt.AlignCenter, text_hour_list_in_ROMAN[index])
            painter.translate(-x_coor_txt, -y_coor_txt)
            painter.restore()
            painter.save()
            angle+=30
            index+=1
        
    def draw_day(self,painter):
        painter.setPen(self.pens['date_box'])
        painter.drawRoundedRect(30, -11, 40, 23, 3, 3)

        painter.setFont(QFont("Helvetica", 12, QFont.Bold))
        painter.setPen(self.pens['date_text'])
        painter.drawText(40, -6, 20, 13, Qt.AlignCenter, str(self.current_day))  


    def draw_hands(self,painter):
        self.sec_ang,self.min_ang,self.hour_ang=self.angles

        painter.rotate(-90)
        painter.setPen(self.pens['sec_hand'])
        painter.drawLine(0, 0, 83.2*math.cos(self.sec_ang), 83.2*math.sin(self.sec_ang))
        painter.setPen(self.pens['min_hand']) 
        painter.drawLine(0, 0, 67.6*math.cos(self.min_ang), 67.6*math.sin(self.min_ang)) 
        painter.setPen(self.pens['hour_hand'])
        painter.drawLine(0, 0, 52*math.cos(self.hour_ang), 52*math.sin(self.hour_ang)) 
        painter.restore()

        painter.setPen(self.pens['inner_center'])
        painter.drawEllipse(-3, -3, 6, 6)
        painter.setPen(self.pens['outer_center'])
        painter.drawEllipse(-1, -1, 2, 2)

if __name__=='__main__':
    app=QApplication([]) # this runs the application in the terminal
    window_clock=clock()
    window_clock.show() # shows the design and working of the object window_clock
    app.exec() # runs the applicaton for infinte loop untill user closes the program
