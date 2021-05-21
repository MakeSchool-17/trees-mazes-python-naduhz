from random import random
import maze
import generate_maze
import sys


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    # Create a stack for backtracking
    stack = []
    # Set current cell to 0
    current_cell_index = 0
    # Set visited cells to 0
    visited_cells = 0

    while current_cell_index != (m.total_cells - 1):
        # Get unvisited neighbours
        unvisited_neighbours = m.cell_neighbors(current_cell_index)
        if unvisited_neighbours:
            # Choose random neighbor to be new cell
            new_cell = unvisited_neighbours[random.randint(0, len(unvisited_neighbours)-1)]
            new_cell_index = new_cell[0]
            new_cell_compass_index = new_cell[1]
            # Visit new_cell
            m.visit_cell(current_cell_index, new_cell_index, new_cell_compass_index)
            # Push current cell to stack
            stack.append(current_cell_index)
            # Set current cell to new_cell
            current_cell_index = new_cell_index
            # Add 1 to visited_cells
            visited_cells += 1
        else:
            # Backtrack to previous cell
            m.backtrack(current_cell_index)
            # Pop from stack to current cell
            current_cell_index = stack.pop()
        m.refresh_maze_view()
    # Now that the maze has been solved we can set it to idle
    m.state = 'idle'


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    # Create a queue
    queue = []
    # Set current_cell_index to 0
    current_cell_index = 0
    # Set in_direction to 0b0000
    in_direction = 0
    # Set visited_cells to 0
    visited_cells = 0
    # Enqueue (current cell, in direction)
    queue.append((current_cell_index, in_direction))

    while (current_cell_index != (m.total_cells - 1)) and queue:
        # Dequeue to current_cell_index, in_direction
        current_cell_index, in_direction = queue.pop(0)
        # Visit current cell
        m.bfs_visit_cell(current_cell_index, in_direction)
        visited_cells += 1
        m.refresh_maze_view()

        # Get unvisited neighbours of current cell
        unvisited_neighbours = m.cell_neighbors(current_cell_index)
        # Enqueue the unvisited neighbours
        for neighbour in unvisited_neighbours:
            queue.append((neighbour[0], neighbour[1]))
    # Trace the solution path
    m.reconstruct_solution(current_cell_index)
    # Path reconstructed, set to idle
    m.state = 'idle'


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
