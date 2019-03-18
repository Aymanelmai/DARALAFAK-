from django.db import models
from datetime import datetime

class Catalogue(models.Model):
  class Meta:
    verbose_name = 'قائمة'
    verbose_name_plural = 'قوائم'
  name = models.CharField(max_length=200, verbose_name='الإسم', unique=True)
  file = models.FileField(upload_to='photos/%Y/%m/%d/', verbose_name="الملف")
  date_created = models.DateTimeField(default=datetime.now, blank=True, verbose_name="تاريخ الإضافة", editable=False)

  def __str__(self):
    return self.name
  
