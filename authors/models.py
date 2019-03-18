from django.db import models
from datetime import datetime
import books as b
from PIL import Image

IMG_HEIGHT = 170
IMG_WIDTH = int(IMG_HEIGHT * 0.8)
class Author(models.Model):
  class Meta:
    verbose_name = 'مؤلف'
    verbose_name_plural = 'مؤلفون'

  name = models.CharField(max_length=200, verbose_name='الإسم', unique=True)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='صورة المؤلف')
  description = models.TextField(blank=True, verbose_name='التفصيل')
  date_created = models.DateTimeField(default=datetime.now, blank=True, verbose_name='تاريخ الإضافة', editable=False)
  
  def books_count(self):
    return b.models.Book.objects.filter(authors__id=self.id).count()
  books_count.short_description = 'عدد الكتب'

  def save(self):
    super().save()
    if self.photo:
      img = Image.open(self.photo.path)
      if img.height >= IMG_HEIGHT or img.width >= IMG_WIDTH:
        dimensions = (IMG_WIDTH, IMG_HEIGHT)
        img.thumbnail(dimensions)
        img.save(img.filename)


  def __str__(self):
    return self.name
