# IoT_Seminarska-naloga
*Vzpostavitev Ubuntu strežnika na rPi 3 in vzpostavitev Sophos-a (kibernetska varnost)*

*1. Vzpostavitev Ubuntu strežnika na Raspberry Pi 3*
 
V tej seminarski nalogi bom opisal postopek vzpostavitve Ubuntu strežnika na napravi Raspberry Pi 3 ter namestitev in konfiguracijo varnostne rešitve Sophos. Namen naloge je prikazati praktičen postopek priprave delujočega strežnika na osnovi priljubljene distribucije Ubuntu, ki je znana po svoji stabilnosti in prilagodljivosti, ter implementacije Sophos-a za povečanje varnosti sistema. 

Projekt se je začel na fakulteti, kjer smo prevzeli paket z napravo Raspberry Pi 3 (rPi 3), ki je cenovno dostopna in učinkovita platforma za različne vrste strežniških in učenjskih projektov. V nadaljevanju bom predstavil korake, ki sem jih izvedel za vzpostavitev sistema. 

Postopek vzpostavitve Ubuntu strežnika:

Prvi korak pri pripravi sistema je bil namestitev operacijskega sistema na napravo Raspberry Pi 3. Za ta namen sem uporabil orodje Raspberry Pi Imager, ki omogoča enostavno zapisovanje operacijskih sistemov na SD kartico. Postopek je potekal na naslednji način: 
1. Namestitev Raspberry Pi Imager-ja Najprej sem prenesel in namestil programsko opremo Raspberry Pi Imager na svoj osebni računalnik. Orodje je na voljo za večino operacijskih sistemov (Windows, macOS, Linux) in je uporabniku prijazno.
2. Izbira Ubuntu strežnika Po zagonu Raspberry Pi Imager-ja sem izbral ustrezno različico operacijskega sistema Ubuntu, zasnovano za Raspberry Pi. Odločil sem se za Ubuntu Server, saj ta različica nudi minimalno okolje, ki je idealno za strežniške aplikacije.
3. Zapisovanje operacijskega sistema na SD kartico Naslednji korak je bil vstavitev SD kartice v režo za pomnilniške kartice na računalniku. Z uporabo Raspberry Pi Imager-ja sem izbral SD kartico kot ciljno napravo in začel postopek zapisovanja izbranega operacijskega sistema. Postopek je trajal nekaj minut.
4. Vstavljanje SD kartice v Raspberry Pi 3 Ko je bil zapis operacijskega sistema zaključen, sem SD kartico vstavil nazaj v napravo Raspberry Pi 3.

S temi koraki sem uspešno pripravil napravo za zagon Ubuntu strežnika.

Ko sem vklopil napravo Raspberry Pi 3 v napajanje, sem na svojem usmerjevalniku preveril, kateri IP naslov je bil dodeljen napravi. Ta IP naslov sem nato nastavil kot statičen, da bi bil vedno enak. Zatem sem se z uporabo protokola SSH povezal na Ubuntu strežnik za nadaljnjo konfiguracijo.

![image](https://github.com/user-attachments/assets/92dc6a07-5442-4903-8a09-787c79251894)

Na strežnik sem namestil NVM (Node Version Manager), ki omogoča enostavno upravljanje različnih različic Node.js. Z uporabo NVM sem namestil Node.js in npm (Node Package Manager). Nato sem dodal knjižnico Express za gradnjo spletnih aplikacij in PM2 Process Manager za upravljanje procesov aplikacij na strežniku.

Nato sem pri upravljalcu domen kupil domeno simon1999.xyz, da bi omogočil javno dostopnost svoje spletne strani na Ubuntu strežniku. Po nakupu domene sem najprej poskrbel, da je bil moj zunanji IP naslov nastavljen kot statičen. Nato sem v nastavitvah domene vnesel svoj zdaj statični zunanji IP kot cilj, kamor se bo domena usmerjala.

![image](https://github.com/user-attachments/assets/73b9f79e-252c-4c27-bb51-50b667b5d712)

Da bi domena simon1999.xyz dejansko delovala, sem moral na svojem usmerjevalniku nastaviti port forwarding. S tem sem omogočil preusmeritev prometa na ustrezne porte svojega Raspberry Pi strežnika, kar je omogočilo dostop do spletne strani iz javnega omrežja.

![image](https://github.com/user-attachments/assets/1bc96d29-8c51-4528-9d68-71c7210a03a7)


*2. Vzpostavitev Sophos-a*

Podjetje, kjer delujem, se uvršča med subjekte kritične infrastrukture, zato smo se odločili vzpostaviti napreden sistem za kibernetsko zaščito – Sophos. Namen te odločitve je izboljšati varnostne ukrepe in zaščititi ključne digitalne procese ter naprave pred sodobnimi kibernetskimi grožnjami.

Sophos je vodilno podjetje na področju kibernetske varnosti, ki ponuja celovite rešitve za zaščito naprav, omrežij in podatkov. Njihove rešitve vključujejo napreden protivirusni sistem, zaščito pred ransomware napadi, filtriranje spletnih vsebin ter sistem za zaznavanje in odzivanje na grožnje (EDR). Sophos je znan po enostavnem upravljanju, kar omogoča tudi manjšim ekipam učinkovito zaščito pred kompleksnimi kibernetskimi napadi.

Sophos igra ključno vlogo tudi pri varovanju naprav interneta stvari (IoT). IoT naprave, ki so pogosto manj zaščitene in bolj ranljive za kibernetske napade, so pomemben del kritične infrastrukture. Sophos z uporabo naprednih metod, kot so segmentacija omrežja, preverjanje nenavadnih vzorcev prometa in uporaba umetne inteligence za odkrivanje groženj, zagotavlja, da IoT naprave ostanejo zaščitene pred morebitnimi vdori ali zlorabami. To omogoča celovito zaščito celotnega ekosistema, kjer so IoT naprave povezane s ključnimi informacijskimi sistemi.

