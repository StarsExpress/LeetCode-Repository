from config import DATA_FOLDER_PATH
import os
from copy import deepcopy


def read_nodes():
    nodes_dict = dict()  # Skip the 1st line that isn't related to node distance.
    nodes = open(os.path.join(DATA_FOLDER_PATH, 'nodes', 'nodes_1k.txt'), 'r').readlines()[1:]
    for node in nodes:
        weight = int(node.replace('\n', ''))
        nodes_dict.update({str(len(nodes_dict) + 1): weight})  # Key: node ordinal; value: weight.

    del nodes, weight
    return nodes_dict


def find_maximal_wis(nodes_dict: dict, query_nodes: list = None):
    if len(nodes_dict) <= 0:
        raise ValueError('Nodes dictionary is empty.')
    if len(nodes_dict) == 1:
        return list(nodes_dict.keys())[0]

    nodes_list, iter_idx = list(nodes_dict.keys()), 2  # Main loop starts from the index of 3rd node, which is 2.
    mwis_dict = {'two_before': {'set': [nodes_list[0]], 'weight': nodes_dict[nodes_list[0]]},
                 'last': {'set': [nodes_list[1]], 'weight': nodes_dict[nodes_list[1]]}}

    if len(nodes_list) >= 3:
        while True:
            # Update MWIS and its weight if two-before set retakes lead over last set.
            if mwis_dict['two_before']['weight'] + nodes_dict[nodes_list[iter_idx]] > mwis_dict['last']['weight']:
                mwis_dict['two_before']['set'].append(nodes_list[iter_idx])
                mwis_dict['two_before']['weight'] += nodes_dict[nodes_list[iter_idx]]
                # Swap two sets for next round of iteration.
                mwis_dict['two_before'], mwis_dict['last'] = mwis_dict['last'], mwis_dict['two_before']

            else:  # If two-before set doesn't retake lead, update its values to last set's values.
                mwis_dict.update({'two_before': deepcopy(mwis_dict['last'])})  # Must use deep copy in dict.

            iter_idx += 1
            if iter_idx == len(nodes_list):
                break

    if mwis_dict['two_before']['weight'] < mwis_dict['last']['weight']:
        mwis = mwis_dict['last']

    else:
        mwis = mwis_dict['two_before']

    del mwis_dict, nodes_list, iter_idx
    if query_nodes is not None:  # If just want to check whether some nodes are in MWIS or not.
        query_list = []
        for node in query_nodes:
            if node in mwis['set']:
                query_list.append('1')
                continue
            query_list.append('0')
        return ''.join(query_list)
    return mwis['set']


if __name__ == '__main__':
    nodes_dictionary = read_nodes()
    query_nodes_list = ['1', '2', '3', '4', '17', '117', '517', '997']
    print(find_maximal_wis(nodes_dictionary, query_nodes_list))
