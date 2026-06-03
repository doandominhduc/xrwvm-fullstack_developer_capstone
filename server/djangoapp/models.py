from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# 1. Định nghĩa Model CarMake
class CarMake(models.Model):
    name = models.CharField( max_length=100) # Dòng bị lỗi
    description = models.TextField()
    # Bạn có thể thêm trường tùy chọn khác nếu thích (ví dụ: country)
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

# 2. Định nghĩa Model CarModel
class CarModel(models.Model):
    # Thiết lập mối quan hệ Nhiều-đến-Một với CarMake (Một hãng có nhiều dòng xe)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    
    # Dealer ID liên kết sang DB Dealers
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    
    # Giới hạn lựa chọn cho loại xe (Choices)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    
    # Năm sản xuất giới hạn từ 2015 đến nay
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2026),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} - {self.name}"