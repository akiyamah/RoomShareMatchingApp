from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from matching_app.models import RoommatePreference
from django.conf import settings
import os


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', default='')
    sex = models.CharField(max_length=10, blank=True, null=True)
    day_of_birth = models.DateField(blank=True, null=True)

    @property
    def age(self):
        if self.day_of_birth:
            today = date.today()
            age = today.year - self.day_of_birth.year - ((today.month, today.day) < (self.day_of_birth.month, self.day_of_birth.day))
            return age
        return None

    profession = models.CharField(max_length=50, blank=True, null=True)
    prefecture = models.CharField(max_length=10, blank=True, null=True)
    period = models.CharField(max_length=10, blank=True, null=True)
    is_smoker = models.CharField(max_length=10, blank=True, null=True)
    has_pets = models.CharField(max_length=10, blank=True, null=True)
    parking = models.CharField(max_length=10, blank=True, null=True)
    self_introduction = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # saveメソッドのオーバーライド
        if not self.user_name:
            self.user_name = self.user.username
        if not self.profile_image:
            self.profile_image = UserProfile.default_profile_image_path()
        super(UserProfile, self).save(*args, **kwargs)

    @classmethod
    def default_profile_image_path(cls):
        return os.path.join('default_images', 'default_profile.jpg')


class UserPurpose(models.Model):
    # ユーザーのルームシェア目的情報を管理するモデル。
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_purpose')
    purpose_name = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.purpose_name


class UserDesiredCohabitee(models.Model):
    # ユーザーの希望する同居人数を管理するモデル。
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_desired_cohabitee')
    cohabitation_number = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.cohabitation_number


class UserRoomLayout(models.Model):
    # ユーザーの希望する部屋の間取りを管理するモデル。
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_room_layout')
    layout = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.layout


class UserRent(models.Model):
    # ユーザーの希望する家賃を管理するモデル。
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rent')
    rent = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.rent




class Prefecture(models.Model):
    #都道府県モデル
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_prefecture = models.ForeignKey(Prefecture, related_name='current_users', on_delete=models.SET_NULL, null=True)
    favorite_prefectures = models.ManyToManyField(Prefecture, related_name='favorited_by_users', blank=True)
    
    def __str__(self):
        return self.user.username

