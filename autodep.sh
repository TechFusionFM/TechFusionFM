echo "Removing Existing Static Files on Apache Server"
rm -rf /var/www/html/*
echo "Coping Static Files to Apache Server"
cp -r ~/TechFusionFM/public/* /var/www/html/
echo "Deployment Complete, visit http://TechFusionFM.com"