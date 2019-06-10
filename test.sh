export GITREPO=$(cd `dirname $0`; pwd)

[ ! -d $GITREPO/output ] && mkdir $GITREPO/output
python -B travis.py $GITREPO $GITREPO/output
