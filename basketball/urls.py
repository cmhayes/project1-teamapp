from django.conf.urls.defaults import patterns, url

from basketball import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='roster_home'),
	url(r'^team/$', views.team, name='roster_course_list'),
	url(r'^player/$', views.player, name='roster_student_list'),
	# url(r'^team/(?P<pk>\d+)$', views.course, name='roster_course'),
	# url(r'^player/(?P<pk>\d+)$', views.student, name='roster_student'),
	)
