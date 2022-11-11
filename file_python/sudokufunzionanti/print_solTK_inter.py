import itertools
numeri=[x for x in range(1,10)]
per=[]

from datetime import datetime
from datetime import datetime
inizio = datetime.now() # t



#PARTE CHE CONTROLLA SUDOKU CHE NON CI SIANO ERRORI FUNZIONA
#PARTE DA AGGIUNGERE ASSEGNA ANDANDO A TENTATIVI QUANDO LE SOLUZIONI PER OGNI POSIZIONE SONO PIU DI UNA
###################à
#PER ORA DA'SOLUZIONI CORRETTE ANCHE SE NON ACNORA LA DEFINITIVA_
#possibile algoritmo: prima scorro per filtrare tutte permutazioni in base alle cifre iniziali,poi filtro ulteriormente in base alle colonne e quadrati
#poi guardo se nel dizionario ci sono delle posizioni che hanno una sola soluzione
#se si la assegno in quella posizione, guardo anche se in seguito il filtraggio
#e stata trovata la soluzione di una intera riga, se si la assegno al sudoku
#risolve sudoku generico
def Sudoku():
    Sudoku.var=""
Sudoku()
#def sudokupiudifficileinparterisolto():
def ciao():
    a=["", "", '', '', 8, 1, '', 6, ""]#sudoku in parte risolto da altra versione dl programma
    b=[3, "", 5, "", "", 9, "", 4, ""]
    c=['', '', '', '', '', '', '', 5, 8]
    d=['', 5, 4, '', 7, '', 1, '', '']
    e=['', 2, '', '', '', '', '', 8, '']
    f=[1, '', 9, '', '', '', 7, '', '']
    g=['', '', '', 3, '', '', '', '', '']
    h=['', '', '', '', '', 2, 4, '', 9]

    k=['', '', 1, '', '', '', '', 2, ""]

#def sudokufacile():
a=["",4,1,"","",9,6,"",8]#LISTA COMBINAZIONI RIGA 7 SE FILTRATA IN BASE ALLE COMBINAZIONE DELLA RIGA 2 VIENE RIDOTTA DA CIRCA 40000 A 16687 COMBINAZIONI POSSIBILI

b=[6,"","","","","","",3,""]

c=["","","",2,7,"","",9,""]

d=["",8,"","","","",1,5,""]
e=[3,5,"","","","","","",""]
f=["","","","",6,8,"",2,""]

g=[7,"",8,"","",5,"","",4]
h=["","",9,4,"","",7,"",3]
k=["","","",1,"","",2,"",""]


def sudokuhard():   
	a=['', '', '4', '7', '5', '', '', '6', '']
	b=['', '', '2', '', '3', '8', '4', '', '']#ci mette troppo a risolverlo perchè non trova soluzioni uniche per una cella
	c=['3', '6', '', '', '', '', '', '', '']
	d=['', '3', '9', '', '', '', '', '', '1']
	e=['7', '', '1', '', '', '', '', '', '']
	f=['', '', '', '4', '', '1', '', '9', '6']
	g=['1', '', '', '9', '', '3', '', '8', '']
	h=['', '2', '', '', '', '', '', '', '4']
	k=['', '', '', '', '8', '', '', '5', '']  
def sudokudifficile():
	a= ['', '', '3', '2', '', '', '1', '', '']
	b= ['', '', '', '9', '', '', '4', '', '']
	c= ['2', '', '9', '8', '', '', '', '6', '']
	d= ['', '', '6', '', '', '5', '7', '', '']
	e= ['', '7', '', '', '', '3', '', '4', '']
	f= ['4', '9', '', '', '', '', '', '', '']
	g= ['', '', '2', '', '', '1', '6', '', '']
	h= ['', '', '7', '3', '', '', '', '', '8']
	k= ['', '', '', '', '', '', '', '', '']




#a=["",4,1,"","",9,6,"",8] intervallo 0 - 8
#LISTA COMBINAZIONI RIGA 7 SE FILTRATA IN BASE ALLE COMBINAZIONE DELLA RIGA 2 VIENE RIDOTTA DA CIRCA 40000 A 16687 COMBINAZIONI POSSIBILI

#b=[6,"","","","","","",3,""]intervallo 9 - 17

#c=["","","",2,7,"","",9,""]intervallo 18 - 26

#d=["",8,"","","","",1,5,""]intervallo 27 - 35
#e=[3,5,"","","","","","",""]intervallo36 - 44
#f=["","","","",6,8,"",2,""]intervallo45 - 53

#g=[7,"",8,"","",5,"","",4]intervallo54 - 62
#h=["","",9,4,"","",7,"",3]intervallo 63 -71
#k=["","","",1,"","",2,"",""]intervallo 72 -80
#filtra all'inizio solamente in base alle cifre iniziali e poi in base ai quadrati e le colonne
Sudoku.var=[a,b,c,d,e,f,g,h,k]
for x in Sudoku.var:
    print(len(x))

for x in Sudoku.var:
    print(x)
def lista_sol():
    lista_sol.var=[]
lista_sol()
def filtro_iniziale():
    print("execute initial filtering")
    sol1,sol2,sol3,sol4,sol5,sol6,sol7,sol8,sol9=[],[],[],[],[],[],[],[],[]
    conta_sud=-1
    lista_ind1,lista_ind2,lista_ind3,lista_ind4,lista_ind5,lista_ind6,lista_ind7,lista_ind8,lista_ind9=[],[],[],[],[],[],[],[],[]

    s1,s2,s3,s4,s5,s6,s7,s8,s9=[],[],[],[],[],[],[],[],[]
    lista_lista_ind=[lista_ind1,lista_ind2,lista_ind3,lista_ind4,lista_ind5,lista_ind6,lista_ind7,lista_ind8,lista_ind9]
    lista_s=[s1,s2,s3,s4,s5,s6,s7,s8,s9]
    lista_sol.var=[sol1,sol2,sol3,sol4,sol5,sol6,sol7,sol8,sol9]
    for sud in Sudoku.var:#FILTRA IN BASE CIFRE INIZIALI IN MODO CHE RIMANGANO NELLA LORO POSIZIONE
        #print(sud)
        conta_sud=conta_sud+1


        for x1 in numeri:
            if x1 not in sud:
                #print(x1)
                lista_s[conta_sud].append(x1)

        for x in range(0,len(a)):
            if sud[x]=="":
                index1=x

                lista_lista_ind[conta_sud].append(index1)#fino a qui funziona



        for v in itertools.permutations(lista_s[conta_sud]):
            lista=["","","","","","","","",""]

            conta=-1
           # print(v)

            for x3 in sud:
                conta=conta+1
              #  print(conta)
                #print(x3)


                for j ,y in zip(lista_lista_ind[conta_sud],v):
                    if x3=="":
                        lista[j]=y
                    else:
                        lista[conta]=x3

            lista_sol.var[conta_sud].append(lista)      

    #ALGORITMO PER FILTRARE -->PER ESEMPIO PER OGNI RIGA FAR SCORRERE TUTTE LE ALTRE
    for x in lista_sol.var:
        print(len(x))
    print("###############")
    print()
filtro_iniziale()
def assegno_singola_cifra():
    print("esec function")
    for int_chiave in range(len(dizio.var)):
        if str(int_chiave) in dizio.var:
            if len(dizio.var[str(int_chiave)][0])==1:#se ho la certezza che una cifra sia la soluzione in quella posizione, la assegno
                print("dizio",dizio.var[str(int_chiave)])
                Sudoku.var[dizio.var[str(int_chiave)][1][0]][dizio.var[str(int_chiave)][1][1]]=dizio.var[str(int_chiave)][0][0]
    #for j in lista_sol[1]:
                print("cifra assegnata=",dizio.var[str(int_chiave)][0][0],"       posizione ",dizio.var[str(int_chiave)][1][0],dizio.var[str(int_chiave)][1][1])
    
quadrato1=Sudoku.var[0][0:3]+Sudoku.var[1][0:3]  +Sudoku.var[2][0:3]
quadrato2=Sudoku.var[0][3:6]+Sudoku.var[1][3:6]  +Sudoku.var[2][3:6]
quadrato3=Sudoku.var[0][6:9]+Sudoku.var[1][6:9]   +Sudoku.var[2][6:9]         

quadrato4=Sudoku.var[3][0:3]+Sudoku.var[4][0:3]  +Sudoku.var[5][0:3]
quadrato5=Sudoku.var[3][3:6]+Sudoku.var[4][3:6]  +Sudoku.var[5][3:6]
quadrato6=Sudoku.var[3][6:9]+Sudoku.var[4][6:9]   +Sudoku.var[5][6:9]    

quadrato7=Sudoku.var[6][0:3]+Sudoku.var[7][0:3]  +Sudoku.var[8][0:3]
quadrato8=Sudoku.var[6][3:6]+Sudoku.var[7][3:6]  +Sudoku.var[8][3:6]
quadrato9=Sudoku.var[6][6:9]+Sudoku.var[7][6:9]   +Sudoku.var[8][6:9] 
def dizio():
        dizio.var={}
dizio()
#serve per memorizzare le cifre che ho già usato
conta=-1#posizionisudoku da 0 a 80(per sudoku 9x9) , posizioni da 0 a 35 (sudoku6x6)

def algoritmo():
    conta=-1

    lista_cif=[]
    lista=[]

    lista_pos=[]

    for volte in range(0,len(numeri)):


                for j,z in zip(Sudoku.var[volte],range(len(Sudoku.var[volte]))):#faccio scorrere una riga alla volta
                        conta=conta+1
                        riga=Sudoku.var[volte]
                        colonna= [row[z] for row in Sudoku.var] 
                        #print(riga)
                        #print(colonna)
                        #print("lkjdfkdfj",lista_riga)

                     #  print("riga",riga)
                      #  print("colonna",colonna)
                     
                        #elif len(numeri)==9:
                        quadrato1=Sudoku.var[0][0:3]+Sudoku.var[1][0:3]  +Sudoku.var[2][0:3]
                        quadrato2=Sudoku.var[0][3:6]+Sudoku.var[1][3:6]  +Sudoku.var[2][3:6]
                        quadrato3=Sudoku.var[0][6:9]+Sudoku.var[1][6:9]   +Sudoku.var[2][6:9]         

                        quadrato4=Sudoku.var[3][0:3]+Sudoku.var[4][0:3]  +Sudoku.var[5][0:3]
                        quadrato5=Sudoku.var[3][3:6]+Sudoku.var[4][3:6]  +Sudoku.var[5][3:6]
                        quadrato6=Sudoku.var[3][6:9]+Sudoku.var[4][6:9]   +Sudoku.var[5][6:9]    

                        quadrato7=Sudoku.var[6][0:3]+Sudoku.var[7][0:3]  +Sudoku.var[8][0:3]
                        quadrato8=Sudoku.var[6][3:6]+Sudoku.var[7][3:6]  +Sudoku.var[8][3:6]
                        quadrato9=Sudoku.var[6][6:9]+Sudoku.var[7][6:9]   +Sudoku.var[8][6:9] 

                        if Sudoku.var[volte][z]=="":
                                lista_pos=[volte,z]
                                if z<=2:
                                    for cif in numeri:

                                        if volte==0 or volte==1 or volte==2:
                                            if cif not in colonna and cif not in riga and cif not in quadrato1:


                                                lista_cif.append(cif)

                                                lista=[lista_cif,lista_pos]
                                                dizio.var[str(conta)]=lista
                                                #  break
                                        elif volte==3 or volte==4 or volte==5:
                                            if cif not in colonna and cif not in riga and cif not in quadrato4:    
                                                lista_cif.append(cif)

                                                lista=[lista_cif,lista_pos]
                                                dizio.var[str(conta)]=lista

                                        elif volte==6 or volte==7 or volte==8:
                                            if cif not in colonna and cif not in riga and cif not in quadrato7:

                                                lista_cif.append(cif)

                                                lista=[lista_cif,lista_pos]
                                                dizio.var[str(conta)]=lista

                                elif 3<=z<=5:
                                        for cif in numeri:
                                            if volte==0 or volte==1 or volte==2:
                                                if cif not in colonna and cif not in riga and cif not in quadrato2:
                                                    lista_cif.append(cif)

                                                    lista=[lista_cif,lista_pos]
                                                    dizio.var[str(conta)]=lista
                                            elif volte==3 or volte==4 or volte==5:
                                                if cif not in colonna and cif not in riga and cif not in quadrato5:    
                                                        lista_cif.append(cif)

                                                        lista=[lista_cif,lista_pos]
                                                        dizio.var[str(conta)]=lista 
                                            elif volte==6 or volte==7 or volte==8:
                                                if cif not in colonna and cif not in riga and cif not in quadrato8:      
                                                        lista_cif.append(cif)

                                                        lista=[lista_cif,lista_pos]
                                                        dizio.var[str(conta)]=lista

                                                       # Sudoku.var[volte][z]=cif
                                else:
                                        for cif in numeri:
                                            if volte==0 or volte==1 or volte==2:
                                                if cif not in colonna and cif not in riga and cif not in quadrato3:
                                                        lista_cif.append(cif)

                                                        lista=[lista_cif,lista_pos]
                                                        dizio.var[str(conta)]=lista
                                            elif volte==3 or volte==4 or volte==5:
                                                if cif not in colonna and cif not in riga and cif not in quadrato6:    
                                                        lista_cif.append(cif)

                                                        lista=[lista_cif,lista_pos]
                                                        dizio.var[str(conta)]=lista  
                                            elif volte==6 or volte==7 or volte==8:
                                                if cif not in colonna and cif not in riga and cif not in quadrato9:      


                                                        lista_cif.append(cif)

                                                        lista=[lista_cif,lista_pos]
                                                        dizio.var[str(conta)]=lista

                        else:
                            pass
                   # if j=="":a

                         #   pass


                        lista_cif=[]
                        lista_pos=[]
                        lista=[]
    print("dizio.var",dizio.var)
algoritmo()
def controllo_ok():
    controllo_ok.var=""
controllo_ok()
def crea_funzione_check_colonne_e_quadrati():#controlla le righe ma adesso modifica la definizione di sudoku
    #ignoro i "" nelle colonne e quadrati
                        colonna1= [row[0] for row in Sudoku.var]

                        colonna2=    [    row[1]   for row in Sudoku.var]
                        colonna3=      [       row[2] for row in Sudoku.var ]
                        colonna4=      [      row[3]  for row in Sudoku.var ]
                        colonna5=      [       row[4] for row in Sudoku.var ]
                        colonna6=      [       row[5]  for row in Sudoku.var]
                        colonna7=      [       row[6]  for row in Sudoku.var]
                        colonna8=      [       row[7]  for row in Sudoku.var]

                        colonna9=      [       row[8]  for row in Sudoku.var]

                        if len(Sudoku.var)==9:
                            quadrato1=Sudoku.var[0][0:3]+Sudoku.var[1][0:3]  +Sudoku.var[2][0:3]
                            quadrato2=Sudoku.var[0][3:6]+Sudoku.var[1][3:6]  +Sudoku.var[2][3:6]
                            quadrato3=Sudoku.var[0][6:9]+Sudoku.var[1][6:9]   +Sudoku.var[2][6:9]         

                            quadrato4=Sudoku.var[3][0:3]+Sudoku.var[4][0:3]  +Sudoku.var[5][0:3]
                            quadrato5=Sudoku.var[3][3:6]+Sudoku.var[4][3:6]  +Sudoku.var[5][3:6]
                            quadrato6=Sudoku.var[3][6:9]+Sudoku.var[4][6:9]   +Sudoku.var[5][6:9]    

                            quadrato7=Sudoku.var[6][0:3]+Sudoku.var[7][0:3]  +Sudoku.var[8][0:3]
                            quadrato8=Sudoku.var[6][3:6]+Sudoku.var[7][3:6]  +Sudoku.var[8][3:6]
                            quadrato9=Sudoku.var[6][6:9]+Sudoku.var[7][6:9]   +Sudoku.var[8][6:9] 
                            CHECK_riga=[x for x in Sudoku.var]
                            CHECK_colonna=[colonna1,colonna2,colonna3,colonna4,colonna5,colonna6,colonna7,colonna8,colonna9]
                            CHECK_quadrato=[quadrato1,quadrato2,quadrato3,quadrato4,quadrato5,quadrato6,quadrato7,quadrato8,quadrato9]
                       # print("checkcolonna",CHECK_colonna)    
                          
                        if len(Sudoku.var)==6:#per controllo finale 
                            quadrato1=Sudoku.var[0][0:3]+Sudoku.var[1][0:3]  +Sudoku.var[2][0:3]
                            quadrato2=Sudoku.var[0][3:6]+Sudoku.var[1][3:6]  +Sudoku.var[2][3:6]
                            quadrato3=Sudoku.var[0][6:9]+Sudoku.var[1][6:9]   +Sudoku.var[2][6:9]         

                            quadrato4=Sudoku.var[3][0:3]+Sudoku.var[4][0:3]  +Sudoku.var[5][0:3]
                            quadrato5=Sudoku.var[3][3:6]+Sudoku.var[4][3:6]  +Sudoku.var[5][3:6]
                            quadrato6=Sudoku.var[3][6:9]+Sudoku.var[4][6:9]   +Sudoku.var[5][6:9]  
                            CHECK_riga=[Sudoku.var[0],Sudoku.var[1],Sudoku.var[2],Sudoku.var[3],Sudoku.var[4],Sudoku.var[5]]
                            CHECK_colonna=[colonna1,colonna2,colonna3,colonna4,colonna5,colonna6,colonna7,colonna8,colonna9]

                            CHECK_quadrato=[quadrato1,quadrato2,quadrato3,quadrato4,quadrato5,quadrato6]
                        
                        if len(Sudoku.var)==3:#per controllo finale 
                                quadrato1=Sudoku.var[0][0:3]+Sudoku.var[1][0:3]  +Sudoku.var[2][0:3]
                                quadrato2=Sudoku.var[0][3:6]+Sudoku.var[1][3:6]  +Sudoku.var[2][3:6]
                                quadrato3=Sudoku.var[0][6:9]+Sudoku.var[1][6:9]   +Sudoku.var[2][6:9]         
                                CHECK_riga=[Sudoku.var[0],Sudoku.var[1],Sudoku.var[2]]
                                CHECK_colonna=[colonna1,colonna2,colonna3,colonna4,colonna5,colonna6,colonna7,colonna8,colonna9]

                                CHECK_quadrato=[quadrato1,quadrato2,quadrato3]
                          #  quadrato4=Sudoku.var[3][0:3]+Sudoku.var[4][0:3]  +Sudoku.var[5][0:3]
                           # quadrato5=Sudoku.var[3][3:6]+Sudoku.var[4][3:6]  +Sudoku.var[5][3:6]
                            #quadrato6=Sudoku.var[3][6:9]+Sudoku.var[4][6:9]   +Sudoku.var[5][6:9]            
                   
                      
                        
                        
                      
                        #numbers = [1, "", "", 4, 5, 6, 7, 8, 9,"", 10]
                        #jjk = [1, "", "", "f", "jkjdkfjdk", 6, 7, 8, 9, 10]
                        #sudoku=[numbers,jjk]
                        COLONNE=[]
                        RIGHE=[]
                        ciao2=[]
                        def senzaspazi(number):
                            if number  == "":
                                  return False 

                            return True
                         
                        for x in CHECK_colonna:
                        # Extract elements from the numbers list for which check_even() returns True
                            senza_spazi_iterator = filter(senzaspazi,x )

                            # converting to list
                            CHECK_colonna_senza_spazi = list(senza_spazi_iterator)
                            #print("senza s",CHECK_colonna_senza_spazi )
                            COLONNE.append(len(set(CHECK_colonna_senza_spazi ))==len(CHECK_colonna_senza_spazi ))
                            #print(Sudoku.var)
                       # print(COLONNE)
                        for x in CHECK_quadrato:
                        # Extract elements from the numbers list for which check_even() returns True
                            senza_spazi_iterator = filter(senzaspazi,x )

                            # converting to list
                            CHECK_quadrato_senza_spazi = list(senza_spazi_iterator)
                            #print("senza s",CHECK_quadrato_senza_spazi )
                            ciao2.append(len(set(CHECK_quadrato_senza_spazi ))==len(CHECK_quadrato_senza_spazi ))                       # CHECK_quadrato_set=[]
                        for x in CHECK_riga:
                        # Extract elements from the numbers list for which check_even() returns True
                            senza_spazi_iterator = filter(senzaspazi,x )

                            # converting to list
                            CHECK_riga_senza_spazi = list(senza_spazi_iterator)
                            #print("senza s",CHECK_riga_senza_spazi )
                            RIGHE.append(len(set(CHECK_riga_senza_spazi ))==len(CHECK_riga_senza_spazi ))      
                            # CHECK_riga_set=[] 
                       # print(RIGHE)
                        #print(COLONNE)
                        #print(ciao2)
                      #  for x in Sudoku.var:
                       #     print(len(x))

                        #for x in CHECK_righe:
                         #   print("ccù",x)
                        if False not in ciao2 and False not in COLONNE and False not in RIGHE :   
                        #if False not in ciao2 and False not in COLONNE and False not in righe:
                           # print("ciao")
                           
                            #print("ciao")
                           # for x in Sudoku.var:
                            #    print(x)
                            #print("ciao")
                            controllo_ok.var=True
                            def ciao():
                                print("non ci sono errori")
                            
                        else:
                            controllo_ok.var=False
                            def ciao():
                                if False in ciao2:
                                    for x in range(len(ciao2)):
                                        if ciao2[x]==False:

                                            print("errore_quadrati",x)
                                if False in COLONNE:
                                    for x in range(len(COLONNE)):
                                        if COLONNE[x]==False:


                                            print("errore_colonne",x)
                                if False in RIGHE:
                                    for x in range(len(RIGHE)):  
                                        if RIGHE[x]==False:
                                            print("errore_righe",x)
                        contavirgolette=0
                        if len(Sudoku.var)==9:
                            for x in Sudoku.var:
                                if False not in ciao2 and False not in COLONNE and False not in RIGHE :  
                                    if "" not in x:
                                        contavirgolette+=1
                                        if contavirgolette==0:
                                            controllo_ok.var=True
                                            print("IL SUDOKU E STATO RISOLTO CORRETTAMENTE")
                        #print(CHECK_colonna)
                        #print("aaaaaaadffdfdddddddddddddddd")
                       # for x in Sudoku.var:
                         #    print(x)
crea_funzione_check_colonne_e_quadrati()
def listasoluzioni_finali():
    listasoluzioni_finali.var=""
listasoluzioni_finali()
def L_F():
    
    L_F.var=""
L_F()


def ulteriore_filtraggio_inbase_righe_colonne():
    soluzione1,soluzione2,soluzione3,soluzione4,soluzione5,soluzione6,soluzione7,soluzione8,soluzione9=[],[],[],[],[],[],[],[],[]
    print(dizio.var,"fjfffffffffffff")
    l_f=[]
    vero=[]
    intero1=0
    intero2=6
    n_lista=0
    n=0
    listasoluzioni_finali.var=[soluzione1,soluzione2,soluzione3,soluzione4,soluzione5,soluzione6,soluzione7,soluzione8,soluzione9]
    l_f1,l_f2,l_f3,l_f4,l_f5,l_f6,l_f7,l_f8,l_f9=[],[],[],[],[],[],[],[],[]
    L_F.var=[l_f1,l_f2,l_f3,l_f4,l_f5,l_f6,l_f7,l_f8,l_f9]
    c=0
    def partealgoritmo6x6():
        for x in range(82):#distribuisco il dizionario sulle varie righe

            if str(x) in dizio.var:

                if x<6:
                    L_F.var[0].append(dizio.var[str(x)])
                elif 6<=x<=11:
                    L_F.var[1].append(dizio.var[str(x)])
                elif 12<=x<=17:
                    L_F.var[2].append(dizio.var[str(x)])

                elif 18<=x<=23:
                    L_F.var[3].append(dizio.var[str(x)])
                elif 24<=x<=29:
                    L_F.var[4].append(dizio.var[str(x)])
                elif 30<=x<=35:
                    L_F.var[5].append(dizio.var[str(x)])
                        #l_f.append(dizio.var[str(x)])

    #a=["",4,1,"","",9,6,"",8] intervallo 0 - 8


    #b=[6,"","","","","","",3,""]intervallo 9 - 17

    #c=["","","",2,7,"","",9,""]intervallo 18 - 26

    #d=["",8,"","","","",1,5,""]intervallo 27 - 35
    #e=[3,5,"","","","","","",""]intervallo36 - 44
    #f=["","","","",6,8,"",2,""]intervallo45 - 53

    #g=[7,"",8,"","",5,"","",4]intervallo54 - 62
    #h=["","",9,4,"","",7,"",3]intervallo 63 -71
    #k=["","","",1,"","",2,"",""]intervallo 72 -80
                   # if x%6==0:
    #def partealgoritmo9x9():
    for x in range(82):#distribuisco il dizionario sulle varie righe

            if str(x) in dizio.var:

                if x<9:
                    L_F.var[0].append(dizio.var[str(x)])
                elif 9<=x<=17:
                    L_F.var[1].append(dizio.var[str(x)])
                elif 18<=x<=26:
                    L_F.var[2].append(dizio.var[str(x)])

                elif 27<=x<=35:
                    L_F.var[3].append(dizio.var[str(x)])
                elif 36<=x<=44:
                    L_F.var[4].append(dizio.var[str(x)])
                elif 45<=x<=53:
                    L_F.var[5].append(dizio.var[str(x)])
                elif 54<=x<=62:
                    L_F.var[6].append(dizio.var[str(x)])
                elif 63<=x<=71:
                    L_F.var[7].append(dizio.var[str(x)])
                elif 72<=x<=80:
                    L_F.var[8].append(dizio.var[str(x)])
                 #   L_F.append(dizio.var[str(x)])
    print("lf1",L_F.var[1])
    #print(lista_sol[5],"sol5")
    #print("ddl",len(L_F[5]))

    for scorrilista in range(len(lista_sol.var)):
        for j in lista_sol.var[scorrilista]:

            cc=0

            for x in L_F.var[scorrilista]:
                    if j[x[1][1]] in x[0]:
                        cc=cc+1
                        if cc==len(L_F.var[scorrilista]):
                                listasoluzioni_finali.var[scorrilista].append(j)
    def ciaao():                            
        for x,j in zip(listasoluzioni_finali.var,range(len(Sudoku))):
            for hh in x:
                if len(x)==1:#SE DOPO IL FILTRAGGIO SCOPRO LA VERA SOLUZIONE DI UNA RIGA , LA ASSEGNO AL SUDOKU IN CORRISPONDENZA DI QUELLA RIGA
                    Sudoku[j]=x[0]
    for x in listasoluzioni_finali.var:
        print(len(x),"len")
    algoritmo()
    #ulteriore_filtraggio_inbase_righe_colonne()
    print(dizio.var)
                   # print(quadrato2.var)
#sembra che con questra sequenza riesca a ridurre sempre di piu il numero di soluzioni per ciascuna riga
ulteriore_filtraggio_inbase_righe_colonne()
assegno_singola_cifra()
algoritmo()
ulteriore_filtraggio_inbase_righe_colonne()
#print(filtro_iniziale())
assegno_singola_cifra()
algoritmo()
ulteriore_filtraggio_inbase_righe_colonne()
#print(filtro_iniziale())
assegno_singola_cifra()
algoritmo()
ulteriore_filtraggio_inbase_righe_colonne()
#print(filtro_iniziale())
assegno_singola_cifra()
algoritmo()
ulteriore_filtraggio_inbase_righe_colonne()
#print(filtro_iniziale())
assegno_singola_cifra()
algoritmo()
ulteriore_filtraggio_inbase_righe_colonne()
#print(filtro_iniziale())
assegno_singola_cifra()
algoritmo()
ulteriore_filtraggio_inbase_righe_colonne()
#print(filtro_iniziale())
assegno_singola_cifra()
#dizio.var={}#devo azzerare dizio ogni volta????
algoritmo()
ulteriore_filtraggio_inbase_righe_colonne()
#print(filtro_iniziale())
assegno_singola_cifra()
algoritmo()
ulteriore_filtraggio_inbase_righe_colonne()
#print(filtro_iniziale())
assegno_singola_cifra()
algoritmo()
ulteriore_filtraggio_inbase_righe_colonne()
#print(filtro_iniziale())
assegno_singola_cifra()
crea_funzione_check_colonne_e_quadrati()
#from somemodule import foo
#print(foo.methods)  
algoritmo()
ulteriore_filtraggio_inbase_righe_colonne()
#print(filtro_iniziale())
assegno_singola_cifra()
algoritmo()
ulteriore_filtraggio_inbase_righe_colonne()
#print(filtro_iniziale())
assegno_singola_cifra()
#print(listasoluzioni_finali.var[2],"dd")
#print(listasoluzioni_finali.var[5],"DD")
#print(listasoluzioni_finali.var[8],"dd")
for x in listasoluzioni_finali.var:
    print(x)
    print()
    
    

for x in listasoluzioni_finali.var:
    print(len(x),"len")
    

print("########################")
print()
print()
for jj in Sudoku.var:
    print(jj)
#  print("f2,",Sudoku.var)
#print(dizio.var)
def faccio_tentativi():
    lista_tentativi_sbagliati=[]
    for x in dizio.var:
        if len(dizio.var[x])==2:
           # for tentativo in dizio.var[x][0]:
            Sudoku.var[dizio.var[x][1][0]][dizio.var[x][1][1]]=dizio[0][0]
            crea_funzione_check_colonne_e_quadrati()
            if controllo_ok.var==True:
                pass
            else:
                Sudoku.var[dizio.var[x][1][0]][dizio.var[x][1][1]]=dizio[0][1]
                crea_funzione_check_colonne_e_quadrati()
                if controllo_ok.var==True:
                    pass
                else:
                     Sudoku.var[dizio.var[x][1][0]][dizio.var[x][1][1]]=""
              #  crea_funzione_check_colonne_e_quadrati()
              #  if controllo_ok.var==True:
               #     Sudoku.var[dizio.var[x][1][0]][dizio.var[x][1][1]]=tentativo
                    #crea_funzione_check_colonne_e_quadrati()

              # else:
                 #   Sudoku.var[dizio.var[x][1][0]][dizio.var[x][1][1]]=""
                   # break
                    #lista_tentativi_sbagliati.append(["tentativo",tentativo,"  posizione ",  [dizio.var[x][1][0]],[dizio.var[x][1][1]]]) 
                  #   Sudoku.var[dizio.var[x][1][0]][dizio.var[x][1][1]]=""
                #print(tentativo,"tentativo")
                #break
    #print(dizio.var[x])
#it(lista_tentativi_sbagliati)
trovato=False
listatrue=[]
#listasoluzioni_finali.var[1]=[[3, 8, 5, 7, 6, 9, 2, 4, 1]]#l'ha già trovata tutta
print(listasoluzioni_finali.var[1],"secondariga")
def ciao():
    if [9,4,2,5,8,1,3,6,7] in listasoluzioni_finali.var[0]:
        listatrue.append(True)
    if [6,1,7,2,3,4,9,5,8] in listasoluzioni_finali.var[2]:
            listatrue.append(True)
    if [8,5,4,6,7,3,1,9,2] in listasoluzioni_finali.var[3]:
            listatrue.append(True)
    if [7,2,3,1,9,5,6,8,4] in listasoluzioni_finali.var[4]: 
            listatrue.append(True)
    if [1,6,9,4,2,8,7,3,5] in listasoluzioni_finali.var[5]:  
            listatrue.append(True)
    if [2,9,8,3,4,7,5,1,6] in listasoluzioni_finali.var[6]:  
            listatrue.append(True)
    if [5,3,6,8,1,2,4,7,9] in listasoluzioni_finali.var[7]:
            listatrue.append(True)
    if [4,7,1,9,5,6,8,2,3] in listasoluzioni_finali.var[8]:

            listatrue.append(True)

    print("soluzione in lista",len(listatrue))
    print(listatrue)

for j2 in listasoluzioni_finali.var[1]:
    for j9 in listasoluzioni_finali.var[8]:
        if j9[0]==j2[0] or j9[1]==j2[1] or j9[2]==j2[2] or j9[3]==j2[3] or j9[4]==j2[4] or j9[5]==j2[5] or j9[6]==j2[6] or j9[7]==j2[7] or j9[8]==j2[8] :
                    
                listasoluzioni_finali.var[8].remove(j9)
    
                                            #if trovato==True:
                                             #   break

trovato=False
for xx in listasoluzioni_finali.var:
    print(len(xx),"len")
controllo_ok.var=False
for j1 in listasoluzioni_finali.var[0]:

#  crea_funzione_check_colonne_e_quadrati()
	if trovato==True:
		break

	for j2 in listasoluzioni_finali.var[1]:
		if trovato==True:
			break

		for j3 in listasoluzioni_finali.var[2]:
			Sudoku.var=[j1,j2,j3]

			crea_funzione_check_colonne_e_quadrati()
#   Sudoku.var=[j1,j2,j3,]

#  print(Sudoku.var)        

			if trovato==True:
				break
# trovato=True
			if controllo_ok.var==True:
				for j4 in listasoluzioni_finali.var[3]:
					if trovato==True:
						break
					for j5 in listasoluzioni_finali.var[4]:
						if trovato==True:
							break

						for j6 in listasoluzioni_finali.var[5]:
							Sudoku.var=[j1,j2,j3,j4,j5,j6]
#   print(Sudoku.var)
							if trovato==True:
								break
							crea_funzione_check_colonne_e_quadrati()  
							if controllo_ok.var==True:   
								for j7 in listasoluzioni_finali.var[6]:
									if trovato==True:
												break

									for j8 in listasoluzioni_finali.var[7]:
										if trovato==True:
												break

										for j9 in listasoluzioni_finali.var[8]:
											Sudoku.var=[j1,j2,j3,j4,j5,j6,j7,j8,j9]   
											crea_funzione_check_colonne_e_quadrati()   

											if controllo_ok.var==True:
												fine= datetime.now()
												print("il sudoku è stato risolto in ",fine-inizio)                   # if trovato==True:
												trovato=True
												# if trovato==True:

												print(j1)
												print(j2)
												print(j3)
												print(j4)
												print(j5)
												print(j6)
												print(j7)
												print(j8)
												print(j9)

												print()
											
												from tkinter import *

												import tkinter as tk
												
												window = tk.Tk()
												import tkinter.ttk

												from tkinter import *
												
												#canvas = Canvas()
												def ciao():	 
													#from tkinter import *
													root = Tk()
													canvas = Canvas()
														 
													root.geometry("500x500")
													
													
													canvas.create_line(200, 100, 500, 100)
														#root.mainloop()
													x=20
													
													y=20
													for i in range(len(Sudoku.var)):
														#x=x+20
														for j in range(len(Sudoku.var)):
															
															#y=y+20
														#	label = tk.Label(root, text=str(Sudoku.var[i][j]))
															password = Label(window, text = "Password").place(x = 30, y = 90)  
															#password.place(x, y)
															password.pack(padx=5, pady=5 )
														
												#window.mainloop()
															#canvas.pack()
												#root.mainloop()
												
												for i in range(len(Sudoku.var)):
														for j in range(len(Sudoku.var)):
															#tkinter.ttk.Separator(window, orient=VERTICAL)
															#canvas.create_line(300, 35, 300, 200, dash=(4, 2))
															frame = tk.Frame(
																master=window,
																relief=tk.RAISED,
																borderwidth=1
															)
															frame.grid(row=i, column=j, padx=len(a), pady=len(a))
															label = tk.Label(master=frame, text=str(Sudoku.var[i][j]))
															label.pack(padx=5, pady=5 )
													
												window.mainloop()							
													
												
													#break

                                                                    
crea_funzione_check_colonne_e_quadrati()                                   
def ciao():
                for j4 in listasoluzioni_finali.var[3]:
                            if trovato==True:
                                    break
                            for j5 in listasoluzioni_finali.var[4]:
                                if trovato==True:
                                    break
                                for j6 in listasoluzioni_finali.var[5]:

                                   # Sudoku.var=[j1,j2,j3,j4,j5,j6]

                                    if trovato==True:
                                        break
                                    for j7 in listasoluzioni_finali.var[6]:
                                        if trovato==True:
                                             break
                                        for j8 in listasoluzioni_finali.var[7]:
                                            if trovato==True:
                                                    break
                                            for j9 in listasoluzioni_finali.var[8]:
                                                if trovato==True:
                                                    break
                                                Sudoku.var=[j1,j2,j3,j4,j5,j6,j7,j8,j9]
                                                crea_funzione_check_colonne_e_quadrati()
                                                if controllo_ok.var==True:
                                                    trovato=True
                                                    break
