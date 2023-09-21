---
layout: container
urltitle:  "Download · RedCaps"
title: "Download · RedCaps"
permalink: "/download"
---

<!-- Download page can use CSS from home page. -->

<link rel="stylesheet" type="text/css" href="/static/css/explore.css">


<div class="cover-subtitle-container">
    <div class="text-left cover-text">Download dataset</div>
</div>  

**Current version:** v1.0 (released in XX month XX year)

**Terms of use:**
Uses are subject to <a href="//www.reddit.com/wiki/api-terms" target="_blank">Reddit API terms</a>.


<a href="" class="btn btn-danger" style="background-color: #d45855">
Click here to download v1.0 (XX GB)
</a>

This file contains JSON files containing 

- XX
- XX
- XX
- ...
along with <a href="" target="_blank">XX license</a>
and <a href="//www.reddit.com/wiki/api" target="_blank">Reddit API terms of use</a>.

- **The file structure**:

```text
- README.txt
- TERMSOFUSE.txt
- metadata/
  ├── subreddit 1/
      ├── <reddit.post.id 1>.json
      ├── <reddit.post.id 2>.json
      ├── ...
      └── ...
  ├── subreddit 2/
  ├── ...
  └── ...
```



<div class="row homesec-title">
    <h2>Metadata format</h2>
  </div>
Each `<reddit.post.id>.json` contains metadata of image posts from a single subreddit,
following this schema.


A sample example from the datatset:
```json
{
    "title": "elon musk at my local barnes and noble",
    "url": "https://i.redd.it/a7oueb592bpb1.jpg",
    "comments": [
        {
            "author": "moxyfloxacin",
            "body": "i hope its pages and pages of the truth i doubt it though",
            "created_utc": "2023-09-19 20:46:15",
            "analysis": {
                "common nouns": {
                    "hope": 1,
                    "page": 2,
                    "doubt": 1,
                    "truth": 1
                },
                "emotion tag": "optimism",
                "attention scores": {
                    "hope": 1.0,
                    "doubt": 0.11211709678173065
                }
            }
        },
        {
          "author": "DataAstronaut_",
          "body": "just listened to walter isacsons podcast with lex friedman from the sound of him talking about elon on it should be an interesting read",
          "created_utc": "2023-09-19 21:22:38",
          "analysis": {
                "common nouns": {
                  "walter": 1,
                  "isacsons": 1,
                  "friedman": 1,
                  "elon": 1,
                  "podcast": 1,
                  "walter isacsons": 1,
                  "interesting read": 1,
                  "walter isacsons podcast": 1,
                  "isacsons podcast": 1
                },
                "verbs": {
                  "listen": 1,
                  "sound": 1,
                  "talk": 1,
                },
                "adjectives": {
                    "interesting": 1,
                    "lex friedman": 1
                },
                "emotion tag": "approval",
                "attention scores": {
                    "listened": 1.0,
                    "read": 0.2401873618364334,
                    "interesting": 0.10860899090766907,
                }
            }
        },
        ...
    ]
}
```
