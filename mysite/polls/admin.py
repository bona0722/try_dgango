from django.contrib import admin
from .models import Question

# Register your models here.
admin.site.register(Question) #admin 사이트에 Question을 등록해줌 코드가 바뀌면 알아서 reroad해줌