#! /bin/bash
dir="./images"
#

i=0
function ergodic(){
    for file in ` ls $1 `
    do
        # echo $2
          filename1=$(basename "$file")
          fname="${filename1%.*}"
          ext="${filename1##*.}"
        if [ -d $1"/"$file ]
        then
             ergodic $1"/"$file $2
        else
             # echo "$1/$file"
             i=$((i+1))
             printf -v s "%05d" $i
             # echo $2
             cp "$1/$file" "$path/${filename}_all/${j}_$s.$ext"
        fi
    done
}



files=$(ls $dir)
for filename in $files
do
  cid_str=$(grep $filename cid.csv)
  cid=$(expr $(echo $cid_str| cut -d' ' -f 1))
  # cid=$(expr $cid)
  printf -v j "%05d" $cid

  if [ -d ./images/$filename/${filename}_all ]
      then
      continue
  fi
  mkdir "./images/$filename/${filename}_all"
  path="./images/$filename/"


ergodic $path "${filename}_all"
done
