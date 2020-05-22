import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
#모델이란 부가적인 메타데이터를 가진 데이터베이스의 구조(layout)를 말합니다.

#설문조사 만들기 묻는 문항과 선택지 필요 question 하나에 choice 여러 개
#1:n관계
class Question(models.Model):
    question_text = models.CharField(max_length=200) #CharField 는 클래스 이름.
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text #return 해주면 더 보기 좋게 나옴

    def was_published_recently(self): #최근에 published 된거냐. 현재로부터 timedelta(하루, 24시간)전보다 크면, 하루 이내에 발간된 날짜라면 최근꺼 
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200) #설문 문항
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text 
    #return 해주면 더 보기 좋게 나옴
#app에 등록되면서 question, choice table이 만들어짐.
# python manage.py makemigrations polls < migrations가 만들어짐 

