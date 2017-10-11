#planning out a class
#for python notation single line # multiple line """

class Time(object):
   """Instances represent times of day
   instance attributes:
      hour: hour of day [lin in  0..23]
      min: minutes of hour [int in 0..59]"""
   def __init__(self, hour, min):
   	"""The time hour:minute.
   	pre: hour in 0..23; min in 0..59"""


   def increment(self, hours, mins):
    	"""Move this time <hours> hours
    	and <mins> minutes into future.
    	pre: hours is int >= 0; mins in 0..59"""



   def isPM(self):
   	"""returns: this time is noon or later"""
   	
