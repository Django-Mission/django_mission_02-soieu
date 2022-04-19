# Generated by Django 4.0.3 on 2022-04-19 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='last_writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='최종 수정자'),
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(choices=[('일반', '일반'), ('계정', '계정'), ('기타', '기타')], verbose_name='카테고리')),
                ('question_title', models.TextField(verbose_name='제목')),
                ('email', models.TextField(verbose_name='이메일')),
                ('checkbox_email', models.BooleanField(verbose_name='이메일체크박스')),
                ('phonenumber', models.TextField(verbose_name='문자메시지')),
                ('checkbox_phonenumber', models.BooleanField(verbose_name='문자메시지체크박스')),
                ('content', models.TextField(verbose_name='내용')),
                ('image', models.ImageField(upload_to='images/', verbose_name='이미지')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='답변 내용')),
                ('writer', models.TextField(verbose_name='생성자')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='최종 수정일시')),
                ('Inquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.inquiry', verbose_name='참조 문의글')),
                ('last_writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='최종 수정자')),
            ],
        ),
    ]