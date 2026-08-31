from django.db import models



class Question(models.Model):
    subject = models.CharField(max_length=150)
    text = models.TextField()
    order = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.text[:30]}'
