echo "Locating CMS Folder"
cd ~/TechFusionFM
echo "Generating Static Files"
hexo deploy
echo "Unescaping xml"
echo "--replacing replace <"
sed -ie 's/\&amp\;lt\;/\</g' ~/TechFusionFM/public/podcast.xml
echo "--replacing replace >"
sed -ie 's/\&amp\;gt\;/\>/g' ~/TechFusionFM/public/podcast.xml
echo "--replacing quotation"
sed -ie 's/\&amp\;quot\;/\"/g' ~/TechFusionFM/public/podcast.xml
echo "--replacing ' "
sed -ie "s/\&amp\;apos\;/\\'/g" ~/TechFusionFM/public/podcast.xml

echo "Removing Existing Static Files on Apache Server"
rm -rf /var/www/html/*
echo "Coping Static Files to Apache Server"
cp -r ~/TechFusionFM/public/* /var/www/html/
echo "Removing Generated Files from CMS Folder"
rm -rf ~/TechFusionFM/public
echo "Deployment Complete, visit http://TechFusionFM.com"
