from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=32, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    sections = models.ManyToManyField(Section, through='ArticleSection')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    main_title = models.BooleanField(verbose_name='Основной')
    sections = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Тэги')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.main_title




