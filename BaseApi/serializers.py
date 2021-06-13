from rest_framework import serializers
from .models import Quiz,Question,ChoiceMCQ

# Admin Side Operations Using API
class QuizAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz 
        fields = '__all__'

class QuestionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ChoiceMCQAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceMCQ
        fields = '__all__'
    
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        read_only_fields = ('category','start_time','end_time','status')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question 
        fields = '__all__'
        read_only_fields =('quiz','title','type','total','current_no')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceMCQ
        fields = '__all__'
        read_only_fields = ['question','title','correct']
    


