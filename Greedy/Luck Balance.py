'''Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. 
She believes in "saving luck", and wants to check her theory.'''

def luckBalance(k, contests):
    contests.sort(key=lambda k :k[0],reverse=True)
    loose=0
    luck=0
    for i in contests:
        if(i[1]==0):
            luck+=i[0]
        else:
            loose+=1    
            if(loose<=k):    
                luck+=i[0]
            else:
                luck-=i[0]
    return luck