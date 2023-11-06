# Developed by Itamar Berman-Eshel (bitman30@gmail.com)

import json
from mergedeep import merge
import sys

arguments = sys.argv
num_args = len(sys.argv) - 1
if num_args == 0:
    print("Invalid number of parameters. Please provide file name and optionally a virtual repository name.")
    sys.exit()
file_name = arguments[1]

global virtual_containing_virtuals
virtual_containing_virtuals = []
# Read the JSON file
#with open('repo.json', 'r') as file:
with open(file_name, 'r') as file:
    data = json.load(file)

def get_children(virtualRepo, visitedRepoKeys):
    result = {}
    if virtualRepo is None:
        return []
    current_virtual_repo_key = virtualRepo['key']
    if current_virtual_repo_key in visitedRepoKeys:
        virtual_containing_virtuals.append(current_virtual_repo_key)
        return {current_virtual_repo_key: "********* created a loop because it includes one of its parent"}
    else:
        result[current_virtual_repo_key] = {'type': 'virtual'}

    visitedRepoKeys.append(current_virtual_repo_key)
    if virtualRepo['repoTypeConfig'] is not None and virtualRepo['repoTypeConfig']['repositoryRefs'] is not None:
        repos_contained_in_current_virtual = virtualRepo['repoTypeConfig']['repositoryRefs']
        for childRepo in repos_contained_in_current_virtual:
            child_repo_descriptor = get_repo_descriptor_by_name(childRepo)
            if child_repo_descriptor is not None and child_repo_descriptor['type'] == "virtual":
                result[current_virtual_repo_key] = merge(result.get(current_virtual_repo_key, {}), (get_children(child_repo_descriptor, visitedRepoKeys)))
            else:
                child_repo_key = child_repo_descriptor['key']
                result[current_virtual_repo_key] = merge(result.get(current_virtual_repo_key, {}), {child_repo_key: {'type': child_repo_descriptor['type']}})  # put current repo in map
    return result


def get_repo_descriptor_by_name(child):
    repo_configs = data["localRepoConfigs"] + data["remoteRepoConfigs"] + data["virtualRepoConfigs"] + data["federatedRepoConfigs"]
    for Repo in repo_configs:
        if Repo['key'] == child:
            return Repo

if num_args == 1:
    for virtualRepoConfig in data['virtualRepoConfigs']:
        tree = get_children(virtualRepoConfig, [])
        print(json.dumps(tree, indent=2))
elif num_args == 2:
    for virtualRepoConfig in data['virtualRepoConfigs']:
        if virtualRepoConfig['key'] == arguments[2]:
            tree = get_children(virtualRepoConfig, [])
            print(json.dumps(tree, indent=2))
else:
    print("Invalid number of parameters. Please provide file name and optionally a virtual repository name.")

if num_args == 1:
    print('Virtuals containing virtuals: ', set(virtual_containing_virtuals))
