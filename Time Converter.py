def timeCoverter():
    try:
        seconds = int(input('Masukkan detik:'))
        list1 = []
        hour = seconds//3600 ; list1.append(hour); list1_string = map(str,list1)
        for item in list1_string:
            item
        list2 = []
        minute = (seconds//60)%60 ; list2.append(minute); list2_string = map(str,list2)
        for item2 in list2_string:
            item2
        list3 = []
        seconds = seconds % (24*3600)%60 ; list3.append(seconds); list3_string = map(str,list3)
        for item3 in list3_string:
            item3
        print('Konversi:','0'+item,':','0'+item2,':','0'+item3)
    except ValueError:
        print('Invalid input!')
timeCoverter()


