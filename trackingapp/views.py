from django.shortcuts import render, redirect
from trackingapp.forms import ExpenseForm, BudgetForm
from trackingapp.models import Expense, Budget
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


# code for index page
def index(request):
    return render(request, 'index.html')


# code for sign up page
def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            form.save()
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)

            return redirect('manage')
    return render(request, 'registration/register.html', {'form': form})


# code for addexpense page
@login_required
def addexpense(request):
    expense = Expense.objects.all().order_by('-date')[:5]
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user = request.user
            exp.save()
            return redirect('addexpense')
    else:
        form = ExpenseForm()
    return render(request, 'addexpense.html', {'form': form, 'expense': expense})



@login_required
# code for manageexpense page
def manage(request):
    expense = Expense.objects.all().order_by('-date')
    return render(request, 'manageexpenses.html', {'expense': expense})

@login_required
def Edit(request, pk):
    obj = Expense.objects.get(id=pk)
    form = ExpenseForm(instance=obj)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('manage')

    return render(request, 'editexpense.html', {'form': form})

@login_required
def Delete(request, pk):
    obj = Expense.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('manage')

    return render(request, 'deleteexpense.html')


# code for addbudget page
@login_required
def addbudget(request):
    budget = Budget.objects.all().order_by('-id')
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addbudget')
    else:
        form = BudgetForm()
    return render(request, 'addbudget.html', {'form': form, 'budget': budget})

@login_required
def Editbudget(request, pk):
    obj = Budget.objects.get(id=pk)
    form = BudgetForm(instance=obj)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('addbudget')

    return render(request, 'edit budget.html', {'form': form})

@login_required
def Deletebudget(request, pk):
    obj = Budget.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('addbudget')

    return render(request, 'deletebudget.html')

