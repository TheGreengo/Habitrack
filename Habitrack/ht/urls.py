from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("select", views.select, name="select"),
    path("calendar/num/<int:cal_id>/", views.calendarNum, name="calendarNum"),
    path("calendar/bin/<int:cal_id>/", views.calendarBin, name="calendarBin"),
    path("update/num/<int:dat>/", views.updateNum, name="updateNum"),
    path("update/bin/<int:dat>/", views.updateBin, name="updateBin"),
    path("calendar/all/", views.calendarAll, name="calendars"),
    path("summary/<int:sum_id>/", views.summary, name="summary"),
    path("summary/all/", views.summaryAll, name="summarys"),
]
