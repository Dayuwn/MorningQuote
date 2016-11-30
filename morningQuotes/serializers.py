from morningQuotes.models import MorningQuote
from rest_framework import serializers

class MorningQuoteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MorningQuote
		fields = ('quote', 'author', 'imageURL', 'date')
