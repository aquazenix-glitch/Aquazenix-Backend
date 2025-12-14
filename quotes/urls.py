from django.urls import path
from .views import QuoteSubmissionView

urlpatterns = [
    path('submit-quote/', QuoteSubmissionView.as_view(), name='submit-quote'),
]
