
import flet as ft

# 1 урок
less_1 = ft.Container(
    ft.Column(controls=[
        # ft.Container(ft.Image(src='src/pages/content/maincraft_page/img/les_1/',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Установка Minecraft и Python',text_align='center'),width=700),
        ft.Container(ft.Text('1. Качаем и устанавливаем Tlauncher.org (если еще не установлен)'),width=700),
        ft.Container(ft.Text('2. Качаем и устанавливаем python с python.org (если еще не установлен)'),width=700),
        ft.Container(ft.Text('3. Качаем и устанавливаем Java.com (если еще не установлен)'),width=700),
        ft.Container(ft.Text('4. Переходим в mif.to/minecraft, листаем вниз до надписи “Дополнительные материалы”, нажи- маем на “установочные файлы для Windows” и качаем. Скаченный архив распакуйте в папку со своим именем и фамилией на рабочем  столе.'),width=700),
        ft.Container(ft.Text('5. Нажимаем на файл в папке с распакованными файлами Install_API и ждём окончания установки'),width=700),
        ft.Container(ft.Text('6. Переходим в папку server, открываем файл  server, меняем строку online.mode = true на online.mode = false, сохраняем и закрываем'),width=700),
        ft.Container(ft.Text('7. В папке Minecraft Tools запускаем сервер - Start_Server. Не закрываем терминал! Сервер  запущен только в открытом состоянии'),width=700),
        ft.Container(ft.Text('8. В Tlauncher выбираем версию 1.11.2, вводим имя на анлийском, нажимаем установить'),width=700),
        ft.Container(ft.Text('После запуска игры выбираем - Сетевая игра, добавить. Имя сервера - своя фамилия, адрес сервера - localhost и подключаемся. Сервер запущен!'),width=700),
    ])
)
# 2 урок
less_2 = ft.Container(
    ft.Column(controls=[
        # ft.Container(ft.Image(src='src/pages/content/maincraft_page/img/les_2/',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Перемещение персонажа',text_align='center'),width=700),
        ft.Container(ft.Text('1. Не закрывайте терминал с запущенным  сервером и клиент minecraft, в пуске, либо  поиске введите IDLE и запустите. IDLE - среда для выполнения кода Python.'),width=700),
        ft.Container(ft.Text('2. В запущенной программе введите строку:'),width=700),
        ft.Container(ft.Text('from mcpi.minecraft import Minecraft',color='#FBD46D'),width=700),
        ft.Container(ft.Text('и нажмите enter'),width=700),
        ft.Container(ft.Text('3. Введите строку и нажмите enter:'),width=700),
        ft.Container(ft.Text('mc = Minecraft.create()',color='#FBD46D'),width=700),
        ft.Container(ft.Text('4. Введите строку и нажмите enter:'),width=700),
        ft.Container(ft.Text('mc.player.setPos(100,100,100)',color='#FBD46D'),width=700),
        ft.Container(ft.Text('5. Если все команды ввелись без ошибок, прог-  рамма не выругалась красным цветом, то   перейдите в клиент Minecraft. Игрок должен   телепортироваться.  Если программа ругается красным, вы либо (вероятно) допустили ошибку при переписы- вании программы - в таком случае введите  строку кода заново, без ошибки, либо у вас  криво встали библиотеки майнкрафта в питон,  их нужно переустановить. Как это сделать  спросите у преподавателя.'),width=700),
        ft.Container(ft.Text('6. Когда все зарботало, зовите препода, он расскажет, что за код написали.'),width=700),
        ft.Container(ft.Text(''),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 3 урок
less_3 = ft.Container(
    ft.Column(controls=[
        # ft.Container(ft.Image(src='src/pages/content/maincraft_page/img/les_3/',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Телепортация по кругу',text_align='center'),width=700),
        ft.Container(ft.Text('1.Писать код и вводить построчно неудобно. Нажми file - new file в IDLE. Появится окно, в котором можно писать многострочный код. Чтобы запустить такой код, нажмите run.'),width=700),
        ft.Container(ft.Text('2. Чтобы телепортация не происходила мгновенно, мы добавим задуржку. Введите:'),width=700),
        ft.Container(ft.Text('\nimport time - добавляем библиотеку для управления временем\ntime.sleep(5) - программа спит 5 секунд',color='#FBD46D'),width=700),
        ft.Container(ft.Text('2. Добавим код с прошлого урока, вся программа будет выглядеть так:'),width=700),
        ft.Container(ft.Text('\nimport time\nfrom mcpi.minecraft import Minecraft\nmc = Minecraft.create()\ntime.sleep(5)\nmc.player.setPos(100,100,100)',color='#FBD46D'),width=700),
        ft.Container(ft.Text('перепишите программу и запустите. Теперь игрок телепортируется не сразу, а через 5 се-кунд после запуска программы.'),width=700),
        ft.Container(ft.Text('3. Напишите программу, где игрока телепортируест каждые 5 секунд. Сделайте не менее 4-х телепортация в разные точки карты. Когда напишите программу, покажите преподавателю'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 4 урок
less_4 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Постройка дома',text_align='center'),width=700),
        ft.Container(ft.Text('1. Блоки строятся с помощью двух команд:'),width=700),
        ft.Container(ft.Text('mc.setBlock(6,5,2,103) - установка одного блока',color='#FBD46D'),width=700),
        ft.Container(ft.Text('где 6,5,2 - координаты установки блока, 103 - тип блока Типов блоков очень много, все не запомнить, можете скачать таблицу с номерами блоков из интернета и закинуть себе в папку.'),width=700),
        ft.Container(ft.Text('mc.setBlocks(1,1,1,10,10,10,103) - установка множества блоков',color='#FBD46D'),width=700),
        ft.Container(ft.Text('В данном случае блоки ставятся внутрь параллелепипеда, 1,1,1 - координаты одного угла, 10,10,10 - координаты противоположного угла, 103 - тип блока'),width=700),
        ft.Container(ft.Image(src='src/pages/content/maincraft_page/img/les_4/1.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Постройте дом с помощью кода. У дома должна дверь, окно, крыша. Как сделаете, покажите преподу.'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 5 урок
less_5 = ft.Container(
    ft.Column(controls=[
        # ft.Container(ft.Image(src='src/pages/content/maincraft_page/img/les_5/',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Случайные числа и вывод в чат',text_align='center'),width=700),
        ft.Container(ft.Text('1. Часто в играх нужно получить случайные  значения. Научимся телепортировать перса в случайные координаты:'),width=700),
        ft.Container(ft.Text('\nimport random - добавляем библиотеку для рандомных чисел\ncount = random.randint(1,6) - в переменную\ncount кладем рандомное число от 1 до 6',color='#FBD46D'),width=700),
        ft.Container(ft.Text('2. Сделайте программу, в которой игрока телепортирует каждые 2 секунды в случайную  точку в кубе 20-20-20 блоков. Чтобы зациклить программу, можно использовать бесконечный цикл while true: , программа будет выглядеть как-то так:'),width=700),
        ft.Container(ft.Text('import time\nimport random\nfrom mcpi.minecraft import Minecraft\nmc = Minecraft.create()\nwhile True:\n   код телепортации',color='#FBD46D'),width=700),
        ft.Container(ft.Text('3. Научимся писать сообщения в чат:'),width=700),
        ft.Container(ft.Text('mc.postToChat(“Hello!”)',color='#FBD46D'),width=700),
        ft.Container(ft.Text('Доработай прогу из второго пунтка, чтобы координаты, куда тэпнулся перс выводились в чат. Сделай и покажи преподу.'),width=700),
    ])
)
# 6 урок
less_6 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Умное перемещение',text_align='center'),width=700),
        ft.Container(ft.Text('1. Первым делом нужно узнать текущее положение игрока. Сделаем это с помощью  getTilePos()'),width=700),
        ft.Container(ft.Image(src='src/pages/content/maincraft_page/img/les_4/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('2. Зная текущее положение, теперь мы можем переместить игрока.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/maincraft_page/img/les_4/3.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Ранее мы перемещали игрока с помощью  координат setPos. Но это не всегда удобно, ведь привязка идёт к координатам Майнкрафта Теперь же вы можете перемещать игрока относительно его начального положения, следить за координатами Майнкрафт больше не нужно.'),width=700),
        ft.Container(ft.Text('3. Напишите скрипт, который перемещает игрока вперед на 5 блоков и назад каждые 2 секунды'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 7 урок
less_7 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Умное строительство',text_align='center'),width=700),
        ft.Container(ft.Text('1. С помощью координат перса теперь мы можем строить блоки относительно него по умному.Создадим лаву под персонажем.'),width=700),
        ft.Container(ft.Image(src='src/pages/content/maincraft_page/img/les_4/4.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('С помощью getTelePos и SetBlock закатайте персонажа со всех сторон в бедрок.'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 8 урок
less_8 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Блок под ногами игрока',text_align='center'),width=700),
        ft.Container(ft.Image(src='src/pages/content/maincraft_page/img/les_4/5.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('с помощью getBlock мы получаем тип блока и сохраняем его в переменной blockType, но ничего с этим не делаем. Выведи значение в чат и поставь задержку в 1 секунду, чтобы чат не долбило без перерыва. Чтобы тип блока определился не 1 раз, а постоянно добавьте цикл while.'),width=700),
        ft.Container(ft.Text('С помощью конструкции if, создайте программу которая проверяет, что под ногами блок песка, и если песок, то превратить его в булжник'),width=700),
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

}