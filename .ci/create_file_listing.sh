echo "{" > listing.json
git ls-tree -r HEAD --name-only | sed '/^\./d' | sed 's/^\(.*\)$/\t"\1": "\1"/' >> listing.json
echo "}" >> listing.json
sed -zi 's/"\n\t/",\n\t/g' listing.json
