from student.models import Student
from organization.models import Organization
from django.db import IntegrityError

def add_student(org_id, name, roll_no, standard, email=None):
    try:
        org = Organization.objects.get(id=org_id)
        student = Student.objects.create(
            organization=org,
            name=name,
            roll_no=roll_no,
            standard=standard,
            email=email
        )
        return student
    except IntegrityError:
        raise Exception("Student with this roll number already exists.")
    except Organization.DoesNotExist:
        raise Exception("Organization not found.")
