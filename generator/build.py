import os
import json

CATEGORIES = ["Developer", "Text", "Math", "Media", "Misc"]

TOOLS = [
    # --- Developer ---
    {"id": "base64-encode-decode", "title": "Base64 Encode/Decode", "category": "Developer", "desc": "Encode and decode text to/from Base64.", "icon": "🔤"},
    {"id": "url-encode-decode", "title": "URL Encode/Decode", "category": "Developer", "desc": "Encode and decode URLs safely.", "icon": "🔗"},
    {"id": "html-encode-decode", "title": "HTML Entity Encode/Decode", "category": "Developer", "desc": "Encode and decode HTML entities.", "icon": "🌐"},
    {"id": "json-formatter", "title": "JSON Formatter", "category": "Developer", "desc": "Format and validate JSON data.", "icon": "📋"},
    {"id": "json-minifier", "title": "JSON Minifier", "category": "Developer", "desc": "Minify JSON data.", "icon": "📦"},
    {"id": "uuid-generator", "title": "UUID/GUID Generator", "category": "Developer", "desc": "Generate v4 UUIDs/GUIDs.", "icon": "🆔"},
    {"id": "lorem-ipsum", "title": "Lorem Ipsum Generator", "category": "Developer", "desc": "Generate dummy text for designs.", "icon": "📝"},
    {"id": "hash-generator", "title": "Hash Generator", "category": "Developer", "desc": "Generate MD5, SHA-1, SHA-256 hashes.", "icon": "🔐"},
    {"id": "unix-timestamp", "title": "Unix Timestamp Converter", "category": "Developer", "desc": "Convert Unix timestamps to dates and vice versa.", "icon": "⏳"},
    {"id": "color-converter", "title": "Color Converter", "category": "Developer", "desc": "Convert colors between HEX, RGB, and HSL.", "icon": "🎨"},
    {"id": "jwt-decoder", "title": "JWT Decoder", "category": "Developer", "desc": "Decode JSON Web Tokens.", "icon": "🔑"},
    {"id": "markdown-previewer", "title": "Markdown Previewer", "category": "Developer", "desc": "Preview Markdown text in real-time.", "icon": "⬇️"},
    {"id": "csv-to-json", "title": "CSV to JSON", "category": "Developer", "desc": "Convert CSV data to JSON.", "icon": "🔄"},
    {"id": "json-to-csv", "title": "JSON to CSV", "category": "Developer", "desc": "Convert JSON data to CSV.", "icon": "🔄"},
    {"id": "sql-formatter", "title": "SQL Formatter", "category": "Developer", "desc": "Format SQL queries.", "icon": "🗄️"},
    {"id": "regex-tester", "title": "Regex Tester", "category": "Developer", "desc": "Test regular expressions.", "icon": "🔍"},

    # --- Text ---
    {"id": "word-counter", "title": "Word & Character Counter", "category": "Text", "desc": "Count words, characters, and lines.", "icon": "📊"},
    {"id": "case-converter", "title": "Case Converter", "category": "Text", "desc": "Convert text to uppercase, lowercase, title case, etc.", "icon": "Aa"},
    {"id": "text-reverser", "title": "Text Reverser", "category": "Text", "desc": "Reverse strings or lines.", "icon": "🔃"},
    {"id": "remove-duplicates", "title": "Remove Duplicate Lines", "category": "Text", "desc": "Remove duplicate lines from text.", "icon": "✂️"},
    {"id": "sort-lines", "title": "Sort Lines", "category": "Text", "desc": "Sort text lines alphabetically or by length.", "icon": "🔢"},
    {"id": "text-to-binary", "title": "Text to Binary", "category": "Text", "desc": "Convert text to binary.", "icon": "01"},
    {"id": "binary-to-text", "title": "Binary to Text", "category": "Text", "desc": "Convert binary to text.", "icon": "10"},
    {"id": "find-replace", "title": "Find & Replace", "category": "Text", "desc": "Find and replace text using strings or regex.", "icon": "🔎"},
    {"id": "whitespace-remover", "title": "Whitespace Remover", "category": "Text", "desc": "Remove extra whitespaces from text.", "icon": "🧹"},
    {"id": "password-generator", "title": "Password Generator", "category": "Text", "desc": "Generate strong random passwords.", "icon": "🛡️"},
    {"id": "prefix-suffix-adder", "title": "Prefix/Suffix Adder", "category": "Text", "desc": "Add prefix/suffix to each line.", "icon": "➕"},
    {"id": "comma-separator", "title": "Comma Separator", "category": "Text", "desc": "Convert column of items to comma-separated list.", "icon": "📑"},

    # --- Math ---
    {"id": "unit-converter", "title": "Unit Converter", "category": "Math", "desc": "Convert length, weight, and temperature.", "icon": "📏"},
    {"id": "base-converter", "title": "Number Base Converter", "category": "Math", "desc": "Convert numbers between hex, dec, oct, bin.", "icon": "🧮"},
    {"id": "percentage-calculator", "title": "Percentage Calculator", "category": "Math", "desc": "Calculate percentages.", "icon": "%"},
    {"id": "bmi-calculator", "title": "BMI Calculator", "category": "Math", "desc": "Calculate Body Mass Index.", "icon": "⚖️"},
    {"id": "roman-numerals", "title": "Roman Numeral Converter", "category": "Math", "desc": "Convert numbers to/from Roman numerals.", "icon": "🏛️"},
    {"id": "prime-checker", "title": "Prime Number Checker", "category": "Math", "desc": "Check if a number is prime.", "icon": "✨"},
    {"id": "color-contrast", "title": "Color Contrast Checker", "category": "Math", "desc": "Check contrast ratio between two colors.", "icon": "🌗"},
    {"id": "gcd-lcm", "title": "GCD/LCM Calculator", "category": "Math", "desc": "Find Greatest Common Divisor and Least Common Multiple.", "icon": "➗"},
    {"id": "random-number", "title": "Random Number Generator", "category": "Math", "desc": "Generate random numbers in a range.", "icon": "🎲"},

    # --- Media ---
    {"id": "image-converter", "title": "Image Converter", "category": "Media", "desc": "Convert images to PNG, JPG, WebP.", "icon": "🖼️", "custom": True},
    {"id": "image-cropper", "title": "Image Cropper", "category": "Media", "desc": "Crop and resize images.", "icon": "✂️", "custom": True},
    {"id": "image-markup", "title": "Image Markup", "category": "Media", "desc": "Draw and add text to images.", "icon": "🖍️", "custom": True},
    {"id": "video-extractor", "title": "Video Frame Extractor", "category": "Media", "desc": "Extract frames/snapshots from video files.", "icon": "🎞️"},
    {"id": "pdf-info", "title": "PDF Metadata Viewer", "category": "Media", "desc": "Inspect PDF files metadata securely.", "icon": "📄"},
    {"id": "qr-generator", "title": "QR Code Generator", "category": "Media", "desc": "Generate QR codes from text/URLs.", "icon": "📱"},
    {"id": "image-to-base64", "title": "Image to Base64", "category": "Media", "desc": "Convert image files to Base64 strings.", "icon": "🔄"},
    {"id": "base64-to-image", "title": "Base64 to Image", "category": "Media", "desc": "Convert Base64 strings to images.", "icon": "🖼️"},
    {"id": "svg-optimizer", "title": "SVG Optimizer", "category": "Media", "desc": "Minify SVG code.", "icon": "📉"},
    {"id": "color-extractor", "title": "Color Extractor", "category": "Media", "desc": "Extract colors from images.", "icon": "🎨"},

    # --- Misc ---
    {"id": "ip-info", "title": "IP Address Info", "category": "Misc", "desc": "Get your current IP address and info.", "icon": "🌐"},
    {"id": "key-event", "title": "Keyboard Event Info", "category": "Misc", "desc": "Get JavaScript event keycodes.", "icon": "⌨️"},
    {"id": "system-info", "title": "System Information", "category": "Misc", "desc": "View browser and OS information.", "icon": "💻"},
    {"id": "meta-tags", "title": "Meta Tag Generator", "category": "Misc", "desc": "Generate HTML meta tags for SEO.", "icon": "🏷️"},
    {"id": "stopwatch", "title": "Stopwatch", "category": "Misc", "desc": "Simple online stopwatch.", "icon": "⏱️"}
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - BrowserTools</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    {extra_head}
</head>
<body>
    <aside class="sidebar" id="sidebar">
        <a href="../index.html" class="sidebar-header">
            🛠️ BrowserTools
        </a>
        <div class="sidebar-content">
            {sidebar_links}
        </div>
    </aside>

    <div class="main-content">
        <header class="topbar">
            <div class="topbar-left">
                <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>
                </button>
                <h1 style="font-size: 1.2rem; font-weight: 600;">{title}</h1>
            </div>
            <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Theme">
            </button>
        </header>

        <main class="content-wrapper">
            <div class="card">
                <p class="text-muted mb-4">{desc}</p>
                {tool_ui}
            </div>
        </main>
    </div>

    <script src="../assets/js/main.js"></script>
    <script>
        {tool_js}
    </script>
</body>
</html>
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BrowserTools - 50+ Web Utilities</title>
    <link rel="stylesheet" href="./assets/css/style.css">
</head>
<body>
    <aside class="sidebar" id="sidebar">
        <a href="./index.html" class="sidebar-header">
            🛠️ BrowserTools
        </a>
        <div class="sidebar-content">
            {sidebar_links}
        </div>
    </aside>

    <div class="main-content">
        <header class="topbar">
            <div class="topbar-left">
                <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>
                </button>
                <h1 style="font-size: 1.2rem; font-weight: 600;">All Tools</h1>
            </div>
            <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Theme">
            </button>
        </header>

        <main class="content-wrapper">
            <p style="margin-bottom: 2rem; color: var(--text-muted);">
                A collection of 50+ tools running entirely in your browser. Fast, private, and secure.
            </p>
            {tool_grids}
        </main>
    </div>

    <script src="./assets/js/main.js"></script>
</body>
</html>
"""

def generate_sidebar_links(is_index=False):
    html = ""
    prefix = "./" if is_index else "../"
    for cat in CATEGORIES:
        html += f'<div class="sidebar-nav-group"><div class="sidebar-nav-title">{cat}</div>'
        for t in TOOLS:
            if t["category"] == cat:
                html += f'<a href="{prefix}{t["id"]}/index.html" class="sidebar-link">{t["icon"]} {t["title"]}</a>'
        html += '</div>'
    return html

def build_index():
    sidebar = generate_sidebar_links(is_index=True)
    grids = ""
    for cat in CATEGORIES:
        grids += f'<h2 style="margin-bottom: 1rem; margin-top: 2rem; font-size: 1.2rem; font-weight: 600; color: var(--text-main);">{cat}</h2>'
        grids += '<div class="tool-grid">'
        for t in TOOLS:
            if t["category"] == cat:
                grids += f'''
                <a href="./{t["id"]}/index.html" class="tool-card">
                    <div class="tool-icon">{t["icon"]}</div>
                    <div class="tool-title">{t["title"]}</div>
                    <div class="tool-desc">{t["desc"]}</div>
                </a>
                '''
        grids += '</div>'

    with open("index.html", "w") as f:
        f.write(INDEX_TEMPLATE.format(sidebar_links=sidebar, tool_grids=grids))


import sys
import shutil

# To handle complex UI logic for each tool, I'll define templates directly here:

def get_tool_logic(tool_id):
    extra_head = ""
    ui = ""
    js = ""

    if tool_id == "base64-encode-decode":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Enter text..."></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnEncode">Encode</button>
            <button class="btn btn-secondary" id="btnDecode">Decode</button>
        </div>
        <textarea id="output" class="input-control" placeholder="Result..." readonly></textarea>
        <button class="btn btn-secondary mt-2" onclick="copyToClipboard(document.getElementById('output').value, this)">Copy Result</button>
        '''
        js = '''
        document.getElementById('btnEncode').onclick = () => {
            try { document.getElementById('output').value = btoa(unescape(encodeURIComponent(document.getElementById('input').value))); }
            catch(e) { alert("Encoding failed"); }
        };
        document.getElementById('btnDecode').onclick = () => {
            try { document.getElementById('output').value = decodeURIComponent(escape(atob(document.getElementById('input').value))); }
            catch(e) { alert("Invalid Base64"); }
        };
        '''
    elif tool_id == "url-encode-decode":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Enter URL or text..."></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnEncode">Encode</button>
            <button class="btn btn-secondary" id="btnDecode">Decode</button>
        </div>
        <textarea id="output" class="input-control" placeholder="Result..." readonly></textarea>
        '''
        js = '''
        document.getElementById('btnEncode').onclick = () => { document.getElementById('output').value = encodeURIComponent(document.getElementById('input').value); };
        document.getElementById('btnDecode').onclick = () => {
            try { document.getElementById('output').value = decodeURIComponent(document.getElementById('input').value); }
            catch(e) { alert("Invalid encoding"); }
        };
        '''
    elif tool_id == "html-encode-decode":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Enter text..."></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnEncode">Encode HTML</button>
            <button class="btn btn-secondary" id="btnDecode">Decode HTML</button>
        </div>
        <textarea id="output" class="input-control" placeholder="Result..." readonly></textarea>
        '''
        js = '''
        document.getElementById('btnEncode').onclick = () => {
            const div = document.createElement('div');
            div.innerText = document.getElementById('input').value;
            document.getElementById('output').value = div.innerHTML;
        };
        document.getElementById('btnDecode').onclick = () => {
            const div = document.createElement('div');
            div.innerHTML = document.getElementById('input').value;
            document.getElementById('output').value = div.innerText;
        };
        '''
    elif tool_id == "json-formatter":
        ui = '''
        <textarea id="input" class="input-control" placeholder='{"hello": "world"}'></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnFormat">Format JSON</button>
        </div>
        <textarea id="output" class="input-control" style="min-height: 300px; font-family: monospace;" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnFormat').onclick = () => {
            try {
                const obj = JSON.parse(document.getElementById('input').value);
                document.getElementById('output').value = JSON.stringify(obj, null, 4);
            } catch(e) { document.getElementById('output').value = "Invalid JSON: " + e.message; }
        };
        '''
    elif tool_id == "json-minifier":
        ui = '''
        <textarea id="input" class="input-control" placeholder='{"hello": "world"}'></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnMinify">Minify JSON</button>
        </div>
        <textarea id="output" class="input-control" style="font-family: monospace;" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnMinify').onclick = () => {
            try {
                const obj = JSON.parse(document.getElementById('input').value);
                document.getElementById('output').value = JSON.stringify(obj);
            } catch(e) { document.getElementById('output').value = "Invalid JSON: " + e.message; }
        };
        '''
    elif tool_id == "uuid-generator":
        ui = '''
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnGen">Generate New UUID v4</button>
        </div>
        <textarea id="output" class="input-control" style="font-family: monospace; font-size: 1.2rem;" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnGen').onclick = () => {
            document.getElementById('output').value = crypto.randomUUID();
        };
        // Auto gen on load
        document.getElementById('btnGen').click();
        '''
    elif tool_id == "lorem-ipsum":
        ui = '''
        <div class="flex gap-2 my-2 items-center">
            <label>Paragraphs:</label>
            <input type="number" id="paras" class="input-control" style="width: 80px;" value="3" min="1" max="20">
            <button class="btn btn-primary" id="btnGen">Generate</button>
        </div>
        <textarea id="output" class="input-control" style="min-height: 300px;" readonly></textarea>
        '''
        js = '''
        const words = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua"];
        document.getElementById('btnGen').onclick = () => {
            let pCount = parseInt(document.getElementById('paras').value) || 3;
            let res = [];
            for(let p=0; p<pCount; p++) {
                let sent = [];
                for(let s=0; s<5; s++) {
                    let w = [];
                    for(let i=0; i<8; i++) w.push(words[Math.floor(Math.random()*words.length)]);
                    w[0] = w[0].charAt(0).toUpperCase() + w[0].slice(1);
                    sent.push(w.join(" ") + ".");
                }
                res.push(sent.join(" "));
            }
            document.getElementById('output').value = res.join("\\n\\n");
        };
        document.getElementById('btnGen').click();
        '''
    elif tool_id == "hash-generator":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Enter text to hash..."></textarea>
        <div class="flex gap-2 my-2 items-center">
            <select id="algo" class="input-control" style="width: auto;">
                <option value="SHA-1">SHA-1</option>
                <option value="SHA-256">SHA-256</option>
                <option value="SHA-384">SHA-384</option>
                <option value="SHA-512">SHA-512</option>
            </select>
            <button class="btn btn-primary" id="btnGen">Generate Hash</button>
        </div>
        <textarea id="output" class="input-control" style="font-family: monospace;" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnGen').onclick = async () => {
            const text = document.getElementById('input').value;
            const algo = document.getElementById('algo').value;
            if(!text) return;
            const msgBuffer = new TextEncoder().encode(text);
            const hashBuffer = await crypto.subtle.digest(algo, msgBuffer);
            const hashArray = Array.from(new Uint8Array(hashBuffer));
            const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
            document.getElementById('output').value = hashHex;
        };
        '''
    elif tool_id == "unix-timestamp":
        ui = '''
        <div class="flex flex-col gap-4">
            <div>
                <label class="input-label">Current Timestamp</label>
                <div class="flex gap-2">
                    <input type="text" id="currentTs" class="input-control" readonly>
                </div>
            </div>
            <div>
                <label class="input-label">Convert Timestamp to Date</label>
                <div class="flex gap-2">
                    <input type="number" id="tsInput" class="input-control" placeholder="e.g. 1609459200">
                    <button class="btn btn-primary" id="btnToDate">Convert</button>
                </div>
                <input type="text" id="dateOutput" class="input-control mt-2" readonly>
            </div>
        </div>
        '''
        js = '''
        setInterval(() => {
            document.getElementById('currentTs').value = Math.floor(Date.now() / 1000);
        }, 1000);
        document.getElementById('btnToDate').onclick = () => {
            const val = document.getElementById('tsInput').value;
            if(!val) return;
            const d = new Date(val * (val.length > 10 ? 1 : 1000));
            document.getElementById('dateOutput').value = d.toLocaleString();
        };
        '''
    elif tool_id == "color-converter":
        ui = '''
        <div class="flex flex-col gap-4">
            <div>
                <label class="input-label">Pick a Color</label>
                <input type="color" id="colorPicker" value="#6366f1" style="width: 100px; height: 50px; cursor: pointer;">
            </div>
            <div>
                <label class="input-label">HEX</label>
                <input type="text" id="hexOut" class="input-control" readonly>
            </div>
            <div>
                <label class="input-label">RGB</label>
                <input type="text" id="rgbOut" class="input-control" readonly>
            </div>
        </div>
        '''
        js = '''
        const hexToRgb = (hex) => {
            const r = parseInt(hex.slice(1, 3), 16), g = parseInt(hex.slice(3, 5), 16), b = parseInt(hex.slice(5, 7), 16);
            return `rgb(${r}, ${g}, ${b})`;
        };
        const update = () => {
            const val = document.getElementById('colorPicker').value;
            document.getElementById('hexOut').value = val.toUpperCase();
            document.getElementById('rgbOut').value = hexToRgb(val);
        };
        document.getElementById('colorPicker').oninput = update;
        update();
        '''
    elif tool_id == "jwt-decoder":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Paste JWT here..."></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnDecode">Decode JWT</button>
        </div>
        <label class="input-label">Header</label>
        <textarea id="outHeader" class="input-control mb-2" style="font-family: monospace;" readonly></textarea>
        <label class="input-label">Payload</label>
        <textarea id="outPayload" class="input-control" style="font-family: monospace; min-height: 150px;" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnDecode').onclick = () => {
            try {
                const token = document.getElementById('input').value.split('.');
                if(token.length !== 3) throw new Error("Invalid JWT format.");
                const header = JSON.parse(atob(token[0].replace(/-/g, '+').replace(/_/g, '/')));
                const payload = JSON.parse(atob(token[1].replace(/-/g, '+').replace(/_/g, '/')));
                document.getElementById('outHeader').value = JSON.stringify(header, null, 2);
                document.getElementById('outPayload').value = JSON.stringify(payload, null, 2);
            } catch(e) { alert("Error decoding JWT: " + e.message); }
        };
        '''
    elif tool_id == "markdown-previewer":
        extra_head = '<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>'
        ui = '''
        <div class="flex flex-col md:flex-row gap-4 h-[60vh]">
            <textarea id="input" class="input-control w-full h-full" placeholder="# Hello\\nWrite markdown here..."></textarea>
            <div id="preview" class="w-full h-full border border-[var(--border-color)] rounded-md p-4 overflow-y-auto bg-[var(--bg-surface)]"></div>
        </div>
        '''
        js = '''
        const input = document.getElementById('input');
        const preview = document.getElementById('preview');
        const update = () => { preview.innerHTML = marked.parse(input.value); };
        input.addEventListener('input', update);
        input.value = "# Hello World\\n\\nStart typing **markdown** here.";
        update();
        '''
    elif tool_id == "csv-to-json":
        ui = '''
        <textarea id="input" class="input-control" placeholder="id,name\\n1,John\\n2,Jane"></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnConvert">Convert to JSON</button>
        </div>
        <textarea id="output" class="input-control" style="min-height: 200px; font-family: monospace;" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnConvert').onclick = () => {
            const lines = document.getElementById('input').value.trim().split('\\n');
            if(lines.length < 2) return;
            const headers = lines[0].split(',');
            const result = [];
            for(let i=1; i<lines.length; i++) {
                const obj = {};
                const currentline = lines[i].split(',');
                for(let j=0; j<headers.length; j++){
                    obj[headers[j]] = currentline[j];
                }
                result.push(obj);
            }
            document.getElementById('output').value = JSON.stringify(result, null, 2);
        };
        '''
    elif tool_id == "json-to-csv":
        ui = '''
        <textarea id="input" class="input-control" placeholder='[{"id":"1", "name":"John"}]'></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnConvert">Convert to CSV</button>
        </div>
        <textarea id="output" class="input-control" style="min-height: 200px; font-family: monospace;" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnConvert').onclick = () => {
            try {
                const arr = JSON.parse(document.getElementById('input').value);
                if(!arr.length) return;
                const headers = Object.keys(arr[0]);
                const replacer = (key, value) => value === null ? '' : value;
                const csv = arr.map(row => headers.map(fieldName => JSON.stringify(row[fieldName], replacer)).join(','));
                csv.unshift(headers.join(','));
                document.getElementById('output').value = csv.join('\\r\\n');
            } catch(e) { document.getElementById('output').value = "Invalid JSON Array"; }
        };
        '''
    elif tool_id == "sql-formatter":
        ui = '''
        <textarea id="input" class="input-control" placeholder="SELECT * FROM table WHERE id=1;"></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnFormat">Uppercase Keywords (Basic)</button>
        </div>
        <textarea id="output" class="input-control" style="min-height: 200px; font-family: monospace;" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnFormat').onclick = () => {
            let sql = document.getElementById('input').value;
            const keywords = ['SELECT', 'FROM', 'WHERE', 'AND', 'OR', 'INSERT', 'INTO', 'VALUES', 'UPDATE', 'SET', 'DELETE', 'ORDER BY', 'GROUP BY', 'JOIN', 'LEFT', 'RIGHT', 'INNER', 'ON'];
            keywords.forEach(kw => {
                const reg = new RegExp(`\\\\b${kw}\\\\b`, 'gi');
                sql = sql.replace(reg, kw);
            });
            document.getElementById('output').value = sql;
        };
        '''
    elif tool_id == "regex-tester":
        ui = '''
        <div class="flex gap-2 mb-2">
            <input type="text" id="regex" class="input-control flex-1" placeholder="^([a-z]+)$">
            <input type="text" id="flags" class="input-control" style="width: 80px;" placeholder="gim" value="g">
        </div>
        <textarea id="input" class="input-control" placeholder="Test string here..."></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnTest">Test Match</button>
        </div>
        <div id="output" class="p-4 border border-[var(--border-color)] rounded-md bg-[var(--bg-surface)] min-h-[100px]"></div>
        '''
        js = '''
        document.getElementById('btnTest').onclick = () => {
            try {
                const re = new RegExp(document.getElementById('regex').value, document.getElementById('flags').value);
                const str = document.getElementById('input').value;
                const matches = str.match(re);
                const out = document.getElementById('output');
                if (matches) {
                    out.innerHTML = `<span style="color:var(--success-color)">Match Found!</span><br/>` + matches.join('<br/>');
                } else {
                    out.innerHTML = `<span style="color:var(--danger-color)">No Match</span>`;
                }
            } catch(e) { document.getElementById('output').innerText = "Invalid Regex: " + e.message; }
        };
        '''
    elif tool_id == "word-counter":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Type or paste text here..."></textarea>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4 text-center">
            <div class="p-4 bg-[var(--bg-surface)] border border-[var(--border-color)] rounded-md">
                <div class="text-2xl font-bold text-[var(--accent-color)]" id="words">0</div>
                <div class="text-sm text-[var(--text-muted)]">Words</div>
            </div>
            <div class="p-4 bg-[var(--bg-surface)] border border-[var(--border-color)] rounded-md">
                <div class="text-2xl font-bold text-[var(--accent-color)]" id="chars">0</div>
                <div class="text-sm text-[var(--text-muted)]">Characters</div>
            </div>
            <div class="p-4 bg-[var(--bg-surface)] border border-[var(--border-color)] rounded-md">
                <div class="text-2xl font-bold text-[var(--accent-color)]" id="charsNoSpaces">0</div>
                <div class="text-sm text-[var(--text-muted)]">Chars (No Spaces)</div>
            </div>
            <div class="p-4 bg-[var(--bg-surface)] border border-[var(--border-color)] rounded-md">
                <div class="text-2xl font-bold text-[var(--accent-color)]" id="lines">0</div>
                <div class="text-sm text-[var(--text-muted)]">Lines</div>
            </div>
        </div>
        '''
        js = '''
        document.getElementById('input').addEventListener('input', (e) => {
            const text = e.target.value;
            document.getElementById('chars').innerText = text.length;
            document.getElementById('charsNoSpaces').innerText = text.replace(/\\s/g, '').length;
            document.getElementById('lines').innerText = text === '' ? 0 : text.split('\\n').length;
            const words = text.trim() === '' ? 0 : text.trim().split(/\\s+/).length;
            document.getElementById('words').innerText = words;
        });
        '''
    elif tool_id == "case-converter":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Enter text..."></textarea>
        <div class="flex flex-wrap gap-2 my-2">
            <button class="btn btn-secondary" onclick="convert('UPPERCASE')">UPPERCASE</button>
            <button class="btn btn-secondary" onclick="convert('lowercase')">lowercase</button>
            <button class="btn btn-secondary" onclick="convert('Title Case')">Title Case</button>
            <button class="btn btn-secondary" onclick="convert('camelCase')">camelCase</button>
            <button class="btn btn-secondary" onclick="convert('snake_case')">snake_case</button>
        </div>
        <textarea id="output" class="input-control" readonly></textarea>
        '''
        js = '''
        window.convert = (type) => {
            const val = document.getElementById('input').value;
            let res = '';
            if(type === 'UPPERCASE') res = val.toUpperCase();
            if(type === 'lowercase') res = val.toLowerCase();
            if(type === 'Title Case') res = val.toLowerCase().split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
            if(type === 'camelCase') res = val.toLowerCase().replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase());
            if(type === 'snake_case') res = val.toLowerCase().replace(/\\s+/g, '_');
            document.getElementById('output').value = res;
        };
        '''
    elif tool_id == "text-reverser":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Enter text..."></textarea>
        <div class="flex flex-wrap gap-2 my-2">
            <button class="btn btn-primary" onclick="reverse('text')">Reverse Entire Text</button>
            <button class="btn btn-secondary" onclick="reverse('words')">Reverse Words</button>
            <button class="btn btn-secondary" onclick="reverse('lines')">Reverse Lines</button>
        </div>
        <textarea id="output" class="input-control" readonly></textarea>
        '''
        js = '''
        window.reverse = (type) => {
            const val = document.getElementById('input').value;
            if(type === 'text') document.getElementById('output').value = val.split('').reverse().join('');
            if(type === 'words') document.getElementById('output').value = val.split(' ').reverse().join(' ');
            if(type === 'lines') document.getElementById('output').value = val.split('\\n').reverse().join('\\n');
        };
        '''
    elif tool_id == "remove-duplicates":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Line 1\\nLine 2\\nLine 1"></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnAction">Remove Duplicate Lines</button>
        </div>
        <textarea id="output" class="input-control" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnAction').onclick = () => {
            const lines = document.getElementById('input').value.split('\\n');
            const unique = [...new Set(lines)];
            document.getElementById('output').value = unique.join('\\n');
        };
        '''
    elif tool_id == "sort-lines":
        ui = '''
        <textarea id="input" class="input-control" placeholder="B\\nC\\nA"></textarea>
        <div class="flex gap-2 my-2 flex-wrap">
            <button class="btn btn-primary" onclick="sort('az')">Sort A-Z</button>
            <button class="btn btn-secondary" onclick="sort('za')">Sort Z-A</button>
            <button class="btn btn-secondary" onclick="sort('len-asc')">By Length (Shortest first)</button>
        </div>
        <textarea id="output" class="input-control" readonly></textarea>
        '''
        js = '''
        window.sort = (type) => {
            const lines = document.getElementById('input').value.split('\\n');
            if(type === 'az') lines.sort();
            if(type === 'za') lines.sort().reverse();
            if(type === 'len-asc') lines.sort((a,b) => a.length - b.length);
            document.getElementById('output').value = lines.join('\\n');
        };
        '''
    elif tool_id == "text-to-binary":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Hello"></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnAction">Convert to Binary</button>
        </div>
        <textarea id="output" class="input-control" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnAction').onclick = () => {
            const val = document.getElementById('input').value;
            document.getElementById('output').value = val.split('').map(char => char.charCodeAt(0).toString(2).padStart(8, '0')).join(' ');
        };
        '''
    elif tool_id == "binary-to-text":
        ui = '''
        <textarea id="input" class="input-control" placeholder="01001000 01100101 01101100 01101100 01101111"></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnAction">Convert to Text</button>
        </div>
        <textarea id="output" class="input-control" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnAction').onclick = () => {
            try {
                const val = document.getElementById('input').value.trim().split(' ');
                document.getElementById('output').value = val.map(bin => String.fromCharCode(parseInt(bin, 2))).join('');
            } catch(e) { document.getElementById('output').value = "Invalid Binary"; }
        };
        '''
    elif tool_id == "find-replace":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Text goes here..."></textarea>
        <div class="flex gap-2 my-2">
            <input type="text" id="find" class="input-control" placeholder="Find">
            <input type="text" id="replace" class="input-control" placeholder="Replace">
            <button class="btn btn-primary" id="btnAction">Replace All</button>
        </div>
        <textarea id="output" class="input-control" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnAction').onclick = () => {
            const text = document.getElementById('input').value;
            const find = document.getElementById('find').value;
            const replace = document.getElementById('replace').value;
            document.getElementById('output').value = text.split(find).join(replace);
        };
        '''
    elif tool_id == "whitespace-remover":
        ui = '''
        <textarea id="input" class="input-control" placeholder="   Too   much   space   "></textarea>
        <div class="flex gap-2 my-2">
            <button class="btn btn-primary" id="btnAction">Remove Extra Whitespaces</button>
        </div>
        <textarea id="output" class="input-control" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnAction').onclick = () => {
            const val = document.getElementById('input').value;
            document.getElementById('output').value = val.replace(/\\s+/g, ' ').trim();
        };
        '''
    elif tool_id == "password-generator":
        ui = '''
        <div class="flex items-center gap-4 mb-4">
            <label>Length:</label>
            <input type="number" id="len" class="input-control" value="16" min="4" max="128" style="width: 80px;">
        </div>
        <div class="flex gap-4 mb-4">
            <label><input type="checkbox" id="upper" checked> Uppercase</label>
            <label><input type="checkbox" id="lower" checked> Lowercase</label>
            <label><input type="checkbox" id="nums" checked> Numbers</label>
            <label><input type="checkbox" id="syms" checked> Symbols</label>
        </div>
        <button class="btn btn-primary mb-4" id="btnGen">Generate Password</button>
        <div class="flex gap-2">
            <input type="text" id="output" class="input-control text-xl font-mono" readonly>
            <button class="btn btn-secondary" onclick="copyToClipboard(document.getElementById('output').value, this)">Copy</button>
        </div>
        '''
        js = '''
        document.getElementById('btnGen').onclick = () => {
            const len = document.getElementById('len').value;
            let chars = "";
            if(document.getElementById('upper').checked) chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            if(document.getElementById('lower').checked) chars += "abcdefghijklmnopqrstuvwxyz";
            if(document.getElementById('nums').checked) chars += "0123456789";
            if(document.getElementById('syms').checked) chars += "!@#$%^&*()_+~`|}{[]:;?><,./-=";

            if(!chars) { document.getElementById('output').value = "Select options!"; return; }

            let pass = "";
            const arr = new Uint32Array(len);
            crypto.getRandomValues(arr);
            for(let i=0; i<len; i++) pass += chars[arr[i] % chars.length];
            document.getElementById('output').value = pass;
        };
        document.getElementById('btnGen').click();
        '''
    elif tool_id == "prefix-suffix-adder":
        ui = '''
        <div class="flex gap-2 mb-2">
            <input type="text" id="prefix" class="input-control" placeholder="Prefix">
            <input type="text" id="suffix" class="input-control" placeholder="Suffix">
        </div>
        <textarea id="input" class="input-control" placeholder="Line 1\\nLine 2"></textarea>
        <button class="btn btn-primary my-2" id="btnAction">Add to each line</button>
        <textarea id="output" class="input-control" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnAction').onclick = () => {
            const pre = document.getElementById('prefix').value;
            const suf = document.getElementById('suffix').value;
            const lines = document.getElementById('input').value.split('\\n');
            document.getElementById('output').value = lines.map(l => pre + l + suf).join('\\n');
        };
        '''
    elif tool_id == "comma-separator":
        ui = '''
        <textarea id="input" class="input-control" placeholder="Item1\\nItem2\\nItem3"></textarea>
        <button class="btn btn-primary my-2" id="btnAction">Convert to Comma Separated</button>
        <textarea id="output" class="input-control" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnAction').onclick = () => {
            const lines = document.getElementById('input').value.split('\\n').filter(l=>l.trim()!=='');
            document.getElementById('output').value = lines.join(', ');
        };
        '''
    elif tool_id == "unit-converter":
        ui = '''
        <div class="flex gap-4">
            <input type="number" id="val" class="input-control" value="1">
            <select id="from" class="input-control"><option value="km">Kilometers</option><option value="mi">Miles</option><option value="m">Meters</option></select>
            <span class="mt-2 text-xl">=</span>
            <select id="to" class="input-control"><option value="mi">Miles</option><option value="km">Kilometers</option><option value="m">Meters</option></select>
        </div>
        <div class="mt-4 text-2xl font-bold text-[var(--accent-color)]" id="result">0.621371</div>
        '''
        js = '''
        const factors = { km: 1000, mi: 1609.34, m: 1 };
        const update = () => {
            const v = parseFloat(document.getElementById('val').value);
            const f = document.getElementById('from').value;
            const t = document.getElementById('to').value;
            if(isNaN(v)) return;
            const inMeters = v * factors[f];
            const out = inMeters / factors[t];
            document.getElementById('result').innerText = out.toPrecision(6);
        };
        document.getElementById('val').oninput = update;
        document.getElementById('from').onchange = update;
        document.getElementById('to').onchange = update;
        '''
    elif tool_id == "base-converter":
        ui = '''
        <div class="grid gap-4">
            <div><label class="input-label">Decimal</label><input type="text" id="dec" class="input-control"></div>
            <div><label class="input-label">Binary</label><input type="text" id="bin" class="input-control"></div>
            <div><label class="input-label">Hexadecimal</label><input type="text" id="hex" class="input-control"></div>
            <div><label class="input-label">Octal</label><input type="text" id="oct" class="input-control"></div>
        </div>
        '''
        js = '''
        const dec = document.getElementById('dec');
        const bin = document.getElementById('bin');
        const hex = document.getElementById('hex');
        const oct = document.getElementById('oct');

        dec.oninput = () => { let v = parseInt(dec.value, 10); if(!isNaN(v)){ bin.value=v.toString(2); hex.value=v.toString(16).toUpperCase(); oct.value=v.toString(8); } };
        bin.oninput = () => { let v = parseInt(bin.value, 2); if(!isNaN(v)){ dec.value=v.toString(10); hex.value=v.toString(16).toUpperCase(); oct.value=v.toString(8); } };
        hex.oninput = () => { let v = parseInt(hex.value, 16); if(!isNaN(v)){ dec.value=v.toString(10); bin.value=v.toString(2); oct.value=v.toString(8); } };
        oct.oninput = () => { let v = parseInt(oct.value, 8); if(!isNaN(v)){ dec.value=v.toString(10); bin.value=v.toString(2); hex.value=v.toString(16).toUpperCase(); } };
        '''
    elif tool_id == "percentage-calculator":
        ui = '''
        <div class="flex items-center gap-2 mb-4">
            <span>What is</span><input type="number" id="p1" class="input-control w-20"><span>% of</span><input type="number" id="v1" class="input-control w-24">
            <button class="btn btn-primary ml-2" onclick="c1()">Calc</button>
            <span class="font-bold ml-2 text-[var(--accent-color)]" id="r1">-</span>
        </div>
        <div class="flex items-center gap-2">
            <input type="number" id="v2a" class="input-control w-24"><span>is what % of</span><input type="number" id="v2b" class="input-control w-24">
            <button class="btn btn-primary ml-2" onclick="c2()">Calc</button>
            <span class="font-bold ml-2 text-[var(--accent-color)]" id="r2">-</span>
        </div>
        '''
        js = '''
        window.c1 = () => { document.getElementById('r1').innerText = (document.getElementById('p1').value / 100 * document.getElementById('v1').value).toFixed(2); };
        window.c2 = () => { document.getElementById('r2').innerText = ((document.getElementById('v2a').value / document.getElementById('v2b').value) * 100).toFixed(2) + '%'; };
        '''
    elif tool_id == "bmi-calculator":
        ui = '''
        <div class="flex gap-4">
            <div><label>Weight (kg)</label><input type="number" id="w" class="input-control" value="70"></div>
            <div><label>Height (cm)</label><input type="number" id="h" class="input-control" value="175"></div>
        </div>
        <button class="btn btn-primary my-4" id="btnCalc">Calculate BMI</button>
        <div class="text-2xl font-bold text-[var(--accent-color)]" id="res"></div>
        '''
        js = '''
        document.getElementById('btnCalc').onclick = () => {
            const w = parseFloat(document.getElementById('w').value);
            const h = parseFloat(document.getElementById('h').value) / 100;
            if(w && h) {
                const bmi = (w / (h * h)).toFixed(1);
                let text = bmi + " (";
                if(bmi < 18.5) text += "Underweight)";
                else if(bmi < 25) text += "Normal)";
                else if(bmi < 30) text += "Overweight)";
                else text += "Obese)";
                document.getElementById('res').innerText = text;
            }
        };
        '''
    elif tool_id == "roman-numerals":
        ui = '''
        <div class="flex gap-4 items-end">
            <div><label>Number</label><input type="number" id="num" class="input-control" placeholder="1-3999"></div>
            <div><label>Roman</label><input type="text" id="rom" class="input-control"></div>
        </div>
        '''
        js = '''
        const val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
        const syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

        document.getElementById('num').oninput = (e) => {
            let num = parseInt(e.target.value);
            if(isNaN(num) || num < 1 || num > 3999) return;
            let res = '';
            for(let i=0; i<val.length; i++) {
                while(num >= val[i]) { res += syms[i]; num -= val[i]; }
            }
            document.getElementById('rom').value = res;
        };
        '''
    elif tool_id == "prime-checker":
        ui = '''
        <div class="flex gap-2">
            <input type="number" id="num" class="input-control" placeholder="Enter integer">
            <button class="btn btn-primary" id="btnCheck">Check</button>
        </div>
        <div class="mt-4 text-xl font-bold" id="res"></div>
        '''
        js = '''
        document.getElementById('btnCheck').onclick = () => {
            const num = parseInt(document.getElementById('num').value);
            if(isNaN(num) || num <= 1) { document.getElementById('res').innerText = "Not Prime"; document.getElementById('res').style.color = 'var(--danger-color)'; return; }
            let isP = true;
            for(let i=2; i<=Math.sqrt(num); i++) if(num % i === 0) { isP = false; break; }
            document.getElementById('res').innerText = isP ? "Is Prime!" : "Not Prime";
            document.getElementById('res').style.color = isP ? 'var(--success-color)' : 'var(--danger-color)';
        };
        '''
    elif tool_id == "color-contrast":
        ui = '''
        <div class="flex gap-4">
            <div><label>Color 1</label><input type="color" id="c1" value="#ffffff" class="w-16 h-16 cursor-pointer"></div>
            <div><label>Color 2</label><input type="color" id="c2" value="#000000" class="w-16 h-16 cursor-pointer"></div>
        </div>
        <div class="mt-4 text-2xl font-bold" id="res"></div>
        '''
        js = '''
        function hexToRgb(hex) {
            var result = /^#?([a-f\\d]{2})([a-f\\d]{2})([a-f\\d]{2})$/i.exec(hex);
            return result ? { r: parseInt(result[1], 16), g: parseInt(result[2], 16), b: parseInt(result[3], 16) } : null;
        }
        function luminance(r, g, b) {
            var a = [r, g, b].map(function (v) { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
            return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
        }
        const calc = () => {
            let rgb1 = hexToRgb(document.getElementById('c1').value);
            let rgb2 = hexToRgb(document.getElementById('c2').value);
            let l1 = luminance(rgb1.r, rgb1.g, rgb1.b);
            let l2 = luminance(rgb2.r, rgb2.g, rgb2.b);
            let ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
            let res = ratio.toFixed(2) + " : 1";
            document.getElementById('res').innerText = res;
        };
        document.getElementById('c1').oninput = calc;
        document.getElementById('c2').oninput = calc;
        calc();
        '''
    elif tool_id == "gcd-lcm":
        ui = '''
        <div class="flex gap-4">
            <input type="number" id="n1" class="input-control" placeholder="Number 1">
            <input type="number" id="n2" class="input-control" placeholder="Number 2">
            <button class="btn btn-primary" id="btnCalc">Calc</button>
        </div>
        <div class="mt-4 text-xl font-bold" id="res"></div>
        '''
        js = '''
        const gcd = (a, b) => !b ? a : gcd(b, a % b);
        const lcm = (a, b) => (a * b) / gcd(a, b);
        document.getElementById('btnCalc').onclick = () => {
            const a = parseInt(document.getElementById('n1').value);
            const b = parseInt(document.getElementById('n2').value);
            if(a && b) {
                document.getElementById('res').innerText = `GCD: ${gcd(a,b)} | LCM: ${lcm(a,b)}`;
            }
        };
        '''
    elif tool_id == "random-number":
        ui = '''
        <div class="flex gap-4 items-end">
            <div><label>Min</label><input type="number" id="min" class="input-control w-24" value="1"></div>
            <div><label>Max</label><input type="number" id="max" class="input-control w-24" value="100"></div>
            <button class="btn btn-primary" id="btnGen">Generate</button>
        </div>
        <div class="mt-8 text-6xl font-bold text-center text-[var(--accent-color)]" id="res">-</div>
        '''
        js = '''
        document.getElementById('btnGen').onclick = () => {
            const min = parseInt(document.getElementById('min').value);
            const max = parseInt(document.getElementById('max').value);
            document.getElementById('res').innerText = Math.floor(Math.random() * (max - min + 1)) + min;
        };
        '''
    elif tool_id == "video-extractor":
        ui = '''
        <div class="flex flex-col gap-4">
            <input type="file" id="videoInput" accept="video/*" class="input-control p-2">
            <video id="videoPlayer" controls class="w-full bg-black rounded-md hidden"></video>
            <div class="flex gap-4 items-center w-full">
                <button class="btn btn-primary hidden" id="btnCapture">Capture Frame at Current Time</button>
                <span id="currentTimeDisplay" class="font-mono"></span>
            </div>
            <div id="frames" class="flex gap-4 flex-wrap mt-4 w-full"></div>
        </div>
        '''
        js = '''
        const input = document.getElementById('videoInput');
        const video = document.getElementById('videoPlayer');
        const btnCapture = document.getElementById('btnCapture');
        const frames = document.getElementById('frames');
        const timeDisplay = document.getElementById('currentTimeDisplay');

        input.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if(file) {
                video.src = URL.createObjectURL(file);
                video.classList.remove('hidden');
                btnCapture.classList.remove('hidden');
            }
        });
        video.addEventListener('timeupdate', () => { timeDisplay.innerText = "Time: " + video.currentTime.toFixed(2) + "s"; });
        btnCapture.addEventListener('click', () => {
            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth; canvas.height = video.videoHeight;
            const ctx = canvas.getContext('2d'); ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            const img = document.createElement('img'); img.src = canvas.toDataURL('image/png');
            img.className = 'w-48 rounded-sm border border-[var(--border-color)] object-contain';

            const wrapper = document.createElement('div'); wrapper.className = 'flex flex-col gap-2';
            const a = document.createElement('a'); a.href = img.src; a.download = `frame-${video.currentTime.toFixed(2)}s.png`;
            a.className = 'btn btn-secondary text-sm p-1'; a.innerText = 'Download';

            wrapper.appendChild(img); wrapper.appendChild(a); frames.insertBefore(wrapper, frames.firstChild);
        });
        '''
    elif tool_id == "pdf-info":
        ui = '''
        <input type="file" id="pdfInput" accept="application/pdf" class="input-control p-2 mb-4">
        <div id="output" class="p-4 bg-[var(--bg-surface)] rounded-md border border-[var(--border-color)] font-mono whitespace-pre-wrap">Select a PDF file...</div>
        '''
        js = '''
        document.getElementById('pdfInput').addEventListener('change', (e) => {
            const file = e.target.files[0];
            if(!file) return;
            document.getElementById('output').innerText = `File Name: ${file.name}\\nSize: ${(file.size/1024).toFixed(2)} KB\\nLast Modified: ${new Date(file.lastModified).toLocaleString()}\\nType: ${file.type}\\n\\n(Note: Full text parsing requires external libs. This views standard file metadata securely in browser.)`;
        });
        '''
    elif tool_id == "qr-generator":
        extra_head = '<script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.3/build/qrcode.min.js"></script>'
        ui = '''
        <div class="flex gap-2 mb-4">
            <input type="text" id="input" class="input-control" placeholder="Enter URL or text">
            <button class="btn btn-primary" id="btnGen">Generate</button>
        </div>
        <div class="flex flex-col items-center">
            <canvas id="canvas" class="border border-[var(--border-color)] rounded-md p-2 bg-white hidden"></canvas>
            <a id="download" class="btn btn-secondary mt-4 hidden">Download QR Code</a>
        </div>
        '''
        js = '''
        document.getElementById('btnGen').onclick = () => {
            const text = document.getElementById('input').value;
            if(!text) return;
            const canvas = document.getElementById('canvas');
            QRCode.toCanvas(canvas, text, { width: 250 }, function (error) {
                if (error) console.error(error);
                canvas.classList.remove('hidden');
                const dl = document.getElementById('download');
                dl.href = canvas.toDataURL();
                dl.download = 'qrcode.png';
                dl.classList.remove('hidden');
            });
        };
        '''
    elif tool_id == "image-to-base64":
        ui = '''
        <input type="file" id="input" accept="image/*" class="input-control p-2 mb-4">
        <textarea id="output" class="input-control h-48" readonly></textarea>
        '''
        js = '''
        document.getElementById('input').onchange = (e) => {
            const file = e.target.files[0];
            if(!file) return;
            const reader = new FileReader();
            reader.onload = (event) => { document.getElementById('output').value = event.target.result; };
            reader.readAsDataURL(file);
        };
        '''
    elif tool_id == "base64-to-image":
        ui = '''
        <textarea id="input" class="input-control h-32 mb-4" placeholder="data:image/png;base64,..."></textarea>
        <button class="btn btn-primary mb-4" id="btnShow">Show Image</button>
        <div>
            <img id="imgOut" class="max-w-full rounded-md hidden shadow-md">
        </div>
        '''
        js = '''
        document.getElementById('btnShow').onclick = () => {
            const val = document.getElementById('input').value.trim();
            if(!val) return;
            const img = document.getElementById('imgOut');
            img.src = val.startsWith('data:image') ? val : 'data:image/png;base64,' + val;
            img.classList.remove('hidden');
        };
        '''
    elif tool_id == "svg-optimizer":
        ui = '''
        <textarea id="input" class="input-control h-48" placeholder="<svg>...</svg>"></textarea>
        <button class="btn btn-primary my-4" id="btnAction">Basic Minify</button>
        <textarea id="output" class="input-control h-48" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnAction').onclick = () => {
            let svg = document.getElementById('input').value;
            svg = svg.replace(/\\n/g, '').replace(/>\\s+</g, '><').replace(/\\s{2,}/g, ' ');
            document.getElementById('output').value = svg;
        };
        '''
    elif tool_id == "color-extractor":
        ui = '''
        <input type="file" id="input" accept="image/*" class="input-control p-2 mb-4">
        <canvas id="canvas" class="max-w-full hidden cursor-crosshair rounded-md shadow-md"></canvas>
        <div class="mt-4 flex gap-4 items-center hidden" id="resBox">
            <div id="colorSwatch" class="w-16 h-16 rounded-md shadow-sm border border-gray-200"></div>
            <input type="text" id="colorHex" class="input-control w-32" readonly>
        </div>
        '''
        js = '''
        const input = document.getElementById('input');
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        const resBox = document.getElementById('resBox');

        input.onchange = (e) => {
            const file = e.target.files[0];
            if(!file) return;
            const img = new Image();
            img.onload = () => {
                canvas.width = img.width; canvas.height = img.height;
                ctx.drawImage(img, 0, 0);
                canvas.classList.remove('hidden');
            };
            img.src = URL.createObjectURL(file);
        };

        canvas.onclick = (e) => {
            const rect = canvas.getBoundingClientRect();
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;
            const x = (e.clientX - rect.left) * scaleX;
            const y = (e.clientY - rect.top) * scaleY;
            const p = ctx.getImageData(x, y, 1, 1).data;
            const hex = "#" + ("000000" + ((p[0] << 16) | (p[1] << 8) | p[2]).toString(16)).slice(-6);
            document.getElementById('colorSwatch').style.backgroundColor = hex;
            document.getElementById('colorHex').value = hex;
            resBox.classList.remove('hidden');
        };
        '''
    elif tool_id == "ip-info":
        ui = '''
        <button class="btn btn-primary mb-4" id="btnAction">Get My IP Info</button>
        <textarea id="output" class="input-control h-48 font-mono" readonly></textarea>
        '''
        js = '''
        document.getElementById('btnAction').onclick = async () => {
            try {
                const res = await fetch('https://ipapi.co/json/');
                const data = await res.json();
                document.getElementById('output').value = JSON.stringify(data, null, 2);
            } catch(e) { document.getElementById('output').value = "Failed to fetch IP data."; }
        };
        '''
    elif tool_id == "key-event":
        ui = '''
        <div class="flex flex-col items-center justify-center p-12 border-2 border-dashed border-[var(--accent-color)] rounded-lg bg-[var(--bg-surface)]">
            <div class="text-xl text-[var(--text-muted)] mb-4">Press any key</div>
            <div class="text-6xl font-bold text-[var(--text-main)]" id="key">-</div>
        </div>
        <div class="grid grid-cols-2 gap-4 mt-8 max-w-lg mx-auto">
            <div><label class="text-sm text-[var(--text-muted)]">event.key</label><input type="text" id="ekey" class="input-control" readonly></div>
            <div><label class="text-sm text-[var(--text-muted)]">event.code</label><input type="text" id="ecode" class="input-control" readonly></div>
            <div><label class="text-sm text-[var(--text-muted)]">event.keyCode</label><input type="text" id="ekc" class="input-control" readonly></div>
        </div>
        '''
        js = '''
        window.addEventListener('keydown', (e) => {
            e.preventDefault();
            document.getElementById('key').innerText = e.keyCode;
            document.getElementById('ekey').value = e.key;
            document.getElementById('ecode').value = e.code;
            document.getElementById('ekc').value = e.keyCode;
        });
        '''
    elif tool_id == "system-info":
        ui = '''
        <div class="grid gap-4">
            <div><label class="input-label">User Agent</label><textarea id="ua" class="input-control h-20" readonly></textarea></div>
            <div class="grid grid-cols-2 gap-4">
                <div><label class="input-label">Platform</label><input type="text" id="plat" class="input-control" readonly></div>
                <div><label class="input-label">Language</label><input type="text" id="lang" class="input-control" readonly></div>
                <div><label class="input-label">Screen WxH</label><input type="text" id="screen" class="input-control" readonly></div>
                <div><label class="input-label">Cookies Enabled</label><input type="text" id="cookies" class="input-control" readonly></div>
            </div>
        </div>
        '''
        js = '''
        document.getElementById('ua').value = navigator.userAgent;
        document.getElementById('plat').value = navigator.platform;
        document.getElementById('lang').value = navigator.language;
        document.getElementById('screen').value = window.screen.width + " x " + window.screen.height;
        document.getElementById('cookies').value = navigator.cookieEnabled;
        '''
    elif tool_id == "meta-tags":
        ui = '''
        <div class="grid gap-4 mb-4">
            <input type="text" id="tTitle" class="input-control" placeholder="Title">
            <input type="text" id="tDesc" class="input-control" placeholder="Description">
            <input type="text" id="tKeywords" class="input-control" placeholder="Keywords (comma separated)">
            <input type="text" id="tAuthor" class="input-control" placeholder="Author">
        </div>
        <button class="btn btn-primary mb-4" onclick="gen()">Generate Meta Tags</button>
        <textarea id="output" class="input-control h-48 font-mono" readonly></textarea>
        '''
        js = '''
        window.gen = () => {
            let res = `<meta charset="UTF-8">\\n`;
            res += `<meta name="viewport" content="width=device-width, initial-scale=1.0">\\n`;
            if(document.getElementById('tTitle').value) res += `<title>${document.getElementById('tTitle').value}</title>\\n`;
            if(document.getElementById('tDesc').value) res += `<meta name="description" content="${document.getElementById('tDesc').value}">\\n`;
            if(document.getElementById('tKeywords').value) res += `<meta name="keywords" content="${document.getElementById('tKeywords').value}">\\n`;
            if(document.getElementById('tAuthor').value) res += `<meta name="author" content="${document.getElementById('tAuthor').value}">\\n`;
            document.getElementById('output').value = res;
        };
        '''
    elif tool_id == "stopwatch":
        ui = '''
        <div class="flex flex-col items-center p-8 bg-[var(--bg-surface)] rounded-md border border-[var(--border-color)]">
            <div class="text-6xl font-mono font-bold text-[var(--text-main)] mb-8" id="display">00:00:00.00</div>
            <div class="flex gap-4">
                <button class="btn btn-primary" id="btnStart">Start</button>
                <button class="btn btn-secondary" id="btnStop">Stop</button>
                <button class="btn btn-secondary" id="btnReset">Reset</button>
            </div>
        </div>
        '''
        js = '''
        let startTime, updatedTime, difference, tInterval, running = 0;
        const display = document.getElementById('display');

        function update() {
            updatedTime = new Date().getTime();
            difference = updatedTime - startTime;
            let hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            let minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
            let seconds = Math.floor((difference % (1000 * 60)) / 1000);
            let milliseconds = Math.floor((difference % 1000) / 10);

            hours = (hours < 10) ? "0" + hours : hours;
            minutes = (minutes < 10) ? "0" + minutes : minutes;
            seconds = (seconds < 10) ? "0" + seconds : seconds;
            milliseconds = (milliseconds < 10) ? "0" + milliseconds : milliseconds;
            display.innerHTML = hours + ':' + minutes + ':' + seconds + '.' + milliseconds;
        }

        document.getElementById('btnStart').onclick = () => {
            if(!running) {
                startTime = new Date().getTime() - (difference || 0);
                tInterval = setInterval(update, 10);
                running = 1;
            }
        };
        document.getElementById('btnStop').onclick = () => {
            clearInterval(tInterval);
            running = 0;
        };
        document.getElementById('btnReset').onclick = () => {
            clearInterval(tInterval);
            running = 0;
            difference = 0;
            display.innerHTML = "00:00:00.00";
        };
        '''
    else:
        # Fallback if I missed any minor one
        ui = "<p>Under construction.</p>"
        js = ""

    return extra_head, ui, js

def generate_all_tools():
    sidebar = generate_sidebar_links(is_index=False)
    for t in TOOLS:
        if t.get("custom"):
            continue # We handle image-converter, cropper, markup separately

        os.makedirs(t["id"], exist_ok=True)
        extra_head, ui, js = get_tool_logic(t["id"])

        content = TEMPLATE.format(
            title=t["title"],
            desc=t["desc"],
            sidebar_links=sidebar,
            extra_head=extra_head,
            tool_ui=ui,
            tool_js=js
        )
        with open(f"{t['id']}/index.html", "w") as f:
            f.write(content)

if __name__ == "__main__":
    build_index()
    generate_all_tools()
    print("Generated fully functional tool suite.")


import re

def handle_custom_tools():
    sidebar = generate_sidebar_links(is_index=False)

    # 1. image-converter
    t = [x for x in TOOLS if x["id"] == "image-converter"][0]
    ui = """
    <div class="toolbar" style="display:flex; gap:1rem; margin-bottom: 2rem; background: var(--bg-surface); padding: 1rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); align-items:center;">
        <select id="format-select" class="input-control" style="width: auto;">
            <option value="image/png">Convert to PNG</option>
            <option value="image/jpeg">Convert to JPEG</option>
            <option value="image/webp">Convert to WebP</option>
        </select>
        <div id="globalActions" style="display: none; gap:0.5rem;">
            <button id="downloadAllBtn" class="btn btn-primary">Download All</button>
            <button id="clearBtn" class="btn btn-secondary">Clear</button>
        </div>
    </div>
    <div class="drop-zone" id="drop-zone" style="width: 100%; min-height: 240px; border: 2px dashed var(--border-color); border-radius: var(--radius-lg); display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; position: relative; margin-bottom: 2rem;">
        <div style="pointer-events: none; text-align: center;">
            <div style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">Drop images here</div>
            <div style="color: var(--text-muted); font-size: 0.9rem;">or click to browse files</div>
        </div>
        <input type="file" id="file-input" multiple accept="image/*" style="position: absolute; inset: 0; opacity: 0; cursor: pointer;">
    </div>
    <div class="grid" id="resultsGrid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 1.5rem; width: 100%;"></div>
    """

    with open("image-converter/index.html", "r") as f:
        orig_content = f.read()

    js_match = re.search(r'<script>(.*?)</script>', orig_content, re.DOTALL)
    js = js_match.group(1) if js_match else ""
    js = js.replace("class='card'", "class='card' style='padding:0;'")
    js = js.replace("class=\"card\"", "class=\"card\" style=\"padding:0;\"")
    js = js.replace("class=\"card-btn btn-download\"", "class=\"btn btn-secondary\" style=\"width:100%; justify-content:center;\"")
    js = js.replace("class=\"card-btn btn-copy\"", "class=\"btn btn-primary\" style=\"width:100%; justify-content:center;\"")

    content = TEMPLATE.format(
        title=t["title"],
        desc=t["desc"],
        sidebar_links=sidebar,
        extra_head="",
        tool_ui=ui,
        tool_js=js
    )
    with open("image-converter/index.html", "w") as f:
        f.write(content)

    # 2. image-cropper
    t = [x for x in TOOLS if x["id"] == "image-cropper"][0]
    ui = """
    <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem;">
        <div class="drop-zone" id="drop-zone" style="width: 100%; min-height: 240px; border: 2px dashed var(--border-color); border-radius: var(--radius-lg); display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; position: relative; margin-bottom: 2rem;">
            <div style="pointer-events: none; text-align: center;">
                <div style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">Drop an image here</div>
                <div style="color: var(--text-muted); font-size: 0.9rem;">or paste from clipboard (Ctrl+V)</div>
            </div>
            <input type="file" id="file-input" accept="image/*" style="position: absolute; inset: 0; opacity: 0; cursor: pointer;">
        </div>
        <div id="workspace" style="display: none; width: 100%;">
            <div style="display: flex; gap: 1rem; align-items: center; background: var(--bg-surface); padding: 1rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-bottom: 1rem; flex-wrap: wrap;">
                <select id="aspect-ratio" class="input-control" style="width: auto;">
                    <option value="free">Freeform</option>
                    <option value="1">1:1 (Square)</option>
                    <option value="1.3333">4:3 (Standard)</option>
                    <option value="1.7777">16:9 (Widescreen)</option>
                    <option value="0.5625">9:16 (Story/Reel)</option>
                </select>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <label style="font-size: 0.9rem;">Corner Radius</label>
                    <input type="range" id="border-radius" min="0" max="50" value="0">
                </div>
                <label style="display: flex; align-items: center; gap: 0.5rem; font-size: 0.9rem;">
                    <input type="checkbox" id="round-crop"> Circular Crop
                </label>
                <select id="format-select" class="input-control" style="width: auto; margin-left: auto;">
                    <option value="image/png">PNG</option>
                    <option value="image/jpeg">JPEG</option>
                    <option value="image/webp">WebP</option>
                </select>
                <button id="save-btn" class="btn btn-primary">Download Crop</button>
                <button id="reset-btn" class="btn btn-secondary">Cancel</button>
            </div>
            <div id="editor-container" style="position: relative; width: 100%; max-height: 70vh; display: flex; justify-content: center; align-items: center; background-image: linear-gradient(45deg, #ccc 25%, transparent 25%), linear-gradient(-45deg, #ccc 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #ccc 75%), linear-gradient(-45deg, transparent 75%, #ccc 75%); background-size: 20px 20px; background-position: 0 0, 0 10px, 10px -10px, -10px 0px; border-radius: var(--radius-md); overflow: hidden;">
                <img id="source-image" src="" style="max-width: 100%; max-height: 70vh; display: block; pointer-events: none; opacity: 0.4;">
                <div id="crop-box" style="position: absolute; border: 2px solid #00f; background: rgba(255, 255, 255, 0.2); box-shadow: 0 0 0 9999px rgba(0, 0, 0, 0.5); cursor: move; width: 200px; height: 200px; top: 10%; left: 10%; border-radius: 0%; overflow: hidden;">
                    <div id="resizer" style="width: 20px; height: 20px; background: #00f; position: absolute; right: -2px; bottom: -2px; cursor: se-resize; border-radius: 50%;"></div>
                </div>
            </div>
        </div>
    </div>
    """

    with open("image-cropper/index.html", "r") as f:
        orig_content = f.read()

    js_match = re.search(r'<script>(.*?)</script>', orig_content, re.DOTALL)
    js = js_match.group(1) if js_match else ""

    content = TEMPLATE.format(
        title=t["title"],
        desc=t["desc"],
        sidebar_links=sidebar,
        extra_head="",
        tool_ui=ui,
        tool_js=js
    )
    with open("image-cropper/index.html", "w") as f:
        f.write(content)

    # 3. image-markup
    t = [x for x in TOOLS if x["id"] == "image-markup"][0]

    # Extract React components and dependencies
    with open("image-markup/index.html", "r") as f:
        markup_html = f.read()

    extra_head = """
    <!-- React & ReactDOM -->
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <!-- Babel -->
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <!-- Fabric.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.1/fabric.min.js"></script>
    """

    ui = """
    <div id="root" style="width: 100%; height: 75vh; border: 1px solid var(--border-color); border-radius: var(--radius-md); overflow: hidden; position: relative;"></div>
    """

    # We extract everything inside <script type="text/babel">
    react_script_match = re.search(r'<script type="text/babel">(.*?)</script>', markup_html, re.DOTALL)
    react_script = react_script_match.group(1) if react_script_match else ""

    # Write the react script into a separate file that we include
    with open("image-markup/app.jsx", "w") as f:
        f.write(react_script)

    # include the script tag at the bottom via `tool_js` block or directly
    js_inclusion = ""

    content = TEMPLATE.format(
        title=t["title"],
        desc=t["desc"],
        sidebar_links=sidebar,
        extra_head=extra_head,
        tool_ui=ui,
        tool_js=js_inclusion
    )

    # Append the text/babel script to the end of body manually because TEMPLATE expects raw JS
    content = content.replace("</body>", '<script type="text/babel" src="app.jsx"></script>\n</body>')

    with open("image-markup/index.html", "w") as f:
        f.write(content)

if __name__ == "__main__":
    handle_custom_tools()
