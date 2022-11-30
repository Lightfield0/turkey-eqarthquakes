import requests, json, folium, webbrowser


adres="https://hublabs.com.tr/api/tr-earthquakes"
harita= folium.Map(locaiton=[39.0250061,35.52],zoom_start=6)
durum=requests.get(adres).status_code

if durum == 200:
    print("Succes")
    veri=json.loads(requests.get(adres).text)

for depremsayisi in range(0,100):
    cordinate=veri["data"][depremsayisi]["geolocation"]
    yer=veri["data"][depremsayisi]["location"]["full"]
    buyukluk=veri["data"][depremsayisi]["ml"]
    derinlik=veri["data"][depremsayisi]["depth"]
    tarih=veri["data"][depremsayisi]["time"]["date"]
    saat=veri["data"][depremsayisi]["time"]["time"]
    print(derinlik,buyukluk,yer,cordinate,tarih,saat)
    enlem,boylam=cordinate.split(",")


    bilgi=yer+"\n" + tarih+"\n" + saat +"\n"+ buyukluk +"\n"+ derinlik +"\n"
    
    
    if float(buyukluk) >= 4:

         folium.Marker(location=[enlem,boylam],popup=bilgi, icon=folium.Icon(color='red')).add_to(harita)

    else:folium.Marker(location=[enlem,boylam],popup=bilgi).add_to(harita)

harita.save("deprem.html")
webbrowser.open("deprem.html")
