#!/usr/bin/env python3
import os
from generate_css import get_css
from generate_html import get_html
from generate_js import get_js

html_content = f"""<!DOCTYPE html>
<html lang="tr" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ScriptDepo - Roblox Script & Oyun Platformu</title>
  <meta name="description" content="Roblox oyuncularının script paylaştığı, coin kazandığı ve oyun keşfettiği modern platform." />
  <meta property="og:title" content="ScriptDepo - Roblox Script & Oyun Platformu" />
  <meta property="og:description" content="Roblox oyuncularının script paylaştığı, coin kazandığı ve oyun keşfettiği modern platform." />
  <meta property="og:image" content="https://i.postimg.cc/vT1sHWqq/Gemini-Generated-Image-xefq68xefq68xefq.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="https://i.postimg.cc/vT1sHWqq/Gemini-Generated-Image-xefq68xefq68xefq.png" />
  <link rel="icon" type="image/png" href="https://i.postimg.cc/vT1sHWqq/Gemini-Generated-Image-xefq68xefq68xefq.png" />
  <link rel="apple-touch-icon" href="https://i.postimg.cc/vT1sHWqq/Gemini-Generated-Image-xefq68xefq68xefq.png" />
  <meta property="og:type" content="website" />
  <meta name="theme-color" content="#7c3aed" />
  <link rel="manifest" href="/manifest.json" />

  <!-- Google Fonts: Plus Jakarta Sans & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Font Awesome Icons (Emoji yasak kuralına uygun) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />

  <!-- Firebase 10.7.1 Compat SDKs -->
  <script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-auth-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-storage-compat.js"></script>

  <style>
{get_css()}
  </style>
</head>
<body>
{get_html()}

  <script>
{get_js()}
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated /index.html! Total size: {len(html_content)} bytes")
