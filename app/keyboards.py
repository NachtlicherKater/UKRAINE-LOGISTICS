from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='11')],
    [KeyboardButton(text='22'), KeyboardButton(text='22')]
])

pravila = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='ㅤПравила серверуㅤ', callback_data='nothing')],
    [InlineKeyboardButton(text='ㅤ§1. Головне.ㅤ', callback_data='glava1')],
    [InlineKeyboardButton(text='ㅤ§2. Поведінка на сервері.ㅤ', callback_data='glava2')],
    [InlineKeyboardButton(text='ㅤ§3. Заборони у тектовому/голосовому чаті.ㅤ', callback_data='glava3')],
    [InlineKeyboardButton(text='ㅤ', callback_data='nothing')],
    [InlineKeyboardButton(text='ㅤ↓↓↓ Меню бота ↓↓↓ㅤ', callback_data='menu')]

])

#------------------------------------------------------------------------------------------------------------------------------------------------------
#cars = ['tesla','mers','bmw']

#async def inline_cars():
#    keyboard = InlineKeyboardBuilder()
#    for car in cars:
#        keyboard.add(InlineKeyboardButton(text=car, url='https://www.google.com/'))
#    return keyboard.adjust(1).as_markup()

vernis1 = InlineKeyboardMarkup(inline_keyboard= [[InlineKeyboardButton(text='ㅤПовернутися назад.ㅤ', callback_data='glava1')]])
vernis2 = InlineKeyboardMarkup(inline_keyboard= [[InlineKeyboardButton(text='ㅤПовернутися назад.ㅤ', callback_data='glava2')]])
vernis3 = InlineKeyboardMarkup(inline_keyboard= [[InlineKeyboardButton(text='ㅤПовернутися назад.ㅤ', callback_data='glava3')]])

glava1 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='§1.1  Незнання правил не звільняє від відповідальності. Приймання правил у Discord передбачає те, що ви вже з ними ознайомилися і не маєте жодних заперечень.',  callback_data='r11')],
    [InlineKeyboardButton(text='§1.2  Данний звід правил може бути змінений адміністрацією без будь-яких попереджень і повідомлень учасників серверу.',  callback_data='r12')],
    [InlineKeyboardButton(text='§1.3  На цьому сервері немає жодних утисків, жорстких заборон(в межах розумного) або дискримінації інших національностей та/або мов. Основна мова спілкування в голосовому або текстовому чаті - Українська, але ніхто не забороняє Вам використовувати будь-яку іншу мову, якщо більшість учасників Discord-серверу не проти її використання.', callback_data='r13')],
    [InlineKeyboardButton(text='§1.4  Будь-які образи, приниження, насмішки над учасниками компанії "UKRAINE-LOGISTICS" у будь-якому вигляді, стилі письма або переносному сенсі — НЕПРИПУСТИМІ. Виняток: якщо людина яку образили, не має нічого проти цих висловлювань і сприймає це як жарт.',  callback_data='r14')],
    [InlineKeyboardButton(text='§1.5  Адміністрація Discord-сервера має повне право змінювати нікнейм, приглушати(мьютити), переміщувати, виганяти, блокувати обліковий запис учасників серверу при порушенні та/або виявленні порушень правил.',  callback_data='r15')],
    [InlineKeyboardButton(text='§1.6  Учасник сервера, який запросив нового співробітника до групи у Телеграмi, зобов`язаний представити його всім у компанії "UKRAINE-LOGISTICS".',  callback_data='r16')],
    [InlineKeyboardButton(text='§1.7  Новоприбулий учасник повинен привітати інших, назвати своє ім`я, вписати нікнейм у дискорді аналогічний ігровому та ознайомитися із розділом правил.',  callback_data='r17')],
    [InlineKeyboardButton(text='§1.8  Ставтеся до інших співробітників компанії так само, як і до себе. Заборонено навмисно заважати проїзду, підрізати, блокувати дорогу та будь-яким чином порушувати правила TruckersMP стосовно інших учасників дорожнього руху, та також своєї компанії.',  callback_data='r18')],
    [InlineKeyboardButton(text='ㅤПовернутися назад.ㅤ', callback_data='pravila')]
    ])

glava2 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='§2.1  Ваш нікнейм, фотографія профілю та статус не повинні викликати огиду, презирство, дискредитацію тих чи інших народів/національностей/окремих гравців. У разі порушення відповідно до правила §1.5 Адміністрація серверу має право втручатися.',  callback_data='r21')],
    [InlineKeyboardButton(text='§2.2  Будь-яка реклама в будь-якому її вигляді ЗАБОРОНЕНА. Незалежно від того, чи це текстовий, чи голосовий чат.',  callback_data='r22')],
    [InlineKeyboardButton(text='§2.3  Заборонено поширювати будь-який вид особистої інформації інших учасників, зокрема номер телефону, адресу, інформацію, яка може бути використана для ідентифікації особи тощо.', callback_data='r23')],
    [InlineKeyboardButton(text='§2.4  Заборонені будь-які види шантажу, погроз, пропаганди насильства, расизму, сексизму тощо.',  callback_data='r24')],
    [InlineKeyboardButton(text='§2.5  Заборонено розсилати будь-який вид спаму, флуду, неправомірних посилань у будь-яких текстових чатах та/або у приватні повідомлення учасників цього серверу.',  callback_data='r25')],
    [InlineKeyboardButton(text='§2.6  Заборонено видавати себе за іншу людину, використовувати інформацію третіх осіб як і їх доказів, згідно до правила §2.3.',  callback_data='r26')],
    [InlineKeyboardButton(text='§2.7  Заборонено ображати Адміністрацію як у прямому, так і у переносному сенсі. Якщо виникли якісь розбіжності з будь-яким привілейованим учасником серверу, постарайтеся вирішити це якомога швидше. Але якщо ви так і не змогли досягти загального порозуміння, зверніться до Голови Серверу щодо цієї проблеми.',  callback_data='r27')],
    [InlineKeyboardButton(text='§2.8  Заборонено ігнорувати та навмисно приховувати інформацію від Адміністрації Discord-сервера.',  callback_data='r28')],
    [InlineKeyboardButton(text='ㅤПовернутися назад.ㅤ', callback_data='pravila')]
    ])

glava3 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='§3.1  Заборонено у текстовому або голосовому чаті використовувати російську символіку, будь-які російсько-патріотичні пісні тощо.',  callback_data='r31')],
    [InlineKeyboardButton(text='§3.2  Використовуйте чати по їх призначенню, не намагайтеся писати або постити будь-що, що не стосується тематики каналу (оффтоп).\nПриклад: Відправляти фото з конвоїв у канал де знаходяться виключно модифікації (моди).',  callback_data='r32')],
    [InlineKeyboardButton(text='§3.3  Заборонено спамити, абьюзити звуковою панелью (Саундбордом у Діскорді). Під спамом мається на увазі багаторазове натискання цієї кнопки (Більше ніж 5 разів за 20 сек).', callback_data='r33')],
    [InlineKeyboardButton(text='§3.4  Намагайтеся утримуватись від нецензурної лексики, оскільки не всі це люблять, особливо у великій кількості, але ніхто не забороняє Вам її використовувати згідно з правилом §1.3.',  callback_data='r34')],
    [InlineKeyboardButton(text='§3.5  Заборонено кричати, неадекватно поводитися, створювати навмисно шум мікрофону (бити по капсулю мікрофона, кричати у нього на занадто близькій відстані, будь-яким чином створювати гучні звуки зі включеним мікрофоном).',  callback_data='r35')],
    [InlineKeyboardButton(text='§3.6  У каналах Діскорду заборонено обговорювати політику. Виняток: дозволяється у голосових чатах ВИКЛЮЧНО ЯКЩО УСІ учасники розмови згодні обговорювати певну тему.',  callback_data='r36')],
    [InlineKeyboardButton(text='§3.7  Намагайтеся не писати капсом (писати текст зі включеним CapsLock).',  callback_data='r37')],
    [InlineKeyboardButton(text='§3.8  Заборонена публікація контенту NSFW(+18) у будь-яких каналах серверу.',  callback_data='r38')],
    [InlineKeyboardButton(text='§3.9  Заборонено показувати демонстрацію екрану з будь-яким NSFW контентом.',  callback_data='r39')],
    [InlineKeyboardButton(text='ㅤПРИМІТКИ.ㅤ',  callback_data='rp')],
    [InlineKeyboardButton(text='ㅤПовернутися назад.ㅤ', callback_data='pravila')]
    ])
#------------------------------------------------------------------------------------------------------------------------------------------------------


menu = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Перейти до Дiскорд-сервера', url='https://discord.gg/6QKSNrqaxh')],
    [InlineKeyboardButton(text='Вступити до ВТК', url='https://truckersmp.com/vtc/72664')],
    [InlineKeyboardButton(text='Зв`язок із Адміністрацією', callback_data='report')],
    [InlineKeyboardButton(text='ㅤ', callback_data='nothing')],
    [InlineKeyboardButton(text='ㅤㅤㅤ⠀⠀⠀↑↑↑ Перейти до правил ↑↑↑⠀⠀ㅤㅤ⠀ㅤ', callback_data='pravila')]

])



remove = ReplyKeyboardRemove()










