from django.db import models

class Organizations(models.Model):
    OrgID = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=550, blank=False)
    address = models.TextField(verbose_name='Organization Address', max_length=800, blank=True)
    email = models.CharField(verbose_name='Organization Email', max_length=100, blank=True)
    contact = models.CharField(verbose_name="Organization Contact", max_length=50, blank=True)
    logo = models.ImageField(upload_to='orgLogos', default='media/orgLogos/memberPlus.jpg', blank=True)
    active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('date_added')

    class Meta:
        db_table = "Organizations_tb"
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"


# Create your models here.
class Members(models.Model):    
    MALE = 'M'
    FEMALE = 'F'
    
    
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    ROLE_CHOICES = [
        ('None', 'None'),
        ('Admin', 'admin'),
    ]
    
    orgID = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    memberID = models.CharField(max_length=50, blank=False)
    firstname = models.CharField(max_length=200, blank=False)
    lastname = models.CharField(max_length=200, blank=False)

    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    DOB = models.DateField()
    gender = models.CharField( max_length=2, choices=GENDER_CHOICES)

    bloodGroup = models.CharField(max_length=20, default="Not Provided")
    maritalStatus = models.CharField(max_length=50, default="Not Provided")
    country = models.CharField(max_length=100, default="Not Provided")

    stateOfOrigin = models.CharField(max_length=200, default="Not Provided")
    town = models.CharField(max_length=200, default="Not Provided")
    LGA = models.CharField(max_length=100, default="Not Provided")

    nextOfKin = models.CharField(max_length=200, default="Not Provided")
    highestQual = models.CharField(max_length=200, default="Not Provided")
    occupation = models.CharField(max_length=200, default="Not Provided")
    proffession = models.CharField(max_length=200, default="Not Provided")
    positionHeld = models.CharField(max_length=200, default="Not Provided")

    role = models.CharField( max_length=50, choices=ROLE_CHOICES, blank=True)



    residentialAddress = models.TextField(max_length=800, default="Not Provided")
    officeAddress = models.TextField(max_length=800, default="Not Provided")
    otherInfo = models.TextField(max_length=800, default="Not Provided")

    profileImg = models.ImageField(
        upload_to='profilePics', default='static/img/passportplaceholderM.jpg' if gender == 'M' else 'static/img/passportplaceholder.jpg', blank=False)
    
    
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.lastname

    class Meta:
        ordering = ('date_added')

    class Meta:
        db_table = "Members_tb"
        verbose_name = "Member"
        verbose_name_plural = "Members"
