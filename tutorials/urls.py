from django.conf.urls import url 
from tutorials import views 
from django.urls import path

urlpatterns = [ 
    path(r'tutorial', views.TutorialAPIView.as_view(), name='tutorial-list'),
   # url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
   # url(r'^api/tutorials/published$', views.tutorial_list_published)
]