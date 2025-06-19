from django.urls import path
from . import views
urlpatterns = [
   path('',views.homePage,name='home'),
   path('login/',views.loginPage,name='login'),
   path('register/',views.registerUser,name='register'),
   path('userprofile/',views.userProfile,name='userprofile'),
   path('doctorprofile/',views.doctorProfile,name='doctorprofile'),
   path('adminprofile/',views.adminProfile,name='adminprofile'),
   path('logout/',views.logout,name='logout'),
   path('reschedule/<int:id>/',views.rescheduleAppointment,name='reschedule-appointment'),
   path('cancelappoinment/<int:id>/',views.cancelAppointment,name='cancel-appointment'),
   path('updateprescription/<int:user_id>/<int:app_id>/',views.updatePrescription,name="updatePrescription")
]