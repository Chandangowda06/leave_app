from django.db import models
from django.contrib.auth.models import User


class College(models.Model):
    college_name = models.CharField(max_length=100)
    principal = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,  related_name='college_principal')

    def __str__(self):
        return self.college_name

class Department(models.Model):
    name = models.CharField(max_length=100)
    hod = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='department_hod')
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StaffDetail(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_type  = models.CharField(max_length=40, choices=(
        ('HOD', 'Head Of Department'),
        ('Principal', 'Principal'),
        ('Staff', 'Staff')
    ))
    sid = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_images', default='/default.png')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.staff.username



class LeaveData(models.Model):
    applicant = models.ForeignKey(StaffDetail, on_delete=models.CASCADE)
    application_id = models.CharField(max_length=10)
    reason = models.CharField(max_length=300)
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    status = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ))
    num_of_days = models.IntegerField()
    previous_leaves = models.IntegerField()
    pdf_file = models.FileField(upload_to='leave_letters/')

    def __str__(self):
        return f"{self.applicant} - {self.status}"

class Approval(models.Model):
    application = models.ForeignKey(LeaveData, on_delete=models.CASCADE)
    approved_hod = models.BooleanField(default=False)
    approved_principal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.application} - HOD: {self.approved_hod}, Principal: {self.approved_principal}"

