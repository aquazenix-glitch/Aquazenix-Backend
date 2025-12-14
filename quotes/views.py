from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer

class QuoteSubmissionView(generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
