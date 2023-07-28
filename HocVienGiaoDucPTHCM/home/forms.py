from django import forms
from home.models import BaiViet
from home.models import TaiKhoan
from home.models import NguoiDung
from home.models import KhoaHoc
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(forms.ModelForm):
    class Meta:
        model = NguoiDung
        fields = "__all__"


class TaikhoanForm(forms.ModelForm):
    class Meta:
        model = TaiKhoan
        fields = "__all__"


class LoginForm(forms.ModelForm):
    class Meta:
        model = TaiKhoan
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = BaiViet
        fields = "__all__"


class CoursesForm(forms.ModelForm):
    class Meta:
        model = BaiViet
        fields = "__all__"


class PayForm:
    class Meta:
        model = KhoaHoc
        fields = "__all__"
