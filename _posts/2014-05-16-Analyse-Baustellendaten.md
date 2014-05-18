---
layout: post
title:  "Analyse Baustellendaten"
date:   2014-05-16 14:00:00 CET
author:	Morris Jobke
categories: [news]
---

Wir haben uns nun einmal hingesetzt und angeschaut, wo es noch Probleme mit den Daten der Baustellen gibt und sind auf mehrere Probleme gestoßen.


### Tippfehler in Rohdaten

Wir haben mehrere Tippfehler in den Rohdaten gefunden. Ein beliebtes Problem - welches einfach zu erkennen ist - ist ein Vertipper in den Wörtern, die die Position der Baustelle beschreiben:

	Lage: zwischen Hübschmannstraße unf Kanzlerstraße

Man erkennt auf den ersten Blick, warum das Skript diese Positionsbeschreibung nicht korrekt erkennt - das **unf** muss ein **und** sein. Schwerer wird dies allerdings bei folgender Beschreibung:

	Straße: Berbisdorfer Straße
	Lage: zwischen Klaffenbacher Weg und Lerchenstraße

Mit OpenStreetMap konnten alle drei Straßen gefunden werden, jedoch konnte kein Schnittpunkt zwischen Berbisdorfer und Lerchenstraße gefunden werden. Ein Blick auf die Karte erklärt auch warum. In der Gesamtübersicht auf der linken Bildhälfte zeigt der Kreis oben, wo die Lerchen**straße** liegt, und das Rechteck unten zeigt die Position des vergrößerten Kartenausschnitts der Baustelle auf der Berbisdorfer Straße, welcher in der linken Bildhälfte dargestellt ist.

![Berbisdorfer Straße](/images/news/2014-05-16-BerbisdorferStraße.jpg)

Auf dem linken Bildausschnitt kann man erkennen, dass es einen Lerchen**weg** in Berbisdorf gibt, welcher bei dieser Baustellenbeschreibung offensichtlich gemeint ist.

### Mehrfache Kreuzungen zweier Straßen miteinander

Vor einiger Zeit gab es folgende Beschreibung einer Baustelle:

	Straße: Annaberger Straße
	Lage: Kreuzung Schulstraße

Wenn man sich nun lediglich einen Kartenausschnitt wie auf der linken Bildhälfte ansieht, ist dies - scheinbar - auch eine korrekte Ortsangabe:

![Annaberger Straße](/images/news/2014-05-16-Annaberger-Schulstraße.jpg)

Das Skript ermittelte nun jedoch zwei verschiedene Kreuzungen für diese eine - scheinbar korrekte - Angabe, was sich auch als richtig herausstellte. Damit ist die veröffentlichte Angabe schlicht unbrauchbar.

### Ortsübliche nicht-kartographierte Ortsangaben

Ein Datensatz gab folgende Ortsangabe an:

	Straße: Zschopauer Straße
	Lage: Schwarzes Holz

Wir konnten weder auf Google Maps, Bing Maps noch auf OpenStreetMap die Position von `Schwarzes Holz` finden - folglich scheiterte unser Skript an deren Positionierung ebenfalls. Hier wären offiziellere Ortsangaben wünschenswert.

## Fazit

Durch den Einsatz von wenigen Zeilen Quelltext und der Nutzung von OpenStreetMap-Daten wurden schnell einige Problembereiche der bisherigen Veröffentlichung ersichtlich. Wir möchten nun zusammen mit der Stadt Chemnitz an einer Problemlösung hierfür arbeiten. Eine Veröffentlichung als Geodaten würde sämtliche oben genannten Problem lösen.
