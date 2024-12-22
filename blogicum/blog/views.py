from django.shortcuts import render

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море <br>
                страшным штормом, потерпел крушение. <br>
                Весь экипаж, кроме меня, утонул; я же, <br>
                несчастный Робинзон Крузо, был выброшен <br>
                полумёртвым на берег этого проклятого острова,<br>
                который назвал островом Отчаяния. <br>'''
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло <br>
                с мели приливом и пригнало гораздо ближе к берегу. <br>
                Это подало мне надежду, что, когда ветер стихнет, <br>
                мне удастся добраться до корабля и запастись едой и <br>
                другими необходимыми вещами. Я немного приободрился, <br>
                хотя печаль о погибших товарищах не покидала меня. <br>
                Мне всё думалось, что, останься мы на корабле, мы <br>
                непременно спаслись бы. Теперь из его обломков мы могли бы <br>
                построить баркас, на котором и выбрались бы из этого<br>
                гиблого места. <br>''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный <br>
                порывистый ветер. 25 октября.  Корабль за ночь разбило <br>
                в щепки; на том месте, где он стоял, торчат какие-то <br>
                жалкие обломки,  да и те видны только во время отлива. <br>
                Весь этот день я хлопотал  около вещей: укрывал и <br>
                укутывал их, чтобы не испортились от дождя. <br>''',
    },
]


def index(request):
    context = {'posts': posts[::-1]}
    return render(request, 'blog/index.html', context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    context = {'post': posts[pk]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    return render(request, template,{'category_slug': category_slug})
