from django import forms
from trackingapp.models import Expense, Budget


class ExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    description = forms.CharField(
        label='description',
        widget=forms.Textarea(attrs={'placeholder': 'describe your expense in a few words'})
    )

    class Meta:
        model = Expense
        fields = ['date', 'time', 'category', 'amount', 'description']


class BudgetForm(forms.ModelForm):

    description = forms.CharField(
        label='description',
        widget=forms.Textarea(attrs={'placeholder': 'describe your target in a few words'})
    )

    class Meta:
        model = Budget
        fields = ['name', 'Amount', 'description']

