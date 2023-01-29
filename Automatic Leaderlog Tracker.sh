0 17 */5 * * /<path-to-script>/leaderlog-next.sh

#!/bin/bash
date=$(date)
epoch=$(cardano-cli query tip --mainnet | jq '.epoch')
echo "Executed ${date} Epoch:${epoch}" >> leaderlog.txt

cardano-cli query leadership-schedule \
   --mainnet \
   --genesis $NODE_HOME/shelley-genesis.json \
   --stake-pool-id <your-pool-ID> \
   --vrf-signing-key-file <path-to-VRF>vrf.skey \
   --next >> leaderlog.txt

echo >> leaderlog.txt
echo "Leaderlog process complete"
cat leaderlog.txt | awk 'BEGIN { print  "\033[36mDate      \033[32m UTC Time\033[31m Slot"
print "\033[0m---------- -------- --------"  } $1 ~ /^[0-9]/ { print "\033[36m" $2,
 "\033[32m" $3, "\033[31m" $1}'
