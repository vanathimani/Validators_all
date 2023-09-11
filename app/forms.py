from typing import Any
from django import forms

def Check_for_s(value):

    if value[0]=='s':
        raise forms.ValidationError('start withs s not allowed')


def Check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('name less then 5 character')


class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100, validators=[Check_for_s, Check_for_len])
    Sage=forms.IntegerField()
    Sid=forms.IntegerField()
    Semail=forms.EmailField()
    Sreemail=forms.EmailField()
    Botcatcher=forms.CharField(max_length=10,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['Semail']
        r=self.cleaned_data['Sreemail']
        
        if e!=r:
            raise forms.ValidationError('Email not matching')
    
    def clean_botcatchert(self):
        bot=self.cleaned_data['Botcatcher']

        if len(bot)>0:
            raise forms.ValidationError('bot')


