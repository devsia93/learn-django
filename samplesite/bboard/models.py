from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    # Rubric - строка с именем класса первичной модели
    # null = True - делаем поле необязательным к заполнению
    # Именованный параметр on deiete управляет каскадными удалениями записей вто
    # ричной модели после удаления записи первичной модели, с которой они были свя
    # заны. Значение protect этого параметра запрещает каскадные удаления (чтобы
    # какой-нибудь несообразительный администратор не стер разом уйму объявлений,
    # удалив рубрику, к которой они относятся).

    class Meta:
        verbose_name_plural = "Объявления"
        verbose_name = "Объявление"
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

# class Bb(models.Model):
#   class Kinds(models.TextChoices):
# 'Куплю'
# BUY = 'b',
# SELL = 's', 'Продам'
# EXCHANGE = 'с', 'Обменяю'
# RENT = 'r'
# __ empty__ = 'Выберите тип публикуемого объявления'
