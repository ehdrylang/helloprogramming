from django.contrib import admin
from board.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',) # 필터 사이드바 생성
    search_fields = ('title','content') # 검색박스 표시하고 title,content에서 검색
    prepopulated_fields = {'slug':('title',)} # slug필드는 title필드를 사용해 미리 채워지게 적용

admin.site.register(Post,PostAdmin)
