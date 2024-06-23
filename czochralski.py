import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Draw crucible
crucible = patches.Circle((0.5, 0.5), 0.3, fill=False, edgecolor='black')
ax.add_patch(crucible)

# Draw silicon melt
melt = patches.Circle((0.5, 0.5), 0.28, color='grey', alpha=0.5)
ax.add_patch(melt)

# Initialize seed crystal and rod
rod = patches.Rectangle((0.45, 0.5), 0.1, 0.3, fill=True, color='black')
seed = patches.Circle((0.5, 0.8), 0.05, fill=True, color='black')
ax.add_patch(rod)
ax.add_patch(seed)

ax.set_aspect('equal')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axis('off')

def animate(i):
    # Move the rod and seed crystal upwards
    rod.set_y(0.5 + 0.005 * i)
    seed.center = (0.5, 0.8 + 0.005 * i)
    return rod, seed

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
plt.show()
