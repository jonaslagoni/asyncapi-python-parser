# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")

git clone https://github.com/asyncapi/spec-json-schemas.git "$SCRIPTPATH/new_specs"
rm -rf "$SCRIPTPATH/../definitions"
mkdir "$SCRIPTPATH/../definitions"
find "$SCRIPTPATH/new_specs/schemas" -name '*-without-$id.json' -exec mv {} "$SCRIPTPATH/../definitions/" \;
rm -rf "$SCRIPTPATH/new_specs"