from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

CATEGORY_CHOICES = [
    ('pages/page.html', 'All'),
    ('pages/contact.html', 'Contact'),
    # ('singlepage/page-files.html', 'Files'),
    # ('singlepage/maps.html', 'MapsYandex'),
    # ('singlepage/kontakty.html', 'Contakt'),
    # ('singlepage/about.html', 'About'),
]


class Content(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    descriptions = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='home/', blank=True)
    content = RichTextUploadingField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Настройки главной страницы'
        verbose_name_plural = 'Настройки главной страницы'

    def __str__(self):
        return self.name

class PagesModel(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=170, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True)
    content = RichTextUploadingField(blank=True)
    code = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    shablon = models.CharField(max_length=500, choices=CATEGORY_CHOICES)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('singlepage:product_detail_page_single', args=[self.slug])

#
# class Slide(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     url = models.CharField(max_length=200, blank=True, default='#')
#     name_one = models.CharField(max_length=200, blank=True, default='#')
#     name_two = models.CharField(max_length=200, blank=True, default='#')
#     image = models.ImageField(upload_to='slide/', blank=True)
#     description = models.CharField(max_length=300, blank=True)
#     content = models.TextField(blank=True)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name

