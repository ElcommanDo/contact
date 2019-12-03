from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    name = forms.CharField(max_length=120,widget=forms.TextInput(
        attrs={"class":"form-control","placeholder":"Enter full name * "}))
    phone = forms.CharField(max_length=120,widget=forms.TextInput(
        attrs={"class":"form-control","placeholder":"Enter your phone  "}))
   
    Email = forms.CharField(max_length=120,widget=forms.EmailInput(
        attrs={"class":"form-control","placeholder":"Enter your Email * "}
    ))
    Msg = forms.CharField(max_length=120,widget=forms.Textarea(
        attrs={"class":"form-control","placeholder":"Your message "}))
    class Meta:
        model = Message
        fields = ('name','phone','Email','Msg')
    def clean_name(self):
        cd = self.cleaned_data
        if len(cd['name'] ) < 8 :
            raise forms.ValidationError("Please Enter our full name ")
        elif any(i.isdigit() for i in cd['name']):
            raise forms.ValidationError("your name mustn`t contain numbers")
        return cd['name']
    def clean_phone(self):
        cd = self.cleaned_data
        if not any(i.isdigit() for i in cd['phone']) or len(cd['phone']) < 11:
            raise forms.ValidationError('Enter Correct Phone number')

        else:
            return cd['phone']
            
