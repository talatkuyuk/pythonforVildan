print("bu program kullanıcının girdiği sayıya kadar rakamları yazar ve yanlarına kare ve küplerini yazar")
sayi=int(input("bir sayı giriniz: "))


print("sayı","\t","kare","\t","küp")
print("----","----","----",sep="\t")
i=1
while (i<=sayi):

    #sayıları formatsız yazar
    #print(i,"\t",i**2,"\t",i**3)

    #sayıları formatlı yazar yani virgülle ayırır
    print('{:,}'.format(i),"\t",'{:,}'.format(i**2),"\t",'{:,}'.format(i**3))

    i=i+1
        
