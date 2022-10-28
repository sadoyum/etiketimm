import os, logging, asyncio
from Plugins import Maho
from telethon import events, Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from Configs import *
from asyncio import sleep 
import time, random

# Bunlar babadan yadigar :) 
anlik_calisan = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

# Sonlandırır kapatır. 
@Maho.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in anlik_calisan:
    return
  else:
    try:
      anlik_calisan.remove(event.chat_id)
    except:
      pass
    return await event.respond('✅ Etiket işlemi başarıyla durduruldu.')


@Maho.on(events.NewMessage(pattern="^/futbol ?(.*)"))
async def mentionall(event):
  global anlik_calisan 
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in Maho.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir.**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Etikete Başlamak için sebep yazın... ✋\n\n(Örnek: /futbol Herkese Merhaba!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
        
    async for usr in Maho.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(futbol)}](tg://user?id={usr.id}),"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await Maho.send_message(event.chat_id, f"📢 ~ **{msg}**\n{usrtxt}")
        await asyncio.sleep(2.9)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"{sender.first_name}"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Etiket işlemi başarıyla durduruldu.**\n\n**Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()

  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in Maho.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(futbol)}](tg://user?id={usr.id}),"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await Maho.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2.9)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"{sender.first_name}"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Etiket işlemi başarıyla durduruldu.**\n\n**Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()

# Aşağıdaki gibidir.

futbol = ['Maldonado', 'Lionel Messi', 'Bobô', 'Matías Delgado', 'Márcio Nobre1', 'Rodrigo Tello', 'Federico Higuaín', 'Lamine Diatta', 'Édouard Cissé', 'Gordon Schildenfeld', 'Filip Hološko', 'Anthony Šerić', 'Tomáš Sivok', 'Tomáš Zápotočný', 'Fabian Ernst', 'Michael Fink', 'Matteo Ferrari', 'Rodrigo Tabata', 'Ricardo Quaresma', 'Roberto Hilbert', 'Guti', 'Marco Aurélio1', 'Manuel Fernandes', 'Simao Sabrosa', 'Hugo Almeida', 'Sidnei', 'Bébé', 'Júlio Alves', 'Edú', 'Julien Escudé', 'Allan McGregor', 'Dentinho', 'Mamadou Niang', 'Pedro Franco', 'Michael Eneramo', 'Atiba Hutchinson', 'Ramon Motta', 'Jermaine Jones', 'Dany Nounkeu', 'Demba Ba', 'José Sosa', 'Alexander Milošević', 'Daniel Opare', 'Duško Tošić', 'Andreas Beck', 'Luiz Rhodolfo', 'Mario Gómez', 'Denis Boyko', 'Aras Özbiliz', 'Alexis Delgado', 'Marcelo Guedes', 'Fabri', 'Adriano Correia', 'Talisca', 'Vincent Aboubakar', 'Ryan Babel', 'Matej Mitrović', 'Pepe', 'Álvaro Negredo', 'Jeremain Lens', 'Gary Medel', 'Cyle Larin', 'Vágner Love', 'Domagoj Vida', 'Enzo Roco', 'Loris Karius', 'Adem Ljajić', 'Nicolas Isimat-Mirin', 'Shinji Kagawa', 'Tyler Boyd', 'Douglas', 'Víctor Ruiz', 'Pedro Rebocho', "Georges-Kévin N'Koudou", 'Muhammed Elneni', 'Abdoulay Diaby', 'Ajdin Hasić', 'Kevin-Prince Boateng', "Fabrice N'Sakala", 'Bernard Mensah', 'Welinton', 'Francisco Montero', 'Josef de Souza', 'Valentin Rosier', 'Raşit Gezzal', 'Alex Teixeira', 'Michy Batshuayi', 'Miralem Pjanić', 'Gedson Fernandes', 'Romain Saïss', 'Mert Günok', 'Ersin Destanoğlu', 'Emre Bilgin', 'Goktug Baytekin', 'Domagoj Vida', 'Welinton', 'Douglas', 'Fabrice NSkala', 'Umut Meras', 'Francisco Montero', 'Valentin Rosier', 'Kerem Kalafat', 'Rıdvan Yılmaz', 'Serdar Saatçi', 'Serkan Emrecan Terzi', 'Aytug Batur Komec', 'Atiba Hutchinson', 'Mehmet Topal', 'Miralem Pjanic', 'Adem Ljajic', 'Alex Teixeira', 'Necip Uysal', 'Gökhan Töre', 'Rachid Ghezzal', 'Oğuzhan Özyakup', 'Georges-Kevin Nkoudou', 'Muhayer Oktay', 'Can Bozdogan', 'Berkay Vardar', 'Emirhan İlkhan', 'Emirhan Delibas', 'Demir Tiknaz', 'Jeremain Lens', 'Michy Batshuayi', 'Kenan Karaman', 'Cyle Larin', 'Güven Yalçın', 'Koray Yagci', 'Ariel Ortega', 'Robert Enke', 'Vladimir Beschastnykh', 'Ivaylo Petkov', 'Sergiy Rebrov', 'Stjepan Tomas', 'Pierre van Hooijdonk', 'Marco Aurelio', 'Fábio Luciano', 'Mert Nobre', 'Fabiano', 'Alex De Souza', 'Stephen Appiah', 'Nicolas Anelka', 'Mateja Kežman', 'Edu Dracena', 'Diego Lugano', 'Deivid', 'Roberto Carlos', 'Wederson', 'Claudio Maldonado', 'Josico', 'Daniel Güiza', 'Fábio Bilica', 'André Santos', 'Cristian Baroni', 'Miroslav Stoch', 'Issiar Dia', 'Mamadou Niang', 'Joseph Yobo', 'Emmanuel Emenike', 'Reto Ziegler', 'Henri Bienvenu', 'Moussa Sow', 'Dirk Kuyt', 'Miloš Krasić', 'Raul Meireles', 'Pierre Webó', 'Bruno Alves', 'Michal Kadlec', 'Samuel Holmén', 'Diego', 'Simon Kjær', 'Fernandão', 'Abdoulaye Ba', 'Fabiano Ribeiro', 'Nani', 'Josef de Souza', 'Robin van Persie', 'Lazar Marković', 'Aatif Chahechouhe', 'Gregory van der Wiel', 'Roman Neustädter', 'Martin Škrtel', 'Jeremain Lens', 'Oleksandr Karavayev', 'Mathieu Valbuena', 'Nebil Dirar', 'Carlos Kameni', 'Mauricio Isla', 'Elif Elmas', 'Roberto Soldado', 'Giuliano', 'Luís Neto', 'Vincent Janssen', 'André Ayew', 'Islam Slimani', 'Michael Frey', 'Diego Reyes', 'Jailson', 'Yassine Benzia', 'Victor Moses', 'Miha Zajc', 'Max Kruse', 'Allahyar Seyyadmeneş', 'Vedat Muriqi', 'Garry Rodrigues', 'Zanka', 'Adil Rami', 'Luiz Gustavo', 'Simon Falette', 'Filip Novák', 'Mame Thiam', 'José Sosa', 'Mauricio Lemos', 'Enner Valencia', 'Marcel Tisserand', 'Mbwana Samatta', 'Papiss Cissé', 'Kemal Ademi', 'Dimitris Pelkas', 'Diego Perotti', 'Attila Szalai', 'Bright Osayi-Samuel', 'Mesut Özil', 'Steven Caulker', 'Kim Min-jae', 'Diego Rossi', 'Mërgim Berisha', 'Max Meyer', 'Miguel Crespo', 'Erol Bulut', 'Saffet Akbaş', 'Tayfun Korkut', 'Elvir Bolić', 'Mustafa Doğan', 'Samuel Johnson', 'Abdullah Ercan', 'Ogün Temizkanoğlu', 'Semih Şentürk', 'Ali Güneş', 'Serhat Akın', 'Ümit Özat', 'Volkan Demirel', 'Tuncay Şanlı', 'Selçuk Şahin', 'Fabio Luciano', 'Mehmet Yozgatlı', 'Mehmet Aurelio', 'Serkan Balcı', 'Önder Turacı', 'Uğur Boral', 'Gökhan Gönül', 'Gökçek Vederson', 'Colin Kâzım Richards', 'Emre Belözoğlu', 'Mehmet Topuz', 'Bekir İrtegün', 'Caner Erkin', 'Hasan Ali Kaldırım', 'Mehmet Topal', 'Alper Potuk', 'Şener Özbayraklı', 'Ozan Tufan', 'Aykut Erçetin', 'Çağlar Birinci', 'Gökhan Zan', 'Ceyhun Gülselam', 'Aydın Yılmaz', 'Selçuk İnan', 'Johan Elmander', 'Felipe Melo', 'Dida', 'Cafu', 'Stam', 'Nesta', 'Maldini', 'Pirlo', 'Gattuso', 'Seedorf', 'Kaka', 'Shevchenko', 'Inzaghi', 'Crespo', 'Diego Altube', 'Thibaut Courtois', 'Alphonse Areola', 'Andriy Lunin', 'Lucas Canizares', 'Luis Lopez', 'Toni Fuidias', 'Diego Del Alamo', 'Luis Federico', 'Sergio Ramos', 'Raphael Varane', 'Daniel Carvajal', 'Adrian De La Fuente', 'Ferland Mendy', 'Marcelo', 'Eder Militao', 'Alvaro Odriozola', 'Victor Chust', 'Sergio Santos', 'Pablo Ramon Parra', 'Miguel Gutierrez', 'David Alaba', 'Jesus Vallejo', 'Rafa Marin', 'Mario Gila', 'Reinier', 'Marco Asensio', 'Federico Valverde', 'Brahim Diaz', 'Luka Modric', 'Toni Kroos', 'Isco', 'Carlos Casemiro', 'Lucas Vazquez', 'Martin Odegaard', 'Marvin Park', 'Sergio Arribas', 'Antonio Blanco', 'Hugo Duro', 'Eduardo Camavinga', 'Dani Ceballos', 'Peter Gonzalez', 'Karim Benzema', 'Luka Jovic', 'Eden Hazard', 'Gareth Bale', 'Vinicius Junior', 'Rodrygo', 'James Rodriguez', 'Mariano Diaz', 'Borja Mayoral', 'Oscar Aranda', 'Juan Latasa', 'Neto', 'Marc-Andre Ter Stegen', 'Inaki Pena', 'Arnau Tenas', 'Lazar Carevic', 'Jordi Alba', 'Sergi Roberto', 'Ronald Araujo', 'Samuel Umtiti', 'Nelson Semedo', 'Clement Lenglet', 'Dani Morer', 'Junior Firpo', 'Gerard Pique', 'Sergio Akieme', 'Santiago Ramos', 'Arnau Comas', 'Sergino Dest', 'Oscar Mingueza', 'Eric Garcia', 'Emerson', 'Alejandro Balde', 'Dani Alves', 'Mika Marmol', 'Sergio Busquets', 'Hiroki Abe', 'Alex Collado', 'Frenkie De Jong', 'Ivan Rakitic', 'Arturo Vidal', 'Riqui Puig', 'Guillem Jaime', 'Miralem Pjanic', 'Philippe Coutinho', 'Carles Alena', 'Konrad De La Fuente', 'Ilaix Moriba', 'Matheus Fernandes', 'Yusuf Demir', 'Nico Gonzalez', 'Abde Ezzalzouli', 'Alvaro Sanz', 'Ferran Jutgla', 'Matheus Pereira', 'Lucas De Vega', 'Estanis Pedrola', 'Adama Traore', 'Luis Suarez', 'Ousmane Dembele', 'Antoine Griezmann', 'Ansu Fati', 'Lionel Messi', 'Rey Manaj', 'Martin Braithwaite', 'Memphis Depay', 'Sergio Agüero', 'Luuk De Jong', 'Ilias Akhomach', 'Ferran Torres', 'Pierre Aubameyang', 'Albert Riera', 'Milan Baroš', 'Tomáš Ujfaluši', 'Mehmet Batdal', 'Serkan Kurtuluş', 'Yiğit Gökoğlan', 'Hakan Balta', 'Fernando Muslera', 'Semih Kaya', 'Emmanuel Eboué', 'Yekta Kurtuluş', 'Engin Baytar', 'Emre Çolak', 'Sabri Sarıoğlu', 'Servet Çetin', 'Necati Ateş', 'Ufuk Ceylan', 'Sercan Yıldırım', 'Fernando Muslera', 'Felipe Melo', 'Hamit Altıntop', 'Gökhan Zan', 'Blerim Džemaili', 'Aydın Yılmaz', 'Selçuk İnan', 'Umut Bulut', 'Wesley Sneijder', 'Bruma', 'Alex Telles', 'Burak Yılmaz', 'Sinan Gümüş', 'Goran Pandev', 'Aurélien Chedjou', 'Fernando Muslera', 'Mariano', 'Maicon', 'Serdar Aziz', 'Ahmet Çalık', 'Tolga Ciğerci', 'Yasin Öztekin', 'Selçuk İnan', 'Eren Derdiyok', 'Younès Belhanda', 'Sinan Gümüş', 'Martin Linnes', 'Ryan Donk', 'Cédric Carrasso', 'Şener Özbayraklı', 'Omar Elabdellaoui', 'Taylan Antalyalı', 'Henry Onyekuru', 'Ryan Babel', 'Radamel Falcao', 'Halil Dervişoğlu', 'Oghenekaro Etebo', 'Martin Linnes', 'Ryan Donk', 'Oğulcan Çağlayan', 'Kerem Aktürkoğlu', 'Ömer Bayram', 'Emre Akbaba', 'Cristiano Ronaldo', 'Pele', 'Maradona', 'Ronaldo', 'Thierry Henry', 'Kaka', 'Sergio Agüero', 'Xavi', 'Ruud Gullit', 'Arthur Zico', 'Lev Yashin', 'Iniesta', 'Lothar Matthäus', 'Giuseppe Meazza', 'Franz Beckenbauer', 'George Best', 'Roberto Baggio', 'Johan Cruyff', 'Luis Figo', 'Andrea Pirlo', 'Marco Van Basten', 'Zlatan Ibrahimovic', 'Sandro Mazzola', 'Ferenc Puskas', 'Zinedine Zidane', 'Alfredo Di Stéfano', 'Rio Ferdinand', 'Paolo Maldini', 'Robin van Persie', 'Iker Casillas', 'Neymar', 'Fabio Cannavaro', 'Yaya Toure', 'Edinson Cavani', 'Gabriel Batistuta', 'Thiago Silva', 'Dennis Bergkamp', 'Franck Ribery', 'Carles Puyol', 'Mesut Özil', 'Dani Alves', 'David Silva', 'Karim Benzema', 'Javier Zanetti', 'Radamel Falcao', 'Bastian Schweinsteiger', 'Gianluigi Buffon', 'Arjen Robben', 'Wayne Rooney', 'Luis Suarez', 'Mbappe', 'Juan Román Riquelme', 'Sergio Ramos', 'Muhammed Salah', 'Cesc Fabregas', 'Gerard Pique', 'Pepe', 'Didier Drogba', 'Robert Lewandowski', 'David Villa', 'Wesley Sneijder', 'Philipp Lahm', "Samuel Eto'o", 'Carlos Tevez', 'Sergio Busquets', 'Samir Nasri', 'Eden Hazard', 'Diego Forlan', 'Klaas Jan Huntelaar', 'Sabri Sarıoğlu']

 
