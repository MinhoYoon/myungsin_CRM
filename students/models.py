from django.conf import settings
from django.db import models
from django.utils import timezone


class 등록(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    이름 = models.CharField(max_length=200)
    과정 = models.CharField(max_length=200)
    월_4주당_수강시간 = range(4,60)
    다음_결제일 = models.DateTimeField(
            default=timezone.now)
    금액 = models.IntegerField(default=150000)
    
    def 등록(self):
        self.등록_날짜 = timezone.now()
        self.save()

    def __str__(self):
        return self.이름
