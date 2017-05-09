#!/bin/bash
### The root path to search has to be provided as an argument. i.e: ./jcenter.sh https://jcenter.bintray.com/org/jfrog/artifactory/client/
path=$1

## run wget on the path to get an index of it's content and save index in a file
function wgetFromPath {
wget $path -O wget.txt
}

## filter out the index to get only the subpath strings in a single file
function filter {
cat wget.txt | cut -f 2 -d ":" wget.txt | awk '{print $1}' | sed 1,10d | sed '$d' | sed '$d' | tr -d \" > paths.txt
## delete the index
rm wget.txt
}

## Iterate on each line in the file to create separate files for each line, append the subpath to the root path and put the files in the '1' folder
function createNextPath {
	## make empty folder that will later contain files, each with a single subpath
	mkdir 1
	## create iterator and set it to 1
	it=1
filename='paths.txt'
while read p; do
	if [[ "$p" == *.xml ]]
then
    echo "removing "$p "from results"
else
echo "path before is: " $path
path2=$path$p
echo "path after is: " $path2
echo $path2 >> 1/$it.txt
path2=$path
fi
((it+=1))

done < $filename
## remove temp file
rm paths.txt
## Using the 'mergeFilesToOne' method to create one file named 'paths.txt' with new paths
mergeFilesToOne
}

function mergeFilesToOne {
for i in 1/*.txt
do
cat $i >> paths.txt
done
rm -rf 1
}

function nextPathFromSingleFile {
mkdir 1
mkdir 2
it=1

filename='paths.txt'
while read p; do
path=$p
if [[ "$p" != */ ]]
	then
	echo "Skipping wget on" $p
	echo $p >> paths3.txt
   else
wget $path -O 1/$it.txt
cat 1/$it.txt | cut -f 2 -d ":" 1/$it.txt | awk '{print $1}' | sed 1,10d | sed '$d' | sed '$d' | tr -d \" > 2/$it.txt
filename="2/$it.txt"
while read p; do
if [[ "$p" == *.xml ]]
then
    echo "removing "$p "from results"
else
echo "path before is: " $path
path2=$path$p
echo "path after is: " $path2
echo $path2 >> paths2.txt
path2=$path
fi
done < $filename
((it+=1))
fi
done < $filename
## Remove temp files and folders
##rm paths.txt
file="paths2.txt"
	if [ -f $file ]; then
   echo "File $file exists, moving on to next folder depth"
   mv paths2.txt paths.txt
rm -rf 1
rm -rf 2
   nextPathFromSingleFile
else
   echo "File $file does not exist."
   rm -rf 1
   rm -rf 2
   cat paths3.txt >> paths.txt
   rm paths3.txt
   echo "Script complete - exiting"
   exit 1
fi


}

function splitFile {
	it=1
	mkdir working
	filename="paths.txt"
	while read p; do
	echo $p >> working/$it.txt
	((it+=1))
	done < $filename
}

#Execute methods
wgetFromPath
filter
createNextPath
nextPathFromSingleFile
