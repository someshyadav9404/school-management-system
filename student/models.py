from django.db import models
from organization.models import Organization
# students/models.p
class Student(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="students")
    name = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True, null=True)
    standard = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.organization.name})"