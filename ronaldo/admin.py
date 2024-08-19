from django.contrib import admin

from .models import User, Comment, Category, Company, Awards, Services, SiteAdminisration, Skills, Blog, Education, Experience, GetInTouch, OurProjects, Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'created_at']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'created_at']


@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message',]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'blog', 'email', 'web_site']


@admin.register(SiteAdminisration)
class SiteAdminisrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'awards', 'projects', 'happy_customers', 'cups_of_cofee']


admin.site.register(Company)
admin.site.register(Services)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(OurProjects)
admin.site.register(Awards)
