from django.contrib import admin
from django.urls import path,include
from classroom.views import classroom, students, teachers,views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('accounts/profile/', views.profile, name='profile'),
	path('accounts/change_password/', views.change_password, name='change_password'),
    path('admin/', admin.site.urls),
    path('', include('classroom.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)