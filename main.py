import tkinter as tk
from tkinter import simpledialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_record(record):
    try:
        wins, losses = map(int, record.split("-"))
        return [1] * wins + [0] * losses
    except ValueError:
        return None

def calculate_pitcher_score(pitcher_record):
    try:
        wins, losses = map(int, pitcher_record.split("-"))
        return wins - losses
    except ValueError:
        return None

def get_total_wins(record):
    try:
        wins, _ = map(int, record.split("-"))
        return wins
    except ValueError:
        return None

# Lista para guardar predicciones
predicciones_guardadas = []

def predict_winner():
    team1 = entry_team1.get().upper()
    team2 = entry_team2.get().upper()

    record_team1 = convert_record(entry_record_team1.get())
    record_team2 = convert_record(entry_record_team2.get())
    pitcher_team1 = calculate_pitcher_score(entry_pitcher_team1.get())
    pitcher_team2 = calculate_pitcher_score(entry_pitcher_team2.get())
    season_record_team1 = get_total_wins(entry_season_record_team1.get())
    season_record_team2 = get_total_wins(entry_season_record_team2.get())

    try:
        total_runs_team1 = int(entry_total_runs_team1.get())
        total_runs_team2 = int(entry_total_runs_team2.get())
        total_games_played = int(entry_total_games_played.get())
        betting_line = float(entry_betting_line.get())
    except ValueError:
        return  # Ignorar si hay error de entrada

    if None in [record_team1, record_team2, pitcher_team1, pitcher_team2, season_record_team1, season_record_team2]:
        return

    score_team1 = sum(record_team1) + pitcher_team1 + season_record_team1
    score_team2 = sum(record_team2) + pitcher_team2 + season_record_team2

    match_line = f"{team1} vs {team2}"
    winner = team1 if score_team1 > score_team2 else team2

    total_over_under = (total_runs_team1 + total_runs_team2) / total_games_played
    over_under = "OVER" if total_over_under > betting_line else "UNDER"

    predicciones_guardadas.append((match_line, winner, over_under))

    # Limpiar campos
    for entry in all_entries:
        entry.delete(0, tk.END)

    global current_game
    current_game += 1
    if current_game >= total_games:
        save_predictions_to_pdf(predicciones_guardadas)

def save_predictions_to_pdf(predictions):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "MLBpredictorPicks.pdf")
    c = canvas.Canvas(desktop_path, pagesize=letter)
    width, height = letter

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, y, "MLB Predictor PICKS")
    y -= 30

    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, y, "Match")
    c.drawString(250, y, "Winner")
    c.drawString(400, y, "Over/Under")
    y -= 20

    c.setFont("Helvetica", 12)
    for match, winner, over_under in predictions:
        if y < 40:
            c.showPage()
            y = height - 50
        c.drawString(30, y, match)
        c.drawString(250, y, winner)
        c.drawString(400, y, over_under)
        y -= 20

    c.save()

# GUI
root = tk.Tk()
root.title("MLB Betting Predictor")

labels = [
    "Home Team Name:", "Away Team Name:",
    "Home Team Last 10 Games Record (e.g., '6-4'):",
    "Away Team Last 10 Games Record (e.g., '6-4'):",
    "Home Pitcher Record (e.g., '5-2'):",
    "Away Pitcher Record (e.g., '5-2'):",
    "Home Team Season Record (e.g., '60-40'):",
    "Away Team Season Record (e.g., '58-42'):",
    "Total Runs Scored by Home Team:",
    "Total Runs Scored by Away Team:",
    "Total Games Played by Both Teams:",
    "Bookmaker Over/Under Line:"
]

all_entries = []
for i, label_text in enumerate(labels):
    tk.Label(root, text=label_text).grid(row=i, column=0, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    all_entries.append(entry)

(
    entry_team1, entry_team2, entry_record_team1, entry_record_team2,
    entry_pitcher_team1, entry_pitcher_team2, entry_season_record_team1,
    entry_season_record_team2, entry_total_runs_team1, entry_total_runs_team2,
    entry_total_games_played, entry_betting_line
) = all_entries

tk.Button(root, text="Predict Outcome", command=predict_winner).grid(row=len(labels), columnspan=2, pady=10)

# Preguntar número de partidos
total_games = simpledialog.askinteger("Number of Games", "How many games do you want to predict?", minvalue=1)
current_game = 0

root.mainloop()
