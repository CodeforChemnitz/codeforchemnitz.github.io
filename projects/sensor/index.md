---
title: Zusammenarbeit der Projekt-Teile
libs:
- mermaid
- underscore
thumb:
plunder: false
---

## Worum es geht

Ein Sensor im Garten, auf dem Dach, im Keller. Er misst Temperatur, Luftfeuchte. Er läuft mit Solarstrom und funkt seine Daten regelmäßig per WLAN weg. Er ist selbstgebaut. Er ist komplett Opensource. Die Daten liegen in einer zentralen Datenbank die per REST-API allen offen steht. Die Daten gehören keinem. Daher liegt die Deutungshoheit bei jedem selbst. **Danke Offenen Daten!**

Und Danke kleiner Sensor. Aber du bist nicht alleine. Bald nicht mehr.

**Ihr könnt ihm helfen!** Baut mehr von ihm. Schaut euch die Implementierungen an. Alles ist offen, alles erweiterbar, alles darf und soll angepasst werden können. Macht Redeploys!


## So arbeitet alles zusammen

<div class="mermaid">
graph TB
  subgraph Erfassung
    Umweltdaten-->Sensor
    Sensor-->API
    API-->Datenbank
  end

  subgraph Auswertung
    Karte-->Datenbank
  end

  subgraph Setup
    Provisionierung-->Sensor
    Provisionierung-->Simulator
  end
</div>

**Projekte auf GitHub:**

- [Sensor-API](http://github.com/codeforChemnitz/SensorAPI)
- [Sensor-Provisionierung](http://github.com/codeforChemnitz/SensorProvisioning)
- [Sensor-Karte](http://github.com/codeforChemnitz/SensorKarte)
- [Sensor-Simulator](http://github.com/codeforChemnitz/SensorSimulator)  -> [codefor-sensors.meteor.com](http://codefor-sensors.meteor.com/)
- [Sensor-Firmware](https://git.dinotools.org/poc/SensorNodeESP8266/tree/src)
- *TODO* Sensor-Bauplan und Materialliste (Arduino)


### Einrichtung des Sensors

Die Erstkonfiguration des Sensors kann bequem über das [Provisionierungs-Tool](http://github.com/codeforChemnitz/SensorProvisioning) erfolgen.
Nach dem Download des Tools wird der Sensor im Setup-Modus angeschalten. Er eröffnet dabei sein eigenes WLAN.
Das Provisionierungs-Tool verbindet sich mit diesem und stellt dann eine Oberfläche zur einfachen Konfiguration bereit.

### Erfassung von Daten

Ein fertig konfigurierter Sensor kann im Betriebsmodus an einer geeigneten Stelle platziert werden.
Er muss Zugriff zum konfigurierten WLAN haben (z.B. Freifunk) um die Daten zyklisch zur [Sensor-API](http://github.com/codeforChemnitz/SensorAPI) zu senden.
Diese speichert sie in seiner Datenbank.

### Auswertung der Daten

Von der Sensor-API können über deren REST-Schnittstelle diese Daten wieder abgefragt werden. Der Zugriff steht per Auth-Token allen offen.
Eine Beispiel-Anwendung ist die [Sensor-Karte](https://github.com/CodeforChemnitz/SensorKarte). In dieser sind alle registrierten Sensoren und deren Standorte aufgeführt. Künftig sollen dort die jeweils erfassten Daten auch eingesehen werden können.

Zum Beipiel könnten die Sensor-Daten auch mit [Graphana](http://grafana.org) aufbereitet werden.

### [Weitere Details](details.html)


## Was uns antreibt

Wir von OK Lab Chemnitz nehmen am Wissenschaftsjahr 2015 teil und haben uns dieses Projekt zur Aufgabe gemacht.
Der Willen Neues zu erforschen, technisches Interesse und eine gute Portion Ehrgeiz sorgten für Fortgang.
