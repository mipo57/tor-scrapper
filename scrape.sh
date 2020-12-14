#!/bin/bash

script_params=()
while test $# -gt 0; do
    case "$1" in
        --input_file)
            shift
            input_file=$1
            shift
            ;;
        --output_file)
            shift
            output_file=$1
            shift
            ;;
        *)
            script_params+=($1)
            shift
            ;;
    esac
  done  

docker_params=(
    -v $(pwd)/src:/home/user/workspace/src:ro
    -v $(realpath $input_file):/home/user/workspace/input_file
    -v $(realpath $output_file):/home/user/workspace/output_file
    --rm
)

script_params+=(
    --input_file /home/user/workspace/input_file
    --output_file /home/user/workspace/output_file
)

command=(docker run)
touch $output_file

${command[@]} -it \
    ${docker_params[@]} \
    $(docker build -q --build-arg USER_UID=$(id -u) --build-arg USER_GID=$(id -g) .) \
    python3 -m src.main \
    ${script_params[@]} \