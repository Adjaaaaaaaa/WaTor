from .config import WIDTH, HEIGHT
import random

class Simulation:
    """
    Manages the main loop and logic of the Wa-Tor simulation.

    Controls the simulation state, handles entity behavior, and updates the graphical interface.
    
    Attributes:
    app: Reference to the main application (UI and planet).
    chronon (int): Current simulation time step.
    running (bool): Indicates whether the simulation is running.
    grid : Simulation grid storing entities.
    """
    def __init__(self, app) -> None:
        """
        Initializes the Simulation object.

        Args:
        app: Reference to the main application, which holds the planet and UI.

        Returns:
        None
        """
        self.app = app
        self.chronon = 0
        self.running = False
        self.grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

    def reset(self) -> None:
        """
        Resets the simulation to its initial state:
        - Chronon counter set to 0.
        - Simulation paused.
        - Grid cleared and repopulated.
        - UI redrawn.

        Returns:
        None
        """
        self.chronon = 0
        self.running = False
        self.grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.app.planet.grid = self.grid
        self.app.planet.populate()
        self.app.draw()

    def stop_simulation(self, screen) -> None:
        """
        Stops the simulation and closes the UI window.

        Args:
        screen: The GUI screen or window to be destroyed.

        Returns:
        None
        """
        self.running = False
        screen.destroy()

    def toggle_simulation(self) -> None:
        """
        Toggles the simulation state:
        - Starts the simulation loop if it was stopped.
        - Pauses it if it was running.

        Returns:
        None
        """
        self.running = not self.running
        if self.running:
            self.simulate()

    def simulate(self) -> None:
        """
        Executes one step (chronon) of the simulation:
        - Increments time step.
        - Shuffles entity positions for randomized actions.
        - Ensures each entity acts only once per chronon.
        - Updates the UI.
        - Schedules the next step after 200ms.

        Returns:
        None
        """
        if not self.running:
            return
        self.chronon += 1

        # Liste des positions à traiter
        positions = [(x, y) for y in range(HEIGHT) for x in range(WIDTH)]
        random.shuffle(positions)

        # Pour éviter que deux entités n'agissent deux fois, on garde trace
        acted = set()

        for x, y in positions:
            if (x, y) in acted:
                continue
            entity = self.grid[y][x]
            if entity is None:
                continue
            entity.set_context(x, y, self.app.planet)
            entity.act()
            acted.add((entity.x, entity.y))

        self.app.draw()
        self.app.screen.after(200, self.simulate)
