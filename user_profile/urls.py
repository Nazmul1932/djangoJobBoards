from django.urls import path
from .views import dashboard, view_application, view_dashboard_jobs


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('job/<int:job_id>/', view_dashboard_jobs, name='view_dashboard_jobs'),
    path('application/<int:application_id>/', view_application, name='view_application'),

]