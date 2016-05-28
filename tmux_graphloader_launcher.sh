#!/bin/bash
coordLoc="infrc:host=192.168.1.170,port=12246"
masters=16
graphName="ldbc_snb_sf0100_01"
numLoaders=12
numThreads=6
splitSfx=".part%04d"
reportInt=2
reportFmt="FDT"
mode="edges"
dataset="/home/jdellit/git/ldbc_snb_datagen/social_network_sf0100"
graphLoaderDir="/home/jdellit/NetBeansProjects/ldbc-snb-impls/snb-interactive-torc"

# Create an array of all the hosts we have leased via rcres
i=0
for host in `rcres ls -l | grep "$(whoami)" | cut -c13-16 | grep "rc[0-9]" | cut -c3-4`;
do
  hosts[i]=$host
  (( i++ ))
done

# Create a new window with the appropriate number of panes
tmux new-window -n GraphLoader
for (( i=0; i<$numLoaders-1; i++ ))
do
  tmux split-window -h
  tmux select-layout tiled
done

# Setup the panes for loading but stop before executing GraphLoader
for (( i=0; i<$numLoaders; i++ ))
do
  tmux select-pane -t $i
  tmux send-keys "ssh rc${hosts[masters+i]}" C-m
  tmux send-keys "cd $graphLoaderDir" C-m
  tmux send-keys "mvn exec:java -Dexec.mainClass=\"net.ellitron.ldbcsnbimpls.interactive.torc.util.GraphLoader\" -Dexec.args=\"--coordLoc $coordLoc --masters $masters --graphName $graphName --numLoaders $numLoaders --loaderIdx $i --numThreads $numThreads --splitSfx \"$splitSfx\" --reportInt $reportInt --reportFmt $reportFmt $mode $dataset\""
done

