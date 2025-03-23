# IoT_Seminarska-naloga
*Vzpostavitev Ubuntu strežnika na rPi 3 in vzpostavitev Sophos-a (kibernetska varnost)*
 
V tej seminarski nalogi bom opisal postopek vzpostavitve Ubuntu strežnika na napravi Raspberry Pi 3 ter namestitev in konfiguracijo varnostne rešitve Sophos. Namen naloge je prikazati praktičen postopek priprave delujočega strežnika na osnovi priljubljene distribucije Ubuntu, ki je znana po svoji stabilnosti in prilagodljivosti, ter implementacije Sophos-a za povečanje varnosti sistema. 

## Vzpostavitev Ubuntu strežnika na Raspberry Pi 3

### 1. Vzpostavitev varnega testnega okolja za IoT in OT

Projekt se je začel na fakulteti, kjer smo prevzeli paket z napravo Raspberry Pi 3 (rPi 3), ki je cenovno dostopna in učinkovita platforma za različne vrste strežniških in učenjskih projektov. V nadaljevanju bom predstavil korake, ki sem jih izvedel za vzpostavitev sistema. 

Postopek vzpostavitve Ubuntu strežnika:

### 1.1 Namestitev Linux Ubuntu Server na Raspberry Pi

![image](https://github.com/user-attachments/assets/3c6dc984-5cfe-46cc-b443-f0e437665b69)

Prvi korak pri pripravi sistema je bil namestitev operacijskega sistema na napravo Raspberry Pi 3. Za ta namen sem uporabil orodje Raspberry Pi Imager, ki omogoča enostavno zapisovanje operacijskih sistemov na SD kartico. Postopek je potekal na naslednji način: 
1. Namestitev Raspberry Pi Imager-ja Najprej sem prenesel in namestil programsko opremo Raspberry Pi Imager na svoj osebni računalnik. Orodje je na voljo za večino operacijskih sistemov (Windows, macOS, Linux) in je uporabniku prijazno.
2. Izbira Ubuntu strežnika Po zagonu Raspberry Pi Imager-ja sem izbral ustrezno različico operacijskega sistema Ubuntu, zasnovano za Raspberry Pi. Odločil sem se za Ubuntu Server, saj ta različica nudi minimalno okolje, ki je idealno za strežniške aplikacije.
3. Zapisovanje operacijskega sistema na SD kartico Naslednji korak je bil vstavitev SD kartice v režo za pomnilniške kartice na računalniku. Z uporabo Raspberry Pi Imager-ja sem izbral SD kartico kot ciljno napravo in začel postopek zapisovanja izbranega operacijskega sistema. Postopek je trajal nekaj minut.
4. Vstavljanje SD kartice v Raspberry Pi 3 Ko je bil zapis operacijskega sistema zaključen, sem SD kartico vstavil nazaj v napravo Raspberry Pi 3.

S temi koraki sem uspešno pripravil napravo za zagon Ubuntu strežnika.

### 1.2 Posodobitev sistema in namestitev osnovnih varnostnih paketov

Ko sem se povezal na Ubuntu server sem najprej posodobil in namestil osnovne varnostne pakete:

- Posodobitev seznama paketov:
Ukaz **sudo apt update** osveži seznam razpoložljivih paketov in njihovih različic iz skladišč.

![image](https://github.com/user-attachments/assets/36cefc92-071f-48db-87f5-9760fb894c3f)

- Nadgradnja obstoječih paketov:
Ukaz **sudo apt upgrade -y** nadgradi vse pakete na novejše različice, ki so na voljo.

- Namestitev osnovnih varnostnih paketov:
Za izboljšano varnost lahko namestimo pakete, kot so:

UFW (Uncomplicated Firewall): **sudo apt install ufw -y**

Fail2Ban (za zaščito pred napadi z ugibanjem gesel): **sudo apt install fail2ban -y**

ClamAV (antivirus za Linux): **sudo apt install clamav -y**

- Omogočanje požarnega zidu (UFW)
**sudo ufw enable** aktivira požarni zid za večjo varnost.

S tem sem si sistem posodobil in izboljšal njegovo varnost.

### 1.3 Registracija in konfiguracija delujoče domene (ali uporaba brezplačnih dinamičnih DNS storitev, če je potrebno)


Ko sem vklopil napravo Raspberry Pi 3 v napajanje, sem na svojem usmerjevalniku preveril, kateri IP naslov je bil dodeljen napravi. Ta IP naslov sem nato nastavil kot statičen, da bi bil vedno enak. Zatem sem se z uporabo protokola SSH povezal na Ubuntu strežnik za nadaljnjo konfiguracijo.

![image](https://github.com/user-attachments/assets/92dc6a07-5442-4903-8a09-787c79251894)

Na strežnik sem namestil NVM (Node Version Manager), ki omogoča enostavno upravljanje različnih različic Node.js. Z uporabo NVM sem namestil Node.js in npm (Node Package Manager). Nato sem dodal knjižnico Express za gradnjo spletnih aplikacij in PM2 Process Manager za upravljanje procesov aplikacij na strežniku.

Nato sem pri upravljalcu domen kupil domeno simon1999.xyz, da bi omogočil javno dostopnost svoje spletne strani na Ubuntu strežniku. Po nakupu domene sem najprej poskrbel, da je bil moj zunanji IP naslov nastavljen kot statičen. Nato sem v nastavitvah domene vnesel svoj zdaj statični zunanji IP kot cilj, kamor se bo domena usmerjala.

![image](https://github.com/user-attachments/assets/73b9f79e-252c-4c27-bb51-50b667b5d712)

Da bi domena simon1999.xyz dejansko delovala, sem moral na svojem usmerjevalniku nastaviti port forwarding. S tem sem omogočil preusmeritev prometa na ustrezne porte svojega Raspberry Pi strežnika, kar je omogočilo dostop do spletne strani iz javnega omrežja.

![image](https://github.com/user-attachments/assets/1bc96d29-8c51-4528-9d68-71c7210a03a7)

Povezava do moje domene: http://simon1999.xyz

![image](https://github.com/user-attachments/assets/a918d8bb-7c5b-432e-a56c-69399b2d62d5)

### 1.4 Nastavitev HTTPS povezave z uporabo SSL/TLS certifikata (npr. Let’s Encrypt)

Namestil sem Certbot in vtičnik za Nginx z ukazom: **sudo apt install certbot python3-certbot-nginx -y**

Certifikat sem pridobil in samodejno konfiguriral Nginx z ukazom: **sudo certbot --nginx -d simon1999.xyz -d www.simon1999.xyz**

Preveril sem, ali je avtomatska obnova omogočena: **sudo certbot renew --dry-run**

Po uspešni namestitvi sem odprl https://simon1999.xyz in preveril, ali povezava uporablja SSL/TLS.

S tem sem uspešno vzpostavil HTTPS povezavo.

Povezava do moje domene: https://simon1999.xyz

![image](https://github.com/user-attachments/assets/7faa1968-5d21-46a0-8f43-49cc1b95c114)

### 1.5 Namestitev Node.js in testnega strežnika

Najprej sem posodobil sistem in namestil Node.js ter npm:
**sudo apt update && sudo apt install nodejs npm -y**

Preveril sem, ali sta bila uspešno nameščena:

![image](https://github.com/user-attachments/assets/6ca2ad74-cf65-44c8-a457-700e4267ca96)

Ustvarjanje testnega strežnika: 

Ustvaril sem novo datoteko test.js ter vanjo sem vpisal preprost HTTP strežnik:

`var http = require('http');`

`http.createServer(function (req, res) {`

  `res.writeHead(200, {'Content-Type': 'text/plain'});`
  
  `res.end('Pozdravljen svet\n');`
  
`}).listen(8080);`

`console.log('Server running');`

Za zagon sem uporabil ukaz: **node test.js**

<br />

Za trajno delovanje strežnika sem namestil pm2:

`sudo npm install -g pm2`

`pm2 start server.js`  

`pm2 startup`

<br />

S tem sem uspešno namestil Node.js in vzpostavil testni strežnik.

### 1.6. Konfiguracija Nginx kot obratnega posrednika (reverse proxy) za usmerjanje prometa na Node.js aplikacijo

Najprej sem namestil nginx: **sudo apt install nginx**.

Nato sem uredil UFW :

![image](https://github.com/user-attachments/assets/4f10b075-306f-4659-8c1d-81ed833dfa3a)

In zadeva že deluje:

 ![image](https://github.com/user-attachments/assets/b6a74e2c-b2e8-496f-8d51-ddb90d2c1db2)

### 1.7 Priključitev LED-diode in pritisnega gumba na Raspberry Pi

Videjo priključene LED-diode, pritisnega gumba ter povezav na Raspberry Pi:

https://github.com/user-attachments/assets/480fe120-dc68-40a9-a43e-24996dba0e62




### 1.8 Razvoj enostavnega spletnega vmesnika, ki omogoča vklop in izklop LED-diode

Spletni vmesnik, ki sem ga razvil za vklop in izklop LED-diode, izgleda tako (za podrobnejši vpogled si lahko ogledate kodo v datoteki index.html):

![image](https://github.com/user-attachments/assets/e06cd065-cb74-4339-a31f-33d8c5736c14)


### 1.9 Prikaz stanja pritisnega gumba v realnem času

Spletni vmesnik sem posodobil tako, da v realnem času prikazuje stanje LED-lučke (ali je vklopljena ali izklopljena). Za podrobnejši vpogled si lahko ogledate kodo v datotekah index.html in LED.py.

![image](https://github.com/user-attachments/assets/47209d52-743a-490a-aff0-e9edc00f9278)


### 1.10 Prikaz delovanja s praktično demonstracijo

Video prikazuje delovanje spletnega vmesnika s praktično demonstracijo na LED-diodi:



https://github.com/user-attachments/assets/2625d1f0-51dd-40ba-a8ab-652e82432aa2


### 2. Varna komunikacija med IoT napravami

V tem delu sem moral zagotoviti varen prenos podatkov med Raspberry Pi in oddaljenim odjemalcem za LED in pritisnnjeni gumb.

### 2.1 Implementacija MQTT ali WebSocket komunikacije med strežnikom in odjemalcem za upravljanje LED in branje stanja gumba

Za komunikacijo med strežnikom in odjemalcem za upravljanje LED in branje stanja gumba sem izbral implementacijo MQTT.

Najprej sem ustvaril virtualno okolje v moji mapi, kjer imam datoteko LED.py s kodo: **python3 -m venv myenv**

![image](https://github.com/user-attachments/assets/1b3d586b-1702-431b-86cf-5f95a35eeef8)

Nato sem vstopil v virtualno okolje z ukazom **activate** ter znotraj okolja namestil **paho-mqtt**:

![image](https://github.com/user-attachments/assets/8457a268-fc75-4095-b445-4c0423fe8763)

Nato sem moral dodati MQTT svoji aplikaciji Flask. To sem storil tako, da sem namestil **Mosquitto**:

![image](https://github.com/user-attachments/assets/bdfcb04e-9784-441e-81a3-bfdcf33dfbbc)
![image](https://github.com/user-attachments/assets/836a2474-0b68-4e11-bbc7-af6f8392024b)

Nato sem seveda moral posodobiti svojo kodo v datoteki LED.py in vključiti MQTT. Za podroben pregled kode odprite datoteko **LED-MQTT.py**

Po tem, ko sem uspel sprogramirati in posodobiti kodo, da je vključevala MQTT, sem šel v virtualno okolje in iz njega zagnal svoj program:

![image](https://github.com/user-attachments/assets/aa6a6e68-ebb7-42c6-b2e4-cde4a29d5bcd)

In zdaj, vsakič, ko pritisnem na gumb, mi javi **"LED turned OFF via MQTT"** ali **"LED turned ON via MQTT"**.

### 2.3 Analiza vpliva šifriranja na zakasnitev in porabo virov

-**Zakasnitev**: Šifriranje povečuje zakasnitev pri prenosu podatkov, saj zahteva dodatno obdelavo podatkov. To se še posebej pozna pri močnejših algoritmih, kot je AES v 256-bitnem načinu, ki so bolj kompleksni.

-**Poraba virov**: Šifriranje porabi več CPU moči in pomnilnika. Močnejši algoritmi (npr. AES-256) povečajo porabo procesorske moči in s tem vplivajo na energetsko porabo, kar je pomembno pri napravah z omejenimi viri, kot so IoT naprave.

## Vzpostavitev Sophos-a

Podjetje, kjer delujem, se uvršča med subjekte kritične infrastrukture, zato smo se odločili vzpostaviti napreden sistem za kibernetsko zaščito – Sophos. Namen te odločitve je izboljšati varnostne ukrepe in zaščititi ključne digitalne procese ter naprave pred sodobnimi kibernetskimi grožnjami.

Sophos je vodilno podjetje na področju kibernetske varnosti, ki ponuja celovite rešitve za zaščito naprav, omrežij in podatkov. Njihove rešitve vključujejo napreden protivirusni sistem, zaščito pred ransomware napadi, filtriranje spletnih vsebin ter sistem za zaznavanje in odzivanje na grožnje (EDR). Sophos je znan po enostavnem upravljanju, kar omogoča tudi manjšim ekipam učinkovito zaščito pred kompleksnimi kibernetskimi napadi.

Sophos igra ključno vlogo tudi pri varovanju naprav interneta stvari (IoT). IoT naprave, ki so pogosto manj zaščitene in bolj ranljive za kibernetske napade, so pomemben del kritične infrastrukture. Sophos z uporabo naprednih metod, kot so segmentacija omrežja, preverjanje nenavadnih vzorcev prometa in uporaba umetne inteligence za odkrivanje groženj, zagotavlja, da IoT naprave ostanejo zaščitene pred morebitnimi vdori ali zlorabami. To omogoča celovito zaščito celotnega ekosistema, kjer so IoT naprave povezane s ključnimi informacijskimi sistemi.

Za namestitev Sophos sistema sem uporabil tradicionalni postopek, ki vključuje vzpostavitev centralnega upravljalnega strežnika in povezavo odjemalskih naprav. Proces sem začel z izbiro ustrezne različice Sophos programske opreme, ki je združljiva z našim sistemskim okoljem in potrebami podjetja.

Najprej sem namestil Sophos Central, ki služi kot osrednja platforma za upravljanje varnostnih rešitev. Namestitev sem izvedel na namenski strežnik, kjer sem konfiguriral osnovne nastavitve, vključno z dodeljevanjem uporabniških pravic, določanjem varnostnih politik in nastavitvijo protokolov za posodobitve. Po uspešni namestitvi sem opravil začetno sinhronizacijo sistema, kar je omogočilo vzpostavitev osnovne varnostne infrastrukture.

![image](https://github.com/user-attachments/assets/df133be7-09f1-4999-a2f9-55ee98fdd34d)

Ko je bila centralna platforma pripravljena, sem na vse računalnike v podjetju namestil Sophos Endpoint Protection. Ta postopek je vključeval:
1. Prenos odjemalske programske opreme: Prenos sem izvedel preko povezave z osrednjim strežnikom.
2. Namestitev: Na posameznih računalnikih sem namestil odjemalsko aplikacijo in omogočil komunikacijo z osrednjim strežnikom Sophos.
3. Povezava in registracija: Vsak računalnik sem registriral v sistem Sophos Central, kar omogoča nadzor in sprotno posodabljanje varnostnih nastavitev za vsako napravo.

Po povezavi vseh računalnikov smo opravili testne preglede sistema, da smo zagotovili pravilno delovanje. Na podlagi rezultatov testiranja smo dodatno prilagodili varnostne politike, kot so samodejno blokiranje potencialnih groženj, redno pregledovanje naprav in obveščanje o varnostnih incidentih.

![image](https://github.com/user-attachments/assets/c9e66996-fdf9-44fa-a3bc-5b960907b81a)

![image](https://github.com/user-attachments/assets/6c8e436f-a6a5-4fd0-85c5-6385846fbdf7)

Ko je v računalnik z nameščenim Sophos Endpoint Protection vstavljen nepooblaščen USB ključek, sistem deluje na naslednji način:

1. Prepoznavanje naprave: Sophos takoj zazna novo povezano napravo in preveri njeno identiteto na podlagi vnaprej določenih pravil.
2. Primerjava z varnim seznamom: Sistem primerja USB napravo z "belim seznamom" dovoljenih naprav, ki so bile predhodno odobrene s strani IT oddelka.
3. Reakcija na nepooblaščeno napravo: Če naprava ni na seznamu, Sophos avtomatsko blokira dostop do nje in prepreči kakršnokoli interakcijo s podatki na ključku. V nekaterih primerih je mogoče prikazati obvestilo uporabniku z razlago, zakaj dostop ni dovoljen.
4. Obveščanje administratorja: Administrator sistema prejme opozorilo v realnem času preko Sophos Central, kjer je naveden računalnik, uporabnik in vrsta blokirane naprave.


https://github.com/user-attachments/assets/c8d3ba6d-0faf-44be-a6bf-b0d8b0a80ce2


