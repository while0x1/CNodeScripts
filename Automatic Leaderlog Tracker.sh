#!/bin/bash

datefile=<path-to-date-log>/leaderDateLog.txt
genesis=<path-to-shelley-genesis>/shelley-genesis.json
vrf=<path-to-vrf>/vrf.skey
export CARDANO_NODE_SOCKET_PATH=<path-to-node-socket>/db/socket

seconds=$((60*60*24*5))
if test -f "$datefile" ; then
        if test "$(($(date "+%s")-$(date -f "$datefile" "+%s")))"  -lt "$seconds" ; then
#                echo "5 Days has not Elapsed"
                exit 1
        fi
fi

date -R > "$datefile"

date=$(date)
epoch=$(cardano-cli query tip --mainnet | jq '.epoch')
echo "Executed ${date} Epoch:${epoch}" >> leaderlog.txt

cardano-cli query leadership-schedule \
   --mainnet \
   --genesis "$genesis" \
   --stake-pool-id <pool-id> \
   --vrf-signing-key-file "$vrf" \
   --next >> leaderlog.txt
#echo "Leaderlog process complete"
#The following will only print out leader slots in the leaderlog.txt file and will colour/arrange the output in a readable fashion

#cat leaderlog.txt | awk 'BEGIN { print  "\033[36mDate      \033[32m UTC Time\033[31m Slot"
#print "\033[0m---------- -------- --------"  } $1 ~ /^[0-9]/ { print "\033[36m" $2,
# "\033[32m" $3, "\033[31m" $1}'
