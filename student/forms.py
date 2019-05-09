from django import forms

from student.models import Student


class StudentForm(forms.ModelForm):
    # def clean_qq(self):
    #     cleaned_data = self.cleaned_data['qq']
    #     if not cleaned_data.isdigit():
    #         raise forms.ValidationError('must be number！')

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession', 'email', 'qq', 'phone'
        )
