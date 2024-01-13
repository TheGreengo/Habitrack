from django.contrib import admin

from .models import NumHabit, NumEntry, BinEntry, BinHabit

admin.site.register(NumEntry)
admin.site.register(NumHabit)
admin.site.register(BinEntry)
admin.site.register(BinHabit)