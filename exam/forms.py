from django import forms

from django.forms import modelformset_factory

from .models import Course,Semester,Student,Faculty,Batch,ExamResult,department



class courseform(forms.ModelForm):
    class Meta:
        model =Course
        fields =['code','title', 'credit_hours']


class semfourm(forms.ModelForm):
    class Meta:
        model =Semester
        fields =['faculty','name' , 'start_date' , 'end_date' , 'courses']
       
        

class stdfourm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'phone', 'batch','faculty']
        

class dpartfourm(forms.ModelForm):
    class Meta:
        model = department
        fields = ['name' ]
        
     
        

class facform(forms.ModelForm):
    class Meta:
        model =Faculty
        fields =['name', 'department', 'faculty_id','courses_taught']
        
        
class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['year', 'department', 'faculty']
        
        

from django import forms
from .models import ExamResult


class ExamResultForm(forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = ['student', 'course', 'semester','mid_exam','final_exam', 'assissments']
        
        
       


