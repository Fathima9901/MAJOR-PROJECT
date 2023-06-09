# Generated by Django 4.1.5 on 2023-04-27 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student', '0003_remove_register_pg_cgpa_remove_register_ug_cgpa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='branch',
            field=models.CharField(blank=True, choices=[('BCA', 'BCA'), ('BCA DS', 'BCA DS')], max_length=20, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='register',
            name='college_mail',
            field=models.EmailField(blank=True, max_length=40, unique=True, verbose_name='College mail'),
        ),
        migrations.AlterField(
            model_name='register',
            name='date_of_birth',
            field=models.DateField(blank=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='register',
            name='mail_id',
            field=models.EmailField(blank=True, max_length=40, unique=True, verbose_name='mail id'),
        ),
        migrations.AlterField(
            model_name='register',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, unique=True, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='register',
            name='tenth',
            field=models.FloatField(blank=True, max_length=5, verbose_name='10th percentage'),
        ),
        migrations.AlterField(
            model_name='register',
            name='twelfth',
            field=models.FloatField(blank=True, max_length=5, verbose_name='12th percentage'),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('position', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=2000, null=True)),
                ('salary', models.IntegerField(null=True)),
                ('experience', models.IntegerField(null=True)),
                ('Location', models.CharField(max_length=2000, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
