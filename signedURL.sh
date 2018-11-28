#!/bin/bash
RED='\033[1;31m'
NC='\033[0m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
echo "Enter your UserName (Mandatory)"
read user
echo "Enter you api key (Mandatory)"
read pass
echo "Enter file name (Mandatory)"
read file
echo "Enter day to expiry (Default 1)"
read days
#echo "Enter repository name (Default: file_transfer)"
#read repo
echo "Enter package name (Default: temp)"
read package
echo "Enter version number (Default: 1.0)"
read version

declare -i time=$(date +%s%0000)

#if [ -z "$repo" ]
#	then
declare	repo=file_transfer
#fi

if [ -z "$package" ]
	then
	package=temp
fi

if [ -z "$version" ]
	then
	version=1.0
fi
echo ""
echo ""
echo -e ${BLUE}Checking if the $repo repository exists${NC}
echo ""
echo ""
defaultowner='jfrog-int'

temp1="$(curl -X GET -u$user:$pass "https://api.bintray.com/repos/jfrog-int/$repo" | python -c "import sys, json; print json.load(sys.stdin)['owner']")" #| jq -r '.owner')"

if [ "$temp1" = "$defaultowner" ]
	then
	echo ""
	echo ""
	echo -e ${GREEN}Repository already exists${NC}
	echo ""
	echo ""
else
	echo -e ${BLUE}Creating the $repo generic repository${NC}
	curl -X POST -u$user:$pass "https://api.bintray.com/repos/jfrog-int/$repo" -H "Content-Type:application/json" -d'{"name": "$repo","type": "generic","private": true}'
	echo ""
	echo ""
	echo ""
fi

echo -e ${BLUE}Checking if the $package package exists${NC}
echo ""
echo ""
temp1="$(curl -X GET -u$user:$pass "https://api.bintray.com/packages/jfrog-int/$repo/$package" | python -c "import sys, json; print json.load(sys.stdin)['name']")" #| jq -r '.name')"

if [ "$temp1" = "$package" ]
	then
	echo ""
	echo ""
	echo -e ${GREEN}Package already exists${NC}
	echo ""
	echo ""
else
	echo -e ${BLUE}Creating the $package package${NC} 
	echo ""
	echo ""
	curl -X POST -u$user:$pass "https://api.bintray.com/packages/jfrog-int/$repo" -H "Content-Type:application/json" --data-binary '{"name": "'$package'"}'
	echo ""
	echo ""
	echo ""
fi

echo -e ${BLUE}Uploading $file${NC}
echo ""
echo ""
curl -T $file -u$user:$pass "https://api.bintray.com/content/jfrog-int/$repo/$package/$version/$file?publish=1"

echo ""
echo ""
echo ""
echo -e ${BLUE}waiting for publication${NC}
echo ""
echo ""
sleep 10

echo -e ${BLUE}Generating signed URL${NC}
echo ""
echo ""

if [ -z "$days" ]
  then
  echo -e ${BLUE}No expiry was given, setting to default of 24 hours${NC}
  echo ""
  echo ""
  echo -e ${BLUE}Generating URL${GREEN}
    curl -X POST -u$user:$pass "https://api.bintray.com/signed_url/jfrog-int/$repo/$file" -H "Content-Type:application/json"
    echo ""
    echo ""
    echo ""
  else
  	declare -i plus=$(($days * 86400000 ))
    declare -i expiry=$((time + plus))
    echo -e ${BLUE}Generating URL${GREEN}
  	curl -X POST -u$user:$pass "https://api.bintray.com/signed_url/jfrog-int/$repo/$file" -H "Content-Type:application/json" -d'{"expiry": '$expiry'}'
fi