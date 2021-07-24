from django.contrib import admin
from django.urls import path, include
from core.views import front_page, sign_up
from job.views import job_detail, add_job, apply_for_job
from django.contrib.auth import views

urlpatterns = [
    path('', front_page, name='front_page'),
    path('sign_up/', sign_up, name='sign_up'),
    path('log_out/', views.LogoutView.as_view(), name='log_out'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('user_profile.urls')),

    path('add_job/', add_job, name='add_job'),
    path('jobs/<int:job_id>', job_detail, name='job_detail'),
    path('<int:job_id>/apply_job/', apply_for_job, name='apply_job'),
]
