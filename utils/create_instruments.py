import os
import sys
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

    from home.models import Instrument

    Instrument.objects.all().delete()

    fake = faker.Faker('pt_BR')
    
    categories = [
    "Guitar",
    "Piano",
    "Drums",
    "Violin",
    "Flute",
    "Saxophone",
    "Trumpet",
    "Bass Guitar",
    "Clarinet",
    "Cello",
    "Accordion",
    "Harp",
    "Timpani",
    "Xylophone",
    "Banjo",
    "Mandolin",
    "Oboe",
    "Tuba",
    "Double Bass",
    "French Horn"
]


    django_categories = [Instrument(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(len(categories)):
        category = choice(django_categories)

        django_contacts.append(
            Instrument(
                name=category,
            )
        )

    if len(django_contacts) > 0:
        Instrument.objects.bulk_create(django_contacts)