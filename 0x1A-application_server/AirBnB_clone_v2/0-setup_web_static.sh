#!/usr/bin/env bash
# setups web servers for deployment of web_static
WHERE="/etc/nginx/sites-available/default"
if ! dpkg -s nginx; then
    apt-get update
    if apt-get -y install nginx; then
	ADD="\\\tlocation \/redirect_me {\n\t\treturn 301 http://heindrickcheung.site;\n\t}\n"
	HEADER="\\\n\tadd_header X-Served-By \$hostname;"
	echo "codingschool School" | sudo tee /usr/share/nginx/html/index.html
	sed -i "30i $ADD" $WHERE
	sed -i "29i $HEADER" $WHERE
	new="\t\terror_page 404 @my404;"
	sudo sed -i "/^\tlocation \/ {$/a \\$new" /etc/nginx/sites-available/default
	new="location @my404 {\n\t\tdefault_type text/html;\n\t\treturn 404 \"Ceci n'est pas une page\";\n\t}"
	sudo sed -i "/^\tserver_name localhost;$/a \\\n\\t$new" /etc/nginx/sites-available/default
    fi
fi
cp /etc/nginx/sites-available/default{,.orig}
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "hello" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
ADD2="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sed -i "/^\tserver_name localhost;$/a \\\n\\t$ADD2" $WHERE
service nginx restart
