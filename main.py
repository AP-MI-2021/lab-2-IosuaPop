'''
1 Găsește ultimul număr prim mai mic decât un număr dat.

Funcția principală: get_largest_prime_below(n)
Funcția de test: test_get_largest_prime_below()
'''
def estePrim(a):
    '''
    Determina daca un numar este Prim
    :param a: int
    :return: true daca e prim false in caz contrar
    '''
    if a < 2 :
        return False
    else:
        x=2
        while x!=a:
            if a % x == 0:
                return False
            x+=1
    return True
def get_largest_prime_below(n):
    '''
    Returneaza cel mai mare numar prim mai mic decat n
    :param n: int
    :return: Un numar int mai mic decat n care este prim , daca nu exista afisam -1
    '''
    n-=1
    while n >= 2:
        if estePrim(n):
            return n
        n-=1
    return -1

def test_get_largest_prime_below():
    '''
    Testeaza corectitudinea functiei get_largest_prime_below(n)
    :return: null
    '''
    assert get_largest_prime_below(2) == -1
    assert get_largest_prime_below(7) == 5
    assert get_largest_prime_below(11) == 7
    assert get_largest_prime_below(21) == 19

'''
7 Determină dacă un număr este antipalindrom: un număr este antipalindrom dacă oricare două cifre egal depărtate de extremități sunt diferite (excepție făcând cifra din mijloc dacă avem un număr impar de cifre). De exemplu: 2783 este antipalindrom, iar 2773 nu este.

Funcția principală: is_antipalindrome(n) -> bool
Funcția de test: test_is_antipalindrome()
'''


def oglindit(n):
    '''
    Calculeaza inversul unui numar
    :param n: int
    :return: un numar int
    '''
    x=int(0)
    while n>0:
        x=x*10+int(n%10)
        n=int(n/10)
    return x

def isantipalindrom(n):
    '''
    Verifica daca un numar este palindrom
    :param n: int
    :return: Daca este antipalindrom returneaza True, in caz contrar returneaza False
    '''
    y=0
    z=n
    w=int(oglindit(n))
    while z!=0:
        z=int(z/10)
        y+=1
    y=int(y/2)
    for i in range(y):
        if int(w%10) == int(n%10):
            return False
        w=int(w/10)
        n=int(n/10)
    return True

def test_is_antipalindrome():
    '''
    Testeaza corectitudinea functiei is_antipalindrome(n)
    :return:
    '''
    assert isantipalindrom(2783) == True
    assert isantipalindrom(2773) == False
    assert isantipalindrom(81) == True
    assert isantipalindrom(121) == False

'''
8 Transformă un număr dat din baza 10 în baza 2. Numărul se dă în baza 10.

Funcția principală: get_base_2(n: str) -> str
Funcția de test: test_get_base_2()
'''

def get_base_2(n):
    '''
    Transforma un numar n din baza 10 in baza 2
    :param n: str
    :return: str
    '''
    a=int(n)
    nr=int(1)
    s=int(1)
    b=''
    c=''
    while s*2<=a:
        s*=2
        nr+=1
    while a > 0:
        if s<=a:
            a=a-s
            b+=str(1)
        else:
            b+=str(0)
        s/=2

    while s>=1:
        b+='0'
        s/=2
    return b


def test_get_base_2():
    '''
    Testeaza corectitudinea functiei get_base_2(n: str)
    :return:
    '''
    assert get_base_2(26) == '11010'
    assert get_base_2(0) == '0'
    assert get_base_2(41) == '101001'
    assert get_base_2(8) == '1000'

def main():
    while True:
        print('1. Găsește ultimul număr prim mai mic decât un număr dat..')
        print('2. Determină dacă un număr este antipalindrom.')
        print('3. Transformă un număr dat din baza 10 în baza 2.')
        print('x. Iesire din program - exit.')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            nr = int(input('Dati un numar: '))
            if nr<=2:
                print("Nu exista numar prim mai mic decat numarul dat.")
            else:
                print(get_largest_prime_below(nr))
        elif optiune == '2':
            nr = int(input('Dati un numar: '))
            print(isantipalindrom(nr))
        elif optiune == '3':
            numere_str = input('Dati un numar: ')
            print(get_base_2(numere_str))
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')

main()