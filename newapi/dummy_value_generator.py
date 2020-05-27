from app1.models import Users,ActivityPeriod
from faker import Faker
import random
faker = Faker()

for i in range (0,10): 
    a = Users.objects.create(real_name=faker.name(),tz=faker.timezone()) 
    a.save() 
    r = random.randint(0, 5) 
    for i in range (0,r): 
        b = ActivityPeriod(user = a,start_time=faker.date_time(),end_time=faker.date_time()) 
        b.save() 