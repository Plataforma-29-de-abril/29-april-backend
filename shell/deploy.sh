#!/bin/bash
# chmod +x shell/deploy.sh
# use example:
# ./shell/deploy.sh user1@123.45.678.910

if [ $# -ne 2 ]; then
    echo "Usage: $0 <server-conection> <project>"
    echo "Ex: $0 user1@123.45.678.910 29-april-backend"
    exit 2
fi

server_conn=$1
project=$2

echo "Deploying on $server_conn at /root/alessandro/$project"
rsync -avz --exclude="postgres-data" --exclude="portal-aulas-api/media" --exclude="shell" --exclude=".env" --exclude=".env.dev" --exclude=".env.prod" --exclude=".git" --exclude="portal-aulas-api/env" --delete . $server_conn:/root/alessandro/$project
echo "Deploy concluído!"