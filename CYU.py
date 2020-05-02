import requests
import time
import webbrowser


def print_face_good():
    print("""
             OOOOOOOOOOO
         OOOOOOOOOOOOOOOOOOO
      OOOOOO  OOOOOOOOO  OOOOOO
    OOOOOO      OOOOO      OOOOOO
  OOOOOOOO  #   OOOOO  #   OOOOOOOO
 OOOOOOOOOO    OOOOOOO    OOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOO  OOOOOOOOOOOOOOOOOOOOOOOOO  OOOO
 OOOO  OOOOOOOOOOOOOOOOOOOOOOO  OOOO
  OOOO   OOOOOOOOOOOOOOOOOOOO  OOOO
    OOOOO   OOOOOOOOOOOOOOO   OOOO
      OOOOOO   OOOOOOOOO   OOOOOO
         OOOOOO         OOOOOO
             OOOOOOOOOOOO\n""")


def print_face_bad():
    print("""__________________________________________________
__________________________________________________
__________________10000000000011__________________
_______________10000000000000000001_______________
_____________00000000000000000000000______________
____________00000111000000001111100001____________
__________10001_______10001_______10001___________
_________1000__________11___________000___________
_________0001_____101_______11______1000__________
_________000______101_______11______1000__________
________10001___________1___________10001_________
________100001_________101_________100001_________
________10000001_____1000001_____10000001_________
_________0000000000000000000000000000000__________
_________1000000000001______100000000000__________
__________000000001____________100000001__________
___________0000001______________1000001___________
____________00000____10000001____00001____________
_____________0000__100000000000_1001____111_______
______1________0000000000000000001_____00000______
_____00000________11000000000001____1000000011____
_____00000001_____________________100000000000____
____0000000000001______________100000000000001____
____000000000000000011_____110000111______________
_________________0100000000000011__1______________
___________11_1100000001___1100000000000000001____
____0000000000000001___________110000000000000____
____00000000000011_________________110000000011___
_____000000001_________________________1000001____
_____100001_______________________________1001____
_______11_________________________________________""")


def print_face_cool():
    print("""_______§§_____§§§___§§§____§§§___§________§§
______§__§___§_____§___§__§___§__§_______§__§
______§__§___§_____§___§__§___§__§_______§__§
______§__§____§§§___§§§____§§§___§§§§____§__§
_§§____§__§_____________________________§__§____§§
§__§___§__§_____________________________§__§___§__§
§___§__§__§_____________________________§__§__§___§
_§___§__§__§___________________________§__§__§___§
__§___§§§§§§§_________________________§§§§§§§___§
___§____§___§_________________________§___§____§
____§§§§_____§_______________________§_____§§§§
___§___§__§§_§_________§§§§§_________§_§§__§___§
___§___§__§__§_______§§_____§§_______§__§__§___§
____§§§§§§___§______§_________§______§___§§§§§§
____§___§___§_§____§__8____8___§____§_§___§___§
_____§§§___§___§___§___________§___§___§___§§§
________§§§§§___§_§_____________§_§___§§§§§
_____________§§__§§_§§§§§§§§§§§_§§__§§
_______________§__§_§__§___§__§_§__§
________________§_§_§__§___§__§_§_§
_________________§§_§__§___§__§_§§
__________________§§_§_§___§_§_§§
___________________§__§§$0n§§__§
____________________§__§§§§§__§
_____________________§§_____§§
_______________________§§§§§""")


def print_face_lover():
    print('''                         oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                 oo             o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""  
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$       
                                """"$$$$$$$$$$$        
                                    $$$$$$$$$$$$       
                                     $$$$$$$$$$"''')


def universite_isim_cekme(url, ana_liste_isim):
    response = requests.get(url)
    with open("response.txt", "w") as file:
        file.write(response.content.decode('utf-8'))

    bolunmemis = response.content.decode('utf-8').split("<p>&nbsp;</p>")[0]
    for universite in bolunmemis.split('<td style="font-weight: 400;"')[1:]:
        if universite.find("Ü.") > -1:
            temp_name = universite.split('>')[1].split('<')[0].strip("\n")
            temp_name = temp_name.replace("İ", "I")

            temp_liste = [temp_name]
            ana_liste_isim.append(temp_liste)
        if universite.find("İZMİR YÜKSEK TEKNOLOJİ ENSTİTÜSÜ") > -1:
            temp_name = universite.split('>')[1].split('<')[0].strip("\n")
            temp_liste = [temp_name]
            ana_liste_isim.append(temp_liste)

    return ana_liste_isim


def universite_siralama_cekme(url, ana_liste_siralama):
    response = requests.get(url)
    bolunmemis = response.content.decode('utf-8').split("<p>&nbsp;</p>")[0]

    for universite in bolunmemis.split('width="75"')[2:]:
        temp_name = universite.split('>')[1].split('<')[0].strip("\n")
        temp_list = [temp_name]
        ana_liste_siralama.append(temp_list)
    for i in range(len(ana_liste_siralama), len(ana_liste_isim)):
        ana_liste_siralama.append("DOLMAD")

    return ana_liste_siralama


def sehir_cekme(url1, sehirler_liste_buyuk):
    response = requests.get(url1)
    with open("sehir.txt", "w") as file:
        file.write(response.content.decode('utf-8'))
    bolunmemis = response.content.decode('utf-8').split("<ol><li>")[1].split("<h3>İlgili başlıklar</h3>*")[0]
    for film in bolunmemis.split('<a')[1:]:
        sehirler_liste_buyuk.append(film.split('>')[1].split('<')[0])
    sehirler_liste_kucuk = sehirler_liste_buyuk.copy()
    sehirler_liste_fk = sehirler_liste_kucuk.copy()

    for b in range(0, len(sehirler_liste_buyuk)):
        sehirler_liste_buyuk[b] = sehirler_liste_buyuk[b].upper()

    for b in range(0, len(sehirler_liste_fk)):
        sehirler_liste_fk[b] = sehirler_liste_buyuk[b].lower()
    return sehirler_liste_buyuk


def offline_response_isim(response, ana_liste_isim):
    bolunmemis = response.split("<p>&nbsp;</p>")[0]

    for universite in bolunmemis.split('<td style="font-weight: 400;"')[1:]:

        if universite.find("Ü.") > -1:
            temp_name = universite.split('>')[1].split('<')[0].strip("\n")
            temp_name = temp_name.replace("İ", "I")

            temp_liste = [temp_name]
            ana_liste_isim.append(temp_liste)
        if universite.find("İZMİR YÜKSEK TEKNOLOJİ ENSTİTÜSÜ") > -1:
            temp_name = universite.split('>')[1].split('<')[0].strip("\n")
            temp_liste = [temp_name]
            ana_liste_isim.append(temp_liste)

    return ana_liste_isim


def offline_response_siralama(response, ana_liste_siralama):
    bolunmemis = response.split("<p>&nbsp;</p>")[0]

    for universite in bolunmemis.split('width="75"')[2:]:
        temp_name = universite.split('>')[1].split('<')[0].strip("\n")
        temp_list = [temp_name]
        ana_liste_siralama.append(temp_list)
    for i in range(len(ana_liste_siralama), len(ana_liste_isim)):
        ana_liste_siralama.append("DOLMADI")

    return ana_liste_siralama


def offline_response_sehir(response, sehirler_liste_buyuk):
    bolunmemis = response.split("<ol><li>")[1].split("<h3>İlgili başlıklar</h3>*")[0]
    for film in bolunmemis.split('<a')[1:]:
        sehirler_liste_buyuk.append(film.split('>')[1].split('<')[0])
    sehirler_liste_kucuk = sehirler_liste_buyuk.copy()
    sehirler_liste_fk = sehirler_liste_kucuk.copy()

    for b in range(0, len(sehirler_liste_buyuk)):
        sehirler_liste_buyuk[b] = sehirler_liste_buyuk[b].upper()

    for b in range(0, len(sehirler_liste_fk)):
        sehirler_liste_fk[b] = sehirler_liste_buyuk[b].lower()

    return sehirler_liste_buyuk

import pygame
pygame.init()

pygame.mixer.music.load("Noisestorm")
pygame.mixer.music.play()



try:
    ana_liste_isim = []
    ana_liste_siralama = []
    sehirler_liste_buyuk = []

    url = "https://www.universitego.com/bilgisayar-muhendisligi-2019-taban-puanlari-ve-basari-siralamalari/"
    url1 = "https://www.turkcebilgi.com/t%C3%BCrkiye%27nin_illeri"
    ana_liste_isim = universite_isim_cekme(url, ana_liste_isim)
    ana_liste_siralama = universite_siralama_cekme(url, ana_liste_siralama)
    sehirler_liste_buyuk = sehir_cekme(url1, sehirler_liste_buyuk)


except requests.exceptions.ConnectionError as errc:
    print("Error Connecting", errc)
    with open("response.txt", "r") as file:
        response = file.read()

    ana_liste_isim = offline_response_isim(response, ana_liste_isim)
    ana_liste_siralama = offline_response_siralama(response, ana_liste_siralama)

    with open("sehir.txt", "r") as file:
        response = file.read()
    sehirler_liste_buyuk = offline_response_sehir(response, sehirler_liste_buyuk)

print("Merhaba!")
print_face_good()
print(
    "CYU(Choose Your University)'ya hosgeldin!\nSanirim bilgisayar muhendisligi okumak gibi bir planin var.\nBelki de bu konuda sana yardimci olabilirim.\nEger siralamani benimle paylasirsan kazanabilecegin universiteleri sana listeleyebilirim. Ayrica universitenin bulundugu sehir hakkında da bilgiler verebilirim sana.")

while True:
    siralama = input("Lutfen sıralamanı gir.\n")
    if not siralama.isdigit():
        print("lütfen sayı girer misin :)")
    if siralama.isdigit():
        break
siralama = int(siralama)
import os
os.system("clear")
print("Girebilecegin universiteler geliyor. HAZIR MISIN?")

for i in range(10, 0, -1):
    print(i)
    if (i) == 3:
        time.sleep(1)
        print(i)
        time.sleep(1)
        print(i)
        time.sleep(1)
        print(i)
        print("Bozuldum gibi sanki")
        time.sleep(1)
        time.sleep(1)
        print("Ya da sen bir yer kazanamadın ???")
        time.sleep(1)
        print(i)
        time.sleep(1)
        print(i)
    time.sleep(1)
time.sleep(2)

if siralama >= 100000:
    if siralama <= 500000:
        print("Baya calismissin ya sınav sonucuna bakacak olursak:)")
elif siralama <= 10000:
    print("Tebrikler mukemmel bir siralaman var!")
    print_face_cool()
time.sleep(5)

counter = 0
for i in range(0, len(ana_liste_siralama)):
    counter += 1

    if ana_liste_siralama[i] == "DOLMADI":
        break

counter -= 1
counter1 = 1

if siralama > 500000:
    print_face_bad()
    print(
        "WOWOOWOWOW\nÜzgünüm dostum barajı geçememişsin. Seneye tekrar hazırlanman lazım :(\nSeneye güzel sonuçlar elde edebilmen dileğiyle...")
    exit()

if siralama > 299330:

    for i in range(counter, len(ana_liste_siralama)):

        index = i
        counter1 = 1
        print("-" * 80)
        for j in range(index, len(ana_liste_isim)):

            print(counter1, "-", "Universitenin Adi:", ana_liste_isim[j][0], "\nUniversitenin Siralamasi:",
                  ana_liste_siralama[j][0], end="", )
            if ana_liste_siralama[j][0] == "D":
                print("OLMADI", end="")
            print("")
            print("-" * 80)
            counter1 += 1
        break

else:

    for i in range(0, len(ana_liste_siralama)):
        sayi = int(ana_liste_siralama[i][0])
        if siralama <= sayi:

            index = i
            counter = 1
            print("-" * 80)
            for j in range(index, len(ana_liste_isim)):

                print(counter, "-", "Universitenin Adi:", ana_liste_isim[j][0], "\nUniversitenin Siralamasi:",
                      ana_liste_siralama[j][0], end="", )
                if ana_liste_siralama[j][0] == "D":
                    print("OLMADI", end="")
                print("")
                print("-" * 80)
                counter += 1
            break

islem = input("Lutfen hangi universiteyi tercih etmek istediginizi belirtin\n")
islem = int(islem) - 1
print("\n\n")
os.system("clear")
print(ana_liste_isim[index + islem][0], ana_liste_siralama[index + islem][0], end="")
if ana_liste_siralama[index + islem][0] == "D":
    print("OLMADI", end="")
print("")


word = ""
flag = False
for letter in ana_liste_isim[index + islem][0]:
    if letter == ".":
        flag = True
        continue
    if flag:
        if letter != " " and letter != "(" and letter != ")":
            word += letter

url_isim = word
url = "https://www.wikizero.com/tr/"

if url_isim.find("İ") == -1 or url_isim.find("I") == -1:
    url_isim = url_isim.lower()
print(url_isim)
url = url + url_isim

if url_isim == "":

    for d in range(0, len(sehirler_liste_buyuk)):

        if ana_liste_isim[index + islem][0].find("ISTANBUL") > -1:
            url_isim = "istanbul"
            url = url + url_isim
            break
        elif ana_liste_isim[index + islem][0].find(sehirler_liste_buyuk[d]) > -1:
            word = sehirler_liste_buyuk[d]

            url_isim = word.lower()
            if url_isim == "bartin":
                url_isim = "bartın"

            if url_isim == "aydin":
                url_isim = "aydın"

            if url_isim == "balikesir":
                url_isim = "balıkesir"

            if url_isim == "kirikkale":
                url_isim = "kırıkkale"
            if url_isim == "kirşehir":
                url_isim = "kırşehir"

            url = url + url_isim
            break

print("Bu arada dostum benden son bir kucuk tavsiye sakin sevgilinle ayni tercihleri yapma tamam mi")
print_face_lover()
time.sleep(7)
webbrowser.open(url)


