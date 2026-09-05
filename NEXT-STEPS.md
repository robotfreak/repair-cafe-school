# 🚀 NÄCHSTE SCHRITTE — repair-cafe-school Repo erstellen

## 1. GitHub Repository erstellen

Gehe auf: https://github.com/new

**Einstellungen:**
- **Repository name:** `repair-cafe-school`
- **Beschreibung:** "Repair-Café Software — Schul-Edition für Repair-AGs an Schulen"
- **Sichtbarkeit:** Öffentlich (oder Privat wenn gewünscht)
- **❌ NICHT** initialisieren (kein README, kein .gitignore, keine Lizenz — das haben wir schon!)

**Erstellen klicken!**

---

## 2. Lokales Repo pushen

```bash
cd ~/repair-cafe-school
git remote add origin git@github.com:robotfreak/repair-cafe-school.git
git push -u origin main
```

---

## 3. Als Submodule ins Haupt-Repo einbinden

```bash
# Ins Repair-Café Repo wechseln
cd ~/repair-cafe

# Schul-Edition als Submodule hinzufügen
git submodule add git@github.com:robotfreak/repair-cafe-school.git school

# Ins school-Verzeichnis wechseln
cd school

# Demo-Daten erstellen (für BUND-Präsentation)
python scripts/seed_school_demo.py

# Commiten im Haupt-Repo
cd ..
git add .
git commit -m "feat: repair-cafe-school als Submodule für Schul-AGs"
git push
```

---

## 4. Demo für BUND-Präsentation testen

```bash
# Repair-Café Service neu starten
sudo systemctl restart repair-cafe

# Statistik abfragen (für Präsentation)
curl http://localhost:5002/api/school/statistics?school_name=Muster-Gymnasium

# Sollte zeigen:
# - 36 Schüler
# - 12 Reparaturen
# - 100% Erfolgsquote
```

---

## 5. In Präsentation verwenden

**Folie 11 (Software-Unterstützung):**

```
→ Live-Demo der Schul-Statistiken
→ Zeigen: 36 Schüler, 12 Gruppen, 100% Erfolg
→ Explain: Schul-spezifische Features
→ Haftung, Sicherheit, Kategorien
```

---

## ✅ CHECKLISTE

- [ ] GitHub Repo `repair-cafe-school` erstellt
- [ ] Lokales Repo gepusht (`git push -u origin main`)
- [ ] Als Submodule in `~/repair-cafe/school/` eingebunden
- [ ] Demo-Daten erstellt (`python scripts/seed_school_demo.py`)
- [ ] Service neu gestartet
- [ ] Statistik für BUND-Präsentation getestet

---

## 📝 REPO-STRUKTUR

```
repair-cafe-school/
├── README.md              # Vollständige Doku
├── requirements.txt       # Python Dependencies
├── .gitignore            # Schließt config.yaml aus
├── app/
│   └── waiver_text_school.py  # Schul-Haftung
└── scripts/
    └── seed_school_demo.py    # Demo-Daten Generator
```

**Geplante Erweiterungen:**
- `app/tickets_school.py` — Ticket-Erstellung mit Schul-Daten
- `app/safety_checklist.py` — Sicherheits-Checklisten
- `app/device_categories.py` — Geräte-Kategorien
- `app/school_statistics.py` — Klassen-Statistiken

---

## 🎯 VORTEILE EIGENES REPO

✅ **Sauber getrennt** — Schul-Features beeinflussen Haupt-Repo nicht  
✅ **Einfache Wartung** — Updates unabhängig vom Haupt-Repo  
✅ **Wiederverwendbar** — Andere Schulen können es nutzen  
✅ **Professionell** — Eigenes Repo für BUND-Präsentation  

---

**Viel Erfolg!** (◕‿◕) ✨

*Version: 2026-09-05 | Für BUND-Präsentation am 22.09.2026*
