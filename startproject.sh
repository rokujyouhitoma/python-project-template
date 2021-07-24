if [ $# -ne 1 ]; then
  echo "$#" 1>&2
  exit 1
fi

old=sample
new=$1

files=(
    "Makefile"
    "pyproject.toml"
    "tests/sample/test_parser.py"
    "tests/sample/test_sample1.py"
)

for ((i=0; i < ${#files[@]}; i++)) {
  sed -i "" -e "s/${old}/${new}/g" ${files[i]}
}

mv src/${old} src/${new}
