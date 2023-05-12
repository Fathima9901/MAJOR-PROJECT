# Generated by Django 4.1.5 on 2023-04-26 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_no', models.CharField(max_length=22, unique=True, verbose_name='enrollment no')),
                ('first_name', models.CharField(max_length=20, verbose_name='first name')),
                ('middle_name', models.CharField(blank=True, max_length=20, verbose_name='middle name')),
                ('last_name', models.CharField(max_length=20, verbose_name='last name')),
                ('branch', models.CharField(choices=[('BCA', 'BCA'), ('BCA', 'BCA DS'), ('BBA', 'BBA'), ('B COM', 'B COM'), ('CSE', 'CSE'), ('EAC', 'EAC'), ('EEE', 'EEE'), ('AI', 'AI'), ('MCA', 'MCA'), ('BSW', 'BSW'), ('MSW', 'MSW'), ('INT PHYSICS', 'INT PHYSICS'), ('INT CHEMISTRY', 'INT CHEMISTRY'), ('INT ENGLISH', 'INT ENGLISH'), ('INT MATHS', 'INT MATHS')], max_length=20, verbose_name='Department')),
                ('mail_id', models.EmailField(max_length=40, unique=True, verbose_name='mail id')),
                ('college_mail', models.EmailField(max_length=40, unique=True, verbose_name='College mail')),
                ('phone_number', models.CharField(max_length=10, unique=True, verbose_name='phone number')),
                ('password', models.CharField(max_length=15, verbose_name='password')),
                ('UG_cgpa', models.FloatField(max_length=5, verbose_name='UG cgpa')),
                ('tenth', models.FloatField(max_length=5, verbose_name='10th percentage')),
                ('twelfth', models.FloatField(max_length=5, verbose_name='12th percentage')),
                ('PG_cgpa', models.FloatField(default=0, max_length=5, verbose_name='PG cgpa')),
                ('address_name', models.CharField(max_length=45, verbose_name='House name')),
                ('post_office', models.CharField(max_length=30, verbose_name='post office')),
                ('city', models.CharField(max_length=25, verbose_name='city')),
                ('district', models.CharField(choices=[('Alappuzha', 'Alappuzha'), ('Eranakulam', 'Eranakulam'), ('Kozhikode', 'Kozhikode'), ('Palakkad', 'Palakkad'), ('Kollam', 'Kollam'), ('Kannur', 'Kannur'), ('Kottayam', 'Kottayam'), ('Pathanamthitta', 'Pathanamthitta'), ('Kasaragod', 'Kasaragod'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Idukki', 'Idukki'), ('Thrissur', 'Thrissur'), ('Malappuram', 'Malappuram'), ('Wayanad', 'Wayanad')], max_length=25, verbose_name='district')),
                ('pincode', models.IntegerField(max_length=6, verbose_name='pincode')),
                ('father_name', models.CharField(max_length=20, verbose_name='father name')),
                ('mother_name', models.CharField(max_length=20, verbose_name='mother name')),
            ],
            options={
                'verbose_name_plural': 'Registration Table',
            },
        ),
    ]
