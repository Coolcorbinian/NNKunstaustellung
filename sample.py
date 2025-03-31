import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from matplotlib.collections import PatchCollection

# Beispielpolygon (L-Form, nicht konvex)
polygon = [
    (0, 0), (4, 0), (4, 2),
    (2, 2), (2, 1), (1, 1),
    (1, 4), (0, 4)
]

# Wächterpunkte berechnen (verwende deine Methode z. B. compute_guard_set)
# Für das Beispiel setzen wir sie manuell:
guards = [(1, 4), (4, 0), (2, 1)]

# --- Visualisierung ---
fig, ax = plt.subplots()
patches = []

# Polygon zeichnen
poly_patch = MplPolygon(polygon, closed=True, edgecolor='black', facecolor='lightgray')
patches.append(poly_patch)
p = PatchCollection(patches, match_original=True)
ax.add_collection(p)

# Eckpunkte beschriften
for i, point in enumerate(polygon):
    ax.plot(*point, 'ko')
    ax.text(point[0] + 0.05, point[1] + 0.05, f"P{i}", fontsize=9)

# Wächterpunkte markieren
for g in guards:
    ax.plot(*g, 'ro')  # rote Punkte
    ax.text(g[0] + 0.1, g[1] + 0.1, "W", fontsize=12, color='red')

# Achsenformat
ax.set_aspect('equal')
ax.set_title("Museumswächter-Problem – Polygon mit Wächtern")
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.grid(True)

plt.show()
