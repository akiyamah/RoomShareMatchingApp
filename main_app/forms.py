from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile, UserPurpose, UserDesiredCohabitee, UserRoomLayout, UserRent
from matching.constants.choices import (
    PURPOSE_CHOICES, DESIRED_COHABITEE_CHOICES, LAYOUT_CHOICES, RENT_CHOICES,
    GENDER_CHOICES, OCCUPATION_CHOICES, PREFECTURE_CHOICES, SMOKING_CHOICES,
    PET_CHOICES, PARKING_CHOICES, COMMUTE_TIME_CHOICES, PERIOD_CHOICES
)


class UserUpdateForm(UserChangeForm):
    password = None  # パスワード変更を無効化
    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="新しいパスワード"
    )
    password_confirm = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="新しいパスワードの確認"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'new_password', 'password_confirm']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        password_confirm = cleaned_data.get("password_confirm")

        if new_password != password_confirm:
            self.add_error("password_confirm", "パスワードが一致しません")




class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = [
            'user_name', 
            'profile_image', 
            'sex', 
            'day_of_birth', 
            'profession', 
            'prefecture', 
            'period', 
            'is_smoker', 
            'has_pets', 
            'parking', 
            'self_introduction',
        ]
        labels = {
            'user_name': 'あなたの使用するネームを記入してください',
            'profile_image': 'プロフィール画像を選択してください',
            'sex': '性別を選択してください',
            'day_of_birth': '生年月日を入力してください',
            'profession': '職業を入力してください',
            'prefecture': 'お住まいの都道府県を選択してください',
            'period': '希望する入居期間を選択してください',
            'is_smoker': '喫煙者ですか？',
            'has_pets': 'ペットを飼っていますか？',
            'parking': '駐車場は必要ですか？',
            'self_introduction': '自己紹介を記入してください',
        }
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}), 
            'sex': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}), 
            'day_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}), 
            'prefecture': forms.Select(choices=PREFECTURE_CHOICES, attrs={'class': 'form-control'}), 
            'period': forms.Select(choices=PERIOD_CHOICES, attrs={'class': 'form-control'}), 
            'is_smoker': forms.Select(choices=SMOKING_CHOICES, attrs={'class': 'form-control'}), 
            'has_pets': forms.Select(choices=PET_CHOICES, attrs={'class': 'form-control'}), 
            'parking': forms.Select(choices=PARKING_CHOICES, attrs={'class': 'form-control'}), 
            'self_introduction': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UserPurposeForm(forms.ModelForm):
    purpose_name = forms.MultipleChoiceField(
        choices=PURPOSE_CHOICES, 
        label='あなたのルームシェアの目的は何ですか？', 
        widget=forms.CheckboxSelectMultiple(),
    )
    class Meta:
        model = UserPurpose
        fields = ['purpose_name']
        widgets = {
            'user': forms.HiddenInput(),
        }

class UserDesiredCohabiteeForm(forms.ModelForm):
    cohabitation_number = forms.MultipleChoiceField(
        choices=DESIRED_COHABITEE_CHOICES, 
        label='希望する同居人数は何人ですか？', 
        widget=forms.CheckboxSelectMultiple(),
    )
    class Meta:
        model = UserDesiredCohabitee
        fields = ['cohabitation_number']
        widgets = {
            'user': forms.HiddenInput(),
        }

class UserRoomLayoutForm(forms.ModelForm):
    layout = forms.MultipleChoiceField(
        choices=LAYOUT_CHOICES, 
        label='希望する部屋の間取りは何ですか？', 
        widget=forms.CheckboxSelectMultiple()
    )
    class Meta:
        model = UserRoomLayout
        fields = ['layout']
        widgets = {
            'user': forms.HiddenInput(),
        }

class UserRentForm(forms.ModelForm):
    rent = forms.MultipleChoiceField(
        choices=RENT_CHOICES, 
        label='希望する家賃はいくらですか？', 
        widget=forms.CheckboxSelectMultiple(),
    )
    class Meta:
        model = UserRent
        fields = ['rent']
        widgets = {
            'user': forms.HiddenInput(),
        }


from .models import Profile, Prefecture

class ProfileForm(forms.ModelForm):
    current_prefecture = forms.ModelChoiceField(queryset=Prefecture.objects.all())
    favorite_prefectures = forms.ModelMultipleChoiceField(queryset=Prefecture.objects.all(), required=False)
    
    class Meta:
        model = Profile
        fields = ['current_prefecture', 'favorite_prefectures']
