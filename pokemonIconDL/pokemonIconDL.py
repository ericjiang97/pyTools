import urllib.request

for i in range(1,151):
    i=str(i)
    if(len(i)<=3):
        zeros = 3 - len(i)
        i = zeros*'0'+i
        print(i)
        url = "http://www.serebii.net/pokedex-xy/icon/"+i+".png"
        print(url)
        urllib.request.urlretrieve(url, i+".png")