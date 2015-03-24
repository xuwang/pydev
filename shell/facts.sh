#!/bin/sh

FACTSD=/etc/facter/facts.d
sudo mkdir -p $FACTSD

sudo cat > $FACTSD/mongodb.sh <<EOF
echo "mongo_admin=admin"
echo "mongo_admin_pass=adminpass"
echo "mongo_dev_db=devdb"
echo "mongo_dev_user=dev"
echo "mongo_dev_pass=devpass"
EOF

sudo chmod +x $FACTSD/*.sh
