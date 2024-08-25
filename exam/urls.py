from django.urls import path
from .views import course_list,course_create,course_detail,course_update,course_delete,course_search
from .views import semester_list,semester_create,semester_update,semester_delete,semester_detail,semster_search
from.views import student_list,student_create,student_update,student_delete,student_search
from .views import faculty_list,faculty_create,faculty_detail,faculty_update,faculty_delete,faculty_search
from .views import dashboard
from .views import batch_list,batch_create,batch_update,butch_delete,butch_search
from .views import exam_resul_create,exam_resul_update,exam_resul_delete,exam_resul_search
from . import views

urlpatterns =[
    
    #course
    
    path('hhhhh',course_list , name='course_list'),
    path('course_create/' ,course_create, name='course_create'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('course/<int:pk>/update/', course_update, name='course_update'),
    path('course/<int:pk>/delete/', course_delete, name='course_delete'),
    path('search/',course_search, name='course_search'),
    path('gg/', dashboard ,name='home'),
    path('dashboard_data/', views.dashboard_data, name='dashboard_data'),

  
    
    
    #semester
    
    path('semester_list/' ,semester_list, name='semester_list' ),
    path('semester_create/' ,semester_create, name='semester_create'),
    path('semester/<int:pk>/update/', semester_update, name='semester_update'),
    path('semester/<int:pk>/delete/', semester_delete, name='semester_delete'),
    path('semesters/<int:pk>/detail/', semester_detail, name='semester_detail'),
    path('semster_search/' ,semster_search, name='semster_search'),
    




    
    
    
    #students
    path('student_list/', student_list , name='student_list'),
    path('student_create/' , student_create, name='student_create'),
    path('students/<int:pk>/update/', student_update, name='student_update'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),
    path('student_search/' ,student_search, name='student_search'),
    
    
    #daptments
    path('dapart/' ,views.dapart_list , name='dapart_list'),
    path('depart_create/' , views.dapart_create, name='depart_create'),
    path('depart/<int:pk>/update/', views.depart_update, name='depart_update'),
    path('depart/<int:pk>/delete/', views.depart_delete, name='depart_delete'),

    




    
    #facultys
    path('faculty_list/' ,faculty_list , name='faculty_list'),
    path('faculty_create/' , faculty_create, name='faculty_create'),
    path('facultys/<int:pk>/detail/', faculty_detail, name='faculty_detail'),
    path('facultys/<int:pk>/update/', faculty_update, name='faculty_update'),
    path('facultys/<int:pk>/delete/', faculty_delete, name='faculty_delete'),
    path('faculty_search/' , faculty_search, name='faculty_search'),
    
    
    
      #batches
    path('batch_list/' ,batch_list , name='batch_list'),
    path('batch_create/' ,batch_create ,name='batch_create'),
    path('butch_update/<int:pk>/update/', batch_update, name='batch_update'),

    path('butchs/<int:pk>/delete/', butch_delete, name='butch_delete'),
    path('butch_search/' ,butch_search, name='butch_search'),
    
    path('exam-results/',views.exam_resul_list, name='exam_list'),
    path('exam_resul_create/' ,exam_resul_create, name='exam_resul_create'),
    path('exam resul/<int:pk>/update/', exam_resul_update, name='exam_resul_update'),
    path('exam resul/<int:pk>/delete/', exam_resul_delete, name='exam_resul_delete'),
    path('exam_result_search/' ,exam_resul_search,name='exam_resul_search' ),

   
    path('<int:student_id>/', views.transcript_detail, name='transcript_detail'),
    
    path('singup/',views.signup ,name='sing_up'),
    path('' , views.login_view , name="login"),
    path('logout/' , views.logout_view , name='logout'),




  
]