from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def create_superuser(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a username")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.username = username
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user
    
    INSTITUTION = (
        ('Abia', 'Abia State University'),
        ('Adamawa', 'Adamawa State University'),
        ('Adekunle', 'Adekunle Ajasin University'),
        ('Adeleke', 'Adeleke University'),
        ('Afe', 'Afe Babalola University'),
        ('Ahmadu', 'Ahmadu Bello University'),
        ('Ajayi', 'Ajayi Crowther University'),
        ('Akwa', 'Akwa Ibom State University'),
        ('Ambrose', 'Ambrose Alli University'),
        ('American', 'American University of Nigeria'),
        ('Anchor', 'Anchor University'),
        ('Arthur', 'Arthur Jarvis University'),
        ('Atiba', 'Atiba University'),
        ('Augustine', 'Augustine University'),
        ('Babcock', 'Babcock University'),
        ('Bauchi', 'Bauchi State University'),
        ('Bayero', 'Bayero University'),
        ('Baze', 'Baze University'),
        ('Bells', 'Bells University of Technology'),
        ('Benson', 'Benson Idahosa University'),
        ('Benue', 'Benue State University'),
        ('Bingham', 'Bingham University'),
        ('Borno', 'Borno State University'),
        ('Bowen', 'Bowen University'),
        ('Caleb', 'Caleb University'),
        ('Caritas', 'Caritas University'),
        ('Chrisland', 'Chrisland University'),
        ('Christopher', 'Christopher University'),
        ('Covenant', 'Covenant University'),
        ('Crawford', 'Crawford University'),
        ('Delta', 'Delta State University'),
        ('Elizade', 'Elizade University'),
        ('Hallmark', 'Hallmark University'),
        ('Landmark', 'Landmark University'),
        ('Mountain', 'Mountain Top University'),
        ('Nnamdi', 'Nnamdi Azikiwe University'),
        ('Obafemi', 'Obafemi Awolowo University'),
        ('Olabisi', 'Olabisi Onabanjo University'),
        ('Redeemers', 'Redeemers University'),
        ('Benin', 'University of Benin'),
        ('Ibadan', 'University of Ibadan'),
        ('Ilorin', 'University of Ilorin'),
        ('Nsukka', 'University of Nigeria Nsukka'),
        ('Port', 'University of Port Harcourt'),
        ('Others', 'Others'),
    )

    LEVEL = (
        ('Researcher', 'Researcher'),
        ('Professor', 'Professor'),
        ('Lecturer', 'Lecturer'),
        ('Student', 'Student'),
        ('Others', 'Others'),
    )

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=250, unique=True)
    institution = models.CharField(choices=INSTITUTION, max_length=100, blank=False)
    level = models.CharField(choices=LEVEL, max_length=10, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    
