from random import choice

userName = ''

while True:
    
    st = input('-->: ')
    st = st.lower()

    if st in ['привет','здравствуй']:
        print(choice(['Здравствуй!','Привет!', 'Добрый день!']))

    if st in ['как тебя зовут', 'как твое имя']:
        print('Меня зовут R2D2')
        userName = input('Как ваше имя?')

    if st in ['пока', 'досвидания'] :
        break

print('Досвидания!', userName)    
