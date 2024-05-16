from django_seed import Seed
from myapp.models import Position, Staff  # Замініть "myapp" на назву вашого додатку

# Створіть екземпляр Seed
seeder = Seed()

# Встановіть генератори даних для моделі Staff
seeder.add_entity(Staff, 5, {
    'position': lambda x: Position.objects.get(positionID=6),  # Отримайте позицію за positionID
    'name': lambda x: seeder.faker.name(),
    'date_of_employment': lambda x: seeder.faker.date_time_this_decade(),
    'salary': lambda x: seeder.faker.random_number(digits=5),
})

# Запустіть генерацію
inserted_pks = seeder.execute()

# Виведіть згенеровані первинні ключі, якщо потрібно
print(inserted_pks)
