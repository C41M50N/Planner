from models import db, Assignment
from faker import Faker
import random

#fake = Factory.create()
fake = Faker()
classes = ['Advanced Math','Anderson Bible', 'Carpenter Bible', 'Rainear Bible', 'AP History', 'AP Psych', 'Chemistry', 'Smart English', 'Dumb English', 'Coding I', 'Forensic Science', 'American Sign Language', 'ELS Prepworks', 'Class Party']
# Spanish
#fake = Factory.create('es_ES')
# Reload tables
db.drop_all()
db.create_all()
# Make 100 fake contacts
for num in range(10):
    randInfo = fake.text()
    randInfoPrime = randInfo[:20]
    randClass = random.choice(classes)
    randDate = fake.date_between(start_date='-30y', end_date='+30y')
    # Save in database
    my_contact = Assignment(assignmtInfo=randInfoPrime, assignmtClass=randClass, assignmtDate=randDate)
    db.session.add(my_contact)

db.session.commit()
