from aiogram import F, Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Ну привет :)')

#@router.message(F.photo)
#async def get_photo(message: Message):
#    await message.answer(f'id photo: {message.photo[-1].file_id}')

@router.message(Command('лого'))
async def photo_profile(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMtZpWRJSCEf1tI5mHzsulvJzj7P44AAgvnMRuYz7BIEkWdaXRkBpgBAAMCAAN5AAM1BA',
                              caption='Тримай логотип нашого серверу!')

@router.message(Command('logo'))
async def photo_profile(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMtZpWRJSCEf1tI5mHzsulvJzj7P44AAgvnMRuYz7BIEkWdaXRkBpgBAAMCAAN5AAM1BA',
                              caption='Тримай логотип нашого серверу!')

@router.message(Command('бот'))
async def photo_profile(message: Message):
    await message.answer('ㅤ', reply_markup=kb.menu)

@router.message(Command('bot'))
async def photo_profile(message: Message):
    await message.answer('ㅤ', reply_markup=kb.menu)

@router.message(Command('правила'))
async def photo_profile(message: Message):
    await message.answer('ㅤ', reply_markup=kb.pravila)

@router.message(Command('rules'))
async def photo_profile(message: Message):
    await message.answer('ㅤ', reply_markup=kb.pravila)

@router.message(Command('buttons'))
async def photo_profile(message: Message):
    await message.answer('КнОпАчЕк БолЬше НеТ :(', reply_markup=kb.remove)

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

@router.callback_query(F.data == 'nothing')
async def nothing(callback: CallbackQuery):
    await callback.answer()

@router.callback_query(F.data == 'menu')
async def menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('ㅤ', reply_markup=kb.menu)


@router.callback_query(F.data == 'rp')
async def rp(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('-Під терміном: «Привілейовані учасники серверу» мається на увазі ті учасники, які мають привілеї згідно з §1.5 пунктом правил.\nТобто: Голова серверу / Адміністрація / Модерація тощо.\n \n-Усі згадування текстових чатів у розділах правил, розповсюджується також і на групу Telegram.' , reply_markup=kb.vernis3)

@router.callback_query(F.data == 'pravila')
async def pravila(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('ㅤ', reply_markup=kb.pravila)

@router.callback_query(F.data == 'glava1')
async def glava1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('ㅤРозділ §1. Головне.ㅤ', reply_markup=kb.glava1)

    @router.callback_query(F.data == 'r11')
    async def r11(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§1.1  Незнання правил не звільняє від відповідальності. Приймання правил у Discord передбачає те, що ви вже з ними ознайомилися і не маєте жодних заперечень.' , reply_markup=kb.vernis1)

    @router.callback_query(F.data == 'r12')
    async def r12(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§1.2  Данний звід правил може бути змінений адміністрацією без будь-яких попереджень і повідомлень учасників серверу.' , reply_markup=kb.vernis1)

    @router.callback_query(F.data == 'r13')
    async def r13(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§1.3  На цьому сервері немає жодних утисків, жорстких заборон(в межах розумного) або дискримінації інших національностей та/або мов. \nОсновна мова спілкування в голосовому або текстовому чаті - Українська, але ніхто не забороняє Вам використовувати будь-яку іншу мову, якщо більшість учасників Discord-серверу не проти її використання.',reply_markup=kb.vernis1)

    @router.callback_query(F.data == 'r14')
    async def r14(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§1.4  Будь-які образи, приниження, насмішки над учасниками компанії "UKRAINE-LOGISTICS" у будь-якому вигляді, стилі письма або переносному сенсі — НЕПРИПУСТИМІ. \nВиняток: якщо людина яку образили, не має нічого проти цих висловлювань і сприймає це як жарт.',reply_markup=kb.vernis1)

    @router.callback_query(F.data == 'r15')
    async def r15(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§1.5  Адміністрація Discord-сервера має повне право змінювати нікнейм, приглушати(мьютити), переміщувати, виганяти, блокувати обліковий запис учасників серверу при порушенні та/або виявленні порушень правил.',reply_markup=kb.vernis1)

    @router.callback_query(F.data == 'r16')
    async def r16(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§1.6  Учасник сервера, який запросив нового співробітника до групи у Телеграмi, зобов`язаний представити його всім у компанії "UKRAINE-LOGISTICS".',reply_markup=kb.vernis1)

    @router.callback_query(F.data == 'r17')
    async def r17(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§1.7  Новоприбулий учасник повинен привітати інших, назвати своє ім`я, вписати нікнейм у дискорді аналогічний ігровому та ознайомитися із розділом правил.',reply_markup=kb.vernis1)

    @router.callback_query(F.data == 'r18')
    async def r18(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§1.8  Ставтеся до інших співробітників компанії так само, як і до себе. Заборонено навмисно заважати проїзду, підрізати, блокувати дорогу та будь-яким чином порушувати правила TruckersMP стосовно інших учасників дорожнього руху, та також своєї компанії.',reply_markup=kb.vernis1)

@router.callback_query(F.data == 'glava2')
async def glava2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('ㅤРозділ §2. Поведінка на сервері.ㅤ', reply_markup=kb.glava2)

    @router.callback_query(F.data == 'r21')
    async def r21(callback: CallbackQuery):
      await callback.answer()
      await callback.message.edit_text('§2.1  Ваш нікнейм, фотографія профілю та статус не повинні викликати огиду, презирство, дискредитацію тих чи інших народів/національностей/окремих гравців. У разі порушення відповідно до правила §1.5 Адміністрація серверу має право втручатися.',reply_markup=kb.vernis2)

    @router.callback_query(F.data == 'r22')
    async def r22(callback: CallbackQuery):
      await callback.answer()
      await callback.message.edit_text('§2.2  Будь-яка реклама в будь-якому її вигляді ЗАБОРОНЕНА. Незалежно від того, чи це текстовий, чи голосовий чат.',reply_markup=kb.vernis2)

    @router.callback_query(F.data == 'r23')
    async def r23(callback: CallbackQuery):
      await callback.answer()
      await callback.message.edit_text('§2.3  Заборонено поширювати будь-який вид особистої інформації інших учасників, зокрема номер телефону, адресу, інформацію, яка може бути використана для ідентифікації особи тощо.',reply_markup=kb.vernis2)

    @router.callback_query(F.data == 'r24')
    async def r24(callback: CallbackQuery):
      await callback.answer()
      await callback.message.edit_text('§2.4  Заборонені будь-які види шантажу, погроз, пропаганди насильства, расизму, сексизму тощо.',reply_markup=kb.vernis2)

    @router.callback_query(F.data == 'r25')
    async def r25(callback: CallbackQuery):
      await callback.answer()
      await callback.message.edit_text('§2.5  Заборонено розсилати будь-який вид спаму, флуду, неправомірних посилань у будь-яких текстових чатах та/або у приватні повідомлення учасників цього серверу.',reply_markup=kb.vernis2)

    @router.callback_query(F.data == 'r26')
    async def r26(callback: CallbackQuery):
      await callback.answer()
      await callback.message.edit_text('§2.6  Заборонено видавати себе за іншу людину, використовувати інформацію третіх осіб як і їх доказів, згідно до правила §2.3.',reply_markup=kb.vernis2)

    @router.callback_query(F.data == 'r27')
    async def r27(callback: CallbackQuery):
      await callback.answer()
      await callback.message.edit_text('§2.7  Заборонено ображати Адміністрацію як у прямому, так і у переносному сенсі. Якщо виникли якісь розбіжності з будь-яким привілейованим учасником серверу, постарайтеся вирішити це якомога швидше. Але якщо ви так і не змогли досягти загального порозуміння, зверніться до Голови Серверу щодо цієї проблеми.',reply_markup=kb.vernis2)

    @router.callback_query(F.data == 'r28')
    async def r28(callback: CallbackQuery):
      await callback.answer()
      await callback.message.edit_text('§2.8  Заборонено ігнорувати та навмисно приховувати інформацію від Адміністрації Discord-сервера.',reply_markup=kb.vernis2)

@router.callback_query(F.data == 'glava3')
async def glava3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('ㅤРозділ §3. Заборони у тектовому/голосовому чаті.ㅤ', reply_markup=kb.glava3)

    @router.callback_query(F.data == 'r31')
    async def r31(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§3.1  Заборонено у текстовому або голосовому чаті використовувати російську символіку, будь-які російсько-патріотичні пісні тощо.',reply_markup=kb.vernis3)

    @router.callback_query(F.data == 'r32')
    async def r32(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§3.2  Використовуйте чати по їх призначенню, не намагайтеся писати або постити будь-що, що не стосується тематики каналу (оффтоп).\nПриклад: Відправляти фото з конвоїв у канал де знаходяться виключно модифікації (моди).',reply_markup=kb.vernis3)

    @router.callback_query(F.data == 'r33')
    async def r33(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§3.3  Заборонено спамити, абьюзити звуковою панелью (Саундбордом у Діскорді). Під спамом мається на увазі багаторазове натискання цієї кнопки (Більше ніж 5 разів за 20 сек).',reply_markup=kb.vernis3)

    @router.callback_query(F.data == 'r34')
    async def r34(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§3.4  Намагайтеся утримуватись від нецензурної лексики, оскільки не всі це люблять, особливо у великій кількості, але ніхто не забороняє Вам її використовувати згідно з правилом §1.3.',reply_markup=kb.vernis3)

    @router.callback_query(F.data == 'r35')
    async def r35(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§3.5  Заборонено кричати, неадекватно поводитися, створювати навмисно шум мікрофону (бити по капсулю мікрофона, кричати у нього на занадто близькій відстані, будь-яким чином створювати гучні звуки зі включеним мікрофоном)', reply_markup=kb.vernis3)

    @router.callback_query(F.data == 'r36')
    async def r36(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§3.6  У каналах Діскорду заборонено обговорювати політику. Виняток: дозволяється у голосових чатах ВИКЛЮЧНО ЯКЩО УСІ учасники розмови згодні обговорювати певну тему.',reply_markup=kb.vernis3)

    @router.callback_query(F.data == 'r37')
    async def r37(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§3.7  Намагайтеся не писати капсом (писати текст зі включеним CapsLock).',reply_markup=kb.vernis3)

    @router.callback_query(F.data == 'r38')
    async def r38(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§3.8  Заборонена публікація контенту NSFW(+18) у будь-яких каналах серверу.',reply_markup=kb.vernis3)

    @router.callback_query(F.data == 'r39')
    async def r39(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text('§3.9  Заборонено показувати демонстрацію екрану з будь-яким NSFW контентом.',reply_markup=kb.vernis3)



#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------

@router.callback_query(F.data == 'report')
async def nothing(callback: CallbackQuery):
    await callback.answer('Тут пока что нихуя нет', show_alert=True)














@router.message(F.text == '1')
async def shto(message: Message):
    await message.answer('2')

@router.message(F.text == 'Курва')
async def shto(message: Message):
    await message.answer('Бобер! Я пьердоле!')
