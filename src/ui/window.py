import tkinter as tk
from PIL import ImageTk, Image
from src.core.config import *
from src.core.shark import Shark
from src.core.tuna import Tuna
from src.core.simulation import Simulation
from src.core.planet import Planet

class WaTor:
    """
    Main application class for the Wa-Tor simulation.

    Handles the UI setup, drawing the simulation grid, user interactions,
    and displaying simulation statistics and history.

    Attributes:
    screen (tk.Tk): The main tkinter window.
    planet (Planet): The simulation environment containing entities.
    simulation (Simulation): The simulation controller.
    width (int): Grid width.
    height (int): Grid height.
    tuna_img (ImageTk.PhotoImage): Image used to display Tuna.
    tuna_icon_img (ImageTk.PhotoImage): Small icon for Tuna in stats.
    shark_img (ImageTk.PhotoImage): Image used to display Shark.
    shark_icon_img (ImageTk.PhotoImage): Small icon for Shark in stats.
    canvas (tk.Canvas): Canvas where the simulation grid is drawn.
    start_btn (tk.Button): Button to start/pause simulation.
    reset_btn (tk.Button): Button to reset simulation.
    stop_btn (tk.Button): Button to stop simulation.
    history_btn (tk.Button): Button to show population history.
    history (list): List storing population counts per chronon.
    """
    def __init__(self, screen: tk.Tk)->None:
        """
        Initializes the Wa-Tor application with UI elements and simulation setup.

        Args:
        screen (tk.Tk): The main tkinter window.

        Returns:
        None
        """
        self.screen = screen
        self.screen.title("Simulation Wa-Tor")
        #self.screen.state('zoomed')  # plein écran (optionnel)

        self.planet = Planet()
        self.planet.populate()

        self.simulation = Simulation(self)
        self.simulation.grid = self.planet.grid  # même grille

        self.width = WIDTH
        self.height = HEIGHT

        self.tuna_img = ImageTk.PhotoImage(Image.open(TUNA_IMAGE_PATH).resize((CELL_SIZE, CELL_SIZE)))
        self.tuna_icon_img = ImageTk.PhotoImage(Image.open(TUNA_IMAGE_PATH).resize((16, 16)))

        self.shark_img = ImageTk.PhotoImage(Image.open(SHARK_IMAGE_PATH).resize((CELL_SIZE, CELL_SIZE)))
        self.shark_icon_img = ImageTk.PhotoImage(Image.open(SHARK_IMAGE_PATH).resize((16, 16)))

        self.canvas = tk.Canvas(screen, width=self.width * CELL_SIZE, height=self.height * CELL_SIZE, bg="#b0e0e6")
        self.canvas.grid(row=0, column=0, columnspan=4)

        self.start_btn = tk.Button(screen, text="Start", command=self.toggle_simulation)
        self.start_btn.grid(row=1, column=0)

        self.reset_btn = tk.Button(screen, text="Reset", command=self.simulation.reset)
        self.reset_btn.grid(row=1, column=1)

        self.stop_btn = tk.Button(screen, text="Stop", command=lambda: self.simulation.stop_simulation(screen))
        self.stop_btn.grid(row=1, column=2)

        self.history_btn = tk.Button(screen, text="History", command=self.show_history)
        self.history_btn.grid(row=1, column=3)

        self.history = []

        self.draw()

    def toggle_simulation(self)-> None:
        """
        Toggles the simulation state between running and paused,
        and updates the start button label accordingly.

        Returns:
        None
        """
        self.simulation.toggle_simulation()
        self.start_btn.config(text="Pause" if self.simulation.running else "Start")

    def draw(self)->None:
        """
        Draws the current state of the simulation grid on the canvas,
        including the fish images and statistics labels.

        Also updates the population history.

        Returns:
        None
        """
        self.canvas.delete("all")
        tuna_count = 0
        shark_count = 0
        self.chronon = self.simulation.chronon

        for y in range(self.height):
            for x in range(self.width):
                entity = self.simulation.grid[y][x]

                # Fond cellule
                self.canvas.create_rectangle(
                    x * CELL_SIZE, y * CELL_SIZE,
                    (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                    fill="#b0e0e6", outline="white"
                )

                # Image poisson
                if isinstance(entity, Tuna):
                    tuna_count += 1
                    self.canvas.create_image(x * CELL_SIZE, y * CELL_SIZE, anchor="nw", image=self.tuna_img)
                elif isinstance(entity, Shark):
                    shark_count += 1
                    self.canvas.create_image(x * CELL_SIZE, y * CELL_SIZE, anchor="nw", image=self.shark_img)

        self.history.append((self.chronon, tuna_count, shark_count))

        # Statistiques
        if hasattr(self, "stats_frame"):
            self.stats_frame.destroy()

        self.stats_frame = tk.Frame(self.screen, bg="#f0f0f0")
        self.stats_frame.grid(row=2, column=0, columnspan=4, sticky="ew")

        self.chronon_label = tk.Label(self.stats_frame, text=f"Chronon: {self.chronon}", fg="black", bg="#f0f0f0", font=("Arial", 10, "bold"))
        self.tuna_icon = tk.Label(self.stats_frame, bg="#f0f0f0", image=self.tuna_icon_img)
        self.tuna_label = tk.Label(self.stats_frame, text=f"Thons: {tuna_count}", fg="green", bg="#f0f0f0", font=("Arial", 10, "bold"))
        self.shark_icon = tk.Label(self.stats_frame, bg="#f0f0f0", image=self.shark_icon_img)
        self.shark_label = tk.Label(self.stats_frame, text=f"Requins: {shark_count}", fg="red", bg="#f0f0f0", font=("Arial", 10, "bold"))

        self.chronon_label.pack(side="left", padx=5)
        self.tuna_icon.pack(side="left")
        self.tuna_label.pack(side="left", padx=5)
        self.shark_icon.pack(side="left")
        self.shark_label.pack(side="left", padx=5)

    def show_history(self)->None:
        """
        Opens a new window displaying the full history of the population
        counts of Tuna and Sharks per chronon in a scrollable text box.

        Returns:
        None
        """
        history_window = tk.Toplevel(self.screen)
        history_window.title("Historique complet")

        text_area = tk.Text(history_window, wrap="word", width=40, height=30)
        scrollbar = tk.Scrollbar(history_window, command=text_area.yview)
        text_area.config(yscrollcommand=scrollbar.set)

        text_area.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        history_window.grid_rowconfigure(0, weight=1)
        history_window.grid_columnconfigure(0, weight=1)

        for c, t, s in self.history:
            text_area.insert("end", f"Chronon {c}: Thons = {t}, Requins = {s}\n")

        text_area.config(state="disabled")
