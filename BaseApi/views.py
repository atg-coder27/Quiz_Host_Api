from django.db.models.deletion import RESTRICT
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from .models import Quiz,Question,ChoiceMCQ
from .serializers import ChoiceSerializer, QuizAdminSerializer,QuestionAdminSerializer,ChoiceMCQAdminSerializer
from .serializers import QuizSerializer,QuestionSerializer
# Create your views here.

# Admin full access  
class QuizAdminView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizAdminSerializer

class QuestionAdminView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionAdminSerializer

class ChoiceMCQAdminView(viewsets.ModelViewSet):
    queryset = ChoiceMCQ.objects.all()
    serializer_class = ChoiceMCQAdminSerializer


# User Side

class QuizView(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    def list(self, request, *args, **kwargs):
        value = super().list(request, *args, **kwargs)
        data = value.data
        for i in range(len(data)):
            id = data[i]["id"]
            quiz = Quiz.objects.get(id = id)
            questions = Question.objects.filter(quiz = quiz)
            serializer = QuestionSerializer(questions,many = True)
            data[i]["questions"] = serializer.data
            for j in range(len(data[i]["questions"])):
                id = data[i]["questions"][j]["id"]
                question = Question.objects.get(id = id)
                choices = ChoiceMCQ.objects.filter(question = question)
                serializer = ChoiceSerializer(choices,many = True)
                data[i]["questions"][j]["choices"] = serializer.data
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        value =  super().retrieve(request, *args, **kwargs)
        data = value.data 
        quiz = Quiz.objects.get(id = data["id"])
        questions = Question.objects.filter(quiz = quiz)
        serializer = QuestionSerializer(questions,many = True)
        questions = serializer.data 
        for i in range(len(questions)):
            question = Question.objects.get(id = questions[i]["id"])
            choices = ChoiceMCQ.objects.filter(question = question)
            serializer = ChoiceSerializer(choices,many = True)
            questions[i]["choices"] = serializer.data
        data["questions"] = questions
        return Response(data)
    
class QuestionView(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        value =  super().list(request, *args, **kwargs)
        data = value.data
        for i in range(len(data)):
            id = data[i]["id"]
            question = Question.objects.get(id = id)
            choices = ChoiceMCQ.objects.filter(question = question)
            serializer = ChoiceSerializer(choices,many = True)
            data[i]["choices"] = serializer.data

        return Response(data)
    
    def retrieve(self, request, *args, **kwargs):
        value =  super().retrieve(request, *args, **kwargs)
        data = value.data
        question =Question.objects.get(id = data["id"])
        choices = ChoiceMCQ.objects.filter(question = question)
        serializer = ChoiceSerializer(choices,many = True)
        data["choices"] = serializer.data
        return Response(data)

class ChoiceView(viewsets.ModelViewSet):
    queryset = ChoiceMCQ.objects.all()
    serializer_class = ChoiceSerializer

    

    



