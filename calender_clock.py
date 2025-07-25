class Clock:
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    def tick(self):
        self.second +=1
        if self.minutes >= 60:
            self.seconds=0
            self.hours += 1
            
        if self.minuets >= 60:
            self.minutes =0
            self.hours +=1
            
        if self.hours >=24:
            self.hours=0
    def __str__(self):
        return f'{self.hours:2}:{self.minutes:2}:{self.seconds:2}'
    class Calendar:
        def __init__(self,day=1,month=1,year=2025):
            self.day=day
            self.month=month
            self.year=year

        def  leap_day(self):
            return(self.year % 4 == 0 and self.year %100 != 0 ) or (self.year % 400 == 0) 
        def 
            