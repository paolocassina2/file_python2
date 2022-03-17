
minuti1=float(input("min/km "))
# ~ sec:km:1000=x:1600
# ~ 5:30=x:60

# ~ print("dfdjfk2",int(0.30))
minuti=round(minuti1,0)
# ~ secondi:100=x:60
secondi=minuti1-minuti

# ~ print("sdfsdj",secondi)
secondi2=secondi*60/100*100
# ~ print(secondi2,"DDD")
sec=minuti*60+secondi2
# ~ print(sec,"secondi")
minuti=sec//60
secondi=sec%60
# ~ print(minuti," minuti")
# ~ print(secondi," secondi")
#non è ancora precisissimo ma quasi
secondialmiglio=(sec*1600/1000)
minutialmiglio=secondialmiglio/60
# ~ print(minutialmiglio,"minuti/miglio")
minutialmiglio1=secondialmiglio//60

# ~ print(minutialmiglio,"a")
# ~ print(minutialmiglio1,"b")
secondi2=minutialmiglio-minutialmiglio1
#secondi:100=x:60
# ~ print(secondi2)
secondi3=round(secondi2*60,0)
# ~ print(secondi3)

print(minutialmiglio1,"min ",end="")
print("e ",secondi3," secondi al miglio")
# ~ minalkil=
# ~ print(secondialmiglio," sec/miglio" )
# ~ 1=secondialmiglio//60
# ~ secondialmiglio1=secondialmiglio-minutialmiglio
# ~ print(secondialmiglio1,"dfjkdj2")
# ~ print(s)
# ~ print(secondialmiglio1)
# ~ print(minutialmiglio,"min/miglio")
