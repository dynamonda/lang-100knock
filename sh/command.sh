#!/bin/sh

FILE="./popular-names.txt"

# 10.行数のカウント(wc)
CountLine () {
    echo "10.行数のカウント"
    wc -l ${FILE}
}

# 11.タブをスペースに置換(sed, tr, expand)
ReplaceTabToSpace () {
    echo "11.タブをスペースに置換"
    FILE11="./popular-names_space.txt"
    # タブ幅=2
    expand -t 2 ${FILE} > ${FILE11}
}

COL1="./col1.txt"
COL2="./col2.txt"

# 12.1列目をcol1.txtに、2列目をcol2.txtに保存(cut)
SaveColumns () {
    echo "12.1列目をcol1.txtに、2列目をcol2.txtに保存"
    cut -f 1 ${FILE} > ${COL1}
    cut -f 2 ${FILE} > ${COL2}
}

# 13.col1.txtとcol2.txtをマージ(paste)
MergeColumns () {
    echo "13.col1.txtとcol2.txtをマージ"
    paste ${COL1} ${COL2} > "./merge_columns.txt"
}

# 14.先頭からN行を出力(head)
HeadLines () {
    echo "14.先頭からN行を出力, N=$1"
    head -n $1 ${FILE}
}

# 15.末尾のN行を出力(tail)
TailLines () {
    echo "15.末尾のN行を出力, N=$1"
    tail -n $1 ${FILE}
}

# 16.ファイルをN分割する(split)
SplitFiles () {
    line=`wc -l ${FILE} | awk '{print $1}'`
    line=`expr ${line} / $1 + 1`

    echo "16.ファイルをN分割する, N=$1, line=${line}"
    
    split -l ${line} ${FILE} "split-"

    # -nオプションがない。。。？
    #split -n $1 -d ${FILE} "split-"
}

# 17.１列目の文字列の異なり(cut, sort, uniq)
Unique () {
    cut -f 1 ${FILE} | sort | uniq
}

# 18. 各行を3コラム目の数値の降順にソート
Sort () {
    sort -n -k 3 -r ${FILE}
}

# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる(cut, uniq, sort)
SortFrequency () {
    cut -f 1 ${FILE} | sort | uniq -c | sort -r
}

#CountLine
#ReplaceTabToSpace
#SaveColumns
#MergeColumns
#HeadLines 3
#TailLines 4
#SplitFiles 3
#Unique
#Sort
SortFrequency
