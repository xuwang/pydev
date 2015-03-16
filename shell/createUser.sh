# If use Puppet facts to manage admin password, then you can use this to create other users accounts.
password=$(sudo facter mongo_adminpass)
mongo admin -u admin -p $password --eval "db.getSiblingDB('dummydb').db.createUser('dummyuser', 'dummysecret')"
mongo admin -u admin -p $password --eval "db.getSiblingDB('dummydb').db.createUser('dummyuser1', 'dummysecret1')"
