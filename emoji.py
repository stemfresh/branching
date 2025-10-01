# Create a Python script with handy emoji utilities and a small CLI.
path = "/mnt/data/emoji_tool.py"
code = r'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
emoji_tool.py — tiny emoji helper + CLI (no external deps)
Usage examples:
  python emoji_tool.py list
  python emoji_tool.py search smile
  python emoji_tool.py random --count 5
  python emoji_tool.py say "Good morning :sunrise: :coffee:"
  python emoji_tool.py spinner --text "Working"
"""

from __future__ import annotations
import argparse
import random
import re
import sys
import time
from dataclasses import dataclass
from typing import List

# Minimal curated emoji set (expand as you like)
@dataclass(frozen=True)
class Emoji:
    name: str          # short name
    char: str          # emoji character
    tags: List[str]    # keywords for search

EMOJIS: List[Emoji] = [
    Emoji("grinning", "😀", ["smile","happy","face"]),
    Emoji("smile", "😄", ["smile","happy","face","grin"]),
    Emoji("wink", "😉", ["smile","wink","playful"]),
    Emoji("laughing", "😂", ["joy","tear","lol"]),
    Emoji("rofl", "🤣", ["lol","rolling","floor","laugh"]),
    Emoji("slight_smile", "🙂", ["smile","soft"]),
    Emoji("upside_down", "🙃", ["sarcasm","flip"]),
    Emoji("thinking", "🤔", ["hmm","question","consider"]),
    Emoji("sunglasses", "😎", ["cool","sun","shades"]),
    Emoji("heart_eyes", "😍", ["love","heart","eyes"]),
    Emoji("kiss", "😘", ["kiss","love"]),
    Emoji("blush", "😊", ["shy","smile"]),
    Emoji("neutral", "😐", ["meh","straight"]),
    Emoji("sleeping", "😴", ["sleep","zzz","tired"]),
    Emoji("cry", "😢", ["sad","tear"]),
    Emoji("sob", "😭", ["sad","loud","cry"]),
    Emoji("angry", "😠", ["mad","annoyed"]),
    Emoji("mind_blown", "🤯", ["shock","explode","wow"]),
    Emoji("party", "🥳", ["celebrate","birthday","tada"]),
    Emoji("clap", "👏", ["applause","praise"]),
    Emoji("thumbs_up", "👍", ["like","approve","ok"]),
    Emoji("thumbs_down", "👎", ["dislike","nope"]),
    Emoji("ok_hand", "👌", ["perfect","agree"]),
    Emoji("pray", "🙏", ["thanks","please","highfive?"]),
    Emoji("muscle", "💪", ["strong","gym","flex"]),
    Emoji("fire", "🔥", ["lit","hot","flame"]),
    Emoji("sparkles", "✨", ["shine","stars","new"]),
    Emoji("star", "⭐", ["favorite","rate"]),
    Emoji("boom", "💥", ["collision","impact","boom"]),
    Emoji("tada", "🎉", ["party","celebrate","confetti"]),
    Emoji("check", "✅", ["done","complete"]),
    Emoji("x", "❌", ["no","fail","error"]),
    Emoji("warning", "⚠️", ["alert","caution"]),
    Emoji("lightbulb", "💡", ["idea","invent"]),
    Emoji("rocket", "🚀", ["ship","launch","startup"]),
    Emoji("hourglass", "⏳", ["wait","time"]),
    Emoji("calendar", "📅", ["date","schedule"]),
    Emoji("pin", "📌", ["pushpin","note"]),
    Emoji("memo", "📝", ["note","write"]),
    Emoji("coffee", "☕", ["drink","break","cafe"]),
    Emoji("tea", "🍵", ["drink","green","cup"]),
    Emoji("cookie", "🍪", ["snack","sweet"]),
    Emoji("pizza", "🍕", ["food","slice","cheese"]),
    Emoji("burger", "🍔", ["food","sandwich"]),
    Emoji("sushi", "🍣", ["food","fish"]),
    Emoji("bento", "🍱", ["food","box"]),
    Emoji("sunrise", "🌅", ["morning","dawn"]),
    Emoji("sun", "☀️", ["day","weather","clear"]),
    Emoji("moon", "🌙", ["night","sleep"]),
    Emoji("cloud", "☁️", ["weather"]),
    Emoji("rain", "🌧️", ["weather","drizzle"]),
    Emoji("snow", "❄️", ["cold","winter"]),
    Emoji("zap", "⚡", ["electric","fast"]),
    Emoji("wave", "👋", ["hello","bye","greet"]),
    Emoji("eyes", "👀", ["look","watch"]),
    Emoji("brain", "🧠", ["smart","think"]),
    Emoji("toolbox", "🧰", ["tools","kit"]),
    Emoji("computer", "💻", ["laptop
