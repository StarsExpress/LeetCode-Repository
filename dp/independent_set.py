import os
from copy import deepcopy
from config import DATA_FOLDER_PATH


def read_nodes():
    nodes_dict = dict()  # 1st line isn't related to node distance.
    nodes = open(os.path.join(DATA_FOLDER_PATH, "nodes", "nodes_1k.txt"), "r").readlines()[1:]
    for node in nodes:
        weight = int(node.replace("\n", ""))
        nodes_dict.update(
            {str(len(nodes_dict) + 1): weight}
        )  # Key: node ordinal; value: weight.

    return nodes_dict


def find_max_independent_set(nodes_dict: dict, query_nodes: list | tuple = None):
    if len(nodes_dict) <= 0:
        raise ValueError("Nodes dictionary empty.")
    if len(nodes_dict) == 1:
        return list(nodes_dict.keys())[0]

    nodes_list, iter_idx = (
        list(nodes_dict.keys()),
        2,
    )  # Main loop starts from 3rd node's index.
    mis_dict = {
        "two_before": {"set": [nodes_list[0]], "weight": nodes_dict[nodes_list[0]]},
        "last": {"set": [nodes_list[1]], "weight": nodes_dict[nodes_list[1]]},
    }

    if len(nodes_list) >= 3:
        while iter_idx != len(nodes_list):
            # Two-before set retakes lead over last set.
            if mis_dict["two_before"]["weight"] + nodes_dict[nodes_list[iter_idx]] > mis_dict["last"]["weight"]:
                mis_dict["two_before"]["set"].append(nodes_list[iter_idx])
                mis_dict["two_before"]["weight"] += nodes_dict[nodes_list[iter_idx]]

                # Swap two sets for next iteration round.
                mis_dict["two_before"], mis_dict["last"] = mis_dict["last"], mis_dict["two_before"]

            else:  # Two-before set doesn't retake lead: use "deep copy" to update dict.
                mis_dict.update({"two_before": deepcopy(mis_dict["last"])})

            iter_idx += 1

    if mis_dict["two_before"]["weight"] < mis_dict["last"]["weight"]:
        mis = mis_dict["last"]

    else:
        mis = mis_dict["two_before"]

    if query_nodes is None:
        return mis["set"]

    query_result = []  # If just want to check whether some nodes are in MIS.
    for node in query_nodes:
        if node in mis["set"]:
            query_result.append("1")
            continue
        query_result.append("0")
    return "".join(query_result)


if __name__ == "__main__":
    nodes_dictionary = read_nodes()
    query_nodes_list = ["1", "2", "3", "4", "17", "117", "517", "997"]
    print(find_max_independent_set(nodes_dictionary, query_nodes_list))
