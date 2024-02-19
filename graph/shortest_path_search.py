from config import DATA_FOLDER_PATH
import os


def process_distances():
    file_path = os.path.join(DATA_FOLDER_PATH, 'edges_distances.txt')
    with open(file_path, 'r') as file:
        nodes = file.read().splitlines()
        file.close()

    distances_dict = dict()  # Keys: nodes tuple (smaller ordinal, bigger ordinal); values: distance.

    for node in nodes:
        distances_list = node.lstrip().rstrip().split('\t')  # Remove boundary spaces and split by \t.
        outgoing_node = distances_list.pop(0)  # 1st item of list is the outgoing node.

        for distance_str in distances_list:  # The rest items indicate distances between outgoing node and other nodes,
            (incoming_node, distance) = distance_str.split(',')
            distance = int(distance)  # Convert distance into integer.
            distance_tuple = (min([outgoing_node, incoming_node]), max([outgoing_node, incoming_node]))

            if distance_tuple not in distances_dict.keys():
                distances_dict.update({distance_tuple: distance})

    del file, file_path, node, nodes, distances_list, outgoing_node, incoming_node, distance
    return distances_dict


if __name__ == '__main__':
    import time

    start_time = time.time()
    distances_dictionary = process_distances()

    end_time = time.time()
    print(f'Run Time: {str(round(end_time - start_time))} seconds.')
