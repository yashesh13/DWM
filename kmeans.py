import math

def eud(x,a,y,b):
    d=math.sqrt((x-a)*2 + (y-b)*2)
    print(d)
    return d


#l=[[1,12,15],[2,12,33],[3,18,15],[4,18,27],[5,24,21],[6,36,42]]
l=[[1,1,1],[2,2,1],[3,4,3],[4,5,4]]
print l
c1_x=l[0][1]
c1_y=l[0][2]
c2_x=l[1][1]
c2_y=l[1][2]
print(c1_x,c1_y)
print('cluster1')
print(c2_x,c2_y)
print('cluster2')
for i in range(2,len(l)):
        d1=eud(l[i][1],c1_x,l[i][2],c1_y)
        d2=eud(l[i][1],c2_x,l[i][2],c2_y)
        if(d1<d2):
            c1_x=(l[i][1]+c1_x)/2
            c1_y=(l[i][2]+c1_y)/2
            print(c1_x,c1_y)
            print(l[i][1],l[i][2])
            print('cluster1')

        else:
            c2_x=(l[i][1]+c2_x)/2
            c2_y=(l[i][2]+c2_y)/2
            print(c2_x,c2_y)
            print(l[i][1],l[i][2])
            print('cluster2')       

