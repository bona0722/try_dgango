from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

#from django.template import loader
from .models import Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template loading해서 거기에서 question object 역순으로 꺼내서 리스트로 만듬. 템플릿을 이용해서 
    #template = loader.get_template('polls/index.html') #이거 rendeing함
    context = {
        'latest_question_list': latest_question_list, #이렇게 사용하는 게 있으면 이거다.
    }
    #return HttpResponse(template.render(context, request)) 
    return render(request, 'polls/index.html', context) 

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)