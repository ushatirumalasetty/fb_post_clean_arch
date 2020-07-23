from usha.models.reactions import Reaction

from django.db.models import Count

def get_total_reaction_count():
    return Reaction.objects.aggregate(count=Count("reaction"))
