from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from morningQuotes.models import MorningQuote
from morningQuotes.serializers import MorningQuoteSerializer

# Views
class MorningQuoteViewSet(viewsets.ModelViewSet):
	queryset = MorningQuote.objects.all().values()
	serializer_class = MorningQuoteSerializer
