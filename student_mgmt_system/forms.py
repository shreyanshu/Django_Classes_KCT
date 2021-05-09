from django import forms
from student_mgmt_system.models import Cordinator

class CordinatorForm(forms.ModelForm):
    class Meta:
        model = Cordinator
        fields = '__all__'
