import re

with open('e:/Downloads/saloon/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Marquee CSS
old_marquee_css = '''    .marquee-strip {
      width: 100vw;
      margin-left: calc(-50vw + 50%);
      background: rgba(158, 42, 75, 0.4);
      padding: 16px 0;
      overflow: hidden;
      white-space: nowrap;
      display: flex;
      border-top: 1px solid rgba(197, 160, 89, 0.2);
      border-bottom: 1px solid rgba(197, 160, 89, 0.2);
      margin-top: 40px;
    }'''
new_marquee_css = '''    .marquee-strip {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      background: rgba(158, 42, 75, 0.85);
      backdrop-filter: blur(8px);
      padding: 14px 0;
      overflow: hidden;
      white-space: nowrap;
      display: flex;
      border-top: 1px solid rgba(197, 160, 89, 0.3);
      border-bottom: 1px solid rgba(197, 160, 89, 0.3);
      z-index: 10;
    }'''
html = html.replace(old_marquee_css, new_marquee_css)

# Remove the marquee HTML from wherever it is
marquee_pattern = re.compile(r'\n?\s*<div class="marquee-strip">.*?</div>\s*</div>\s*', re.DOTALL)
match = marquee_pattern.search(html)
if match:
    marquee_html = match.group(0).strip()
    html = html.replace(match.group(0), '\n')

    # Now, find the hero section's closing tag.
    html = html.replace('</section>\n<!-- ══════════════════════════════════════════════════════════\n     BESPOKE SERVICES', '  ' + marquee_html + '\n</section>\n<!-- ══════════════════════════════════════════════════════════\n     BESPOKE SERVICES')

# 2. Fix Gallery Image Cropping on Mobile
html = html.replace('''      .gallery-grid {
        grid-template-columns: 1fr 1fr;
        grid-template-rows: repeat(3, 170px);
        gap: 10px;
      }''', '''      .gallery-grid {
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 250px 170px 170px;
        gap: 10px;
      }''')

# Add object-position to images
html = html.replace('</style>', '''
    .g-item:nth-child(1) img {
      object-position: top center !important;
    }
    .svc-img-hero img {
      object-position: top center !important;
    }
  </style>''')

# 3. Fix Service Card Image height on Mobile
html = html.replace('''      .svc-img-hero {
        height: 200px;
      }''', '''      .svc-img-hero {
        height: 260px;
      }''')

with open('e:/Downloads/saloon/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed marquee position and image cropping.")
