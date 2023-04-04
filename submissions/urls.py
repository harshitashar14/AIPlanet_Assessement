from django.urls import path
from .views import EnrolledHackathonView, SubmissionView, GetEnrolledSubmissions

urlpatterns = [
   path('', EnrolledHackathonView.as_view()),
   path('get_all', EnrolledHackathonView.as_view()),
   path('submit',SubmissionView.as_view()),
   path('submission/<int:id>', SubmissionView.as_view()),
   path('all_submission', GetEnrolledSubmissions.as_view())
]