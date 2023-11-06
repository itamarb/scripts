# Artifactory Repository Tree Parser

# repoTree.py
repoTree is a small Python3 script that can check Virtual repositories for nested Locals and Remotes

## Installation
The script requires the "mergedeep" package. To get it, run:

```
pip install mergedeep
```

## Usage
To run the script, get the repositories.json file either from a Support Bundle or through the API. Then put the filename into the script as an option:

```
python ./repoTree.py artifactory.repository.config.json
```
Or:
```
python3 repoTree.py artifactory.repository.config.json
```

Expected Output:
```
{
  "nuget": {
    "type": "virtual",
    "nuget-local": {
      "type": "local"
    },
    "nuget-remote": {
      "type": "remote"
    },
    "nuget-devexpress": {
      "type": "remote"
    }
  }
}
```

You can optionally provide the script with a virtual repository name to list:
```
python ./repoTree.py artifactory.repository.config.json libs-releases
```
Or:
```
python3 repoTree.py artifactory.repository.config.json libs-releases
```

 

