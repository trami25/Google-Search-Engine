
from trie import Trie
from graph import Graph
from parser_fax import *
import os
import time
graf=[]
sta=[]
sve_stavke={}
dict_link={} #vezuje link za 
dict_word={}
svi_html_fajlovi=[]
trie_dict={}
graph=Graph(True)
parser=Parser()

def merge(a,b,lista):
    i=j=0
    while i+j<len(lista):
        if j ==len(b) or (i<len(a) and a[i]<b[j]):
            lista[i+j]=a[i]
            i+=1
        else:
            lista[i+j]=b[j]
            j+=1

def sort1(lista_vrednosti):
    n=len(lista_vrednosti)
    if n<2:
        return
    a=lista_vrednosti[0:n//2]
    b=lista_vrednosti[n//2:n]
    sort1(a)
    sort1(b)
    merge(a,b,lista_vrednosti)

def get_key(val,lista,povez):
    
    for key, value in povez.items():
         if val == value:
            if key not in lista:
                return key
def prikaz(i,pit,brojevi,povez,mogu,pov):
    lista=[]
    i=1
    j=0 
    for a in mogu:
        for broj in brojevi:
            if i<=pit: 
                ej=get_key(broj,lista,povez)
                if ej not in lista:
                    lista.append(ej)
                
                print(str(i),". ",ej, " : ",str(broj))
                if a in pov[ej]:
                    if i==1:
                    
                        for word in pov[ej]:
                        
                            if word!=a:
                                j+=1
                            else:
                                index=j
                                break
            
                            

                        if index>1 and index!=len(pov[ej])-1 and index!=len(pov[ej])-2:
                            print('...',pov[ej][index-2],\
                            pov[ej][index-1],\
                            pov[ej][index],\
                            pov[ej][index+1],\
                            pov[ej][index+2],'....')
                        elif index==1:
                            print('...',pov[ej][index-1],\
                        pov[ej][index],\
                        pov[ej][index+1],\
                        pov[ej][index+2],\
                        pov[ej][index+3],'....')
                        elif index==0:
                            print(pov[ej][index],\
                        pov[ej][index+1],\
                        pov[ej][index+2],\
                        pov[ej][index+3],'....')
                        elif index==len(pov[ej])-1:
                            print('...',pov[ej][index-3],\
                        pov[ej][index-2],\
                        pov[ej][index-1],\
                        pov[ej][index])
                        elif index==len(pov[ej])-2:
                            print('...',pov[ej][index-2],\
                        pov[ej][index-1],\
                        pov[ej][index],\
                        pov[ej][index+1])
                    i+=1    
                else:
                    i+=1
                    continue        
    
def pretraga1(mogu,trenutni,pov):
    svi=[]
    y=[]
    svi_fajlovi=file_opening(trenutni,svi)
    linkovi=[]
    brojevi=[]
    n=0
    broj=0
    for d in svi_fajlovi:
        for t in svi_html_fajlovi:
            if  t==d:
                trie=Trie()
#            print(dict_word.keys())
#            print(len(dict_word.keys()))
                if d in pov.keys():
                    for word in pov[d]:
                        trie.insert(word)
                    for word in mogu:
                        all=trie.query(word)
                        if len(all)!=0:
                            for a in all:
                                broj+=int(a[1])  
                    if broj!=0:
                        linkovi.append(d)
                        q=0
                        for b in graph.vertices():
                            if str(b)==d:
                                q=graph.degree(b,False)
                                break
                        y.append(q) 
                        n=broj*1.255+q*2.255    
                        brojevi.append(n)
                        trie_dict[d]=n
                        break
                    else:
                        break
    sort1(brojevi)
    print(y)
    brojevi.reverse()
    while True:
            try:
                pit=int(input('Koliko rezultata pretrage zelite? '))
            except ValueError:
                print('MORATE UNETI CEO BROJ!')
                continue
            else:
                if pit>=len(linkovi):
                        print('PRIKAZ REZULTATA! ')
                        print('------------')
                        print('UKUPNO: ',len(linkovi))
                        prikaz(i,len(linkovi),brojevi,trie_dict,mogu,pov)
                        dan=input('Zelite li menjati broj rezultata? (da/ne)')
                        while dan not in ('da','ne'):
                            print('PROBAJTE PONOVO JER NISTE UNELI DOBAR PODATAK')
                        if dan=='da':
                            continue
                        else:
                            break    

        
                else:
                    print('PRIKAZ REZULTATA! ')
                    print('UKUPNO: ',len(linkovi))
                    prikaz(i,pit,brojevi,trie_dict,mogu,pov)
                    dan=input('Zelite li menjati broj rezultata? (da/ne)')
                    while dan not in ('da','ne'):
                            print('PROBAJTE PONOVO JER NISTE UNELI DOBAR PODATAK')
                    if dan=='da':
                            continue
                    else:
                            break   

def pretraga2(mogu,ne_mogu,trenutni,pov):
    dostupni=[]
    tr=None
    svi=[]
    svi_fajlovi=file_opening(trenutni,svi)
    linkovi=[]
    brojevi=[]
    n=0
    pretrage={}
    for d in svi_fajlovi:
        for t in svi_html_fajlovi:
            if  t==d:
                trie=Trie()
                if d in pov.keys():
                    for word in pov[d]:
                        trie.insert(word)
                    for e in ne_mogu:    
                        if trie.search(e):
                            break
                        else:
                            dostupni.append(d)
                    for word in mogu:
                        broj=0
                        all=trie.query(word)
                        if len(all)!=0:
                            for a in all:
                                broj+=a[1]
                        pretrage[word]=broj
                    break
    
    if len(pretrage.keys())!=1:
            pass
    for d in dostupni:   
                    linkovi.append(d)
                    q=0
                    for b in graph.vertices():
                        if str(b)==d:
                            q=graph.degree(b,False)
                            break 
                        n=broj*1.255+q*2.25    
                        brojevi.append(n)
                        trie_dict[d]=n
    sort1(brojevi)
    brojevi.reverse()
    while True:
            try:
                pit=int(input('Koliko rezultata pretrage zelite? '))
            except ValueError:
                print('MORATE UNETI CEO BROJ!')
                continue
            else:
                if pit>=len(linkovi):
                        print('PRIKAZ REZULTATA! ')
                        print('------------')
                        print('UKUPNO: ',len(linkovi))
                        prikaz(i,len(linkovi),brojevi,trie_dict,mogu,pov)
                        dan=input('Zelite li menjati broj rezultata? (da/ne)')
                        while dan not in ('da','ne'):
                            print('PROBAJTE PONOVO JER NISTE UNELI DOBAR PODATAK')
                        if dan=='da':
                            continue
                        else:
                            break    
                else:
                    print('PRIKAZ REZULTATA! ')
                    print('UKUPNO: ',len(linkovi))
                    prikaz(i,pit,brojevi,trie_dict,mogu,pov)
                    dan=input('Zelite li menjati broj rezultata? (da/ne)')
                    while dan not in ('da','ne'):
                        print('PROBAJTE PONOVO JER NISTE UNELI DOBAR PODATAK')
                        if dan=='da':
                            continue
                        else:
                            break    

def pretraga3(mogu,mora,trenutni,pov):
    dostupni=[]
    o=len(mora)
    tr=None
    p=0
    svi=[]
    svi_fajlovi=file_opening(trenutni,svi)
    linkovi=[]
    brojevi=[]
    n=0
    pretrage={}
    for d in svi_fajlovi:
        for t in svi_html_fajlovi:
            if  t==d:
                trie=Trie()
                if d in pov.keys():
                    for word in pov[d]:
                        trie.insert(word)
                    for e in mora:    
                        if  trie.search(e):
                            p+=1
                    if p==o:
                        dostupni.append(d)

                        for word in mora:
                            broj=0
                            all=trie.query(word)
                            if len(all)!=0:
                                for a in all:
                                    broj+=a[1]
                            pretrage[word]=broj
                        break
    if len(pretrage.keys())!=1:
            pass
    for d in dostupni:   
                    linkovi.append(d)
                    q=0
                    for b in graph.vertices():
                        if str(b)==d:
                            q=graph.degree(b,False)
                            break 
                        n=broj*1.255+q*2.25    
                        brojevi.append(n)
                        trie_dict[d]=n
    sort1(brojevi)
    brojevi.reverse()
    while True:
            try:
                pit=int(input('Koliko rezultata pretrage zelite? '))
            except ValueError:
                print('MORATE UNETI CEO BROJ!')
                continue
            else:
                if pit>=len(linkovi):
                        print('PRIKAZ REZULTATA! ')
                        print('------------')
                        print('UKUPNO: ',len(linkovi))
                        prikaz(i,len(linkovi),brojevi,trie_dict,mora,pov)
                        dan=input('Zelite li menjati broj rezultata? (da/ne)')
                        while dan not in ('da','ne'):
                            print('PROBAJTE PONOVO JER NISTE UNELI DOBAR PODATAK')
                        if dan=='da':
                            continue
                        else:
                            break    
                else:
                    print('PRIKAZ REZULTATA! ')
                    print('UKUPNO: ',len(linkovi))
                    prikaz(i,pit,brojevi,trie_dict,mora,pov)
                    dan=input('Zelite li menjati broj rezultata? (da/ne)')
                    while dan not in ('da','ne'):
                        print('PROBAJTE PONOVO JER NISTE UNELI DOBAR PODATAK')
                        if dan=='da':
                            continue
                        else:
                            break  



def searching(mogu, ne_mogu,mora,trenutni,povez):
    if len(ne_mogu)==0 and len(mora)==0:
#        print('NEMA NEPOTREBNIH RECI') 
#        print('NEMA OBAVEZNIH RECI')
        pretraga1(mogu,trenutni,povez)
    elif len(ne_mogu)==0 or len(mora)==0:
        if len(ne_mogu)>len(mora)==0:
            pretraga2(mogu, ne_mogu,trenutni,povez)
        else:
            pretraga3(mogu,mora,trenutni,povez)
    

def pitanjce(trenutni_folder,i,dict_word):
    index,s=listanje_direktorijuma(trenutni_folder,i)
    pita=input('Da li želite da idete dublje? (da ili ne)').lower()
    while pita not in ("da","ne"):
        print("Niste uneli dobar podatak, probajte ponovo!")
        pita=input('Da li želite da idete dublje? (da ili ne)').lower()
    if pita=="ne":
        pass
    else:
        main(trenutni_folder,i,dict_word)
    pitanje=input('Da li želite da pretražujete trenutni folder? (da ili ne)').lower()
    while pitanje not in ("da","ne"):
        print("Niste uneli dobar podatak, probajte ponovo!")
        pitanje=input('Da li želite da pretražujete trenutni folder? (da ili ne)').lower()
    if pitanje!="ne":
        b=0
        if len(s)!=0:
            for st in s: 
                b+=1
        if b==0:
            print('U ovom folderu nema html fajlova!')
        else:
            making_of(trenutni_folder,dict_word)
    

def main(root,ind,dict_word):
    
    while True:
        index,s=listanje_direktorijuma(root,ind)
        try:
            upit=int(input('Koju stavku biste hteli da pregledate? (Unesite broj ili 0 za nazad ili 00 za izlaz iz aplikacije ) '))
        except ValueError:
            print('NISTE UNELI DOBAR PODATAK, TREBA  BROJ ILI 0 ZA IZLAZ DA SE UPIŠE')
            continue
        else:
            if str(upit)=="0":
                break
            elif str(upit)=="00":
                exit()  
            elif upit not in sve_stavke.keys():
                    print("Ne postoji stavka pod ovim brojem")
                    continue
            else:
                stavka=sve_stavke[upit]
        f = os.path.join(root,stavka)
        if os.path.isfile(f):
            print('Ovo je dokument!')
        else:
            pitanjce(f,index,dict_word)
         
def listanje_direktorijuma(root,i):
    sta=[]
    for u in os.listdir(root):
        f = os.path.join(root,u)
        
        sve_stavke[i]=u
        if f[-4:]=='html':
            sta.append(u)
        print(i,' ',u)
        i+=1
    return i,sta
    
def file_opening(root,svi): #lista sve do fajlova i izdvaja ih
    for filename in os.listdir(root):
        f = os.path.join(root,filename)
        if os.path.isfile(f):
            svi.append(f)
        else:
           file_opening(f,svi)

    return svi
        
def priprema(root_dic): #broji html fajlove i izdvaja ih zasebno
    index=0
    svi=[]
    broj_fajlova=0
    
    svi_fajlovi=file_opening(root_dic,svi)
    for ef in svi_fajlovi:
        if ef[-4:]=="html":
            svi_html_fajlovi.append(ef)  #stavlja html fajlove na jedno mesto
            index+=1
            broj_fajlova+=1
    return broj_fajlova,svi_fajlovi  #vraca broj html fajlova

def making_of(trenutni_folder,povez):
    while True:
        ne=[]
        da=[]
        a=input('Pretraga:  ')
        a=a.strip().split(' ')
        o=len(a)
        #print(a)
        if o==0:
            print('Niste uneli podatak za pretragu')
            continue
        
        elif 'AND' ==a[o-1] or 'OR' ==a[o-1] or 'NOT' ==a[o-1]:
            print('Niste uneli drugi podatak za pretragu')
            continue
        else:
            for u in range(o):
                if a[u]=='NOT':
                    j=u+1
                    for i in range(j,o):
                        ne.append(a[i])
                    a.remove(a[u])
                    break
                elif a[u]=='AND':
                    for i in range(o):
                        da.append(a[i])
                    da.remove(a[u])
                    break
                elif a[u]=='OR':
                    a.remove(a[u])
                    break
                
    #           print('Reci bez oznaka')
                searching(a,ne,da,trenutni_folder,povez)
                break
        p=input('Da li zelite da pretrazujete dalje?: (da ili ne)').lower()
        while p not in ("da","ne"):
            print("Niste uneli dobar podatak, probajte ponovo!")
            p=input('Da li zelite da pretrazujete dalje?: (da ili ne)').lower()
        if p =='ne':
            break
        else:
            continue    

   
#    if i==0:
#        print("U ovom folderu nema sajtova za pretraživanje!")
            
if __name__=='__main__':
    root_dic="C:\\Users\\mniko\\Fakultet\\python-2.7.7-docs-html"    #pocetni direktorijum
    i=1
    print("DOBRO DOŠLI U GOOGLE!")
    broj_html_fajlova,svi_fajlovi=priprema(root_dic) # funkcija koja izdvaja sve html fajlove na jedno mesto
#    print(broj_html_fajlova)
    lista_linkova=[]
    lista_reci=[]
#    print(svi_html_fajlovi)
    for ef in svi_fajlovi:
        j=0
        for e in graph.vertices():
            if str(e)==ef:
                j+=1
        if j==0:
                efi=graph.insert_vertex(ef)
                
                lista_linkova,lista_reci=parser.parse(ef)
                dict_link[ef]=lista_linkova
                dict_word[ef]=lista_reci
                for link in lista_linkova:
                    for e in graph.vertices():
                        if str(e)==link:
                            j+=1
                    if j==0:
                        efit=graph.insert_vertex(link)
                        graph.insert_edge(efi,efit,link)

#    print(graph.edge_count(),graph.vertex_count())
    pitanjce(root_dic,i,dict_word)
    while True:
        main(root_dic,i,dict_word)