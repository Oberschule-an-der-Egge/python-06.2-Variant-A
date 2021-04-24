# Homer's Magic Hammock

Schaut euch die ersten Minuten der Simpons Episode "Treehouse of Horror XIII" an, um Homers magische Hängematte kennenzulernen:

[![Treehouse of Horror](https://img.youtube.com/vi/Kag4x4B5IwA/1.jpg)](https://www.youtube.com/watch?v=Kag4x4B5IwA)

## Aufgaben

- Implementiert eine Klasse `Homer`
  - mit den Attributen `name`: Homer, `age`: 39 und `city`: Springfield
  - mit der Methode `do_chores()`
- Implementiert eine Funktion (nicht Methode!) `magic_hammock()`
  - die ein Homer Objekt annimmt und es zusammen mit einem Klon wieder zurückgibt
  - die Rückgabe erfolgt als Liste
- Zusätzlich kann ein `Homer`-Objekt die Methode `do_chores()` ausführen:
  - bei Ausführung antwortet (=`return`) der Original-Homer: `Nope!`
  - die Klon-Homers antworten: `Ok!`
  
## Bonus

Fair Warning: Die Bonusaufgaben sind dieses Mal richtig tricky. Die Lösung der o.g. Aufgaben ist ausreichend.

- Die magische Matratze kann mehr als ein Homer-Objekt annehmen und gibt eine entsprechende Zahl an Klonen zurück
- Die magische Matratze kann auch ein Flanders-Objekt annehmen (und entsprechende Klone erzeugen!)

## Automatisches Testen
Wir probieren automatisches Testen aus. Damit bekommt ihr bei jedem Push eine sofortige Rückmeldung, ob euer Code die Anforderungen erfüllt.

**Wichtig:** Ihr müsst euren Code in `main.py` schreiben, bitte keine eigenen Dateien anlegen.
