from django import forms
from testapp.models import *

class enquiry_form(forms.Form):
    name=forms.CharField()
    phone=forms.CharField()
    email=forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class SM_upload_form(forms.ModelForm):
    class Meta:
        model=SM_upload
        fields='__all__'

class Rlink_upload_form(forms.ModelForm):
    class Meta:
        model=Rlink_upload
        fields='__all__'

class RV_upload_form(forms.ModelForm):
    class Meta:
        model=RV_upload
        fields='__all__'
#Assignment submission
class Assignment_form(forms.Form):
    aid=forms.IntegerField()

class Assignment_form1(forms.Form):
    id=forms.IntegerField()
    class Meta:
        fields='__all__'

class Assignment_submission_form(forms.ModelForm):

    class Meta:
        model=Assignment_submission
        fields='__all__'
        widgets = {'assignment':forms.HiddenInput(),'student_name':forms.HiddenInput()}
#Assignment report query form1


class Assignment_report_query_form(forms.Form):
    CHOICES = ( ('submitted', 'submitted'),('NotSubmit', 'NotSubmit'))
    report_choice_field = forms.ChoiceField(label='select which report type (submitted, Notsubmit)?',choices=CHOICES)
