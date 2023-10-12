from django.db import models

# Create your models here.
class Author(models.Model):
    book = models.OneToOneField('Book', models.DO_NOTHING, primary_key=True)  # The composite primary key (book_id, author_name) found, that is not supported. The first column is selected.
    author_name = models.CharField(max_length=33)

    class Meta:
        managed = True
        db_table = 'author'
        unique_together = (('book', 'author_name'),)

    def __str__(self):
        return self.author_name



class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=33)
    copy_number = models.IntegerField()
    publisher = models.CharField(max_length=33)
    rent_cost = models.IntegerField()
    provider = models.ForeignKey('RentProvider', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'book'





class DeliveryMan(models.Model):
    lp_number = models.CharField(primary_key=True, max_length=7)
    name = models.CharField(max_length=33)
    vehicle_type = models.CharField(max_length=33)
    availability_date = models.DateField()
    phone = models.CharField(max_length=11)
    provider = models.ForeignKey('RentProvider', models.DO_NOTHING)
    provider_address = models.CharField(max_length=80)
    recipient_address = models.CharField(max_length=80)

    class Meta:
        managed = True
        db_table = 'delivery_man'

    



class Payment(models.Model):
    t_id = models.CharField(primary_key=True, max_length=50)
    paid_by = models.ForeignKey('RentTaker', models.DO_NOTHING, db_column='paid_by')
    received_by = models.ForeignKey('RentProvider', models.DO_NOTHING, db_column='received_by')
    amount = models.IntegerField()
    book = models.ForeignKey(Book, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'payment'

    


class RentProvider(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = True
        db_table = 'rent_provider'

    

class RentTaker(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = True
        db_table = 'rent_taker'


class Rents(models.Model):
    rent_taker = models.OneToOneField(RentTaker, models.DO_NOTHING, primary_key=True)  # The composite primary key (rent_taker_id, book_id) found, that is not supported. The first column is selected.
    book = models.ForeignKey(Book, models.DO_NOTHING)
    rent_date = models.DateField()
    rent_end_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'rents'
        unique_together = (('rent_taker', 'book'),)


class User(models.Model):
    nid = models.CharField(primary_key=True, max_length=10)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=80)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=33)
    fname = models.CharField(max_length=33)
    lname = models.CharField(max_length=33)
    age = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'user'
