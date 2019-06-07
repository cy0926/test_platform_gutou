### django自带admin的使用
我们看把__models.py__中创建的表映射到admin后台进行管理
```python
from user_app.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','describe','status','start_time','id'] # 这是定义需要显示的自带
    search_fields = ['name']  # 定义搜索栏，允许用什么关键词进行搜索
    list_filter = ['status']  # 过滤器

admin.site.register(Event, ProjectAdmin)
```
参考：https://docs.djangoproject.com/en/2.1/ref/contrib/admin/