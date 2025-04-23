Sure! Here's the translated `README.md` in English, suitable for your GitHub repository:

---

# 🧠 MLB Regular Season Betting Predictor

A desktop application built in Python with a graphical interface (Tkinter) that predicts the winner of MLB (Major League Baseball) games based on recent team performance, pitcher stats, and betting lines. At the end, all predictions are saved to a PDF file on your desktop.


## 🚀 Features

- User-friendly GUI for data input.
- Winner prediction based on:
  - Last 10 games record
  - Starting pitcher’s win/loss record
  - Full-season team record
  - Betting line (Over/Under)
- Automatically generates a PDF report of all predictions.

---

## 🛠️ How to Use

### Requirements

- Python 3.x
- Libraries:
  - `tkinter` (included with Python)
  - `reportlab` (for PDF generation)

### Install Dependencies

```bash
pip install reportlab
```

### Run the App

Save the file as `mlb_predictor.py` (or any name you prefer) and run:

```bash
python mlb_predictor.py
```

### What Does It Do?

1. Asks how many games you want to predict.
2. For each game, prompts you to enter:
   - Home and away team names
   - Last 10 games record (format: `6-4`)
   - Pitcher record (format: `5-2`)
   - Season record (format: `60-40`)
   - Total runs scored
   - Number of games played
   - Betting line (e.g., `8.5`)
3. Predicts which team will win and whether the game will go **OVER** or **UNDER** the betting line.
4. After all predictions, it generates a **`MLBpredictorPicks.pdf`** on your desktop with the results.

---

## 📂 Project Structure

```
main.py
README.md
```

---

## 🧠 How It Works

The predictor calculates a score for each team by summing:
- Wins in the last 10 games
- Pitcher’s win-loss difference
- Total season wins

Then it compares the average total runs per game to the betting line to predict **OVER** or **UNDER**.

---

## 📄 License

This project is open-source under the MIT License. Feel free to use, modify, and improve it!
