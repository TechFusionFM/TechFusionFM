echo "Locating CMS Folder"
cd ~/TechFusionFM
echo "Generating Static Files"
hexo generate
echo "Removing Existing Static Files on Apache Server"
rm -rf /var/www/html/*
echo "Coping Static Files to Apache Server"
cp -r ~/TechFusionFM/public/* /var/www/html/
echo "Removing Generated Files from CMS Folder"
rm -rf ~/TechFusionFM/public
echo "Deployment Complete, visit http://TechFusionFM.com"
