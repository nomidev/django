from django.db import models

# Create your models here.
class CodeType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    use_flag = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'common_code_type'

    def __str__(self):
        return self.name
    
class Code(models.Model):
    code_type = models.ForeignKey(CodeType, related_name='codes', on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    code_name = models.CharField(max_length=200)
    code_description = models.TextField(blank=True)
    order_no = models.IntegerField(default=0)
    use_flag = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('code_type', 'code')
        ordering = ['order_no']

    def __str__(self):
        # return f'{self.code_type.name} - {self.code_name}'    
        return f'{self.code_name}'    