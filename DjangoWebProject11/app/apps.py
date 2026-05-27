from django.shortcuts import render

def index(request):
    context = {
        'company_name': 'ТОВ «TechVision»',
        'slogan': 'Рішення для бізнесу майбутнього',
        'features': [
            'Корпоративні веб-портали',
            'CRM-системи під ключ',
            'Інтеграція з зовнішніми сервісами',
            'Підтримка та супровід 24/7',
        ],
    }
    return render(request, 'app/index.html', context)


def management(request):
    managers = [
        {'name': 'Іван Петренко', 'position': 'Генеральний директор', 'email': 'ivan.petrenko@techvision.com'},
        {'name': 'Олена Коваль', 'position': 'Директор з маркетингу', 'email': 'olena.koval@techvision.com'},
        {'name': 'Максим Іванов', 'position': 'Технічний директор', 'email': 'maksym.ivanov@techvision.com'},
    ]
    return render(request, 'app/management.html', {'managers': managers})


def about(request):
    return render(request, 'app/about.html')


def contacts(request):
    return render(request, 'app/contacts.html')
