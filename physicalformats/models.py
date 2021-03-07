from django.db import models
from datetime import datetime

class PhysicalFormat(models.Model):
  class Meta:
    verbose_name = 'نوع'
    verbose_name_plural = 'أنواع'

  name = models.CharField(max_length=200, verbose_name='الإسم', unique=True)
  description = models.TextField(blank=True, verbose_name='التفصيل')
  date_created = models.DateTimeField(default=datetime.now, blank=True, editable=False, verbose_name='تاريخ الإضافة')
  def __str__(self):
    return self.name