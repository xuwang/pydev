# If use Puppet facts to manage admin password, then you can use this to create other users accounts.
admin_user=$(sudo facter mongo_admin)
admin_pass=$(sudo facter mongo_admin_pass)
dev_db=$(sudo facter mongo_dev_db)
dev_user=$(sudo facter mongo_dev_user)
dev_pass=$(sudo facter mongo_dev_pass)
cat > /tmp/newuser.js <<EOF
db.getSiblingDB("$dev_db").createUser({"user":"$dev_user", "pwd":"$dev_pass", "roles":["dbOwner"	]})
EOF
mongo admin -u $admin_user -p $admin_pass < /tmp/newuser.js
#rm /tmp/newuser.js