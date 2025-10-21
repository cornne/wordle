import tkinter as tk
from tkinter import messagebox
import random

WORDS = ["apple", "grape", "crane", "flame", "stone", "world", "chair", "house", "dream", "night"]

WORD_LEN = 5
MAX_TRIES = 6

COLORS = {
    "bg": "#121213",
    "empty": "#121213",
    "text": "#d7dadc",
    "green": "#538d4e",
    "yellow": "#b59f3b",
    "gray": "#3a3a3c",
    "key_default": "#818384",
}

class Wordle:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle Unlimited")
        self.root.config(bg=COLORS["bg"])
        self.game_frame = None
        self.show_main_menu()

    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        menu_frame = tk.Frame(self.root, bg=COLORS["bg"])
        menu_frame.pack(expand=True)
        tk.Label(menu_frame, text="Wordle Unlimited", font=("Helvetica", 36, "bold"),
                bg=COLORS["bg"], fg=COLORS["text"]).pack(pady=20)
        tk.Button(menu_frame, text="Start Game", width=20, height=2,
                 font=("Helvetica", 14, "bold"), bg=COLORS["key_default"], fg="white",
                 command=self.start_game).pack(pady=10)
        tk.Button(menu_frame, text="How to Play", width=20, height=2,
                 font=("Helvetica", 14, "bold"), bg=COLORS["key_default"], fg="white",
                 command=self.show_instructions).pack(pady=10)
        tk.Button(menu_frame, text="Exit", width=20, height=2,
                 font=("Helvetica", 14, "bold"), bg=COLORS["key_default"], fg="white",
                 command=self.root.quit).pack(pady=10)

    def show_instructions(self):
        messagebox.showinfo("How to Play",
            "Guess the 5-letter word in 6 tries or less.\n"
            "- Green: Letter is correct and in the right position.\n"
            "- Yellow: Letter is in the word but in the wrong position.\n"
            "- Gray: Letter is not in the word.\n"
            "- Use the keyboard or on-screen buttons to input letters.\n"
            "- Press ENTER to submit a guess, or BACKSPACE to delete.\n"
            "- Press RESTART to start a new game at any time.\n"
            "- Press BACK TO MENU to return to the main menu.")

    def start_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_ui()
        self.new_round()

    def create_ui(self):
        self.tiles = []
        self.buttons = {}
        self.game_frame = tk.Frame(self.root, bg=COLORS["bg"])
        self.game_frame.pack(pady=20)
        for r in range(MAX_TRIES):
            row = []
            for c in range(WORD_LEN):
                lbl = tk.Label(self.game_frame, text="", width=4, height=2, font=("Helvetica", 24, "bold"),
                              bg=COLORS["empty"], fg=COLORS["text"], relief="solid", bd=1)
                lbl.grid(row=r, column=c, padx=5, pady=5)
                row.append(lbl)
            self.tiles.append(row)
        layout = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        kb = tk.Frame(self.root, bg=COLORS["bg"])
        kb.pack(pady=10)
        for line in layout:
            row = tk.Frame(kb, bg=COLORS["bg"])
            row.pack(pady=3)
            for ch in line:
                btn = tk.Button(row, text=ch, width=4, height=2,
                               font=("Helvetica", 12, "bold"),
                               bg=COLORS["key_default"], fg="white",
                               command=lambda c=ch: self.press(c))
                btn.pack(side="left", padx=3)
                self.buttons[ch] = btn
        bottom = tk.Frame(kb, bg=COLORS["bg"])
        bottom.pack(pady=3)
        tk.Button(bottom, text="ENTER", width=6, height=2,
                 bg=COLORS["key_default"], fg="white",
                 command=self.submit).pack(side="left", padx=4)
        tk.Button(bottom, text="⌫", width=4, height=2,
                 bg=COLORS["key_default"], fg="white",
                 command=self.delete).pack(side="left", padx=4)
        tk.Button(bottom, text="RESTART", width=8, height=2,
                 bg=COLORS["key_default"], fg="white",
                 command=self.new_round).pack(side="left", padx=4)
        tk.Button(bottom, text="BACK TO MENU", width=12, height=2,
                 bg=COLORS["key_default"], fg="white",
                 command=self.show_main_menu).pack(side="left", padx=4)
        self.root.bind("<Key>", self.keypress)

    def new_round(self):
        self.word = random.choice(WORDS)
        self.row = 0
        self.col = 0
        self.game_over = False
        for r in range(MAX_TRIES):
            for c in range(WORD_LEN):
                self.tiles[r][c].config(text="", bg=COLORS["empty"])
        for btn in self.buttons.values():
            btn.config(bg=COLORS["key_default"])
        print("[DEBUG] New word:", self.word)

    def press(self, ch):
        if self.game_over or self.col >= WORD_LEN:
            return
        lbl = self.tiles[self.row][self.col]
        lbl.config(text=ch.upper())
        self.col += 1

    def delete(self):
        if self.col > 0:
            self.col -= 1
            lbl = self.tiles[self.row][self.col]
            lbl.config(text="")

    def keypress(self, e):
        if self.game_over: return
        if e.keysym == "Return":
            self.submit()
        elif e.keysym == "BackSpace":
            self.delete()
        elif e.char.isalpha():
            self.press(e.char.upper())

    def submit(self):
        if self.col < WORD_LEN: return
        guess = "".join(self.tiles[self.row][c].cget("text") for c in range(WORD_LEN)).lower()
        colors = self.grade(guess)
        for i, color in enumerate(colors):
            lbl = self.tiles[self.row][i]
            lbl.config(bg=color)
            ch = guess[i].upper()
            if ch in self.buttons:
                cur_color = self.buttons[ch].cget("bg")
                if color == COLORS["green"]:
                    self.buttons[ch].config(bg=COLORS["green"])
                elif color == COLORS["yellow"] and cur_color != COLORS["green"]:
                    self.buttons[ch].config(bg=COLORS["yellow"])
                elif color == COLORS["gray"] and cur_color not in [COLORS["green"], COLORS["yellow"]]:
                    self.buttons[ch].config(bg=COLORS["gray"])
        if guess == self.word:
            self.win()
        else:
            self.row += 1
            self.col = 0
            if self.row == MAX_TRIES:
                self.lose()

    def grade(self, guess):
        res = [COLORS["gray"]] * WORD_LEN
        secret = list(self.word)
        for i in range(WORD_LEN):
            if guess[i] == secret[i]:
                res[i] = COLORS["green"]
                secret[i] = None
        for i in range(WORD_LEN):
            if res[i] == COLORS["gray"] and guess[i] in secret:
                res[i] = COLORS["yellow"]
                secret[secret.index(guess[i])] = None
        return res

    def win(self):
        self.game_over = True
        messagebox.showinfo("🎉", f"You guessed it! Word: {self.word.upper()}")
        self.ask_new()

    def lose(self):
        self.game_over = True
        messagebox.showinfo("❌", f"You lost! The word was {self.word.upper()}")
        self.ask_new()

    def ask_new(self):
        if messagebox.askyesno("Next Round", "Play another round?"):
            self.new_round()
        else:
            self.show_main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    Wordle(root)
    root.mainloop()