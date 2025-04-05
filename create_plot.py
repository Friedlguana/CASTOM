import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random




def create_plot(container_needed):
    # ======== Container Data ========
    CONTAINERS = {}
    cont=[]
    for item in Overall_List:#Overall List is the List In my Sorter

        if item.placed_cont == container_needed:
            itemer = {"Position": (float(item.x), float(item.y), float(item.z)), "Dimensions": (float(item.width), float(item.depth), float(item.height))}
            cont.append(itemer)
    CONTAINERS[container_needed] = cont

    # ======== Visualization Functions ========
    def plot_cuboid(ax, position, dimensions, color):
        """Plot a 3D cuboid with specified position and dimensions"""
        x, y, z = position
        dx, dy, dz = dimensions

        # Define cuboid vertices
        vertices = [
            [x, y, z],
            [x + dx, y, z],
            [x + dx, y + dy, z],
            [x, y + dy, z],
            [x, y, z + dz],
            [x + dx, y, z + dz],
            [x + dx, y + dy, z + dz],
            [x, y + dy, z + dz]
        ]

        # Define cube faces
        faces = [
            [vertices[0], vertices[1], vertices[5], vertices[4]],  # Bottom
            [vertices[2], vertices[3], vertices[7], vertices[6]],  # Top
            [vertices[0], vertices[3], vertices[2], vertices[1]],  # Front
            [vertices[4], vertices[5], vertices[6], vertices[7]],  # Back
            [vertices[0], vertices[4], vertices[7], vertices[3]],  # Left
            [vertices[1], vertices[5], vertices[6], vertices[2]]  # Right
        ]

        ax.add_collection3d(Poly3DCollection(faces, facecolors=color,
                                             edgecolors='black', alpha=0.8))

    def visualize_containers():
        """Create interactive 3D visualization for all containers"""
        n_containers = len(CONTAINERS)
        n_cols = 1  # Maximum 3 columns
        n_rows = 1
        fig = plt.figure(figsize=(18, 18))

        for idx, (name, items) in enumerate(CONTAINERS.items(), 1):
            ax = fig.add_subplot(n_rows, n_cols, idx, projection='3d')
            ax.set_title(f"Container {name}", fontweight='bold')
            ax.set_xlabel("X-axis")
            ax.set_ylabel("Y-axis")
            ax.set_zlabel("Z-axis")

            # Plot each item with random color
            for item in items:
                color = (random.random(), random.random(), random.random())
                plot_cuboid(ax, item["Position"], item["Dimensions"], color)

            # Set equal aspect ratio
            ax.set_box_aspect([1, 1, 1])

        plt.tight_layout()
        plt.show()

    # ======== Run Visualization ========
    if __name__ == "__main__":
        visualize_containers()
        def create_plot(container_needed):

            CONTAINERS = {}
            cont=[]
            for item in Overall_List:

                if item.placed_cont == container_needed:
                    itemer = {"Position": (float(item.x), float(item.y), float(item.z)), "Dimensions": (float(item.width), float(item.depth), float(item.height))}
                    cont.append(itemer)
            CONTAINERS[container_needed] = cont

    # ======== Visualization Functions ========
    def plot_cuboid(ax, position, dimensions, color):
        """Plot a 3D cuboid with specified position and dimensions"""
        x, y, z = position
        dx, dy, dz = dimensions

        # Define cuboid vertices
        vertices = [
            [x, y, z],
            [x + dx, y, z],
            [x + dx, y + dy, z],
            [x, y + dy, z],
            [x, y, z + dz],
            [x + dx, y, z + dz],
            [x + dx, y + dy, z + dz],
            [x, y + dy, z + dz]
        ]

        # Define cube faces
        faces = [
            [vertices[0], vertices[1], vertices[5], vertices[4]],  # Bottom
            [vertices[2], vertices[3], vertices[7], vertices[6]],  # Top
            [vertices[0], vertices[3], vertices[2], vertices[1]],  # Front
            [vertices[4], vertices[5], vertices[6], vertices[7]],  # Back
            [vertices[0], vertices[4], vertices[7], vertices[3]],  # Left
            [vertices[1], vertices[5], vertices[6], vertices[2]]  # Right
        ]

        ax.add_collection3d(Poly3DCollection(faces, facecolors=color,
                                             edgecolors='black', alpha=0.8))

    def visualize_containers():
        """Create interactive 3D visualization for all containers"""
        n_containers = len(CONTAINERS)
        n_cols = 1  # Maximum 3 columns
        n_rows = 1
        fig = plt.figure(figsize=(18, 18))

        for idx, (name, items) in enumerate(CONTAINERS.items(), 1):
            ax = fig.add_subplot(n_rows, n_cols, idx, projection='3d')
            ax.set_title(f"Container {name}", fontweight='bold')
            ax.set_xlabel("X-axis")
            ax.set_ylabel("Y-axis")
            ax.set_zlabel("Z-axis")

            # Plot each item with random color
            for item in items:
                color = (random.random(), random.random(), random.random())
                plot_cuboid(ax, item["Position"], item["Dimensions"], color)

            # Set equal aspect ratio
            ax.set_box_aspect([1, 1, 1])

        plt.tight_layout()
        plt.show()

    # ======== Run Visualization ========
    if __name__ == "__main__":
        visualize_containers()