from django.urls import path,include
from rest_framework.routers import DefaultRouter 
from . import views

router = DefaultRouter()
router.register('adminquiz',views.QuizAdminView, basename='adminquiz')
router.register('adminquestion',views.QuestionAdminView, basename='adminquestion')
router.register('adminchoices',views.ChoiceMCQAdminView, basename='adminchoice')
router.register('quiz',views.QuizView, basename= 'userquiz')
router.register('question',views.QuestionView, basename= 'userquestion')
router.register('choices',views.ChoiceView, basename= 'userchoice')

urlpatterns = [
    path('',include(router.urls)),
]