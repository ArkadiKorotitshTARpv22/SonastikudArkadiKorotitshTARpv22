print("tehtud Arkadi Korotitsh TARpv22 poolt")

from sonastikmodule import*

laused=[]
russian=[]
english=[]
russian=loe_failist("russian.txt")
print(russian)
english=loe_failist("english.txt")
print(english)
while True:
    v=int(input("1-lisada kõik muudatused-\n2-tõlkida sõna-\n3-lisada sõna-\n4-muuta sõna-\n5-testige oma teadmisi-\n6-kuulata sõna-\n"))
    if v==1:
        for jj in range (len(russian)):
            line=russian[jj]
            laused.append(line)
        kirjuta_failise("russian.txt",laused)
        laused=[]
        for j in range (len(english)):
            line=english[j]
            laused.append(line)
        kirjuta_failise("english.txt",laused)
    elif v==2:
        tolkida(russian, english)
    elif v==3:
        russian, english=addsona(russian, english)
    elif v==4:
        russian, english=mudasona(russian, english)
    elif v==5:
        russian, english=test(russian, english)
        for jj in range (len(russian)):
            line=russian[jj]
            laused.append(line)
        kirjuta_failise("laused.txt",laused)
    elif v==6:
        laused=[]
        sona = choose_sona(russian, english)
        for jj in range (len(russian)):
            if sona == english[jj]:
                text = sona
                laused.append(text)
                Helista(laused[0],"en")
        text = sona
        laused.append(text)
        Helista(laused[0],"ru")
