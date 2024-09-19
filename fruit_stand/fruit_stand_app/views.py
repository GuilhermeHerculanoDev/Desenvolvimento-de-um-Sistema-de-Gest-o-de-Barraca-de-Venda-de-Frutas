from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .models import Users
from .models import Fruits
from  .models import Reports

def home(request):
    return render(request, 'home.html')


def screen_login(request):
    return render(request, 'authentication/login.html')


def register(request):
    return render(request, 'authentication/register.html')


def register_sellers(request):
    if request.method == "POST":
        new_name = request.POST.get('name').lower()
        password = request.POST.get('password')

        if Users.objects.filter(name=new_name).exists():
            return render(request, 'authentication/register.html', {'mensseger': "Já existe um vendedor com esse nome"})

        new_sellers = Users(name=new_name, password=make_password(password))
        new_sellers.save()
        return render(request, 'authentication/login.html')
    
    return render(request, 'authentication/register.html')


def login(request):
    if request.method == "POST":
        name_user = request.POST.get('name')
        password = request.POST.get('password')
        try:
            users = Users.objects.get(name=name_user)

            if check_password(password, users.password):
                return render(request, 'sales.html', {'fruits': Fruits.objects.all(), 'name': name_user})
            else:
                return render(request, 'authentication/login.html')

        except Users.DoesNotExist:
            return render(request, 'authentication/login.html', {'menssege': 'Vendedor não encontrado'})
        

def search(request):
    search_name = request.POST.get('search', '')
    search_fresh = request.POST.get('fresh')
    search_classification = request.POST.get('classification')
    search_amount = request.POST.get('amount')
    search_value = request.POST.get('value')

    fruits = Fruits.objects.all()

    if search_name:
        fruits = fruits.filter(name=search_name)
    if search_fresh in ['Sim', 'Não']:
        fruits = fruits.filter(fresh=search_fresh)
    if search_classification:
        fruits = fruits.filter(classification=search_classification)
    if search_amount:
        fruits = fruits.filter(amount=search_amount)
    if search_value:
        fruits = fruits.filter(value=search_value)

    return render(request, 'sales.html', {'fruits': fruits})


def sell(request):
    fruit = request.POST.get('name_fruit')
    name = request.POST.get('name_user')
    return render(request, 'sell.html', {'name_fruit': fruit, 'name': name})


def sell_fruit(request):
    name_fruit = request.POST.get('name_fruit')
    name_user = request.POST.get('name_user')
    discount = request.POST.get('desconto') 
    quantidade_final = request.POST.get('amount')
    
    if not quantidade_final:
        return render(request, 'sell.html', {
            'message': "A quantidade não pode estar vazia", 'name_fruit': name_fruit, 'name': name_user
        })
    
    quantidade_final = int(quantidade_final)

    if quantidade_final <= 0:
        return render(request, 'sales.html', {
            'fruits': Fruits.objects.all(), 'name': name_user, 'name_fruit': name_fruit
        })
    
    sell = Fruits.objects.get(name=name_fruit)
    price = float(sell.value)  
    quantidade_inicial = int(sell.amount)

    if quantidade_final > quantidade_inicial:
        return render(request, 'sell.html', {
            'message': "Não tem essa quantidade de fruta no estoque", 'name_fruit': name_fruit, 'name': name_user
        })
    
    if not discount:  
        final_value = quantidade_final * price
    else:  
        discount = int(discount) 
        final_price = quantidade_final * price
        final_discount = final_price * (discount / 100)
        final_value = final_price - final_discount
        final_value = round(final_value, 2)

    new_amount = quantidade_inicial - quantidade_final
    sell.amount = new_amount
    sell.save()

    if new_amount <= 0:
        delete = Fruits.objects.filter(amount=0)
        delete.delete()
        return render(request, 'sales.html', {'fruits': Fruits.objects.all()})
    
    report = Reports.objects.create(
        user=name_user,
        fruit=name_fruit,
        amount=quantidade_final,
        value=final_value,
    )

    return render(request, 'sales.html', {'fruits': Fruits.objects.all(), 'name': name_user})



def report(request):
    users = request.POST.get('name_user')
    print(users)
    report = {
        'reports': Reports.objects.filter(user = users)
    }
    return render(request, 'report.html', report)


def exit(request):
    return render(request, 'sales.html', {'fruits': Fruits.objects.all()})