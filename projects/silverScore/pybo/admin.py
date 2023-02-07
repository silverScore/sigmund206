from django.contrib import admin
# 추가
from .models import Question, Answer


# Register your models here.
# [검색] 기능 추가
# 클래스 상속이다.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
from django.contrib import admin

# Register your models here.
