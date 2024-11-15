
import flet as ft

# 1 урок
less_1 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Добро пожаловать на первый урок! На занятиях преподаватель - наставник, который отвечает на вопросы и указыват верный путь обучения. Чтобы преподаватеоль не повторял одно и тоже ученикам много раз (он всё таки не попугай)), Максим Николаевич придумал этот учебник. Внимательно читай учебник, в нём есть ответы на большинство вопросов.'),width=700),
        ft.Container(ft.Text('Задача первого урока - познакомиться с движком роблокс студио. Создать ландшавт и добавить несколько предметов из библиотеки компонентов'),width=700),
        ft.Container(ft.Text('Первым делом запусти Roblox Studio. Иконку найдешь на рабочем столе.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/0.png',width=100),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Откроется окно входа, либо, если прошлый ученик не вышел из своего аккаунта, сразу откроентя его аккаунт. Если открылся чужой аккаунт, обязательно выйди из него и зайди в свой. И сам не забывай в конце занятия выходить из своего аккаунта, чтобы всякие жулики ничего тебе не испортили'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/1.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Введи данные своего акаанута и войди. Если забыл логин или пароль, попробуй восстановить. Иногда быстрее будет создать новый аккаунт. На первом занятии на это обычно уходит немало времени) Для создания нового аккааунта зайди на сайт roblox.com и создай акканут)'),width=700),
        ft.Container(ft.Text('После входа в Роблокс студио увидешь основное меню.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/3.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Из левого меню вам понадобится певые два пункта - создание новой игры и ваши сохраненные игры'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/4.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Во вкладке New (Создание новой игры), выбираем шаблон - Baseplate - базовая плита, или пустой мир. С него начнем знакомство с движком роблокса'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/5.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Слева по-умолчанию открыто несколько окно - эдитор и тулбокс. Закрой их. Они нам пока не нужны.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/6.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('В первую очередь научимся запускать игру. Да, мы еще ничего не сделали, не написали код ни для какой игры, но у нас уже есть baseplate - плита, по которой можно ходить, есть спавнер. А что еще нужно для старта? Найди сверху синий треугольник - запуск игры, нажми на него. После загрузки твой персонаж появится на спавнере. Перемещение происходит, как в обычной игре. Попробуй подвигаться, попрыгать. После нажми на красный квадрат - стоп игра. И попробуй подвигаться по экрану в режиме разработки. Там все то же самое. WASD для перемещений, зажатая кнопка мыши для вращения.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/7.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Теперь научимся создавать ландшавт. Любая игра разрабатывается в несколько этапов, в первую очередь обычно делают графику, ландшавт, здания, транспорт, лес и прочее. С этого и начнем.Найди в верхней группе инструментов - Editor и нажми.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/8.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Откроется окно, состоящее из двух вкладок - Create и Edit. Create - генерирует мир автоматически по заданым настройкам. Это самый быстрый способ создать ландшавт. Так же в этой вкладке можно загрузить готовый ландшавт или отчистить текущий ландшавт. Интереснее вкладка Edit - ручное создание ландшавта. Она включает в себя 9 инструментов, вам понадобится лишь несколько.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/9.png',width=200),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Первый инструмент - Draw, создает ландшавт. У каждого инструмента есть много настроек, форма рисования - сфера, куб или цилинд. Размер рисования, снизу можно выбрать материал. Попробуйте разные настройки. В режиме add материал добавляется, если переключить на subtract - материал будет вырезаться, получается 3д стёрка.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/10.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Sculpt - выращивает материал. Им удобно редактировать неровености, делать ландшавт более реалистичным. Инструментом удобно вытягивать материал, либо наоборот - всасывать'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/11.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Smooth - сглаживает материал. Иногда, после удаления материала остаются неестественные неровности. Их удобно сгладить с помощью этого инструмента'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/12.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Paint - перекрашивает материал.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/13.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Sea level - создает море. При нажатии  а инструмент появляется куб, который можно растягивать, задавая размеры области, которая зальётся водой. После задания размеров нужно нажать на кнопку create снизу инструмента'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/14.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Слева сверху есть кнопки назад и вперед - управляют историей разарботки, можно откатиться на шаг назад, если что-то не получилось'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/15.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Ну и напоследок - Toolbox. Это отдельная вкладка, которую нужно запустить, нажав на toolbox в верхней группе инструментов. Это ююлиотека предметов. Роблокс студио работает только на английском, поэтому и в поиск нужно вводить предметы на английском. После перетягивать нужные предметы на экран. Например, gun - оружие. Попробуйте добавить несколько предметов из библиотеки Toolbox'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_1/16.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('На этом первый урок подошел к концу. В результате у вас должен появиться како-то ландшавт и предметы из Toolbox. Полноценную игру на первом уроке делать не нужно. Цель - познакомиться с роблокс студио, и у вас это должно было получиться. Покажите свою разработку учителю. Он вас похвалит и даст разрешение перейти к следующему уроку.'),width=700,margin=ft.margin.only(bottom=40)),
    ])
)

# 2 урок
less_2 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Игра - Враги на острове. И вот твоя первая игра - враги на острове. Создай пустой мир - baseplate. Начни с графики. Должен получиться остров, ни большой, ни маленький, в середине - гора. В горе обязатиельно пещера. Далььше из тулбокса посади деревья, раскидай по острову различное оружие и врагов. Добавь несколько спавнеров, чтобы не спавниться постоянно в одном и том же месте. Упор сделай на реализм. Легко сделать игру, где земля летает в воздухе, а вот реалистичную игру, в которую играть инетресно - сделать не так просто. На берегу острова добавь песок, на песке посади пальмы, палатку. В пещере воткни факелы. В-общем - постарайся! Подсказок больше не будет. Со всеми интсрументами для создания игры ты познакомился на первом уроке. Удачи!'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_2/1.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('В игру из примера можно поиграть. Для этого найдите в людях в роблоксе - RoboCore_ks, в его играх найдёте игру - island.'),width=700),
    ])
)

# 3 урок
less_3 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Здания - основа многих игр. Интресная планировка, взаимодействие с предметами - это очень интересно. Конечно, часть домов можно взять из тулбокса, но есть пробелма - если разместить в игре много предметов из тулбокса, они станут много вестить и сильно тормозить, на телефоне могут и вовсе не запуститься. С точки зрения оптимизации игры - всегда лучше все делать своими руками, а не брать готовые компоненты.'),width=700),
        ft.Container(ft.Text('Начнём) Дом - это набор прямоугольных стенок, пола и треуглоьной крыши. Всё это обычные геометрические объекты. В роблоксе их называют - элементарные блоки (обекты). Найдите в верхней группе инструментов Part и выбирете несколько фигур'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_3/1.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Четыре ваших главных друга пр иработе с элементарными блоками - это инстурменты на верхней панели: Select - выбрать, Move - пере5местить, Scale - изменить размер, Rotate - вращать'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_3/2.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Начнем строить дом. Как он строится в реальности - так же в игре. Вначале фундамент - плита, на которой будет расположен дом.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_3/3.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Выбираем плиту и нажимаем сочетание клавиш ctrl+D. Вам покажется, что ничего не случилось, но на самом деле плита скапировалась сама в себя, и теперь стены строить будет легче.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_3/4.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Постройте несколько стен и запустите игру. Стены упадут. Это происходит из-за того, что все создаваемые объекты в роблокс имеют физические свойства - прежде всего вес. Значит, если их создать в воздухе - они упадут.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_3/5.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Чтобы закрепить стены в пространстве, выбираем все стены и нажимаем в верхней группе инструментов - Anchor'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_3/6.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('После создания стен, их можно раскрасить, либо задать материал. '),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_3/7.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Ну и напоследок несколько примеров. Первый - это дом из контер страйк. Он недоделан, только каркасс. Туда нужно вставить окна и двери, мебель из тулбокса. Но смысл понятен.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_3/8.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Другой пример - игра - мочи зомби в одном из наших детских центров.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_3/9.gif',width=700),margin=ft.margin.only(left=0)),
    ])
)

# 4 урок
less_4 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Построй свой город. Инструментов новых в этом уроке нет. Закерпляем то, что изучили раньше. Постройка города - выпускной проект. После его сдачи учителю, вы будете допущены на следующий уровень - написание скриптов, так что постарайтесь.'),width=700),
        ft.Container(ft.Text('Инструментов новых нет, но есть основные принципы. Первое - в любом проекте графика создается от большего к малому. Сначала дороги и дома, потом остановки, лавочки, детские площадки, мусорки, машины и прочее. В первую очередь прикиньте дороги. Можно найти в тулбоксе.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_4/1.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('После строим первый этаж многоэтажного здания. Основу города будут составлять советские 5-ти этажки. В видео показано схематично, вы постарайтесь, добавте окна, материал стен - кирпич. Сделайте подъезд.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_4/2.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('После можно выбрать все объекты первого этажа и сгрупировать. Теперь это один объект, им будет проще управлять. Еопируем первый этаж и делаем еще 5'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_4/3.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('У вас получилось одно здание. Его можно так же скопировать и перенести. И вот у вас получился скелет города. Теперь можно добавлять мелкие предметы. И не забудьте про ландшавт! Наш город не должен стоять на базовой плите. Нужна травка, речушка. Покажите всё, чему научились.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_4/4.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text(''),width=700),
    ])
)

# 5 урок
less_5 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Поздравляю с прохождением блока по графике в роблокс! Теперь переходим к скриптам. Скрипты в роблоксе пишутся на языке программирования - Lua. '),width=700),
        ft.Container(ft.Text('Сначала познакомимся с двумя новыми вкладками. Это Explorer и Propirties'),width=700),
        ft.Container(ft.Text('Explorer  - проводник'),width=700),
        ft.Container(ft.Text('Propirties  - свойства'),width=700),
        ft.Container(ft.Text('По умолчанию, находдятся они справа от сцены (основного экрана). Добавить их можно через вкладку View'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/1.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Вы уже умеетет добавлять парты (кирпичи), изменять их цвет и размер. Вы все это делаете вручную. Этот способ рабоатет, когда нужно разово что-то сделать, без скриптов и повторений. '),width=700),
        ft.Container(ft.Text('Есть еще 2 способа изменять параметры и создавать парты'),width=700),
        ft.Container(ft.Text('Первый - через свойства (пропертиз). Создайте парт, выберете его в проводнике (експлоер), сни зу отгобразяться его свойства. Найдите свойство size (рамзер) и измените его.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/2.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Попробуйте изменить дургие свойства, например, цвет или прозрачность'),width=700),
        ft.Container(ft.Text('Таким образом можно легко изменять свойства объектов. Причем точнее, чем вручную. Некоторые свойства можно поменять вручную, через верхнюю группу инструментов. Другие - только через пропертиз.'),width=700),
        ft.Container(ft.Text('Теперь разберемся с третим спомобом создавать и изменять объекты - через скрипты.'),width=700),
        ft.Container(ft.Text('Наведите в эксплоере на wiorspace, рядом появится плюсик, енажмите на него, откроется окно, выберите в нем - script'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/3.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('По умолчанию при создании любого скрипта, в нём уже будет строчка кода - print("Hello world!"). Этот код выводит в консоль надпись Hello world'),width=700),
        ft.Container(ft.Text('Давайте проверим это. Для этого нужно открыть консоль. Она открывается снизу сцены (рабочей области), найти её можно так же во вкладе View'),width=700),
        ft.Container(ft.Text('Откройте консоль, перейдите обратно на вкладку Place и запустите игру.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/4.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Если вы все сделали правильно, в консоли увидите сообщение - hello world'),width=700),
        ft.Container(ft.Text('Теперь давайте потренируемся в написании скриптов, изучим язык программирования. Начнем с самых озов - переменных и операций над ними.'),width=700),
        ft.Container(ft.Text('Минимальный кирпичик любого языка программирования - это переменная. Если сказать просто, переменная - это коробочка, которая имеет имя и в нее можно что-то положить. Если сложно, переменная - это именованый выделенный участок памяти, в котором кодируется информация в каком-либо формате данных'),width=700),
        ft.Container(ft.Text('Переходим обратно в скрипт и попробуем создать несколько переменных '),width=700),
        ft.Container(ft.Text('a=2\nb=3'),width=700),
        ft.Container(ft.Text('Запустите код. Что произошло?'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/5.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Ничего не произошло. Ведь мы просто создали переменные a и b и положили в них значниея - числа 2 и 3. Давайте попробуем вывести на экран их сумму'),width=700),
        ft.Container(ft.Text('a=2\nb=3\nc=a+b\nprint(c)'),width=700),
        ft.Container(ft.Text('Напишите и запустите данный код'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/6.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Поздавляю, вы написали свою первую программу. Всё, что она делает, это складывает 2 числа и выводит их на экран. Но это уже работает. Давайте разберем по строкам, что же мы сделали.'),width=700),
        ft.Container(ft.Text('a=2 - создали переменную a и задали ей значение - 2\nb=3 - создали переменную b и задалми ей значение - 3\nc=a+b - создали переменную c и задали ей значение - результат выражения a+b. В момент работы этой строки, вначале в a и b подставятся их значения, потом проведется операция сложения, результат запишется в переменную c\nprint(c) - выводим значение перменной c на экран, именно значение перемнной, а не имя. Чтобы вывыести в print текст, нужно написать его в кавычках.'),width=700),
        ft.Container(ft.Text('Помимо сложения чисел, есть множество других операций. Основные математические - это\n+ сложение\n- вычитание\n* умножение \n/ деление'),width=700),
        ft.Container(ft.Text('Давайте напишем программу, в которой опробуем все четыре операции'),width=700),
        ft.Container(ft.Text('a=20\nb=10\nprint(a+b)\nprint(a-b)\nprint(a*b)\nprint(a/b)'),width=700),
        ft.Container(ft.Text('Напишите и запустите программу'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/7.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Получим на кажждой стркое значения выражения, написанного в print'),width=700),
        ft.Container(ft.Text('Теперь давайте допустим ошибку и посмотрим, что нам выдаст консоль, например, разделим на ноль'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/8.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Появится надпись Inf. Это сокращение от infinitite, или - бесконечность.'),width=700),
        ft.Container(ft.Text('Теперь же давайте сделаем ошибку в написании. Напрмиер, неправильно напишем слово print.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/9.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Выдаст ошибку. Любая надпись красным в консоли - ошибка. (иногда предупреждение) Из-за ошибки, скрипт скорее всего не запустится и не будет работать'),width=700),
        ft.Container(ft.Text('В консоли вам всегда подскажут, на какой строке произошла ошибка и дадут инфромацию - что конкретно сломалось. Иногда она информативна, иногда совсем не понятна. Просто посмотрите в указанную строку и поищите, что вы сделали не так.'),width=700),
        ft.Container(ft.Text('Вот мы сделали уже много всего, перейдем к первоначальному вопросу - как с помощью скрипта создавать и изменять объекты?'),width=700),
        ft.Container(ft.Text('Перепишите и запустите к себе такой код:'),width=700),
        ft.Container(ft.Text('local detal = Instance.new("Part",workspace)\ndetal.Size = Vector3.new(10,10,10)\ndetal.Position = Vector3.new(0,0,10)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/10.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('На воркспейсе, рядом с спавном, создастся парт, размером 10х19х10. Давайте разберем код, который написали:'),width=700),
        ft.Container(ft.Text('local detal = Instance.new("Part",workspace) - создаем локальную переменную с именем detal и кладем в нее объект - Парт, созданный на воркспейсе\ndetal.Size = Vector3.new(10,10,10) - указываем размер созданному парту через переменную, в которой он лежит\ndetal.Position = Vector3.new(0,0,10) - указываем позицию созданному парту через переменную, в которой он лежит'),width=700),
        ft.Container(ft.Text('Вот так все просто. Через пару-тройку занятий вы запомните, как пишется этот код и станет совсем просто создавать новые объекты'),width=700),
        ft.Container(ft.Text('Давайте усложним и добавим еще несколько свойств. Сами разберитесь, что они делают.'),width=700),
        ft.Container(ft.Text('local detal = Instance.new("Part",workspace)\ndetal.Shape = "Cylinder"\ndetal.Size = Vector3.new(10,10,10)\ndetal.Position = Vector3.new(0,0,10)\ndetal.BrickColor = BrickColor.new(180)\ndetal.Anchored = true'),width=700),
        ft.Container(ft.Text('Задание на урок - Сделайте дом с помощью кода. Там должен быть проем под дверь и окно, треугольная крыша. Дом не должен быть слишком большим или маленьким, просто одна комната, куда можно зайти через дверной проем.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/11.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/12.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/13.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/14.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/15.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/16.png',width=700),margin=ft.margin.only(left=0)),

        ft.Container(ft.Text(''),width=700),
        # ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_5/',width=700),margin=ft.margin.only(left=0)),
    ])
)
# 6 урок
less_6 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Эффекты для блоков',text_align='center'),width=700),
        ft.Container(ft.Text('1. Создаём part'),width=700),
        ft.Container(ft.Text('2. Далее на панели Explorer наводим на Part и нажимаем на +'),width=700),
        ft.Container(ft.Text('3. В раскрывшемся списке нажимаем на прямоугольный значок в верхнем правом углу, для того что бы раскрыть его еще больше и увидеть все доступные инструменты.'),width=700),
        ft.Container(ft.Text('4. Находим колонку Effects в которой находятся все стандартные эффекты Роблокс Студио. Выбираем понравившийся нажав на него ЛКМ.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_6/1.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Далее опишем основные эффекты. Попробуйте добавить каждый по очереди к блоку, и посмотреть, как он работает.'),width=700),
        ft.Container(ft.Text('5.Explosion — взрыв Простой эффект взрыва для которого нужно  будет настроить местоположение и триггер  для активации (событие или таймер).'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_6/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('6. Fire — огонь Постоянный эффект горения который можно  вообще никак не настраивать, все и так  замечательно.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_6/3.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('7. Highlight — выделение Эффект перекрашивает блок и позволит  немного поиграться с насыщенностью цвета. '),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_6/4.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('8. ParticleEmitter — излучатель частиц Интересный эффект плавно поднимающихся  частиц от блока. Он имеет множество настроек,  размер частиц, цвет и т.д.. '),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_6/5.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('9. Smoke — дым Еще один динамичный эффект дыма. Можно  задать область распространения и его цвет. '),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_6/6.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Sparkles — искры Крутой эффект искр испускаемых блоком. Так же  имеет множество настроек вроде области, цвета  искр и т.п.. '),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_6/7.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('На этом все. Простой урок. Просто потестите разные эффекты, чтобы в будущем их применять и делать крутые игры.'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)

# 7 урок
less_7 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Делаем меню', text_align='center'),width=700),
        ft.Container(ft.Text('1. При создании собственной игры в Роблокс  очень часто возникает необходимость создания  меню в котором игроки смогут просматривать  разные разделы, открывать вкладку с магазином  или получать какую то информацию. Во вкладке Explorer находим StarterGui,  нажимаем на кнопку + и выбираем Screen Gui'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_7/1.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('2.Внутри ScreenGui при помощи кнопки +  вставляем TextButton (это будет кнопка  нажав на которую вы откроете меню)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_7/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Размещаем его в любом месте на экране и редактируем внешний вид (шрифт, цвет фона, размер и т.д.)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_7/3.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Внутрь ScreenGui вставляем Frame (это  область меню внутри которого можно будет  размещать другие кнопки, разделы или какую  то информацию)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_7/4.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Размещаем Frame в любом месте, редактируем его размер, цвет, прозрачность и другие параметры влияющие на внешний вид'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_7/5.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Внутрь Frame вставляем TextButton и стилизуем ее по своему вкусу (это будет кнопка для закрытия меню)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_7/6.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('После того как вы добавили все необходимое  во Frame необходимо снять галочку с параметра Visible для того что бы меню было закрыто при  запуске игры'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_7/7.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('К TextButton (который отвечает за открытие  меню) прикрепляем LocalScript в котором  прописываем следующий код : \nscript.Parent.MouseButton1Click:Connect(function() \n      script.Parent.Parent.Frame.Visible = true \nend)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_7/8.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('К TextButton (который находится внутри  Frame и отвечает за закрытие меню)  прикрепляем LocalScript в котором прописываем  следующий код : \nscript.Parent.MouseButton1Click:Connect(function() \n    script.Parent.Parent.Parent.Frame.Visible = false \nend)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_7/9.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Проверяем работу меню. Запускаем симулятор  и нажимаем кнопку Menu что бы открыть меню.  нажимаем кнопку закрыть меню, что бы закрыть  меню. Все должно работать. По такому же  принципу можно добавить и другие кнопки,  разделы или любую информацию в меню.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_7/10.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Добавьте меню к игре - зомби на острове, или любой другой, созданной ранее. В меню должен быть 1 пункт - правила игры. Напишите эти правила'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 8 урок
less_8 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Создаём двухсторонний телепорт',text_align='center'),width=700),
        ft.Container(ft.Text('1. Заходим в Roblox Studio нажимаем Part и  выбираем Block В меню справа в строке Size изменяем размер  на 4,1,4 и устанавливаем галочку в пункте  Anchored Переименовываем блок на Teleport1 и меняем  цвет на красный (для лучшего восприятия) Дублируем телепорт через ctrl+d У дублированного блока изменяем название на  Teleport2 и изменяем цвет на синий (для удобства  восприятия)'),width=700),
        ft.Container(ft.Text('2. Создаем скрипт на первом телепорте и пишем код:'),width=700),
        ft.Container(ft.Text('\nscript.Parent.Touched:Connect(function(hit)\n    if game.Players:GetPlayerFromCharacter(hit.Parent) then\n        if script.Parent.Locked == false and script.Parent.Parent.Teleport2.Locked == false then\n            script.Parent.Locked = true\n            script.Parent.Parent.Teleport2.Locked = true\n            hit.Parent:MoveTo(workspace.Teleport2.Position)\n            wait(1)\n            script.Parent.Locked = false\n            script.Parent.Parent.Teleport2.Locked = false\n        end\n    end\nend)'),width=700),
        ft.Container(ft.Text('3. К блоку Teleport2 так же прикручиваем скрипт и добавляем тот же код, НО при этом меняем все надписи в коде Teloport2 на Teleport1'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_8/1.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Готово, можно запустить симуляцию и протестировать телепорты.'),width=700),
        ft.Container(ft.Text(''),width=700),
        ft.Container(ft.Text('Создаём односторонний телепорт',text_align='center'),width=700),
        ft.Container(ft.Text('1. Для того что бы создать односторонний  портал, нужно второй блок (Teleport2)  уменьшить до размера 1 и можно сделать его  невидимым (для этого устанавливаем значение  параметра Transparency = 1)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_8/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('2.Снимаем галочку с параметра CanCollide и удаляем скрипт для Teleport2'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_8/3.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Изменяем код в скрипте который прикреплен к Teleport1 на этот:\n\nscript.Parent.Touched:Connect(function(hit)\n    if game.Players:GetPlayerFromCharacter(hit.Parent) then\n        hit.Parent.HumanoidRootPart.CFrame = workspace.Teleport2.CFrame\n    end\nend)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_8/4.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Готово, можно запускать симуляцию и тестировать.'),width=700),
        ft.Container(ft.Text('Напишите программы для одностороннего и двустороннего телепорта, покажите учителю для доступа к следующему уроку'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 9 урок
less_9 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Делаем кил-блок',text_align='center'),width=700),
        ft.Container(ft.Text('1. Перейдите во вкладку MODEL и при помощи инструмента Part создайте блок.'),width=700),
        ft.Container(ft.Text('2. Создайте скрипт на part'),width=700),
        ft.Container(ft.Text('\nВпишите код в скрипт:\nscript.Parent.Touched:Connect(function(hit)\n   if hit.Parent:FindFirstChild("Humanoid") then\n       hit.Parent.Humanoid.Health = 0\n   end\nend)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_9/1.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Запустите игру и наступите на блок. Персонажа должно убить. Проверьте, что все работает как надо.'),width=700),
        ft.Container(ft.Text('Сделайте игру - паркур в башне. Поднимаешся наверх, если падаешь - попадаешь на кил блок и умираешь.'),width=700),
    ])
)
# 10 урок
less_10 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Смена дня и ночи',text_align='center'),width=700),
        ft.Container(ft.Text('1. Создаём скрипт на workspace'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_10/1.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('2. Прописываем в скрипт следующий код:'),width=700),
        ft.Container(ft.Text('\nwhile wait(0.1) do\n     game.Lighting:SetMinutesAfterMidnight(game.Lighting:GetMinutesAfterMidnight()+1)\nend'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_10/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Запустите игру и наблюдайте за изменениями Для замедления наступления дня и ночи измени  параметр wait(0.1) увеличив его (например  wait(0.5) или wait(0.9) )'),width=700),
        ft.Container(ft.Text(''),width=700),
        ft.Container(ft.Text(''),width=700),
        ft.Container(ft.Text(''),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 11 урок
less_11 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Щахматы',text_align='center'),width=700),
        ft.Container(ft.Text('Предидущие уроки не были полноценными играми, на них вы получиали практику в написании готового кода. Следущие уроки будут посвящены разработке игр.'),width=700),
        ft.Container(ft.Text('Игры Шахматы - необычная. Шахматных фигур там не будет) Эта игра нужна лишь для одного - научится использовать циклы в роблокс'),width=700),
        ft.Container(ft.Text('Для начала, создадим блок, размером 12х1х12 и добавим на него скрипт.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_11/1.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Теперь переименуйте Part в b1 и напишите в нем скрипт - \nlocal b1 = game.Workspace.b1'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_11/2.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Теперь созданный блок записан в коде в переменную b1, и мы можем манипулировать им с помощью кода.'),width=700),
        ft.Container(ft.Text('Первое, что изучим - это циклы. Циклы - это повторяющееся действие. Запишите следующие код и запустите его:'),width=700),
        ft.Container(ft.Text('\nfor i=1, 100 do \n    print(i)\nend'),width=700),
        ft.Container(ft.Text('В консоли должно отобразиться 100 чисел по порядку. Вот так и работают циклы. i=1 - с какого числа начинаем. (,100) - до какого числа идем. Если не указать через запятую третье число, по умолчанию оно равно 1. То есть делаем цикл от 1 до 100 с шагом 1. Переменная i в теле цикла будет в каждой итерации изменена, согласно текущему шагу цикла.'),width=700),
        ft.Container(ft.Text('Теперь давайте оживим наш блок. Мы же можем через Size управлять размерами блока, давайте заставим блок плавно увеличиться'),width=700),
        ft.Container(ft.Text('\nlocal b1 = game.Workspace.b1\n\nfor i=1, 100 do \n	b1.Size = Vector3.new(12,i,12)\n	wait(0.2)\nend'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_11/3.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Застваим блок увеличить высоту до 20, а потом обратно до 1.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_11/4.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Отлично! Нно как зациклить изменение размеров блока, чтобы он постоянно ходил вверх и вниз? Для этого изучим еще один цикл - while'),width=700),
        ft.Container(ft.Text('while true do\n   Какой-то код\nend'),width=700),
        ft.Container(ft.Text('Какой-то код будет бесконенчо исполнятся сверху вниз в цикле. Попробуем на практике:'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_11/5.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Теперь перйдем к игре. Сделайте шахматную доску, состоящую из блоков 12х12, которые рандомно летят вверх и вниз. Ты спавнишься с одной стороны, задача - перейти на другую. Тебе мешают зомби, так же добавь оружку.'),width=700),
        ft.Container(ft.Text('Ниже - пример одной линии шахмат.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_11/6.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text(''),width=700),

    ])
)
# 12 урок
less_12 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Игра - сбор яблок',text_align='center'),width=700),
        ft.Container(ft.Text('1. Суть игры - сбор яблок на время. Успел -  победил, не успел - тебя убило. Начать стоит с графики. Добавьте лабиринт с элементами паркура. На уровне пупка  разместите яблоки - красные сферы.  Baseplate удалите, чтобы всё висело в воздухе'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_12/1.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Не забудьте заякорить все объекты, чтобы они не упали после старта игры.'),width=700),
        ft.Container(ft.Text('2. Все созданные яблоки из part нужно переименовать в apple1, apple2 и т.д'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_12/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('3. На Baseplate создайте скрипт. В него нужно поместить все яблоки, чтобы этим управлять. Так же написать функцию, которая будет  считать съеденные яблоки и написать  скрипты, чтобы яблоки исчезали при касании'),width=700),
        ft.Container(ft.Text('После того, как перепишите скрипт, запустите игру, попробуйте коснуться яблок. Яблоки должны исчезать, а в Output будет выводитьсе количество собранный яблоке \nП.С \nБлок с if в коде нужно повторить на все яблоки'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_12/3.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Когда перепишите код и убедитесь, что все работает, попросите учителя объяснить, как он работает.'),width=700),
        ft.Container(ft.Text('4. Создайте красную плиту снизу лабиринта. Это будет kill-блок, при касании которого  персонаж умирает. Напишем скрипт, в котором блок при старте появляется снизу, через 10 секунд переходит наверх и убивает персонажа '),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_12/4.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Нижние и верхние координаты платформы нужно подобрать самостоятельно через свойства  объекта. Запустите и протестируйте программу'),width=700),
        ft.Container(ft.Text('5. Сейчас через 10 секунд персонажа убивает плита, при этом обратно она не возвращается. Т.е. чтобы поиграть еще раз, нужно переза- пустить игру. Добавим авторестарт: Поместим перемещение плиты в бесконечный цикл, а так же через 10 секунд плита подни- мается, убивает персонажа, ждёт 2 секунды и  опускается обратно. В это время персонаж  спавнится и можно пройти игру еще раз.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_12/5.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сейчас нам не хватает только возможности выйграть. Добавим её. Для начала переиме- нуйте Part kill блока плиты на LLL. После этого дополните скрипт на бесплейте, который писали в 3-ем шаге:'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_12/6.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('При съедании последнего яблока, скрипт с kill блоком выключается, в консоль выводится  сообщение о победе.'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 13 урок
less_13 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Паркур - игра башня',text_align='center'),width=700),
        ft.Container(ft.Text('Ранее,в 9 уроке вы уже делали игру с паркуром в башне. Что будет теперь? Теперь будет 3 башни)'),width=700),
        ft.Container(ft.Text('Смысл такой - ты поднимаешься наверх в первой башне, снизу - килл блок, в процессе собираешь яблоки. Если все собраны, то дверь открывается и пропускает вас во вторую башню. Во второй башне вы уже спускаетесь сверху вниз и так же собираете яблоки и открываете дверь. И в третьей башне, когда добираетесь до верха - игра пройдена. Выведите таймер на экран, по истечению которого - проигрываете.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_13/1.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text(''),width=700),
        
    ])
)
# 14 урок
less_14 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Игра - контер страйк',text_align='center'),width=700),
        ft.Container(ft.Text('Да, это будет полноценная игра counter strike, но только на одной карте. На рабочих столах у вас есть игра контер страйк, зайдите, выберите карту, которую будете повторять. После займитесь графикой - воссоздайте карту в роблоксе.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/1.jpg',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('теперь присутпим к механике игры - выбору внчале команды, и спавне в месте команды.'),width=700),
        ft.Container(ft.Text('Смысл урока в том, что при запуске игры, у вас будут спрашивать, к какой команде хотите присоединиться - террористы или спецназ. У  каждой команды при этом будет свой спавн в  разных концах карты. Заходите в яндекс картинки в браузере и вводите  cs террорист png. После чего вам нужно найти  и скачать персонажа обязательно на прозрачном фоне!'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Тоже самое проделываете и со спецназовцем. Картинки сохраняете в свою папку на рабочем столе.'),width=700),
        ft.Container(ft.Text('Так же нужно скачать картинку, на фоне которой будут находиться значки выбора команды'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/3.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('2. Браузере заходите в roblox creator под своим аккаунтом, выбираете dashboard, далее creations, далее development items, и наконец decals'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/4.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Загружаем 3 картинки по очереди. Каждой даём свое понятное название на анг языке.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/5.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('3. Создаем новый мир - baseplate в Roblox Studio'),width=700),
        ft.Container(ft.Text('4. Перейдите в раздел MODEL и нажмите кнопку  Insert Object. После чего кликните по пункту  Decal в появившемся меню Insert Basic Object  что бы создать папку Teams в окне Explorer'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/6.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Проверьте, что папк Teams в Explorer создалась'),width=700),
        ft.Container(ft.Text('5. В окне Explorer наведите курсор на папку  StarterGui и проверьте есть ли внутри  StarterGui пункт ScreenGui, если его нет,  необходимо нажать на + и добавить ScreenGui.  После чего создайте внутри области ScreenGui  три кнопки ImageButton, при этом две из них  должны находиться внутри другой'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/7.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('6. Выровняйте кнопки и вставьте внутрь них  изображения. Для этого вернитесь на сайт  Роблокс — Create в раздел DEVELOPMENT  ITEMS — DECALS и нажмите на три точки на  загруженном изображении, после чего  нажмите COPY ASSET ID что бы скопировать  ID картинки. Далее вернитесь в Роблокс  Студио, нажмите на изображение и в окне  Properties найдите пункт image и вставьте туда  скопированный ранее ID.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/8.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Внутри StarterGui — ScreenGui — ImmageButton  создаем LocalScript и пишем в него  следующий код'),width=700),
        ft.Container(ft.Text('\nlocal Red = script.Parent:WaitForChild("Red")\nlocal Blue = script.Parent:WaitForChild("Blue")\nlocal REvent = game:GetService("ReplicatedStorage" ):WaitForChild("SelectTeam")\nRed.MouseButton1Click:Connect(function()\n    REvent:FireServer("Red")\n    wait()\n    script.Parent.Parent:Destroy()\nend)\nBlue.MouseButton1Click: Connect (function()\n    REvent: FireServer("Blue")\n    wait()\n    script.Parent.Parent:Destroy()\nend)'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/9.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/10.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('В окне VIEW отключаем видимость интерфейса нажав на кнопку UI Visibility'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/11.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Это нужно, чтобы скрыть кнопки-картинки,  которые сейчас открыты на весь экран'),width=700),
        ft.Container(ft.Text('10. Переходим во вкладку Model и создаем два спавнера нажав соответствующую кнопку в верхнем меню.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/12.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('11. В окне Explorer выберите один из спавнеров. После чего в окне Properties найдите и измените параметр BrickColor в разделе Appearance и TeamColor в разделе Teams на Red для одного спавнера и Blue для другого спавнра.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/13.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('12. Нажимаем + на папке Teams и создаем две команды Teams и переименовываем их в Terorist и Conter. После чего для каждой из них меняем TeamColor на соответствующий цвет.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/14.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('13. Внутри ReplicatedStorage создайте RemoteEvent и переименуйте его в SelectTeam'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/15.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('14. Что бы при каждом респавне у Вас не появлялась табличка выбора, необходимо выбрать ScreenGue и в окне Properties отключить пункт ResetOnSpawn.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/16.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('15. Переименуйте кнопки ImageButton созданные на шаге 5 на соответствующие Terorist и Conter'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_14/17.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('И вот теперь можно запустить игру! При  первом запуске вам предложат выбрать команду и вы заспавнитесь на соответствующем спавненре. Если что-то не работает, в первую  очередь проверьте output на наличие ошибок. Код скриптов можно получить по этой ссылке: https://disk.yandex.ru/d/2T3ln93hpSKtfQ '),width=700),
        ft.Container(ft.Text('Раскидайте спавнера оружия по карте, игра готова!'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 15 урок
less_15 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Создадим чумовой инвентарь',text_align='center'),width=700),
        ft.Container(ft.Text('15 урок - простенький, на инвентарь. Здесь дейтсивтельно ничего сложного, не как в 14 уроке)'),width=700),
        ft.Container(ft.Text('1. Научимся создавать инвентарь и кастомные предметы. '),width=700),
        ft.Container(ft.Text('Инвентарь хранится в папке StarterPack. Создадим на данной папке игровой элемент - Tool. После создания переименуйте Tool в  Torch (Факел). Создайте part размером  0.5x0.5x0.5 и поместите его в Tourch. После запустите игру.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_15/1.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('При клике на инвентарь - Tourch на полу будет появляться part, который вы создали. Если  кликнуть еще раз - он исчезнет.'),width=700),
        ft.Container(ft.Text('2. Чтобы блок появлялся в руке, переименуйте part в Handle. (Ручка) Запустите программу и покликайте на  инвентарь.'),width=700),
        ft.Container(ft.Text('3. Создайте тело факела с помощью двух  цилиндров. Разместите цилиндры как на  картинке ниже, после объедините их с помощью Union.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_15/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Получившийся объект переименуйте в “Факел”'),width=700),
        ft.Container(ft.Text('4. Чтобы прикрепить факел к ручке, пененесите Handle обратно в видимую часть - Workspace. Поместите факел на ручку и сврите соединение с помощью сварки - Create - Weld. После переместите получившиеся объекты  обратно в Tourch. Запустите и протестируйте игру. При выборе  факела теперь в руке будет появляться факел.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_15/3.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_15/4.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('5. Добавим огонь. Для этого переместите факел обратно в Workspace. Создайте сферу и поме- стите сверху факела. Приварите сферу к факелу как и раньше - Create - Weld. После на свере + создайте еффект fire. Настройте его, чтобы сильно не фигачил. После того, как все сделано - переместите  объекты обратно в Tourch/'),width=700),
        ft.Container(ft.Image(src='src/pages/content/roblox_page/img/les_15/5.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('В конце измените у сферы свойство transparency на 1 - она станет прозрачной.'),width=700),
        ft.Container(ft.Text('На этом первая часть курса по программированию в роблоксе закончена! Ты успешно её прошёл, поздравляю!'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)

less_print = {
    'Урок 1': less_1,
    'Урок 2': less_2,
    'Урок 3': less_3,
    'Урок 4': less_4,
    'Урок 5': less_5,
    'Урок 6': less_6,
    'Урок 7': less_7,
    'Урок 8': less_8,
    'Урок 9': less_9,
    'Урок 10': less_10,
    'Урок 11': less_11,
    'Урок 12': less_12,
    'Урок 13': less_13,
    'Урок 14': less_14,
    'Урок 15': less_15,
}