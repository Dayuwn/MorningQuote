from django.core.management.base import BaseCommand, CommandError
from morningQuotes.models import MorningQuote
import json
import random


def read_quotes(filename):
	with open(filename) as f:
		lines = (l.strip() for l in f)
		return [json.loads(l) for l in lines if l]

def get_random_quote():
	quotes = read_quotes('./quotes.json')
	quote = random.choice(quotes)
	return (quote[0], quote[1])

class Command(BaseCommand):
	args = '<>'
	help = 'Updates the quote, runs everyday.'

	def handle(self, *args, **options):
		quote, author = get_random_quote()
		MorningQuote.objects.all().delete()
		quoteobj = MorningQuote(quote= quote, author=author, imageURL="www.google.com")
		quoteobj.save()