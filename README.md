# Video Discovery

## Overview

This code is mostly the quick start code from POE, modified for the hackathon.  The use case is a bot that
answers questions about a particular domain ( in this case California DMV rules ) and also finds snippets
of video showing the related situation from TwelveLabs.  

## Requirements

Server subscription and startup from Modal, then you can use the bot at https://poe.com/Poe_AutoBot.  See the quick start guide below.

## Current issues/Caveats

TwelveLabs can give you video snippets if you do a search using their UI, but at the moment, their API
only gives you a jpg thumbnail.  Future iterations should have a url to a video snippet instead.

Your bot may be nonfunctional until you update the bot settings.  See the instructions here https://developer.poe.com/server-bots/updating-bot-settings and specifically,
execute this command: 

curl -X POST https://api.poe.com/bot/fetch_settings/<botname>/<access_key>

## 
This is the companion repository to the Poe server bot
[quick start](https://developer.poe.com/server-bots/quick-start). Please follow that
guide for instructions on how to use this repository.
