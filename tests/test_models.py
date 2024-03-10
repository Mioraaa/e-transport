

import pytest
from django.db import IntegrityError
from django.utils import timezone
import uuid

from common.models import CustomUser, Destination, Customer, Message, Bagages,\
    Driver, Car


class TestDestinationModel:

    @pytest.mark.django_db
    def test_create_destination(self):
        id = 'ABC123'
        start_in = 'CityA'
        end_in = 'CityB'
        start_at = timezone.now()
        costs = 50.00
        
        Destination.objects.create(
            id=id,
            start_in=start_in,
            end_in=end_in,
            start_at=start_at,
            costs=costs,
        )
    
        assert Destination.objects.count() == 1


class TestMessageModel:
    
    @pytest.mark.django_db
    def test_create_message(self):
        user_name = 'Same'
        user_contact =  21545
        message_content = 'Hello world'

        Message.objects.create(
            name=user_name,
            contact=user_contact,
            message_content=message_content,
        )
        
        assert Message.objects.count() == 1
    
    @pytest.mark.django_db
    def test_invalid_message(self):
        with pytest.raises(IntegrityError):
            Message.objects.create(
                name='Same',
                contact=545,
            )
            
            
class TestCustomerModel:
    
    @pytest.fixture
    def destination(self) -> Destination:
        return Destination.objects.create(
            id = 'Id1',
        )

    @pytest.fixture
    def message(self) -> Message:
        return Message.objects.create(
            name='Same',
            contact=251,
            message_content='message_content',
        )
    
    @pytest.mark.django_db
    def test_create_costumer(self, destination, message):
        contact_one = 14887
        contact_two = 58966
        
        Customer.objects.create(
            first_phone_number=contact_one,
            second_phone_number=contact_two,
            customer_name='Same',
            destination=destination,
            messages=message
        )
        
        assert Customer.objects.count() == 1
        
   
    @pytest.mark.django_db
    def test_invalid_costumer(self):
        with pytest.raises(IntegrityError):
            Customer.objects.create(
                first_phone_number=58966,
                second_phone_number=58966,
            )
            

class TestBagagesModel:
    
    @pytest.fixture
    def destination(self) -> Destination:
        return Destination.objects.create(
            id = 'Id1',
        )
    
    @pytest.fixture
    def customer(self, destination) -> Customer:
        return Customer.objects.create(
            first_phone_number=256,
            second_phone_number=587,
            destination=destination
        )
        
    @pytest.mark.django_db
    def test_create_bagage(self, customer):
        Bagages.objects.create(
            id=uuid.uuid4(),
            customer=customer
        )
    
        assert Bagages.objects.count() == 1
    
    @pytest.mark.django_db
    def test_invalid_bagage(self):
        with pytest.raises(IntegrityError):
            Bagages.objects.create(
                id=uuid.uuid4()
            )
            
            
class TestCarModel:
    
    @pytest.fixture
    def driver(self) -> Driver:
        return Driver.objects.create(
            id='Same45'
        )
    
    @pytest.fixture
    def destination(self) -> Destination:
        return Destination.objects.create(
            id = 'Id1',
        )
    
    @pytest.mark.django_db
    def test_create_car(self, destination, driver):
        Car.objects.create(
            driver=driver,
            destination=destination
        )
        
        assert Car.objects.count() == 1
        
    @pytest.mark.django_db
    def test_invalid_car(self):
        with pytest.raises(IntegrityError):
            Car.objects.create(
                id='Same45',
                driver='Same'
            )