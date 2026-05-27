from django.views import View
from django.shortcuts import render
from datetime import date

class NewsListView(View):
    def get(self, request):
        news_list = [
            {
                'title': 'Запуск нової платформи для малого бізнесу',
                'date': date(2026, 5, 10),
                'summary': 'Ми представили хмарне рішення для автоматизації продажів та обліку.',
            },
            {
                'title': 'TechVision стала партнером міжнародної конференції',
                'date': date(2026, 4, 22),
                'summary': 'Компанія виступила спонсором конференції з цифрової трансформації бізнесу.',
            },
            {
                'title': 'Відкриття нового офісу у Львові',
                'date': date(2026, 3, 5),
                'summary': 'Розширюємо присутність в регіонах для кращої підтримки клієнтів.',
            },
        ]
        return render(request, 'news/news_list.html', {'news_list': news_list})
