This script is used to get a list of all files under a specific path in jcenter.
To run, simply run './jcenter.sh' and provide the path as an argument. i.e: </br>
./jcenter.sh http://jcenter.bintray.com/org/jfrog/

This will create the paths.txt file and output a list of all files into it.

To get a list of files on your user's repositories (not on jcenter), run the dl.sh script, i.e: </br>
./dl.sh http://dl.bintray.com/itamarb/maven/
