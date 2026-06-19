import matplotlib.pyplot as plt
import matplotlib.patches as patches

cols, rows = 12, 12  # taille de la grille

def draw_tile(ax, x, y, pattern):
    if pattern == 0:
        ax.add_patch(patches.Polygon([[x, y], [x + 1, y], [x, y + 1]], color='black'))
    elif pattern == 1:
        ax.add_patch(patches.Polygon([[x + 1, y], [x + 1, y + 1], [x, y]], color='black'))
    elif pattern == 2:
        ax.add_patch(patches.Polygon([[x + 1, y + 1], [x, y + 1], [x + 1, y]], color='black'))
    elif pattern == 3:
        ax.add_patch(patches.Polygon([[x, y + 1], [x, y], [x + 1, y + 1]], color='black'))
    elif pattern == 4:
        ax.add_patch(patches.Rectangle((x, y), 1, 1, color='black'))
    elif pattern == 5:
        ax.add_patch(patches.Rectangle((x, y), 1, 1, color='white'))
    elif pattern == 6:
        ax.add_patch(patches.Polygon([[x, y], [x + 1, y + 1], [x + 1, y]], color='black'))
    elif pattern == 7:
        ax.add_patch(patches.Polygon([[x, y + 1], [x + 1, y + 1], [x + 1, y]], color='black'))

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, cols)
ax.set_ylim(0, rows)
ax.set_aspect('equal')
ax.axis('off')

pattern_grid = [
    [0, 1, 6, 0, 4, 5, 6, 7, 0, 1, 4, 6],
    [4, 0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1],
    [1, 2, 3, 4, 6, 5, 0, 1, 2, 3, 4, 6],
    [4, 6, 0, 3, 1, 2, 4, 0, 1, 2, 3, 0],
    [3, 4, 6, 1, 2, 3, 0, 1, 4, 5, 0, 3],
    [0, 3, 1, 2, 4, 6, 5, 0, 1, 2, 3, 4],
    [4, 0, 3, 1, 2, 4, 6, 0, 1, 2, 4, 6],
    [0, 3, 4, 6, 0, 3, 1, 2, 4, 0, 1, 6],
    [1, 4, 0, 3, 2, 4, 6, 1, 2, 0, 3, 4],
    [6, 0, 1, 4, 5, 0, 3, 4, 6, 0, 1, 2],
    [3, 4, 6, 0, 3, 1, 2, 4, 6, 0, 3, 1],
    [2, 4, 0, 3, 1, 2, 4, 0, 1, 2, 4, 6],
]

for y in range(rows):
    for x in range(cols):
        draw_tile(ax, x, rows - y - 1, pattern_grid[y][x])

plt.savefig("untitled_1975_fidele.png", dpi=300, bbox_inches='tight')
plt.show()
