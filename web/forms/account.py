from django import forms
from django.core.validators import RegexValidator
from web import models


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label="手机号", validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    password = forms.CharField(label="密码", widget=forms.PasswordInput())
    comfirm_password = forms.CharField(label="重复密码", widget=forms.PasswordInput())
    code = forms.CharField(label="验证码", widget=forms.TextInput())

    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ['username', 'email', 'password', 'comfirm_password', 'mobile_phone', 'code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():  # name是在数据库中的字段名
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = "请输入%s" % (field.label,)
