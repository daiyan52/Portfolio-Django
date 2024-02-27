from django.urls import path
from testapp.views import homeView,citybeatView,quizAppView,footFusionView

app_name = 'testapp'
urlpatterns = [
    path('home/', homeView.as_view(), name='home'),
    path('citybeat/', citybeatView.as_view(), name='citybeat'),
    path('quizApp/', quizAppView.as_view(), name='quizApp'),
    path('footfusion/', footFusionView.as_view(), name='footfusion'),
]
