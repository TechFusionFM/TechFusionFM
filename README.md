# TechFusionFM
[![HitCount](http://hits.dwyl.io/techfusionfm/techfusionfm.svg)](http://hits.dwyl.io/techfusionfm/techfusionfm)

Podcast hosting and feed generation website for TechFusionFM.com. Based on [Hexo](https://hexo.io), and theme [Anatole](https://github.com/hi-caicai/farbox-theme-Anatole). 

The website is the exact the same as deployed to https://TechFusionFM.com but static.

### Deployment
1. Make sure you have npm, 
2. Make sure you have apache2 in ```/var/www/html/``` 
3. Make sure apache2 is active, by typing these in the terminal: ```sudo service apache2 status.```
  3.1 If not active type these in the terminal: ```sudo service apache2 start.``` and check again
  3.2 If active, proceed to the next step
4. Make sure there's nothing you want to keep in ```/var/www/html/```, since the next step will wipe the ```/var/www/html/``` folder.
5. Install dependencies
```
$ cd TechFusionFM/
$ npm install
```
6. Deploy
```
$ sh autodep.sh
```

### Author
CMS:       [Hexo](https://hexo.io)

Theme Based on:  [Anatole](https://github.com/hi-caicai/farbox-theme-Anatole)

Telegram Bot, Custom Deployment Script, Show Notes, Custom XML Parser and Theme Customization: [Fengwei Jerry Zhang - zhang96](https://github.com/zhang96)


The content including but not limited to text displayed on the website, pictures and logos, audio files, [TechFusionFM.com](https://TechFusionFM.com) have exclusive right to them unless authorized. 

### License

[Creative Commons 4.0 BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/) for all files under /source/,	MIT for all other contents and code. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
