from django.shortcuts import render,redirect,get_object_or_404
from django .http import HttpResponse
from .models import Course,Semester,Student,Faculty,Batch,ExamResult,department
from .forms import courseform,semfourm,stdfourm,facform,BatchForm,ExamResultForm,dpartfourm
from django.db.models import DecimalField, Sum, F
from decimal import Decimal
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



#dash

def dashboard(request):
    return render(request,'home.html')
#course


def course_list(request):
    courses= Course.objects.all()
    return render(request,'course_list.html',{'courses': courses})

def course_create(request):
    form=courseform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    context={'form':form}
    return render(request,'course_create.html',context)

def course_detail(request, pk):
    courses = Course.objects.get( pk=pk)
    context={
        'courses':courses
    }
    return render(request, 'course_detail.html',context)

# Update an existing course

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = courseform(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # Replace with your list view name
    else:
        form = courseform(instance=course)
    return render(request, 'course_update.html', {'form': form})


def course_delete(request, pk):
    course_obj = Course.objects.get( pk=pk)
    if request.method == 'POST':
        course_obj.delete()
        return redirect('course_list')
    return render(request, 'course_delete.html', {'course': course_obj})

def course_search(request):
    query = request.GET.get('q')
    if query:
        results = Course.objects.filter(title__icontains=query)  | Course.objects.filter(code__icontains=query)
    
    else:
        results = Course.objects.none()

    return render(request, 'course_search.html', {'results': results, 'query': query})

#semester

def semester_list(request):
    semesters=Semester.objects.all()
    return render(request,'semester_list.html',{'semesters': semesters})

def semester_create(request):
    form=semfourm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('semester_list')
    context ={
        'form':form
    }
    return render(request,'semester_create.html',context)
def semester_detail(request, pk):
    semester = Semester.objects.get( pk=pk)
    context={
        'semester':semester
    }
    return render(request, 'semester_detail.html',context)


# Update an existing semester

def semester_update(request, pk):
    semester = get_object_or_404(Semester, pk=pk)
    if request.method == 'POST':
        form = semfourm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
            return redirect('semester_list')  # Replace with your list view name
    else:
        form = semfourm(instance=semester)
    return render(request, 'semeter_update.html', {'form': form})

def semester_delete(request, pk):
    semesters=Semester.objects.get(pk=pk)
    if request.method =='POST':
        semesters.delete()
        return redirect('semester_list')
    return render(request,'semester_delete.html',{'semester': semesters})

def semster_search(request):
    query = request.GET.get('q')
    if query:
        results = Semester.objects.filter(name__icontains=query)
    
    else:
        results = Semester.objects.none()

    return render(request, 'semester_search.html', {'results': results, 'query': query})

#student

def student_list(request):
    students =Student.objects.all()
    return render(request,'student_list.html',{'students':students})

def student_create(request):
    form=stdfourm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    context ={
        'form':form
    }
    return render(request,'student_create.html',context)

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = stdfourm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Replace with your list view name
    else:
        form = stdfourm(instance=student)
    return render(request, 'student_update.html', {'form': form})

def student_delete(request, pk):
    students=Student.objects.get(pk=pk)
    if request.method =='POST':
        students.delete()
        return redirect('student_list')
    return render(request,'student_delete.html',{'students': students})

def student_search(request):
    query = request.GET.get('q')
    if query:
        results = Student.objects.filter(name__icontains=query) | Student.objects.filter(student_id__icontains=query) | Student.objects.filter(phone__icontains=query) | Student.objects.filter(batch__year__icontains=query) | Student.objects.filter(faculty__name__icontains=query) 
    else:
        results = Student.objects.none()

    return render(request, 'student_search.html', {'results': results, 'query': query})




#faculty

def faculty_list(request):
    facultys=Faculty.objects.all()
    return render(request,'faculty_list.html',{'facultys':facultys})

def faculty_create(request):
    form=facform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('faculty_list')
    context ={
        'form':form
    }
    return render(request,'faculty_create.html',context)

def faculty_detail(request, pk):
    facultys = Faculty.objects.get( pk=pk)
    context={
        'facultys':facultys
    }
    return render(request, 'faculty_detail.html',context)


def faculty_update(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        form = facform(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')  # Replace with your list view name
    else:
        form = facform(instance=faculty)
    return render(request, 'faculty_update.html', {'form': form})

def faculty_delete(request, pk):
    facultys=Faculty.objects.get(pk=pk)
    if request.method =='POST':
        facultys.delete()
        return redirect('faculty_list')
    return render(request,'faculty_delete.html',{'facultys': facultys})

def faculty_search(request):
    query = request.GET.get('q')
    if query:
        results = Faculty.objects.filter(name__icontains=query) | Faculty.objects.filter(department__name__icontains=query) 
    else:
        results = Faculty.objects.none()

    return render(request, 'faculty_search.html', {'results': results, 'query': query})

#department

def dapart_list(request):
    dapartments=department.objects.all()
    return render(request,'daprt_list.html',{'dapartments':dapartments})

def dapart_create(request):
    form=dpartfourm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('dapart_list')
    context ={
        'form':form
    }
    return render(request,'depart_create.html',context)

def depart_update(request, pk):
    dapartments = get_object_or_404(department, pk=pk)
    if request.method == 'POST':
        form = dpartfourm(request.POST, instance=dapartments)
        if form.is_valid():
            form.save()
            return redirect('dapart_list')  # Replace with your list view name
    else:
        form = dpartfourm(instance=dapartments)
    return render(request, 'depart_update.html', {'form': form})

def depart_delete(request, pk):
    dapartments=department.objects.get(pk=pk)
    if request.method =='POST':
        dapartments.delete()
        return redirect('dapart_list')
    return render(request,'depart_delete.html',{'dapartments': dapartments})





#batches

def batch_list(request):
    butchs =Batch.objects.all()
    return render(request,'batch_list.html',{'butchs':butchs})

def batch_create(request):
    form=BatchForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('batch_list')
    context ={
        'form':form
    }
    return render(request,'butch_create.html',context)

def batch_update(request, pk):
    butchs = get_object_or_404(Batch, pk=pk)
    if request.method == 'POST':
        form = BatchForm(request.POST, instance=butchs)
        if form.is_valid():
            form.save()
            return redirect('batch_list')  
    else:
        form = BatchForm(instance=butchs)
    return render(request, 'butch_update.html', {'form': form})

def butch_delete(request, pk):
    butchs=Batch.objects.get(pk=pk)
    if request.method =='POST':
        butchs.delete()
        return redirect('batch_list')
    return render(request,'butch_delete.html',{'butchs': butchs})

def butch_search(request):
    query = request.GET.get('q')
    if query:
        results = Batch.objects.filter(year__icontains=query) | Batch.objects.filter(department__name__icontains=query) |  Batch.objects.filter(faculty__name__icontains=query) 
    else:
        results = Batch.objects.none()

    return render(request, 'butch_search.html', {'results': results, 'query': query})



#exam result
def exam_resul_list(requst):
    examresults=ExamResult.objects.all()
    return render(requst,'exam_result_list.html',{'examresults':examresults})

def exam_resul_create(request):
    form=ExamResultForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('exam_list')
    context ={
        'form':form
    }
    return render(request,'exam_result_create.html',context)


def exam_resul_update(request, pk):
    exam_result = get_object_or_404(ExamResult, pk=pk)
    if request.method == 'POST':
        form = ExamResultForm(request.POST, instance=exam_result)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamResultForm(instance=exam_result)
    return render(request, 'exam_resul_update.html', {'form': form})

def exam_resul_delete(request, pk):
    results=ExamResult.objects.get(pk=pk)
    if request.method =='POST':
        results.delete()
        return redirect('exam_list')
    return render(request,'exam_resul_delete.html',{'results': results})




def exam_resul_search(request):
    query = request.GET.get('q')
    if query:
        results = ExamResult.objects.filter(student__name__icontains=query) |  ExamResult.objects.filter(course__title__icontains=query) | ExamResult.objects.filter(semester__name__icontains=query)
    else:
        results = ExamResult.objects.none()

    return render(request, 'exam_resul_search.html', {'results': results, 'query': query})




def calculate_sgpa(student, semester):
    results = ExamResult.objects.filter(student=student, semester=semester)
    
    # Ensure we get Decimal values, fallback to 0 if None
    total_credits = results.aggregate(total=Sum('course__credit_hours', output_field=DecimalField()))['total'] or Decimal(0)
    
    # Convert the score to a 0-4 scale
    total_points = results.aggregate(points=Sum((F('score') / Decimal(100)) * F('course__credit_hours') * Decimal(4), output_field=DecimalField()))['points'] or Decimal(0)
    
    sgpa = total_points / total_credits if total_credits > 0 else Decimal(0)
    return round(sgpa, 2)

def calculate_ogpa(student):
    results = ExamResult.objects.filter(student=student)
    
    # Ensure we get Decimal values, fallback to 0 if None
    total_credits = results.aggregate(total=Sum('course__credit_hours', output_field=DecimalField()))['total'] or Decimal(0)
    
    # Convert the score to a 0-4 scale
    total_points = results.aggregate(points=Sum((F('score') / Decimal(100)) * F('course__credit_hours') * Decimal(4), output_field=DecimalField()))['points'] or Decimal(0)

    ogpa = total_points / total_credits if total_credits > 0 else Decimal(0)
    return round(ogpa, 2)


def transcript_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    results = ExamResult.objects.filter(student=student).select_related('course', 'semester')
    semesters = Semester.objects.filter(examresult__student=student).distinct()

    transcript_data = []
    for semester in semesters:
        semester_results = results.filter(semester=semester)
        sgpa = calculate_sgpa(student, semester)

        transcript_data.append({
            'semester': semester,
            'results': semester_results,
            'sgpa': sgpa,
        })

    ogpa = calculate_ogpa(student)

    context = {
        'student': student,
        'transcript_data': transcript_data,
        'ogpa': ogpa,
    }
    return render(request, 'transcript_detail.html', context)


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect('home')
    context = {
        'form': form
    }
    return render(request , 'signup.html' , context)

def login_view(request):
    form=AuthenticationForm(request , data=request.POST)
    if form.is_valid():
        user=form.get_user()
        login(request,user)
        return redirect('home')
    return render(request,'loging.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request , 'logout.html')


def dashboard_data(request):
    data = {
        'courses': Course.objects.count(),
        'semesters': Semester.objects.count(),
        'students': Student.objects.count(),
        'departments': department.objects.count(),
        'faculty': Faculty.objects.count(),
        'batches': Batch.objects.count(),
        'exam_results': ExamResult.objects.count(),
    }
    return JsonResponse(data)
     




