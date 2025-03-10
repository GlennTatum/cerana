# HOW TO USE THIS SCRIPT
# Make sure to initially build the custom openvscode-server before hand
# ./run-docker.sh github.com/repository
docker run -it --init -e GITHUB_WORKSPACE=$1 -e BASE_URL=$2 -p 3000:3000 -v "$(pwd):/home/src:cached" codeserver:url
#gitpod/openvscode-server