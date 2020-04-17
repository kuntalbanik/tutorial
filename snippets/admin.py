from django.contrib import admin
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
# Register your models here.

admin.site.register(Snippet)