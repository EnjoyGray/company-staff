import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

from django_seed import Seed
from cstaff.models import Staff

# Створіть екземпляр Seed знову
seeder = Seed.seeder()

# Заповнюємо базу даних
seeder.add_entity(Staff, 50000, {
    'name': lambda x: seeder.faker.name(),
    'salary': lambda x: seeder.faker.random_number(digits=4),
})

# Викликаємо метод execute для створення співробітників
staff = seeder.execute()


print("Staff:", staff)
