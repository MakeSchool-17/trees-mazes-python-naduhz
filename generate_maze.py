import maze
import random


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    # TODO: Implement create_dfs
    # Create a stack for backtracking
    stack = []
    # Choose a cell index at random from the grid to be current cell
    current_cell_index = random.randint(0, m.total_cells)
    # Set visited cells to 1
    visited_cells = 1

    while visited_cells < m.total_cells:
        # Get unvisited neighbours
        current_cell_neighbours = m.cell_neighbors(current_cell_index)
        if len(current_cell_neighbours) >= 1:
            # Choose random neighbour cell
            new_cell = current_cell_neighbours[random.randint(0, len(current_cell_neighbours)-1)]
            new_cell_index = new_cell[0]
            new_cell_compass_index = new_cell[1]
            # Knockdown walls
            m.connect_cells(current_cell_index, new_cell_index, new_cell_compass_index)
            # Push current cell to stack
            stack.append(current_cell_index)
            # Set current cell to new cell
            current_cell_index = new_cell_index
            # Add 1 to visited cells
            visited_cells += 1
        else:
            stack.pop()
            current_cell_index = stack[-1]
        m.refresh_maze_view()
    # Since maze has been generated, we can now solve
    m.state = 'solve'


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return


if __name__ == '__main__':
    main()
