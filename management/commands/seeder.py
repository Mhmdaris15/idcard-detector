# seeder.py

import random
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password  # Import make_password
from ktp_api.models import CustomUser, IDCard, IDCardMatch

def create_seed_users(num_users=10):
    for _ in range(num_users):
        username = f'user_{random.randint(1, 1000)}'
        email = f'{username}@example.com'
        password = make_password('password123')  # Hash the password
        full_name = f'User {random.randint(1, 100)}'
        date_of_birth = '2000-01-01'  # Example date of birth
        address = '123 Example St, City, Country'  # Example address
        
        user = CustomUser.objects.create(username=username, email=email, password=password,
                                         full_name=full_name, date_of_birth=date_of_birth, address=address)
        create_id_card(user)

def create_id_card(user):
    full_name = user.full_name
    date_of_birth = user.date_of_birth
    nationality = 'Nationality'
    id_number = f'{random.randint(100000, 999999)}-{random.randint(1000, 9999)}'
    issue_date = '2020-01-01'  # Example issue date
    expiry_date = '2030-01-01'  # Example expiry date
    photo_url = 'https://example.com/photo.jpg'  # Example photo URL

    id_card = IDCard.objects.create(user=user, full_name=full_name, date_of_birth=date_of_birth,
                                     nationality=nationality, id_number=id_number,
                                     issue_date=issue_date, expiry_date=expiry_date, photo_url=photo_url)
    create_id_card_match(user, id_card)

def create_id_card_match(user, id_card):
    match_score = random.uniform(0, 1)  # Example match score

    IDCardMatch.objects.create(user=user, id_card=id_card, match_score=match_score)

if __name__ == '__main__':
    create_seed_users()
