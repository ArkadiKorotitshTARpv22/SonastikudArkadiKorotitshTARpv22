from gtts import gTTS
import os
from random import*

def loe_failist(fail:str)->list:
    f=open(fail,"r",encoding="utf-8-sig")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend 

def kirjuta_failise(fail:str,jarjend:list):
    f=open(fail,"w",encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+"\n")
    f.close()

def Helista(text:str, keel:str):
    obj=gTTS(text=text, lang=keel,slow=False).save("helistaAK.mp3")
    os.system("helistaAK.mp3")

def translate(r:list,e:list):
    rr=len(e)
    language = int(input("Kui soovite tõlkida inglise keelest vene keelde-1\n Kui soovite tõlkida vene keelest inglise keelde-2\n"))
    if language==1:
        print(e)
        engsona = input("Kirjutage sõna, mida soovite tõlkida.\n")
        for jj in range (rr):
            if engsona == e[jj]:
                print(r[jj])
                print(f"{engsona} vene keeles {r[jj]}\n")
    if language==2:
        print(r)
        russona = input("Kirjutage sõna, mida soovite tõlkida.\n")
        for jj in range (rr):
            if russona == r[jj]:
                print(e[jj])
                print(f"{russona} inglise keeles {e[jj]}\n")
    return r,e

def test (r:list,e:list):
    oige = 0
    rr=len(e)
    kuipalju=int(input(f"Kui plaju sonad te tahate testiga,max{len(e)})))\n"))
    if kuipalju <= len(e):
        for j in range (kuipalju):
            random_word=choice(e)
            for jj in range (rr):
                if random_word == e[jj]:
                    answer=input(f"Tõlgi {random_word} vene keelde\n")
                    if answer == r[jj]:
                        oige +=1
    result = oige/kuipalju * 100
    print(f"Teie tulemus on {result}%")
    return r, e

def choose_sona(r:list, e:list):
    language = int(input("Millises keeles soovite sõna kuulda\n1-inglise keeles\n2-vene keeles\n"))
    rr = len(e)
    if language == 1:
        print(e)
        sona = input("Kirjutage sõna, mida soovite kuulda\n")
        for jj in range(rr):
            if sona == e[jj]:
                return sona
    elif language == 2:
        print(r)
        sona = input("Kirjutage sõna, mida soovite kuulda\n")
        for jj in range(rr):
            if sona == r[jj]:
                return sona

def mudasona (r:list,e:list): 
    sona=input("Kirjutage sõna, mida soovite muuta\n")
    if sona in r:
        sonachange=input("Kirjutage muudetud sõna\n")
        ind=r.index(sona)
        e.pop(ind)
        e.insert(ind, sonachange)
    elif sona in e:
        sonachange=input("Kirjutage muudetud sõna\n")
        ind=e.index(sona)
        e.pop(ind)
        e.insert(ind, sonachange)
    return r,e

def addsona (r:list,e:list):
    engsona = input("Kirjutage sõna, mida soovite lisada inglise keeles\n")
    russona = input("Nüüd kirjutage selle venekeelne tõlge\n")
    e.append(engsona)
    r.append(russona)
    print (r, e)
    return r, e

def tolkida (r:list,e:list):
    sona=input("Kirjutage sõna, mida tõlgide\n")
    if sona in r:
        ind=r.index(sona)
        print(f"{sona} on inglise {e[ind]}\n")
    elif sona in e:
        ind=e.index(sona)
        print(f"{sona} on vene {r[ind]}\n")
    else:
        v=int(input("Sõnad, mida sõnaraamatus ei ole, kas soovite seda lisada? (print_1)\n"))
        if v == 1:
            addsona(r,e)