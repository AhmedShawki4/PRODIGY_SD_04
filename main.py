import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def is_safe(self, row, col, num):
        for x in range(9):
            if self.grid[row][x] == num or self.grid[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_safe(row, col, num):
                            self.grid[row][col] = num
                            if self.solve():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True


class SudokuApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.geometry("550x500")
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        self.entries = [[ctk.CTkEntry(self, width=50) for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.solve_button = ctk.CTkButton(self, text="Solve", command=self.solve_sudoku)
        self.solve_button.grid(row=10, columnspan=9)

    def solve_sudoku(self):
        try:
            for i in range(9):
                for j in range(9):
                    value = self.entries[i][j].get()
                    if value.isdigit() and value != '':
                        self.grid[i][j] = int(value)
                    else:
                        self.grid[i][j] = 0

            solver = SudokuSolver(self.grid)
            if solver.solve():
                for i in range(9):
                    for j in range(9):
                        self.entries[i][j].delete(0, tk.END)
                        if self.grid[i][j] != 0:
                            self.entries[i][j].insert(0, str(self.grid[i][j]))
            else:
                messagebox.showinfo("Result", "No solution exists.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Initialize the app directly
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
app = SudokuApp()
app.mainloop()
