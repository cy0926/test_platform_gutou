from django.db import models
from user_app.models.project import Project


# Create your models here.

class Module(models.Model):
    """
    模块表
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=50, null=False)
    describe = models.TextField("描述", max_length=50, null=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name