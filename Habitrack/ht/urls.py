from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
    path("calendar/<int:cal_id>/", views.calendar, name="calendar"),
    path("calendar/all/", views.calendarAll, name="calendars"),
    path("summary/<int:sum_id>/", views.summary, name="summary"),
    path("summary/all/", views.summaryAll, name="summarys"),
]
