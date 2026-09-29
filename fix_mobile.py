import re

with open('e:/Downloads/saloon/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Marquee Strip CSS
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
      background: rgba(158, 42, 75, 0.85); /* Slightly less transparent */
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

# Move marquee-strip from inside hero-stats to be a direct child of hero section (at the end)
# Find the marquee-strip HTML block
marquee_match = re.search(r'(<div class="marquee-strip">.*?</div>\s*</div>)', html, flags=re.DOTALL)
if marquee_match:
    marquee_html = marquee_match.group(1)
    # Actually the regex matched the closing </div> of marquee-content and marquee-strip.
    pass

# A safer way: just extract the block and place it before </section> of hero
marquee_match2 = re.search(r'(<div class="marquee-strip">.*?</div>\s*</div>)', html, flags=re.DOTALL)
if marquee_match2:
    marquee_html = marquee_match2.group(1)
    # Remove it from current location
    html = html.replace(marquee_html, '')
    # Insert before </section> which is the end of the hero section
    html = html.replace('</section>\n<!-- ══════════════════════════════════════════════════════════\n     BESPOKE SERVICES HORIZONTAL SLIDER', marquee_html + '\n</section>\n<!-- ══════════════════════════════════════════════════════════\n     BESPOKE SERVICES HORIZONTAL SLIDER')


# 2. Fix Gallery Image Cropping on Mobile
# In the 600px media query, the grid rows are repeat(3, 170px)
html = html.replace('''      .gallery-grid {
        grid-template-columns: 1fr 1fr;
        grid-template-rows: repeat(3, 170px);
        gap: 10px;
      }''', '''      .gallery-grid {
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 250px 170px 170px;
        gap: 10px;
      }''')

# Add top center object-position to the first gallery item
# Wait, let's just add it globally for all images
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
print("Changes applied!")
