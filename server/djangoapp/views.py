# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
# from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# 1. Hàm xử lý Đăng nhập (Login View)
@csrf_exempt
def login_user(request):
    # Lấy username và password từ dữ liệu JSON gửi lên từ React
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    
    # Xác thực thông tin tài khoản dựa trên Django Auth
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    
    if user is not None:
        # Nếu tài khoản hợp lệ, tiến hành thiết lập Session đăng nhập
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)


# 2. THAY THẾ / MỞ KHÓA HÀM LOGOUT THEO YÊU CẦU ĐỀ BÀI TẠI ĐÂY
@csrf_exempt
def logout_request(request):
    logout(request)          # Chấm dứt session làm việc của user trên server
    data = {"userName": ""}  # Trả về chuỗi username rỗng theo đúng định dạng đề bài
    return JsonResponse(data)


# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
# ...

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...