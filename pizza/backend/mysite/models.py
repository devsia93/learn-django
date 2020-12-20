from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from transliterate import translit, get_available_language_codes


def generation_slug(text):
    new_slug = slugify(translit(u"".join(text), 'ru', reversed=True))
    return new_slug


class Pizza(models.Model):
    slug = models.SlugField(max_length=75, blank=True, unique=True)
    title = models.CharField(
        max_length=25, db_index=True, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    cook = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.PROTECT)
    topings = models.ManyToManyField(
        'Toping', blank=True, related_name='Топинги')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generation_slug(self.title)
        self.title = '. '.join(
            map(lambda s: s.strip().capitalize(), self.title.split('. ')))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pizza_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('pizza_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('pizza_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Пиццы"
        verbose_name = "Пицца"
        ordering = ['title']


class Toping(models.Model):
    slug = models.SlugField(max_length=75, blank=True, unique=True)
    title = models.CharField(
        max_length=25, db_index=True, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')

    def get_absolute_url(self):
        return reverse('toping_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('toping_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('toping_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Топинги'
        verbose_name = 'Топинг'
        ordering = ['title']
