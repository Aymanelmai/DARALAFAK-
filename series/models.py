from django.db import models
from datetime import datetime

class Serie(models.Model):
  class Meta:
    verbose_name = 'سلسلة'
    verbose_name_plural = 'سلاسل'

  name = models.CharField(max_length=200, verbose_name='الإسم', unique=True)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='الصورة')
  description = models.TextField(blank=True, verbose_name='التفصيل')
  date_created = models.DateTimeField(default=datetime.now, blank=True, editable=False, verbose_name='تاريخ الإضافة')
  def __str__(self):
    return self.name
