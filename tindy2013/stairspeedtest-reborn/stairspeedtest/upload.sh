#!bin/bash
ret=""
for f in "$@"
do
    ref=`curl --retry 5 --progress-bar -F source=@$f "https://img.gtary.com/api/1/upload/?format=txt&type=reborn"`
    ret=${ret}"["${f}"]: "${ref}"\n"
    rm -rf ${f}
done

echo -e $ret