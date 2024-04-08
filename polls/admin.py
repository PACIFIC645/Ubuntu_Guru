# polls/admin.py

from django.contrib import admin
from .models import Question, Choice
from .models import BlogPost

# Inline class to show Choices directly within the Question form
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0  # Do not display any extra blank choice fields by default

    def get_extra(self, request, obj=None, **kwargs):
        # Only add extra choice fields if the question object is new and has no choices yet
        if obj is None or obj.choice_set.count() == 0:
            return 3  # Adjust the number as per your requirement
        return 0

# ModelAdmin class for the Question model
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

# Register the admin class with the associated model
admin.site.register(Question, QuestionAdmin)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'updated_on')
    list_filter = ('created_on', 'author')
    search_fields = ['title', 'content']


