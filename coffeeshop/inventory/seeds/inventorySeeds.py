from django_seed import Seed

seeder = Seed.seeder()

from inventory.models import CoffeeName
seeder.add_entity(CoffeeName, 10)

inserted_pks = seeder.execute()