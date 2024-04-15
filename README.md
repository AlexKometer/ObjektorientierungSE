# Objektorientierung
Sakai Aufgabe 6.1

Diese Anwendung ist dazu gedacht, personenbezogene Experimentdaten zu speichern und zu analysieren. Sie nutzt die Klassen `Person` und `Experiment` für die Datenverwaltung und die Berechnung von gesundheitsbezogenen Metriken.

## Klassen

### Person
Diese Klasse verwaltet personenbezogene Daten und berechnet die geschätzte maximale Herzfrequenz. Die Daten werden als JSON gespeichert.

Attribute:
- `name`: Name der Person
- `age`: Alter der Person

Methoden:
- `save()`: Speichert die Attribute der Person in einer JSON-Datei.
- `estimate_max_hr()`: Berechnet die geschätzte maximale Herzrate basierend auf dem Alter.

### Experiment
Diese Klasse verwaltet die Experimentdaten, die mit einer Person verbunden sind.

Attribute:
- `name`: Name des Experiments
- `date`: Datum des Experiments
- `subject`: Name der beteiligten Person

Methoden:
- `save()`: Speichert die Attribute des Experiments in einer JSON-Datei.

## Anwendung

### `main.py`
Dies ist das Hauptskript der Anwendung, das die Benutzereingaben aufnimmt und die Datenverarbeitung durchführt. Es ermöglicht das Erstellen von Personen- und Experimentobjekten und speichert diese Daten.

### `test.py`
Dieses Skript wird für automatische Tests ohne Benutzerinteraktion verwendet. Es erstellt festgelegte Objekte und führt die Funktionalitäten der Anwendung aus.

## Verwendung

Beim Start des Programmes wird der Benutzer gefragt, ob er selbst Daten eingeben will, oder ob ein `test` mit vordefinierten Daten ausgeführt werden soll. 

`the README.md file was generated with the use of OpenAI/ChatGPT4`
