from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name="menu_name")
    description = models.TextField(blank=True, verbose_name="menu_description")
    level = models.IntegerField(default=0, verbose_name="menu_level")
    url_type = models.ForeignKey('common.Code', on_delete=models.SET_NULL, null=True, blank=True, related_name='menu_url_type', verbose_name="menu_url_type")
    url = models.CharField(max_length=200, blank=True, verbose_name="menu_url")
    view = models.CharField(max_length=100, blank=True, verbose_name="menu_view")
    view_param = models.CharField(max_length=100, blank=True, verbose_name="menu_view_param")
    order_no = models.IntegerField(default=0, verbose_name="order_no")
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='submenus')
    display_flag = models.BooleanField(default=True, verbose_name="display_flag")
    use_flag = models.BooleanField(default=True, verbose_name="use_flag")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")

    class Meta:
        ordering = ['order_no'] # 순서대로 정렬

    def __str__(self):
        return self.name