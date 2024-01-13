from django.db import models

# So, for the database side of things, I think that we'll have a bunch of 
# habits, and then entries which correspond to them. When on the calendar page, 
# we'll simply get a list of all of the different entries, and populate a list
# of all of the calendar days, and we'll initially populate them with a blank
# value, and then update all of them if they actually have been entered in. So,
# in essence, our backend will actually be a backend, and not just a query 
# logger haha.


class BinHabit(models.Model):
    name = models.CharField(max_length=5)
    goal = models.FloatField()
    start = models.DateField()
    stop = models.DateField()

    def __str__(self):
        return self.name

class BinEntry(models.Model):
    habit = models.ForeignKey(BinHabit, on_delete=models.CASCADE)
    res = models.BooleanField()
    date = models.DateField()
    
    def __str__(self):
        return str(self.habit) + " entry for " + str(self.date)

class NumHabit(models.Model):
    name = models.CharField(max_length=5)
    goal = models.FloatField()
    start = models.DateField()
    stop = models.DateField()

    def __str__(self):
        return self.name

class NumEntry(models.Model):
    habit = models.ForeignKey(NumHabit, on_delete=models.CASCADE)
    res = models.FloatField()
    date = models.DateField()

    
    def __str__(self):
        return str(self.habit) + " entry for " + str(self.date)