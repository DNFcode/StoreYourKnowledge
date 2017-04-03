from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
import requests
from bs4 import BeautifulSoup
import itertools
from collections import defaultdict, Counter
import operator

from syk.apps.main.models import MapVertex, MapEdge


class Command(BaseCommand):
    def handle(self, *args, **options):
        keywords = ["javascript", "python", "reactjs", "ajax", "django", "json"]
        ignore = ["php", "angularjs", "html", "css", "css3", "html5"]
        vertexes = MapVertex.objects.filter(title__in=keywords)
        connections_list = [vertex.connections for vertex in vertexes]
        tags_set = set()
        tags_set.update(itertools.chain(*connections_list))

        multipiers = {keyword: 1 for keyword in keywords}
        for vertex in vertexes:
            if vertex.parents:
                if vertex.parents[0] in keywords:
                    multipiers[vertex.title] += 1

        results = defaultdict(int)
        for child in tags_set:
            for parent in keywords:
                if child not in keywords and child not in ignore:
                    try:
                        edge = MapEdge.objects.get(vertexes="{}-{}".format(*sorted([child, parent])))
                        results[child] += edge.hits / MapVertex.objects.get(title=parent).hits * multipiers[parent]
                    except ObjectDoesNotExist:
                        pass

        print(sorted(results.items(), key=operator.itemgetter(1), reverse=True))
        print("!!")
        print(Counter(itertools.chain(*connections_list)))