from django.db import models
from django.core.validators import RegexValidator


# Model for Registration
class UserRegistration(models.Model):
    number = models.CharField(
        max_length=10,
        primary_key=True,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Phone number must be exactly 10 digits.",
                code='invalid_phone_number'
            )
        ],
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Model for Login
class UserLogin(models.Model):
    number = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, to_field='number')
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"Login attempt by: {self.number}"
