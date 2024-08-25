from django.db import models
from django.db.models import DecimalField, Sum, F
from decimal import Decimal

from exam.grading_system import get_grade_and_points


#diwaan galinta courseska
class Course(models.Model):
    code = models.CharField(max_length=50,unique=True)
    title = models.CharField(max_length=200)
    credit_hours = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        return self.title
    
#diwaan galinta sesmesterka
class Semester(models.Model):
    faculty=models.ForeignKey('Faculty',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
    
# diwaangalinta ardayga
class Student(models.Model):
    name= models.CharField(max_length=400)
    student_id = models.CharField(max_length=50,unique=True)
    phone = models.IntegerField()
    batch = models.ForeignKey('Batch',on_delete=models.CASCADE)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class department(models.Model):
    name=models.CharField(max_length=678)
    def __str__(self):
        return self.name

    
    def __str__(self):
        return self.name

# diwan galinta fucults
class Faculty(models.Model):
    name = models.CharField(max_length=400)
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    faculty_id = models.CharField(max_length=100,unique=True)
    courses_taught = models.ManyToManyField(Course)

    def __str__(self):
        return self.name 

#batches
class Batch(models.Model):
    year = models.CharField(max_length=300)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)

    def __str__(self):
        return self.year
    
from django.db import models

class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    mid_exam = models.FloatField()
    final_exam = models.FloatField(blank=True)
    assissments = models.FloatField()
    score = models.FloatField(blank=True, null=True)
    grade = models.CharField(max_length=2, blank=True)
    credit_points = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate total score as the sum of mid_exam, final_exam, and assissments
        self.score = self.mid_exam + self.final_exam + self.assissments
        
        # Calculate grade and credit points based on total score
        self.grade, self.credit_points = get_grade_and_points(self.score)
        
        # Save the updated instance
        super().save(*args, **kwargs)
