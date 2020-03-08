#!/bin/python3
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import datetime, pytz

class JalaliFormat :
    def __init__(self,ti,jformat) :
        self.ti = ti
        self.jformat = jformat
    #convert to jalali 

    def jconvert (self):

        worldtime = self.ti
        w = str(worldtime).split()
        #date
        date = w[0].split('-')
        #time
        time = w[1].split(':')
        convert = JalaliDateTime.to_jalali(datetime.datetime(
                int(date[0]),
                int(date[1]),
                int(date[2]),
                int(time[0]),
                int(time[1]),
                int(time[2]))
        ).strftime(self.jformat)

        return convert 

    #convert to %Y%m%d%H%M%S for Rit by priority
    def jsort (self):

        worldtime = self.ti
        w = str(worldtime).split()
        #date
        date = w[0].split('-')
        #time
        time = w[1].split(':')
        jsoort = JalaliDateTime.to_jalali(datetime.datetime(
                int(date[0]),
                int(date[1]),
                int(date[2]),
                int(time[0]),
                int(time[1]),
                int(time[2]))
        ).strftime("%Y%m%d%H%M%S")

        return jsoort
        
