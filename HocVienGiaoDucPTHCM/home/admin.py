from django.contrib import admin
from .models import NguoiDung, TaiKhoan, BaiViet, KhoaHoc

# Register your models here.
admin.site.register(NguoiDung)
admin.site.register(TaiKhoan)
admin.site.register(BaiViet)
admin.site.register(KhoaHoc)
