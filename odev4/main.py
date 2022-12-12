def bul(matris1,matris2,matris3):
    if(len(matris1)==len(matris2)):
        for i in range(0,3):
            for j in range(0,3):
                matris3[i][j]=matris1[i][j]+matris2[i][j]
    else:
        return False



matris1=[[1,2,3],[4,5,6],[7,8,9]]
matris2=[[1,2,3],[4,5,6],[7,8,9]]
matris3=[]
topla=bul(matris1,matris2,matris3)
if(topla!=False):
    print(matris3)
else:
    print("toplanamadi")

