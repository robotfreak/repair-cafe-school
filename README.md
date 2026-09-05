# repair-cafe-school

**Repair-Café Software — Schul-Edition für Repair-AGs an Schulen**

---

## ✨ FEATURES

Diese Schul-Edition erweitert das bewährte Repair-Café System um schulspezifische Features:

- ✅ **Vereinfachte Haftung** (für Minderjährige)
- ✅ **Elterliche Einwilligung** (Pflicht vor Teilnahme)
- ✅ **Sicherheits-Checklisten** (vor jeder Reparatur)
- ✅ **Geräte-Kategorien** (Freigabe nach Klasse)
- ✅ **Klassen-Statistiken** (Erfolg nach Schule/Lehrer)
- ✅ **Demo-Daten** (für Präsentationen)

---

## 🚀 SCHNELLSTART

### **1. Als Submodule ins Haupt-Repo einbinden:**

```bash
cd ~/repair-cafe
git submodule add https://github.com/robotfreak/repair-cafe-school.git school
cd school
pip install -r requirements.txt
```

### **2. Konfiguration aktivieren:**

```python
# In app/config.py
SCHOOL_MODE = True
SCHOOL_CONFIG = {
    'require_parental_permission': True,
    'require_safety_checklist': True,
    'enable_class_statistics': True,
}
```

### **3. Demo-Daten erstellen:**

```bash
cd school
python scripts/seed_school_demo.py
```

### **4. Service neu starten:**

```bash
sudo systemctl restart repair-cafe
```

---

## 📋 SCHUL-FEATURES IM DETAIL

### **1. Haftungsausschluss (Schul-Version)**

**Datei:** `app/waiver_text_school.py`

- Eltern müssen unterschreiben (Minderjährige!)
- Schule muss zustimmen
- Vereinfachte Haftung für Schulen
- Gilt pro Schuljahr (einmal unterschreiben)

### **2. Ticket-Erstellung mit Schul-Daten**

**Datei:** `app/tickets_school.py`

Zusätzliche Felder:
- `student_name` — Name des Schülers
- `student_class` — Klasse (z.B. "7b")
- `school_name` — Name der Schule
- `teacher_name` — Betreuender Lehrer
- `has_permission` — Elterliche Einwilligung (True/False)

### **3. Sicherheits-Checkliste**

**Datei:** `app/safety_checklist.py`

**MUSS vor jeder Reparatur ausgefüllt werden:**

```
□ Gerät frei von Netzspannung?
□ Aufsichtspersonen informiert?
□ Erste-Hilfe-Koffer griffbereit?
□ Werkzeuge in Ordnung?
□ Arbeitsplatz sicher?
□ Raum gelüftet (wenn gelötet)?
```

### **4. Geräte-Kategorien**

**Datei:** `app/device_categories.py`

| Kategorie | Beschreibung | Aufsicht | Alter |
|-----------|-------------|----------|-------|
| **Cat 1** | Frei (Dynamo-Lampen, USB) | Nein | ab Klasse 5 |
| **Cat 2** | Mit Aufsicht (Löten, 24V) | Ja | ab Klasse 7 |
| **Cat 3** | Nicht erlaubt (230V, Akku) | Niemals | - |

### **5. Klassen-Statistiken**

**Datei:** `app/school_statistics.py`

- Erfolgsquote nach Klasse
- Beste Reparierer (Rangliste)
- Lehrer-Übersicht
- Schul-Jahr Statistiken

---

## 📦 INSTALLATION

### **Voraussetzungen:**

```bash
# Haupt-Repo muss installiert sein
cd ~/repair-cafe
source venv/bin/activate
pip install -r requirements.txt
```

### **Schul-Features installieren:**

```bash
cd ~/repair-cafe/school
pip install -r requirements.txt
```

### **Datenbank migrieren:**

```bash
# Neue Tabellen für Schul-Features
python scripts/migrate_school.py
```

---

## 🎯 WORKSHOP-VORBEREITUNG

### **Checkliste für Lehrer:**

```
□ Eltern-Einwilligungen eingesammelt
□ Schule hat zugestimmt
□ Sicherheits-Checklisten ausgedruckt
□ Geräte nach Kategorien sortiert
□ Aufsicht organisiert (1:4)
□ Erste-Hilfe-Koffer bereit
□ Raum gelüftet
```

### **Demo-Daten für Präsentation:**

```bash
# Erstellt realistische Test-Daten:
# - 36 Schüler (12 Gruppen)
# - 12 reparierte Lampen
# - 100% Erfolgsquote

python scripts/seed_school_demo.py
```

---

## 📊 STATISTIKEN ABFRAGEN

### **Nach Schule:**

```bash
curl http://localhost:5002/api/school/statistics?school_name=Muster-Gymnasium
```

### **Nach Lehrer:**

```bash
curl http://localhost:5002/api/school/statistics?teacher_name=Hr.+Mustermann
```

### **Rangliste:**

```bash
curl http://localhost:5002/api/school/leaderboard?limit=10
```

---

## 🔒 SICHERHEIT

### **Wichtigste Regeln:**

1. ✅ **Niemals 230V-Geräte** in der Schule
2. ✅ **Immer Aufsicht** bei Kategorie 2
3. ✅ **Elterliche Einwilligung** PFLICHT
4. ✅ **Sicherheits-Checkliste** vor jeder Reparatur
5. ✅ **Erste-Hilfe** immer griffbereit

### **Haftungsausschluss:**

Die Schul-Edition bietet rechtliche Absicherung, ersetzt aber **KEINE** Rechtsberatung. Bei Unsicherheit:

- Schuljuristen konsultieren
- Versicherung informieren
- Kultusministerium fragen

---

## 📞 SUPPORT

**GitHub Issues:** https://github.com/robotfreak/repair-cafe-school/issues

**Dokumentation:** Siehe `docs/` Ordner

**Beispiel-Schulen:**
- Muster-Gymnasium (Demo-Daten)
- Test-Schule (zum Ausprobieren)

---

## 📄 LIZENZ

MIT License — Frei nutzbar für Schulen und Repair-Cafés.

---

## 🎉 VIEL ERFOLG!

**Repair-AGs an Schulen sind die Zukunft!** 🌱🔧

---

*Version: 2026-09-05 | Für BUND-Präsentation am 22.09.2026*
