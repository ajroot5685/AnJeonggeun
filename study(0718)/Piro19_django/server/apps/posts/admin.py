# import resource
from django.contrib import admin
from .models import Post, User

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'more_than_1000', 'created_date')
    list_display_links = ('title', 'price')
    list_filter = ('title', 'price')
    search_fields = ('title', 'price')
  
    fieldsets = [
        ('게시글',{'fields': ['title', 'price', 'content', 'region', 'photo']}),
        ('작성자',{'fields': ['user',]}),    
    ]
  
    def more_than_1000(self, obj):    
        if(int(obj.price) > 1000):
            return 'o'
        else:
            return 'x'      
    
admin.site.register(Post, PostAdmin)
admin.site.register(User)