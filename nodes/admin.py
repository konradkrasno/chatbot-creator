from django.contrib import admin

from nodes.models import Node, Question, Answer

admin.site.register(Node)
admin.site.register(Question)
admin.site.register(Answer)
