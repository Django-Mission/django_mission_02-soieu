from operator import truediv
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

# 나중에 커스텀할 때 사용?
User = get_user_model()

# Create your models here.

# basic


class Faq(models.Model):
    CATEGORY_SORT = [
        ('일반', '일반'),
        ('계정', '계정'),
        ('기타', '기타'),
    ]

    question = models.TextField(verbose_name='질문')
    category = models.TextField(verbose_name='카테고리', choices=CATEGORY_SORT)
    answer = models.TextField(verbose_name='답변')
    writer = models.TextField(verbose_name='생성자')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    last_writer = models.ForeignKey(
        to=User, verbose_name='최종 수정자', on_delete=models.CASCADE, null=True, blank=True)
    last_modified_at = models.DateTimeField(
        verbose_name='최종 수정일시', auto_now=True)


# advanced
class Inquiry(models.Model):
    CATEGORY_SORT = [
        ('일반', '일반'),
        ('계정', '계정'),
        ('기타', '기타'),
    ]
    category = models.TextField(verbose_name='카테고리', choices=CATEGORY_SORT)
    question_title = models.TextField(verbose_name='제목')
    email = models.TextField(verbose_name="이메일")
    checkbox_email = models.BooleanField(verbose_name="이메일체크박스")
    phonenumber = models.TextField(verbose_name="문자메시지")
    checkbox_phonenumber = models.BooleanField(verbose_name="문자메시지체크박스")
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='이미지', upload_to='images/')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    writer = models.ForeignKey(
        to=User, verbose_name='작성자', on_delete=models.CASCADE, null=True, blank=True)


class Answer(models.Model):
    # Inquiry : answer = 1 : N
    Inquiry = models.ForeignKey(
        verbose_name='참조 문의글', to='Inquiry', on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='답변 내용')
    writer = models.TextField(verbose_name='생성자')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    last_writer = models.ForeignKey(
        to=User, verbose_name='최종 수정자', on_delete=models.CASCADE, null=True, blank=True)
    last_modified_at = models.DateTimeField(
        verbose_name='최종 수정일시', auto_now=True)
