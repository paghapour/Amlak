from django.db import models

from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('Date Time of Creation'))
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])