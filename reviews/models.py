from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
# from django.urls import reverse_lazy
from taggit.managers import TaggableManager


# Create your models here.
class Problem(models.Model):
    # post_num = models.IntegerField('글 번호')
    title = models.CharField('제목', max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='게시자', on_delete=models.CASCADE)
    
    # url shortener + 미리보기 + Validator
    url = models.CharField('문제 링크', max_length=1000)
    tags = TaggableManager(blank=True)
    description = models.TextField('설명')

    study = models.ForeignKey("studies.Study", verbose_name='스터디', on_delete=models.CASCADE, default=1)
    # display = models.BooleanField(default=True)


    class Meta:
        db_table = 'problem'


    def __str__(self) -> str:
        return self.title
    
    # def delete(self):
    #     pass

    # def create(self):
    #     pass

    # def get_absolute_url(self):
    #     return reverse_lazy('reviews:detail', kwargs={'pk': self.pk})


class Review(models.Model):
    content = models.TextField('내용')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='작성자', on_delete=models.CASCADE)
    problem = models.ForeignKey("reviews.Problem", verbose_name='문제', on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)

    class Meta:
        db_table = 'review'


    def __str__(self) -> str:
        return f'Review by {self.user}, on {self.problem}'


class Comment(models.Model):
    content = models.TextField('내용')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='작성자', on_delete=models.CASCADE)
    review = models.ForeignKey("reviews.Review", verbose_name='리뷰', on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    tags = TaggableManager(blank=True)

    class Meta:
        db_table = 'comment'

    def __str__(self) -> str:
        return f'Comment by {self.user}, on {self.review}'
