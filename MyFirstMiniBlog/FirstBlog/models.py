from audioop import reverse

from django.db import models

class Post(models.Model):
    '''note data'''
    title = models.CharField('Topic', max_length=100)
    description = models.TextField('Text of the note')
    author = models.CharField('Author', max_length=100)
    date = models.DateField('Date')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

