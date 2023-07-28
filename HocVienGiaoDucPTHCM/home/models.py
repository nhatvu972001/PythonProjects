from django.db import models


# Create your models here.
class TaiKhoan(models.Model):
    UserID = models.AutoField(primary_key=True)
    Email = models.CharField(max_length=50)
    MatKhau = models.CharField(max_length=20)
    TenND = models.CharField(max_length=50)

    def __str__(self):
        return self.Email

    class Meta:
        db_table = "home_taikhoan"


class NguoiDung(models.Model):
    UserID = models.AutoField
    Email = models.CharField(max_length=50)
    TenND = models.CharField(max_length=50)

    def __str__(self):
        return self.TenND

    class Meta:
        db_table = "home_nguoidung"


class BaiViet(models.Model):
    IDBai = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(TaiKhoan, on_delete=models.CASCADE)
    Email = models.CharField(max_length=50)
    TenND = models.CharField(max_length=50)
    TitleBai = models.CharField(max_length=500)
    ContentBai = models.TextField(max_length=2000)
    Ngay = models.DateTimeField()

    def __str__(self):
        return self.TitleBai

    class Meta:
        db_table = "home_baiviet"


class KhoaHoc(models.Model):
    IDKH = models.AutoField(primary_key=True)
    TenKH = models.CharField(max_length=50)
    GiaKH = models.BinaryField()
    ThoiGian = models.DateTimeField()

    def __str__(self):
        return self.TenKH

    class Meta:
        db_table = "home_khoahoc"
