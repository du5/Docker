#!bin/bash
jsonRet=""
for f in "$@"
do
    convert ${f} ${f}.jpg
    f=${f}.jpg
    ref=$(curl --progress-bar -F smfile=@$f https://sm.ms/api/v2/upload | jq '"[\(.data.filename)](\(.data.url))"')
    ref=${ref//\"/}
    jsonRet=${jsonRet}$ref"\n"
    rm -rf ${f}
done

echo -e $jsonRet