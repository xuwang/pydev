# If use Puppet facts to manage admin password, then you can use this to create other users accounts.
admin_user=$(sudo facter mongo_admin)
admin_pass=$(sudo facter mongo_admin_pass)
dev_deb=$(sudo facter mongo_dev_db)
dev_user=$(sudo facter mongo_dev_user)
dev_pass=$(sudo facter mongo_dev_pass)
mongo admin -u $admin_user -p $admin_pass --eval "db.getSiblingDB($dev_db).db.createUser($dev_user, $dev_pass)"
