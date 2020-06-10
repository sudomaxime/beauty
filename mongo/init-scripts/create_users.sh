#!/bin/bash
set -e

mongo <<EOF
use admin
db.createUser(
  {
    user: "$MONGO_DATABASE_ADMIN_NAME",
    pwd: "$MONGO_DATABASE_ADMIN_PASSWORD",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)
exit
EOF

mongo <<EOF
use admin
db.auth("$MONGO_DATABASE_ADMIN_NAME", "$MONGO_DATABASE_ADMIN_PASSWORD")
use $MONGO_INITDB_DATABASE
db.createUser(
  {
    user: "$MONGO_INITDB_DATABASE_ADMIN",
    pwd: "$MONGO_INITDB_DATABASE_PASSWORD",
    roles: [ { role: "readWrite", db: "$MONGO_INITDB_DATABASE" } ]
  }
)
exit
EOF