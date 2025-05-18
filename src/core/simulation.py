from .config import WIDTH, HEIGHT
import random

class Simulation:
    def __init__(self, app) -> None:
        self.app = app
        self.chronon = 0
        self.running = False
        self.grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

    def reset(self):
        self.chronon = 0
        self.running = False
        self.grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.app.planet.grid = self.grid
        self.app.planet.populate()
        self.app.draw()

    def stop_simulation(self, screen):
        self.running = False
        screen.destroy()

    def toggle_simulation(self):
        self.running = not self.running
        if self.running:
            self.simulate()

    def simulate(self):
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
