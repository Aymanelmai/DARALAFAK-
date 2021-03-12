from datetime import datetime

import requests
from PIL import Image
from django.core.validators import MaxValueValidator
from django.db import models

from authors.models import Author
from categories.models import Category
from physicalformats.models import PhysicalFormat
from publishers.models import Publisher
from series.models import Serie
from ckeditor.fields import RichTextField


def get_current_year():
  return datetime.now().year


IMG_HEIGHT = 300
IMG_WIDTH = int(IMG_HEIGHT * 0.8)
class Book(models.Model):
  class Meta:
    verbose_name = 'كتاب'
    verbose_name_plural = 'كتب'

  title = models.CharField(max_length=200, verbose_name="عنوان الكتاب", unique=True)
  short_title = models.CharField(max_length=58, verbose_name="عنوان قصير", blank=True)
  authors = models.ManyToManyField(Author, verbose_name="أسماء المؤلفين")
  publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, verbose_name="الناشر", blank=True, default=None)
  category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="تصنيف الكتاب")
  serie = models.ForeignKey(Serie, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="السلسلة", default=None)
  serie_number = models.IntegerField(verbose_name="رقم السلسلة", null=True, blank=True)
  physical_format = models.ForeignKey(PhysicalFormat, on_delete=models.DO_NOTHING, verbose_name="نوع الكتاب")
  isbn = models.CharField(max_length=13, verbose_name="الرقم الدولي")
  edition = models.CharField(max_length=200, blank=True, null=True, verbose_name="الطبعة")
  description = RichTextField()
  front_image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="صورة أمامية")
  back_image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="صورة خلفية")
  summary = models.FileField(upload_to='summaries/%Y/%m/%d', verbose_name="ملف الفهرس", blank=True)
  price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="الثمن")
  y_dimension = models.IntegerField(verbose_name="طول الكتاب", default=24)
  x_dimension = models.IntegerField(verbose_name="عرض الكتاب", default=17)
  pages = models.IntegerField(verbose_name="عدد الصفحات")
  is_published = models.BooleanField(default=True, verbose_name="منشور؟")
  is_available = models.BooleanField(default=True, verbose_name="موجود؟")
  # keywords = models.ManyToManyField(Keyword, verbose_name="كلمات المفاتيح", blank=True)
  date_published = models.PositiveIntegerField(default=get_current_year, verbose_name="سنة الإصدار", validators=[MaxValueValidator(9999)])
  date_created = models.DateTimeField(default=datetime.now, blank=True, verbose_name="تاريخ الإضافة", editable=False)
  
  def __str__(self):
    return self.title
  
  def save(self, *args, **kwargs):
    # we fill short_title with title if it is empty
    if not self.short_title:
      self.short_title = self.title[:58]
    super(Book, self).save(*args, **kwargs)

    # we resize images
    imgs = (self.front_image, self.back_image)
    for img in imgs:
      img = Image.open(img.path)
      if img.height >= IMG_HEIGHT or img.width >= IMG_WIDTH:
        dimensions = (IMG_WIDTH, IMG_HEIGHT)
        img.thumbnail(dimensions)
        img.save(img.filename)

    # we post to facebook
    pageId = '346035018903244'
    token = 'EAAFSMGETZAmkBAKfmAqxQ47XdU8VXoCuUOYNPJZAJh9lWSaibFPcWpXMG06ZA2xLGfis4WBpZC9gPUVqaB9zwXPY7nEcd7G0DzlLN3mKiqauOqmoiDfZCmbfb8rOAwEAtr8vzOTrUkhFZAew07WyiSmaB9X5DCotGYXi2t0nvmMLKrNlXof8ICKk91eZAwGrkKBYeOZAbwCZAlgZDZD'
    message = 'الكتاب: {}\nالمؤلف: {}\nتاريخ الإضافة: {}\nللمزيد من المعلومات: {}'.format(self.title, self.authors_names(), self.date_created.strftime("%b %d %Y %H:%M:%S"), 'https://www.daralafak.com/book/' + str(self.id))
    r = requests.post('https://graph.facebook.com/v8.0/' + pageId + '/feed', params={'message': message, 'access_token': token})
    print(r.text)
  
  def authors_names(self):
    names = [author.name for author in self.authors.all()]
    return ' / '.join(names)
  
  def serie_name(self):
    res = ''
    if self.serie:
      res = self.serie.name
      if self.serie_number:
        res += ' - ' + str(self.serie_number)
    return res
  authors_names.short_description = 'مؤلف الكتاب'
