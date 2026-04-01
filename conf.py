project = 'MIPPIA API'
copyright = '2025, MIPPIA'
author = 'MIPPIA'
release = '1.1.2'

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
    'sphinxext.opengraph',
    'sphinx_sitemap',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'docs-v1.0', 'docs-v1.1', 'robots.txt']

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']
html_extra_path = ['robots.txt']

html_favicon = '_static/favicon.ico'
html_baseurl = 'https://docs.mippia.com/'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
]

sitemap_url_scheme = '{link}'

ogp_site_url = 'https://docs.mippia.com/'
ogp_site_name = 'MIPPIA API Documentation'
ogp_image = 'https://docs.mippia.com/_static/og-image.png'
ogp_description_length = 200
ogp_type = 'website'

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#2563eb",
        "color-brand-content": "#2563eb",
    },
    "dark_css_variables": {
        "color-brand-primary": "#60a5fa",
        "color-brand-content": "#60a5fa",
    },
    "navigation_with_keys": True,
    "announcement": """
        <div class="version-switcher">
            Version: <select onchange="window.location.href=this.value">
                <option value="/" selected>1.1.2 (Latest)</option>
                <option value="/v1.1/">1.1</option>
                <option value="/v1.0/">1.0</option>
            </select>
        </div>
    """,
}
