# hexo-generator-multiple-podcast
A generator for Hexo that can produce more than one podcast per blog, based on presence of media files, categories, or tags

This is very much beta software, and it's not even quite feature-complete. Use at your own risk, YMMV, etc.

## Configuration Quick Reference

In `_config.yml`

```yaml
podcasts:
- feed:
    path: foot-cast.xml # relative to site root
    title: My Football Podcast
    subtitle: My ramblings about football
    image: img/podcast/FootCast.jpg # relative to config.url + config.root
    non_feed_url: category/footcast/ # the non-feed source for this content
    category: FootCast # see below for tag-based feed
    limit: 100 # how many episodes will be in the feed, max
    content: true # whether to include text content along with the podcast; see note below
    content_encoded: true # same as above, but includes the complete encoded text of the post; see note below
    itunes:
      summary: I am right about football; if you agree, you are right too.
      author: Me, Myself, and I # defaults to config.author
      owner: Me, Myself, and I 
      email: me@example.com # e-mail from which iTunes podcast is registered
      category: Sports # the category from iTunes; make sure to use their values
      subcategory: Football # same as above
      explicit: clean # valid values are yes, no, and clean
    media_base_url: http://myhostingprovider.com/mysubdir/ # why repeat that in every post?
    default_media_type: audio/mpeg # can be overridden in post
- feed:
    path: basket-cast.xml # relative to site root
    title: My Basketball Podcast
    subtitle: My ramblings about basketball
    image: img/podcast/BasketCast.jpg # relative to config.url + config.root
    non_feed_url: tag/basketcast/ # the non-feed source for this content
    tag: basketcast # see above for category-based feed
    limit: 20 # how many episodes will be in the feed, max
    itunes:
      summary: I am right about basketball too
      author: Me, Myself, and I # defaults to config.author
      owner: Me, Myself, and I 
      email: me@example.com # e-mail from which iTunes podcast is registered
      category: Sports # the category from iTunes; make sure to use their values
      subcategory: Basketball # same as above
      explicit: clean # valid values are yes, no, and clean
    media_base_url: http://myhostingprovider.com/myothersubdir/
    default_media_type: audio/mpeg # can be overridden in post
```

**Content Note**: If you want control over the content or encoded content placed into the podcast feed, you can put a script file in the `scripts` directory of your site, and use it to set `content` or `content_encoded` to a function that receives the post and returns the content. For example, if I wanted to add "BOO-YAH!" to the content for BasketCast (the second feed in the above example), and I wanted it in bold type for the people who viewed encoded content, I could do the following:

```js
hexo.config.podcasts[1].feed.content = post =>
  `${post.content} - BOO-YAH!`
hexo.config.podcasts[1].feed.content_encoded = post =>
  `${post.content} - <strong>BOO-YAH!</strong>`
```

In each post:

```yaml
---
title: The Next Episode
date: 2017-04-22 12:34:56
# categories: or tags:, as appropriate
media: episode-file-name.mp3 # or a complete path; required (will be appended to feed:media_base_url)
length: 3443223 # size of the file in bytes; required
duration: "14:38" # HH:MM:SS or MM:SS; required
subtitle: Soon to the be the previous episode # optional (defaults to empty)
media_type: audio/mpeg # MIME type of the media file; optional (defaults to default_media_type)
author: Me # optional (defaults to feed:itunes:author)
image: next.png # for the episode; optional (defaults to feed image)
explicit: clean # optional (defaults to feed:itunes:explicit)
chapters: # optional, excluded from feed if absent
- [ "00:00:00.000", "Chapter 1" ]
- [ "00:05:00.000", "Five Minutes In" ]
# and so on
---
```
