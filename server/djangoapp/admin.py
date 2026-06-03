from django.contrib import admin
from .models import CarMake, CarModel

# Cấu hình hiển thị dạng bảng (Inline) cho CarModel ngay trong trang của CarMake
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

# Quản lý giao diện của CarMake trên Admin
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'country']
    inlines = [CarModelInline]

# Quản lý giao diện của CarModel trên Admin
class CarModelAdmin(admin.ModelAdmin):
    fields = ['car_make', 'dealer_id', 'name', 'type', 'year']
    list_display = ['name', 'car_make', 'type', 'year', 'dealer_id']

# Đăng ký chính thức với Admin Site
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)