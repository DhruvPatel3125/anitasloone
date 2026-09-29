import re

with open('e:/Downloads/saloon/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Marquee CSS before </style>
marquee_css = '''
    /* Marquee Strip */
    .marquee-strip {
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
    }
    .marquee-content {
      display: flex;
      align-items: center;
      animation: scrollMarquee 25s linear infinite;
    }
    .marquee-item {
      font-family: "Playfair Display", serif;
      font-size: 1.4rem;
      font-style: italic;
      color: var(--text-main);
      padding: 0 30px;
    }
    .marquee-sep {
      color: var(--gold);
      font-size: 0.8rem;
    }
    @keyframes scrollMarquee {
      0% { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }
'''
html = html.replace('</style>', marquee_css + '\n  </style>')

# 2. Add Marquee HTML after <div class="hero-stats">...</div>
marquee_html = '''
        <div class="marquee-strip">
          <div class="marquee-content">
            <span class="marquee-item">Bridal Makeup</span><span class="marquee-sep">◆</span>
            <span class="marquee-item">Korean Facials</span><span class="marquee-sep">◆</span>
            <span class="marquee-item">Nanoplastia</span><span class="marquee-sep">◆</span>
            <span class="marquee-item">Gel Extensions</span><span class="marquee-sep">◆</span>
            <span class="marquee-item">Shirodhara</span><span class="marquee-sep">◆</span>
            <span class="marquee-item">Potli Pedicure</span><span class="marquee-sep">◆</span>
            <span class="marquee-item">Bridal Makeup</span><span class="marquee-sep">◆</span>
            <span class="marquee-item">Korean Facials</span><span class="marquee-sep">◆</span>
            <span class="marquee-item">Nanoplastia</span><span class="marquee-sep">◆</span>
            <span class="marquee-item">Gel Extensions</span><span class="marquee-sep">◆</span>
            <span class="marquee-item">Shirodhara</span><span class="marquee-sep">◆</span>
            <span class="marquee-item">Potli Pedicure</span>
          </div>
        </div>
'''
html = re.sub(r'(<div class="hero-stats">.*?</div>)', r'\1' + marquee_html, html, flags=re.DOTALL)

# 3. Fix list item bullets
html = html.replace("content: '—';", "content: '•';")
html = html.replace("color: var(--rose-bright);", "color: var(--gold);")

# 4. Remove svc-tags
html = re.sub(r'<div class="svc-tags">.*?</div>', '', html, flags=re.DOTALL)

# 5. Fix svc-num formatting (e.g. "01 · BRIDAL ARTISTRY" -> "01")
html = re.sub(r'<span class="svc-num">(0\d+) .*?</span>', r'<span class="svc-num">\1</span>', html)

# 6. Make svc-num font larger to match screenshot
css_svc_num_old = '''    .svc-num {
      font-family: "Playfair Display", serif;
      font-size: .84rem;
      letter-spacing: .22em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 10px;
      display: block;
      font-weight: 500;
    }'''
css_svc_num_new = '''    .svc-num {
      font-family: "Playfair Display", serif;
      font-size: 1.2rem;
      letter-spacing: .1em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 10px;
      display: block;
      font-weight: 600;
    }'''
html = html.replace(css_svc_num_old, css_svc_num_new)

# Write back
with open('e:/Downloads/saloon/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Modifications applied.")
