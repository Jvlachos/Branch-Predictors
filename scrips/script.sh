#! /bin/bash

#@Author :Dimitris Vlachos(csd4492)
#bash script to collect the usefull data from the benchmark stats files
#the resulting files will contain two lines 
#1) the number of commited branches that were mispredicted 
#2) the total number of branches executed
# The files will be moved at each benchmark's directory with their names being the parameters of the simulation
#must be run from gem5/hy425 directory

path=~/"gem5/hy425"


for b in $path/*/ ; do
    let a=1
    base=$(basename $d)
   
    if [ -d "$b" ]; then
    for d in $b*/ ; do
        
        for c in $d; do
            name=$c
            if [ $a -ne 1 -a  $a -ne 2 ] 
            then
            base_dir="$(basename $name)"
            
            cd $name ; grep branch stats.txt | grep num | grep -Eo  '[[:digit:]]+' > "$base_dir.txt" ; (cd .. ;   mv "$name/$base_dir.txt" . )
            fi
            ((a=a+1))
  
        done
    done    
    fi
done  
#run python script for plots 
(cd ~/gem5/hy425; python3  collect_n_plot.py)