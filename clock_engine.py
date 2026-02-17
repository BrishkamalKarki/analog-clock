from datetime import datetime
import nepali_datetime, time, math


class get_engine():

    def update_time_day(self):

        self.current_sec=datetime.now().second
        if self.current_sec==0:
            self.current_sec=60

        self.current_min=datetime.now().minute
        if self.current_min==0:
            self.current_min=60
        self.current_min_in_sec=self.current_min*60+self.current_sec

        self.current_hrs=datetime.now().hour % 12
        self.current_hrs_in_sec=self.current_hrs*60*60+self.current_min_in_sec

        
        self.current_day=nepali_datetime.date.today().day
        if self.current_day in [day for day in range(10)]:
            self.current_day=f"0{self.current_day}"

        return self.angle(), self.current_day

    def angle(self):

        self.sec_ang=self.current_sec*6*math.pi/180
        self.min_ang=self.current_min_in_sec*0.1*math.pi/180
        self.hour_ang=self.current_hrs_in_sec*math.pi/(120*180)

        return self.sec_ang, self.min_ang, self.hour_ang


time=get_engine()
time.update_time_day()