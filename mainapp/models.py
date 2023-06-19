from django.db import models

from authapp.models import User


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=256)
    content = models.TextField(verbose_name="Контент")
    image = models.ImageField(verbose_name='изображение', upload_to='news/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    class Status(models.TextChoices):
        ZERO = '0', 'заблокирован',
        FIRST = '1', 'Опубликован',
        TWO = '2', ' Ожидает проверки'

    news = models.ForeignKey(News, verbose_name='новость', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='комментарий')
    status = models.CharField(verbose_name='статус', max_length=1, choices=Status.choices, default=Status.ZERO)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'комментарий'
        verbose_name_plural = 'комменатрии'


class Favorite(models.Model):
    news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'




class Products(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=128)
    image = models.ImageField(verbose_name='Изображение товара', upload_to='products/%Y/%m/%d')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    info = models.TextField(verbose_name='Информация', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class FeedBack(models.Model):
    product = models.ForeignKey(Products, verbose_name='Выберите продукт для заказа',on_delete=models.CASCADE)
    address = models.CharField(verbose_name='Адрес объекта недвижимости', max_length=256)
    full_name = models.CharField(verbose_name='ФИО', max_length=100)
    tel = models.IntegerField(verbose_name='Телефон')
    email = models.EmailField(verbose_name='email')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name}{self.email}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = ' Обратная связь'

