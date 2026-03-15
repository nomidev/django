from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import SafeString

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        self.fields['username'].widget.attrs['placeholder'] = '아이디를 입력하세요'
        self.fields['password1'].widget.attrs['placeholder'] = '비밀번호를 입력하세요'
        self.fields['password2'].widget.attrs['placeholder'] = '비밀번호를 다시 입력하세요'
        self.fields['email'].widget.attrs['placeholder'] = '이메일을 입력하세요'        

        print(self.fields) # OrderedDict([('username', <django.forms.fields.CharField object at 0x7f8c8c8c8c10>), ('password1', <django.forms.fields.CharField object at 0x7f8c8c8c8c40>), ('password2', <django.forms.fields.CharField object at 0x7f8c8c8c8c70>), ('email', <django.forms.fields.EmailField object at 0x7f8c8c8c8ca0>)])

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control mt-1'

    def as_div(self):
        # A basic method override to add a class to the generated <div>
        return SafeString(super().as_div().replace("<div>", "<div class='mb-3'>"))
