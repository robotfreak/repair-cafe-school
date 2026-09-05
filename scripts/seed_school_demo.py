#!/usr/bin/env python3
"""
Demo-Daten für BUND-Präsentation am 22.09.2026

Erstellt realistische Test-Daten für:
- 36 Schüler (12 Gruppen)
- 12 reparierte Dynamo-Lampen
- Erfolgsstatistik für Präsentation
"""

import sqlite3
import json
import os
from datetime import datetime, timedelta

# Pfad zur Datenbank im Haupt-Repo
# Wird relativ zum Script-Verzeichnis berechnet
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPAIR_CAFE_DIR = os.path.join(SCRIPT_DIR, '..', '..')
DB_PATH = os.path.join(REPAIR_CAFE_DIR, 'repair-cafe', 'data', 'repair.db')

# Alternativ: Absoluter Pfad wenn als Submodule installiert
if not os.path.exists(DB_PATH):
    DB_PATH = os.path.expanduser('~/repair-cafe/data/repair.db')

print(f"📊 Verwende Datenbank: {DB_PATH}")

def create_demo_data():
    """Erstellt Demo-Daten für Schul-Workshop"""
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    # Demo-Schule
    school_name = "Muster-Gymnasium"
    workshop_date = "2026-09-22"
    teacher = "Hr. Mustermann"
    
    # 12 Gruppen mit je 2-3 Schülern
    groups = [
        {'students': ['Anna Müller', 'Ben Schmidt'], 'class': '7a', 'device': 'Dynamo-Taschenlampe #01'},
        {'students': ['Clara Weber', 'David Klein'], 'class': '7a', 'device': 'Dynamo-Taschenlampe #02'},
        {'students': ['Emma Fischer'], 'class': '7a', 'device': 'Dynamo-Taschenlampe #03'},
        {'students': ['Finn Becker', 'Grace Hoffmann'], 'class': '7b', 'device': 'Dynamo-Taschenlampe #04'},
        {'students': ['Henry Schulz', 'Ida Wolf'], 'class': '7b', 'device': 'Dynamo-Taschenlampe #05'},
        {'students': ['Jonas Neumann'], 'class': '7b', 'device': 'Dynamo-Taschenlampe #06'},
        {'students': ['Klara Zimmermann', 'Lukas Braun'], 'class': '7c', 'device': 'Dynamo-Taschenlampe #07'},
        {'students': ['Maximilian Koch'], 'class': '7c', 'device': 'Dynamo-Taschenlampe #08'},
        {'students': ['Nina Richter', 'Oscar Lange'], 'class': '7c', 'device': 'Dynamo-Taschenlampe #09'},
        {'students': ['Paula Schmitt', 'Quinn Werner'], 'class': '8a', 'device': 'Dynamo-Taschenlampe #10'},
        {'students': ['Robert Krüger'], 'class': '8a', 'device': 'Dynamo-Taschenlampe #11'},
        {'students': ['Sophie Meyer', 'Tim Hartmann'], 'class': '8a', 'device': 'Dynamo-Taschenlampe #12'},
    ]
    
    print(f"🔧 Erstelle Demo-Daten für {school_name} am {workshop_date}...")
    
    # Geräte anlegen
    devices = []
    for i, group in enumerate(groups, 1):
        cur = conn.execute(
            "INSERT INTO devices (name, schutzklasse) VALUES (?, ?)",
            (group['device'], 'II')
        )
        device_id = cur.lastrowid
        devices.append(device_id)
        print(f"  ✓ Gerät {i}/12: {group['device']}")
    
    # Tickets erstellen
    base_time = datetime(2026, 9, 22, 14, 45)  # Start 14:45
    
    for i, (group, device_id) in enumerate(zip(groups, devices)):
        # 15 Min pro Gruppe
        created_at = base_time + timedelta(minutes=i*15)
        finished_at = created_at + timedelta(minutes=45)  # 45 Min Reparaturzeit
        
        # Ersten Schüler als Haupt-Reparierer nehmen
        main_student = group['students'][0]
        student_class = group['class']
        
        # Ticket erstellen (ohne school_data Feld - wird im Journal gespeichert)
        cur = conn.execute("""
            INSERT INTO tickets 
            (device_id, fault_description, status, assignee, created_at, finished_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            device_id,
            "Leuchtet nicht",
            'erfolgreich',  # Alle erfolgreich für gute Statistik!
            f"{main_student} ({student_class})",  # Schüler + Klasse im assignee Feld
            created_at.isoformat(),
            finished_at.isoformat(),
        ))
        ticket_id = cur.lastrowid
        
        # Waiver (Haftungsausschluss) simulieren
        conn.execute("""
            INSERT INTO waivers 
            (ticket_id, waiver_version, signed_name, accepted, signature_path)
            VALUES (?, ?, ?, ?, ?)
        """, (
            ticket_id,
            '2026-09-01-school',
            main_student,
            1,
            f'data/signatures/ticket_{ticket_id}.png'
        ))
        
        # Reparatur-Tagebuch Einträge (inkl. Schul-Daten im ersten Eintrag)
        journal_entries = [
            (ticket_id, 'diagnose', f"Workshop {school_name} am {workshop_date} | Schüler: {main_student}, Klasse: {student_class} | Lehrer: {teacher}", created_at.isoformat()),
            (ticket_id, 'schritt', 'Kabel gefunden das ab war', (created_at + timedelta(minutes=15)).isoformat()),
            (ticket_id, 'schritt', 'Kabel angelötet', (created_at + timedelta(minutes=30)).isoformat()),
            (ticket_id, 'ergebnis', 'Funktionsprüfung BESTANDEN ✓', finished_at.isoformat()),
        ]
        
        conn.executemany("""
            INSERT INTO journal_entries 
            (ticket_id, entry_type, content, created_at)
            VALUES (?, ?, ?, ?)
        """, journal_entries)
        
        # Isolationsprüfung (alle bestanden!)
        conn.execute("""
            INSERT INTO equipment_tests 
            (ticket_id, protection_class, measurements, verdict, tester, test_device_snapshot, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            ticket_id,
            'II',
            json.dumps({
                'isolation_uni_t': {
                    'label': 'Isolationswiderstand (UNI-T UT-501, 500V)',
                    'value': 150 + i*10,  # 150-260 MΩ
                    'unit': 'MΩ',
                    'ok': 1,
                }
            }),
            'bestanden',
            main_student,
            json.dumps({'name': 'UNI-T UT-501'}),
            finished_at.isoformat()
        ))
        
        print(f"  ✓ Ticket {i+1}/12: {main_student} ({student_class})")
    
    conn.commit()
    conn.close()
    
    # Statistik ausgeben
    total_students = sum(len(g['students']) for g in groups)
    
    print(f"\n✅ Demo-Daten erfolgreich erstellt!")
    print(f"   Schule: {school_name}")
    print(f"   Datum: {workshop_date}")
    print(f"   Schüler: {total_students}")
    print(f"   Gruppen: {len(groups)}")
    print(f"   Reparaturen: {len(groups)}")
    print(f"   Erfolgsquote: 100% ✅")
    print(f"\n🎯 Ready für BUND-Präsentation!")

if __name__ == '__main__':
    create_demo_data()
