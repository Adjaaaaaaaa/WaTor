from .config import WIDTH, HEIGHT
class Simulation:
    """
    A class that manages and runs the simulation.

    This class handles the simulation lifecycle, including initialization,
    reset, toggling between start and pause, and periodic simulation steps.
    It operates on a 2D grid where entities act based on their context.

    Attributes:
    app (object): Reference to the main application that owns this simulation.
    chronon (int): The current time step of the simulation.
    running (bool): Indicates whether the simulation is active or paused.
    start_btn (str): Label for the start/pause button.
    history (list): Stores the history of simulation steps (currently unused).
    grid (list): A 2D list representing the simulation grid.

    Methods:
    __init__(app):
    Initializes the simulation with a reference to the main app.

    reset():
    Resets the simulation state to its initial configuration and repopulates the grid.

    stop_simulation(screen):
    Stops the simulation and closes the given GUI window.

    toggle_simulation():
    Starts or pauses the simulation based on its current state.

    simulate():
    Performs a single time step of the simulation by updating all entities in the grid.
    """


    def __init__(self, app) -> None:
        self.app = app
        self.chronon = 0
        self.running = False
        self.start_btn = "Start"
        self.history = []
        self.grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

    def reset(self)-> None:
        self.chronon = 0
        self.history.clear()
        self.running = False
        self.start_btn = "Start"
        self.grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

        self.app.planet.grid = self.grid
        self.app.planet.populate()
        self.app.draw()

    def stop_simulation(self, screen)-> None:
        self.running = False
        screen.destroy()

    def toggle_simulation(self)-> None:
        if not self.running:
            self.running = True
            print("Démarrer")
            self.simulate()
        else:
            self.running = False
            print("Pause")

    def simulate(self)-> None:
       pass
