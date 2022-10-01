import PySimpleGUI as sg
import rsa

layout = [
    [sg.Text('Фамилия:', size=(10, 1)), sg.InputText(), sg.Text(key='ASCII1')], #key='in_surname'
    [sg.Text('Имя:', size=(10, 1)), sg.InputText(), sg.Text(key='ASCII2')], #key='in_name'
    [sg.Submit(), sg.Cancel()],
    [sg.Output(size=(88, 20), key='_output_')],
    [sg.Button("Вторая часть", key="part2")]
]

window = sg.Window('Виндоус Форма', layout)

while True:  # The Event Loop
    event, values = window.read()
    # print(event, values)  # debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        window['_output_'].Update('')
        if values[0] and values[1]:
            print("\t".join(values[0]), end="\n\n")
            print("\t".join("+" * len(values[0])), end="\n\n")
            print("\t".join(values[1]), end="\n\n")
            print("\t".join("=" * len(values[1])), end="\n\n")
            i = 0
            result = ""
            ascii_list = [list(), list()]
            while i < len(values[0]) and i < len(values[1]):
                ascii_list[0].append(ord(values[0][i]))
                ascii_list[1].append(ord(values[1][i]))
                add = chr(ascii_list[0][i] + ascii_list[1][i])
                result += add
                i += 1
                print(add, end="\t")
            who = 0
            if i < len(values[1]):
                who = 1
            while i < len(values[who]):
                ascii_list[who].append(ord(values[who][i]))
                add = values[who][i]
                result += add
                i += 1
                print(add, end="\t")
            window['ASCII1'].Update(value=str(ascii_list[0]))
            window['ASCII2'].Update(value=str(ascii_list[1]))

            (pubkey, privkey) = rsa.newkeys(16)  # 4096
            encrypted_surname = encrypted_name = str()
            for i in range(len(values[0])):
                encrypted_surname += chr(ord(values[0][i]) ** pubkey.e % pubkey.n)
            for i in range(len(values[1])):
                encrypted_name += chr(ord(values[1][i]) ** pubkey.e % pubkey.n)
            window[0].Update(value=encrypted_surname)
            window[1].Update(value=encrypted_name)
        else:
            print('Please enter 2 strings.')
    if event == 'part2':
        layout2 = [
            [sg.Text('Введите число:'), sg.InputText(), sg.Text(key='2_left_num')],
            [sg.Text('И введите еще 3 числа:'), sg.Text(key='divides')],
            [sg.Text('А:'), sg.InputText(size=(7, 1)),
             sg.Text('B:'), sg.InputText(size=(7, 1)),
             sg.Text('C:'), sg.InputText(size=(7, 1))],
            [sg.Submit(), sg.Cancel()],
            [sg.Output(size=(88, 20), key='_output_')],
        ]
        window2 = sg.Window("Вторая Виндоус Форма", layout2)
        while True:  # The Event Loop
            event2, nums = window2.read()
            # print(event, values)  # debug
            if event2 in (None, 'Exit', 'Cancel'):
                window2.close()
                break
            if event2 == 'Submit':
                try:
                    if nums[0]:
                        nums[0] = int(nums[0])
                        window2['2_left_num'].Update(
                            value="Too few digits" if nums[0] < 10 else "Вторая цифра слева = " + str(nums[0])[1]
                        )
                        if nums[1] and nums[2] and nums[2]:
                            nums[1] = int(nums[1])
                            nums[2] = int(nums[2])
                            nums[3] = int(nums[3])
                            if (nums[1] == 0 or nums[2] == 0 or nums[3] == 0):
                                window2['divides'].Update(value=str("Нулевые числа писать не надо"))
                            else:
                                if nums[0] % nums[1] == 0 and nums[0] % nums[2] == 0 and nums[0] % nums[3] == 0:
                                    window2['divides'].Update(value=str("✅ Делится"))
                                else:
                                    window2['divides'].Update(value=str("❌ Не делится"))
                        else:
                            window2['divides'].Update(value=str("Нужно все 3 числа"))
                    else:
                        window2['2_left_num'].Update(value="Это поле должно быть заполнено")

                    # window2['_output_'].Update('')
                    count = 0
                    for i in range(10, 100):
                        if i * 2 % 10 == 8 and i * 3 % 10 == 4:
                            print(i)
                            count += 1
                    if count == 0:
                        print('''Не удалось найти такие двузначные числа, которые
                                        — при умножении на 2 заканчиваются на 8,
                                        — а при умножении на 3 - на 4 :-(''')
                except:
                    print("Должны быть только числа")
window.close()