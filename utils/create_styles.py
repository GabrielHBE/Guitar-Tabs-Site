import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent


sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from home.models import Style

    Style.objects.all().delete()

    fake = faker.Faker('pt_BR')
    
    categories = [ "Rock", 
                  "Pop", 
                  "Hip Hop", 
                  "Jazz", 
                  "Blues", 
                  "Classical", 
                  "Reggae", 
                  "Country", 
                  "Electronic", 
                  "Funk", 
                  "Soul", 
                  "R&B", 
                  "Metal", 
                  "Punk",
                  "Latin", 
                  "Reggaeton", 
                  "Disco", 
                  "Folk", 
                  "Gospel", 
                  "Opera" ]

    django_categories = [Style(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(len(categories)):
        category = choice(django_categories)

        django_contacts.append(
            Style(
                name=category,
            )
        )

    if len(django_contacts) > 0:
        Style.objects.bulk_create(django_contacts)