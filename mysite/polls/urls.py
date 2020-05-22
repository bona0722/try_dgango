from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [ 
    # 하드코딩한 것은 /polls/란 이름을 바꾸면 안 됨. 
    path('', views.index, name='index'), #url을 만들 때 polls앱에서 polls/ < 라고 하면 인덱스 콜
    #name이란 지금까지 url이 매칭돼왔다 polls하고 index매칭 . name이란것은 이때의 url을 우리가 이름으로 reference하려고 지은거다
    #이 이름을 적으면 매칭돼 있는 url패턴 path부분을 가져올 수 있다. 그렇다면 index.html에서 "/polls/{{ question.id }}/" 이렇게 안 써도 된다.
    path('<int:question_id>/', views.detail, name='detail'),#question id 주면 detail view를 보여줌
    path('<int:question_id>/results/', views.results, name='results'),#question view를 주면 설문결과
    path('<int:question_id>/vote/', views.vote, name='vote'), # voting하는걸 해주면 됨
    #해주고 html도 만들어줘야함
]
#나한테 위임한 게 있을텐데 아무것도 없으면 view.index를 불러달라.