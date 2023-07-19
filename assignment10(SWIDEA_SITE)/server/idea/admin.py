from django.contrib import admin
from .models import Idea, Devtool, IdeaStar

# Register your models here.
admin.site.register(Idea)
admin.site.register(Devtool)
admin.site.register(IdeaStar)