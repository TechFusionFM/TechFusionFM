# You've got the following unique IP.
#cat /var/log/apache2/access.log |awk '$9==200' &&'(index($7, "mp3") !=0)' &&'$2=$3=$4=$5=$6=$8=$10=$11=""; {print $0}'  | sort | uniq 
# User Agent Strings 
#cat /var/log/apache2/access.log |awk -F\" '{print $5 $6}'| sort | uniq 
cat /var/log/apache2/access.log |awk -F\" '(index($2, "mp3") !=0) {print}'| sort | uniq   > ~/1.txt
cat ~/1.txt |awk '$2=$3=$5=$6=$8=$10=$11=""; {print $0}' > ~/2.txt
rm ~/1.txt
cat ~/2.txt |awk '$4=""; {print $0}' | sort | uniq 
rm ~/2.txt


