from django.contrib import admin
from blog.models import Category,Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}   
    list_display = ('title','category','author','status','is_featured','created_at')
    search_fields = ('id','title','status','category__name')
    list_editable = ('is_featured',)

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
