from config import DATA_FOLDER_PATH
import os
from copy import deepcopy


def read_nodes():
    nodes_dict = dict()  # 1st line isn't related to node distance.
    nodes = open(os.path.join(DATA_FOLDER_PATH, 'nodes', 'nodes_1k.txt'), 'r').readlines()[1:]
    for node in nodes:
        weight = int(node.replace('\n', ''))
        nodes_dict.update({str(len(nodes_dict) + 1): weight})  # Key: node ordinal; value: weight.

    del nodes, weight
    return nodes_dict


def find_max_independent_set(nodes_dict: dict, query_nodes: list | tuple = None):
    if len(nodes_dict) <= 0:
        raise ValueError('Nodes dictionary is empty.')
    if len(nodes_dict) == 1:
        return list(nodes_dict.keys())[0]

    nodes_list, iter_idx = list(nodes_dict.keys()), 2  # Main loop starts from index of 3rd node, which is 2.
    mis_dict = {'two_before': {'set': [nodes_list[0]], 'weight': nodes_dict[nodes_list[0]]},
                'last': {'set': [nodes_list[1]], 'weight': nodes_dict[nodes_list[1]]}}  # MIS: maximal independent set.

    if len(nodes_list) >= 3:
        while True:
            # Update MWIS and its weight if two-before set retakes lead over last set.
            if mis_dict['two_before']['weight'] + nodes_dict[nodes_list[iter_idx]] > mis_dict['last']['weight']:
                mis_dict['two_before']['set'].append(nodes_list[iter_idx])
                mis_dict['two_before']['weight'] += nodes_dict[nodes_list[iter_idx]]
                # Swap two sets for next round of iteration.
                mis_dict['two_before'], mis_dict['last'] = mis_dict['last'], mis_dict['two_before']

            else:  # If two-before set doesn't retake lead, update its values to last set's values.
                mis_dict.update({'two_before': deepcopy(mis_dict['last'])})  # Must use deep copy in dict.

            iter_idx += 1
            if iter_idx == len(nodes_list):
                break

    if mis_dict['two_before']['weight'] < mis_dict['last']['weight']:
        mis = mis_dict['last']

    else:
        mis = mis_dict['two_before']

    del mis_dict, nodes_list, iter_idx
    if query_nodes is not None:  # If just want to check whether some nodes are in MWIS or not.
        query_result = []
        for node in query_nodes:
            if node in mis['set']:
                query_result.append('1')
                continue
            query_result.append('0')
        return ''.join(query_result)
    return mis['set']


if __name__ == '__main__':
    nodes_dictionary = read_nodes()
    query_nodes_list = ['1', '2', '3', '4', '17', '117', '517', '997']
    print(find_max_independent_set(nodes_dictionary, query_nodes_list))
