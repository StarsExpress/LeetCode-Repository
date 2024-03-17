from config import DATA_FOLDER_PATH
import os
import random
from copy import deepcopy


def find_vertices_relations():  # Return a dictionary showing all vertices connected to each vertex.
    vertices_dict = dict()
    edges = open(os.path.join(DATA_FOLDER_PATH, 'edges', 'edges_4k.txt'), 'r').readlines()
    for edge in edges:
        items_list = edge.replace('\n', '').split('\t')
        items_list.pop(-1)  # Remove last element, which is an empty string.
        vertices_dict.update({items_list[0]: items_list[1:]})  # Key: 1st vertex; value: the rest vertices in same row.

    del edges, items_list
    return vertices_dict


def find_min_cut(vertices_dict: dict):
    if len(vertices_dict) <= 2:  # Only run random contraction when at least 3 vertices exist.
        return

    vertices_dict = deepcopy(vertices_dict)  # To prevent altering dictionary of outer scope.
    while len(vertices_dict) > 2:
        vertex_1 = random.choice(list(vertices_dict.keys()))  # Randomly select 1st vertex from keys list.
        # Randomly select 2nd vertex from vertices list of 1st vertex. Edge between them are to be contracted.
        vertex_2 = random.choice(vertices_dict[vertex_1])

        while vertex_2 in vertices_dict[vertex_1]:  # Remove 2nd vertex from vertices list of 1st vertex.
            vertices_dict[vertex_1].remove(vertex_2)
        while vertex_1 in vertices_dict[vertex_2]:  # Remove 1st vertex from vertices list of 2nd vertex.
            vertices_dict[vertex_2].remove(vertex_1)

        vertices_dict[vertex_1].extend(vertices_dict[vertex_2])  # Put 2nd vertex's vertices list to that of 1st vertex.

        for vertex in vertices_dict[vertex_2]:  # For each vertices list having 2nd vertex, replace it with 1st vertex.
            while vertex_2 in vertices_dict[vertex]:
                vertices_dict[vertex].append(vertex_1)
                vertices_dict[vertex].remove(vertex_2)

        del vertices_dict[vertex_2]  # Vertex 2nd is merged into vertex 1st.

    # Track both remaining vertices' list length as number of crossing edges from both angles.
    crossing_edges_list = [len(vertices_list) for vertices_list in vertices_dict.values()]
    # Make sure both angles show the same crossing edges count.
    assert crossing_edges_list.count(crossing_edges_list[0]) == len(crossing_edges_list)
    del vertices_dict, vertex_1, vertex_2
    return crossing_edges_list[0]  # Number of crossing edges.


if __name__ == '__main__':
    vertices_dictionary = find_vertices_relations()
    min_cut_list, iterations = [], 40
    for _ in range(iterations):
        min_cut_list.append(find_min_cut(vertices_dictionary))
    print(f'Min cut list: {min_cut_list}\nMin cut: {str(min(min_cut_list))}')
    print(f'Min cut count: {str(min_cut_list.count(min(min_cut_list)))} out of {str(len(min_cut_list))}.')
