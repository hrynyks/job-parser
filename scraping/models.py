from django.db import models

from scraping.utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='City name', unique=True)
    slug = models.CharField(max_length=50, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'City name'
        verbose_name_plural = 'City names'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
            super().save(*args, **kwargs)


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50, verbose_name='Programming language', unique=True)
    slug = models.CharField(max_length=50, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Programming name'
        verbose_name_plural = 'Programming languages'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
            super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Title of vacancy')
    company_name = models.CharField(max_length=250, verbose_name='Company name')
    description = models.TextField(verbose_name='Description of vacancy')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='City')
    programming_language = models.ForeignKey('ProgrammingLanguage', on_delete=models.CASCADE, verbose_name='Programming Language')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancy'

    def __str__(self):
        return self.title


