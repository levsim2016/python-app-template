#!/bin/bash

get_scripts_directory() {
  os_name=$(uname | tr '[:upper:]' '[:lower:]')
  app_root=$(pwd)
  bin_dir=''

  case $os_name in
    linux*|darwin*|freebsd*)
      bin_dir='/venv/bin'
      ;;
    msys*|mingw64*|cygwin_nt*)
      bin_dir='/venv/Scripts'
      ;;
  esac

#  if [ ! -d "$bin_dir" ] && [ "$bin_dir" = "${app_root}/venv/bin" ] && [ -d "${app_root}/venv/Scripts" ]; then
#    echo 'sdsdsd'
#    bin_dir='/venv/Scripts'
#  fi

  echo ${app_root}${bin_dir}
}

activate() {
  if [ $# -eq 0 ]; then
      echo -1
  fi
  
  /bin/bash -c ". ${1}"
}

cd $(dirname $(realpath $0))/..

scripts_dir=$(get_scripts_directory)

echo $scripts_dir

script_path=$scripts_dir/activate

activate $script_path
