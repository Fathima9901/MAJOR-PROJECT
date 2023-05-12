import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Company(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=2000, null=True)
    salary = models.IntegerField(null=True)
    experience = models.IntegerField(null=True)
    Location = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name

# Create your models here.


gender_choice = (
    ('M', 'Male'),
    ('F', 'Female'),
)

district_choices = (
    ('Alappuzha', 'Alappuzha'),
    ('Eranakulam', 'Eranakulam'),
    ('Kozhikode', 'Kozhikode'),
    ('Palakkad', 'Palakkad'),
    ('Kollam', 'Kollam'),
    ('Kannur', 'Kannur'),
    ('Kottayam', 'Kottayam'),
    ('Pathanamthitta', 'Pathanamthitta'),
    ('Kasaragod', 'Kasaragod'),
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Idukki', 'Idukki'),
    ('Thrissur', 'Thrissur'),
    ('Malappuram', 'Malappuram'),
    ('Wayanad', 'Wayanad'),
)

branch_choices = (
    ('BCA', 'BCA'),
    ('BCA DS', 'BCA DS'),
)


class Register(models.Model):
    enrollment_no = models.CharField(max_length=22, unique=True, verbose_name='enrollment no')
    first_name = models.CharField(max_length=20, verbose_name='first name')
    middle_name = models.CharField(max_length=20, verbose_name='middle name', blank=True)
    last_name = models.CharField(max_length=20, verbose_name='last name')
    date_of_birth = models.DateField(verbose_name='date of birth', default=datetime.date.today)
    gender = models.CharField(max_length=1, choices=gender_choice, verbose_name='gender', blank=True, )
    branch = models.CharField(max_length=20, choices=branch_choices, verbose_name='Department', blank=True)
    mail_id = models.EmailField(max_length=40, unique=True, blank=True, verbose_name='mail id')
    college_mail = models.EmailField(max_length=40, unique=True, blank=True, verbose_name='College mail')
    phone_number = models.CharField(max_length=10, unique=True, verbose_name='phone number', blank=True)
    password = models.CharField(max_length=15, verbose_name='password')
    current_cgpa = models.FloatField(max_length=5, verbose_name='current cgpa')
    tenth = models.CharField(max_length=5, verbose_name='10th percentage', blank=True)
    twelfth = models.CharField(max_length=5, verbose_name='12th percentage', blank=True)
    address_name = models.CharField(max_length=45, verbose_name='House name')
    post_office = models.CharField(max_length=30, verbose_name='post office')
    city = models.CharField(max_length=25, verbose_name='city')
    district = models.CharField(max_length=25, choices=district_choices, verbose_name='district')
    pincode = models.IntegerField(verbose_name='pincode')
    father_name = models.CharField(max_length=20, verbose_name='father name')
    mother_name = models.CharField(max_length=20, verbose_name='mother name')


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Registration Table'







# Create your models here.

class CampusDrive(models.Model):

    """
    Campus drive details of every company year by year.
    """

    company = models.ForeignKey(Company, db_index=True, on_delete=models.CASCADE)
    drive_year = models.IntegerField()
    package = models.CharField(max_length=10, db_index=True)
    bond_period = models.IntegerField()
    dateofdrive = models.DateField(null=False, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.CampusDrive = None

    def __str__(self):
        return self.CampusDrive



