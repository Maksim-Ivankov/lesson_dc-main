import flet as ft
from assets.variable import *
# 1 урок html
html_1 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Добро пожаловать на курс старшего программирования! Вначале будет просто, будет казаться, что ты гений прогарммирования, потом будет невероятно сложно и захочется бросить, и вот потом, если продолжить несмотря ни на что - у тебя получится и ты станешь программистом. Удачи!'),width=700),
        ft.Container(ft.Text('Почему WEB? Потому что это просто, несмотря на то, что программирование - сложная штука. Важно сделать первый шаг, чтобы хоть что-то начало получаться. Идеальная точка входа здесь - это сайты. Рекорд ученика - пробежал html и css за 2 месяца. Вам желаем того же. HTML и CSS строго говоря - даже не языкы программирования. Это язык гипертекстовой разметки и каскадная таблица стилей. Первый язык программирования на вашем пути - это Java Script. Сложность начнется там, а до этого вы уже научитесь верстать сайты. От простого к сложному.'),width=700),
        ft.Container(ft.Text('Хватит болтовни, начинаем. На заняия удобнее ходить со своим ноутбуком (если есть), или как минимум с флешкой, на которую будете сохранять данные. На общих компах хранить не до конца безопасно. Есть жулики, которые могут "случайно" удалить'),width=700),
        ft.Container(ft.Text('Создаем папку на рабочем столе, называем своей именем и фамилией. Правой кнопкой мыши по папке - открыть с помомощью VScode. Vscode - это редактор кода. Код можно писать хоть в блокноте, но в редакторе - удобнее. Есть подсветка кода и много других фишек. Слева в директории правой кнопкой мыши - создать файл, имя - 1.html. Далее в зоне кода - вводим ! и нажимаем enter'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/1.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Теперь зайди в папку и открой свой файл. Увидел? Он открылся в браузере. Винда уже понимает, что файлы с расширением .html - это сайты, и открывать их нужно в браузере. Теперь найди в коде <title></title> и между ними введи что-нибудь. Например, <title>Чебурек</title>. ернись в браузер и обнови страницу своего сайта. Что нибудь изменилось? Да! Название вкладки изменилось на то, что ты написал. Как это работает?'),width=700),
        ft.Container(ft.Text('Какие-то слова внутри <> называются теги. С помощью тегов мы говорим с браузером. Программирование - это общение. Не зря есть языки программирования. Это как языки в реальной жизни. Чтобы говорить с китайцем, нужно знать язык - китайский. А чтобы говорить с бразуром, нужно занть язык - html. Просто, не правда ли? Каждая часть системы говорит на своем языке. Например, айфоны говорят на языке Swift, андроиды - на Котлине, большая часть винды - на языке C.'),width=700),
        ft.Container(ft.Text('Каждый тег что-то говорит браузреу. Разберем, что.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Когда мы ввели ! и нажали enter - мы раскрыли сниппет. Это подсказки от VSCode, чтобы не писать часто используемые конструкции кода самостоятельно каждый раз. Абсолютно каждая страница в интернете включает в себя базу - код, который изображен выше. Можете сами проверить - в браузере перейдите на любой сайт, в пустом месте правой кнопкой мыши - просмотреть код страницы.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/3.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Да, код яндекс музыки может выглядеть пугающе, или даже уродски, но это потому, что его сгенерировал фреймворк, в котором работали люди. Что-это такое, разберем позже. Через пол годика) Но даже в таком коде вы увидите уже знакомые теги - html, head, body.'),width=700),
        ft.Container(ft.Text('Пойдём дальше. Внутри тега body пишется видимая часть сайта. Напишите там любой текст, зайдите в браузер и обновите страницу с сайтом.'),width=700),
        ft.Container(ft.Text('Текст появился нас странице? Прекрасно! Теперь попробуйте поместить введенный текст внутрь тега h1. Должно получиться так - <h1>Текст</h1>. Затем перейдите в браузер и обновите страницу. Текст стал большим и жирным?'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/4.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('В структуре сайта html отвечает за скелет сайта. С помощью html добавляется текст и картинки. Никакого дизайна. За дизайн и красоту будет отвечать CSS. Следующие 6 уроков ты будешь учиться работать с разными тегами в html. Их не так много. На самом деле весь html можно пройти часов за 6. Время прохождения зависит только от того, насколько ты будешщь тормозить в процессе.'),width=700),
        ft.Container(ft.Text('Как будет выглядеть обучение дальше? Я даю тебе картинку сайта. Тебе нужно написать код по этой картинке. Чтобы сайт выглядел так же. Начнем? Вот первый сайт, который ты должен сделать.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/5.png',width=700),margin=ft.margin.only(left=0)),
        
        ft.Container(ft.Text('Сайт можно открыть по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_1.html',selectable=True),width=700),
        ft.Container(ft.Text('Для написания сайта нужно узнать о нескольких тегах.'),width=700),
        ft.Container(ft.Text('Теги h1 - h6. Это заголовки. h1 - лавный закголовок и самый большой и жирный. h6 - самый маленький заголовок. Попробуйте подобавлять внутрь текст и посмотрите, как он отобразится'),width=700),
        ft.Container(ft.Text('Тег p - абзац. Если напсиать текст на разных строках, он по умолчанию выведется на одной. Браузеру нужно явно сказать, что это абзац - его с новой строки.'),width=700),
        ft.Container(ft.Text('Помимо тегов, которые уже что-то делают, у них могут быть персональные настройки - атрибуты. Пишутся они так - <p align="center">Текст</p>'),width=700),
        ft.Container(ft.Text('Внтруи открывающего тега, после названия тега. В данном случае align - выровнять, center - по центру. Так же можно выровнять по левому краю (left) и по правому краю (right)'),width=700),
        ft.Container(ft.Text('Сайт пиши сверху вниз, строка за строкой Удачи!'),width=700,margin=ft.margin.only(bottom=40)),
    ])
)
# 2 урок html
html_2 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('На втором уроке научимся работать со списками.'),width=700),
        ft.Container(ft.Text('Списки бывают 3-х типов - нумерованные, ненумерованные, списки с описанием.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/15.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт, который нужно сделать весьма прост. Создайте новый файл, назовите его 2.html и вперед!'),width=700),
        ft.Container(ft.Text('Сайт доступен по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_2.html',selectable=True),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/6.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 3 урок html
html_3 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Сегодня научимся работать с картинками. Добавлять их на страницу, изменять размер, позиционировать'),width=700),
        ft.Container(ft.Text('Для добавления картинки на страницу, используем тег img. Он одинарный! Закрывающего тега, как у большинства у него нет. <img>'),width=700),
        ft.Container(ft.Text('У тега img есть множество атрибутов. Основной - src (путь). Так же атрибутами можно задать ширину (weight) и высоту (height) изображения'),width=700),
        ft.Container(ft.Text('Путь указывается относительный (относительно файла в котором сейчас работаем), либо абсолютный (от корня операционки). Относительные пути предбпочитительнее, т.к. при занрузке сайта на сервер, корневые каталоги могут измениться, картинки не будут найдены. С относительным путём проблем нет практически никогда.'),width=700),
        ft.Container(ft.Text('Предположим, что картинка находится в папке img, называется - 1.png, на уровне вместе с папкой img находится файл 3.html. Тогда относительный путь будет иметь вид - url="src/pages/content/web_page/img/1.png"'),width=700),
        ft.Container(ft.Text('А весь тег получится таким - <img src="src/pages/content/web_page/img/1.png",width=400,height=400>'),width=700),
        ft.Container(ft.Text('Попробуй добавить какую-нибудь картинку на сайт.'),width=700),
        ft.Container(ft.Text('Кстати, сайт к этому уроку будет выглядет так:'),width=700),
        ft.Container(ft.Text('Поулчить сайт по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_3.html',selectable=True),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/7.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Единственный вопрос, который осталось решить - как сделать так, чтобы картинки стояли вокруг текста слева и справа? Для этого используй атрибут выравнивание - align. ПРикол с ним в том, что когда, например картенке прописываешь align="right", то контент, который следует после в коде, будет огибать картинку справа. '),width=700),
        ft.Container(ft.Text('Мы коснулись блочных и строчных элементов. Текст - это блочный элемент. Даже если в теге <p> написать одно слово, это слово займет всю ширину строки, и не позволит другому тексту или картинкам заскочить на свою строку. Align меняет это поведение, и делает блочный элемент - строчным. Строчные элементы занимают ровно столько места, сколько для них выделено.'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 4 урок html
html_4 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В 4-ом сайте научимся переходить на другие страницы. Раньше весь сайт у нас состоял из одной страницы. В реальность у сайтов могут быть десятки, а то и сотни страниц, которые связаны между собой ссылками.'),width=700),
        ft.Container(ft.Text('В четвертом сайте будет три страницы - 3 отдельных файла html, каждый из которых будет содержать ссылку на соседний. Создайте папку с названием - 4 сайт (или как-то так) и создайте в ней три файла. (например, 4_1.html,4_2.html,4_3.html)'),width=700),
        ft.Container(ft.Text('За ссылки в html отвечает тег <a>. Атрибут href показывает, куда ссылка должна перевести.'),width=700),
        ft.Container(ft.Text('Так <a href="yandex.ru">Нажми на меня</a> создаст текст/ссылку - нажми на меня, при клике по которой тебя перебросит на сайт яндекса.'),width=700),
        ft.Container(ft.Text('Чтобы сделать многостраничный сайт, ножно прописать относительные ссылки на соседние файлы (по тому же принципу, что и в картинках)'),width=700),
        ft.Container(ft.Text('Вот вся информация, что тебе нужна. В остальном - ничего нового.'),width=700),
        ft.Container(ft.Text('Сайт получишь по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_4.html',selectable=True),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/8.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/9.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/10.png',width=700),margin=ft.margin.only(bottom=40)),
    ])
)
# 5 урок html
html_5 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('5 сайт - это работа с таблицами. В реальности таблицы на html ты, наверное, никогда писать не будешь, однако они закладывают способ мышления, который нужно усвоить.'),width=700),
        ft.Container(ft.Text('Таблицы состоят из строк, внутри которых находятся ячейки. Это принцип многих интерфейсов.'),width=700),
        ft.Container(ft.Text('Таблицу создает тег <table></table>. Но сам по сибе он не даст ничего, ведь в нем нет строк и ячеек.'),width=700),
        ft.Container(ft.Text('Строку создает тег <tr></tr>, ячейку - тек <td></td>'),width=700),
        ft.Container(ft.Text('Вставь к себе на сайт следующий код - <table><tr><td>1</td><td>2</td><td>3</td></tr></table> и посмотри, что получится. А теперь внтурь тега table добавь атрибут border="1". У таблицы появится рамка и станет чуть понятнее, что происходит'),width=700),
        ft.Container(ft.Text('Теперь ты знаешь, как создавать строки и ячейки. Если присмотреться к таблице, то некоторые ячейки объеденены - две в одну. Это делаетс с помощью атрибута colspan="2" или rowspan="2" внутри td. Эти атрибуты объединяют 2 ячейки по горизонтали или вертикали.>'),width=700),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_7.html',selectable=True),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/11.png',width=700),margin=ft.margin.only(left=0)),
    ])
)
# 6 урок html
html_6 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Поздравляю! Ты в выпусконом проекте HTML. Надеюсь, что предидущие 5 уроков пролетели для тебя незаметно.'),width=700),
        ft.Container(ft.Text('Здесь нужно собрать сайт вк на чистом html, состоящий из 3-х страниц.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/12.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/13.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/14.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Подсказка будет всего одна, связанная со структурой страницы. Как сделать такую структуру? С помощью таблицы! Не зря же мы их проходили. Сейчас сайты на таблицах уже ни кто не строит, но лет 20 назад только так и делали, css еще не был настолько развит, а на таблицах неплохо писалась адаптивная структура'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/html/16.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Вся первая страница - это таблица, состоящая из 1 строки и 3 ячеек. В первой ячейке - меню. Так вот меню - это тоже таблица. Таблица 2х8. Получается таблица в таблице. Когда будет много и важно в нем не запутаться. На то это и выпускной проект HTML. Удачи!'),width=700),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_8.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 1 урок css
css_1 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Поздравляю! Ты изучил HTML и переходишь к CSS. CSS отвечает за дизайн страницы. Научимся же делать красиво) Код CSS пишется в отдельном файле - style.css. Первым делом нам нужно связать страницу HTML и CSS. Для этого в head HTML страницы подключаем внешний файл с помощью: < link rel="stylesheet" href="style.css" type="text/css"> CSS работает по следующему принципу: тег{Свйоство1; Свойство2; Свойство3;} Например: p{color:red;} - покрсит весь текст, находящийся в p в красный цвет. В конце каждого свойства нужно ставить точку с запятой. Так мы показываем браузеру конец строки. А как быть если мы не хотим красить все теги p в красный, а, например только один? Для этого нужно тегу p даём идентификатор: <p id="text1"> В css: #text1{color:green;} - покарсит текст тега с id="text1" в зелёный цвет. Не может быть два тега с одним id. Чтобы покрасить несколько тегов p в один цвет, используем класс: <p class="text2">. В CSS к классу обращаемся через точку: .text2{color:black;}'),width=700),
        ft.Container(ft.Text('КОРОЧЕ - просто позови учителя, он покажет, как работает css за 5 минут и начнешь делать уроки'),width=700),
        ft.Container(ft.Text('А ниже сайт, который нужно сделать.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/1.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_1.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 2 урок css
css_2 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Разберёмся, что такое блочные и встроенные элементы. Блочные - занимают всю строку, а встроенные, только то место, которое под них выделенно. Что это значит? Сделайте тег p с небольшим текстом и дайте ему рамку через CSS. Рамка задаётся свойством: border:1px solid black; где 1px - толщина рамки, solid - тип рамки, здесь - сплошная, black - цвет рамки. Вы увидите, что рамка идёт не вокруг текста, а растянута во всю ширину экрана. Она идёт даже там, где нет текста. Это и называется блочный элемент. А что же тогда встроенный элемент? Встроенный элемент, это, например тег span. Напишите такую конструкцию: <span>Текст</span> Далее дайти тегу span id, и в CSS пропишите рамку. Вы увидите, что рамка идёт только вокруг текста. Это и есть встроенный элемент. Чтобы вместо маркера списка поставить картинку, используем свойство CSS: list-style-image: url(img.png);'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_2.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 3 урок css
css_3 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В уроке про таблицы HTML я говорил, что ранее таблицы использовались для разметки страницы, но сменились свойствами CSS и тегом DIV. Так вот пора с ним познакомиться. Что же такое DIV? С его братаном - тегом span вы уж езнакомы. Теги DIV и SPAN - это невидимые коробочки, внутрь которых можно положить что угодно, и через CSS задать этим коробочкам любой размер и положение на странице. Синтаксис: <div id="box1"><p>Текст></p><img></div> В css: #box1{width:200px;height:200px;border:1px solid black;margin-top:50px;margin-left:100px;} Получим квадрат 200х200 пикселей с чёрной рамкой, внутри которого лежит текст и картинка. Квадрат находится на расстоянии 50 пикселей от верхнего края и 100 пикселей от левого края.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/3.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_3.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 4 урок css
css_4 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В данном сайте новых блоков особо нет. Единственное, что нужно знать - это то, что тегам можно давать блочные и встроенные свойства напрямую через CSS Для этого в css для выбранного тега прописываем свойство: display:block; - чтобы сделать элемент блочным display:inline-block; - чтобы сделать элемент встроенным, с вкелючением некоторых свойств блочного элемента display:inline; - чтобы сделать элемент встроенным У свойства display есть ещё несколько значений. Если хотите изучить их подробнее, идите в справочник) В примере сайта вам предложена только одна страница, ваша задача сделать сначала её - главную страницу сайта, а потом самостоятельно придумать и сделать остальные - услуги, цены, контакты в таком же стиле, что и главная.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/4.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_4.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 5 урок css
css_5 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В уроке объясню только одно - как убрать нижнее подчёркивание у ссылки. Хотя и сами могли это найти в справочнике или в интернете. text-decoration:none; Всё остальное вы и так знаете. На этом всё. Больше ничего вам не расскажу. Будете искать ответы сами. Думаете это шутка?) А вто и нет. На самом деле я серьёзно. Следующее чему вы научитесь - это не новому тегу или атрибуту, а задавать правильные вопросы и искать на них ответы. В данному курсе я вас не смогу обучить вообще всему. Я закладываю фундамент, а вот дом на нём вам предстоит строить самостоятельно. Учитесь.)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/5.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_5.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 6 урок css
css_6 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Ух ты! До конца CSS осталось всего два сайта. Но каких?) Очень интересных. Эти два сайта - реальны. Я вытащил их из сети. То есть вы повторите процесс разработки какого-то программиста из другой страны. Дерзайте)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/6.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_6.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 7 урок css
css_7 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Финальный сайт CSS! Сделайте его, и попадёте в нирвану. Станете соколом, который освоил вёрстку сайтов! Сможете собирать свои сайты. Ты очень крутой! Удачи!'),width=700),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/7.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/8.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/9.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/10.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/11.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/web_page/img/css/12.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_7.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)

# 1 урок js
js_1 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В РАЗРАБОТКЕ',text_align='center'),width=700,margin=ft.margin.only(top=300)),
        ft.Container(ft.Text('У нас лапки, но мы работаем. Скоро здесь что-то появится.',text_align='center'),width=700),
    ])
)
# 2 урок js
js_2 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В РАЗРАБОТКЕ',text_align='center'),width=700,margin=ft.margin.only(top=300)),
        ft.Container(ft.Text('У нас лапки, но мы работаем. Скоро здесь что-то появится.',text_align='center'),width=700),
    ])
)
# 3 урок js
js_3 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В РАЗРАБОТКЕ',text_align='center'),width=700,margin=ft.margin.only(top=300)),
        ft.Container(ft.Text('У нас лапки, но мы работаем. Скоро здесь что-то появится.',text_align='center'),width=700),
    ])
)
# 4 урок js
js_4 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В РАЗРАБОТКЕ',text_align='center'),width=700,margin=ft.margin.only(top=300)),
        ft.Container(ft.Text('У нас лапки, но мы работаем. Скоро здесь что-то появится.',text_align='center'),width=700),
    ])
)
# 5 урок js
js_5 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В РАЗРАБОТКЕ',text_align='center'),width=700,margin=ft.margin.only(top=300)),
        ft.Container(ft.Text('У нас лапки, но мы работаем. Скоро здесь что-то появится.',text_align='center'),width=700),
    ])
)


less_print = {
    'HTML 1': html_1,
    'HTML 2': html_2,
    'HTML 3': html_3,
    'HTML 4': html_4,
    'HTML 5': html_5,
    'HTML 6': html_6,
     'CSS 1':  css_1,
     'CSS 2':  css_2,
     'CSS 3':  css_3,
     'CSS 4': css_4,
     'CSS 5': css_5,
     'CSS 6': css_6,
     'CSS 7': css_7,
      'JS 1':  js_1,
      'JS 2':  js_2,
      'JS 3':  js_3,
      'JS 4':  js_4,
      'JS 5':  js_5,
}