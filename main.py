import fakedata
if __name__ == '__main__':
    data = fakedata
    x = 0
    while x != 1:
        nombreRandom = data.RandomName()
        sex = data.CheckSex(nombreRandom)
        nombreOne = data.RandomOneName()
        sexOne = data.CheckSex(nombreOne)
        nombreTwo = data.RandomTwoName()
        sexTwo = data.CheckSex(nombreTwo)
        email = data.RandomEmail(nombreRandom)
        emailPersonalizado = data.PersonalizedEmail(nombreRandom, 'outlook.com')
        sexRandom = data.RandomSex()
        print("".center(50, '-'))
        print(f'Nombre ramdom: {nombreRandom}')
        print(f'Email random: {email}')
        print(f'Sexo : {sex}')
        print(f'Email personalizado: {emailPersonalizado}')
        print(f'Un solo nombre: {nombreOne}')
        print(f'Sexo One: {sexOne}')
        print(f'Dos nombre: {nombreTwo}')
        print(f'Sexo Two: {sexTwo}')
        print(f'Sexo Random: {sexRandom}')
        print("".center(50, '-'))
        x += 1