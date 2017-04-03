import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
import operator

from syk.apps.main.models import MapVertex, MapEdge


class Command(BaseCommand):
    def handle(self, *args, **options):
        pages = 20
        for i in range(1, pages + 1):
            tags_r = requests.get("http://stackoverflow.com/tags?page={}&tab=popular".format(i))
            soup = BeautifulSoup(tags_r.text, "html.parser")
            tags = map(lambda s: s.text, soup.select(".post-tag"))
            amounts = map(lambda s: int(s.text), soup.select(".item-multiplier-count"))
            print(i)

            for tag, amount in zip(tags, amounts):
                theme_r = requests.get("http://stackoverflow.com/questions/tagged/{}".format(tag))
                soup = BeautifulSoup(theme_r.text, "html.parser")
                related_tags = list(map(lambda s: s.text, soup.select(".js-gps-related-tags .post-tag")))
                related_amounts = list(map(lambda s: int(s.text), soup.select(".js-gps-related-tags .item-multiplier-count")))

                parents = filter(lambda p: p[0]/amount >= 0.3, zip(related_amounts, related_tags))

                MapVertex.objects.get_or_create(
                    title=tag,
                    defaults={
                        "hits": amount,
                        "connections": related_tags,
                        "parents": list(map(operator.itemgetter(1), parents)),
                    },
                )

                for related_tag, related_amount in zip(related_tags, related_amounts):
                    MapEdge.objects.get_or_create(
                        vertexes="{}-{}".format(*sorted([tag, related_tag])),
                        defaults={"hits": related_amount},
                    )