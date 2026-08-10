from pathlib import Path
from html import escape

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "assets" / "readme"
FONT_PATH = Path(__file__).with_name("michroma-regular.ttf")

font = TTFont(FONT_PATH)
glyph_set = font.getGlyphSet()
cmap = font.getBestCmap()
hmtx = font["hmtx"]
units_per_em = font["head"].unitsPerEm


def display_text(text, x, y, size, fill="#edf5fa", anchor="start", letter_spacing=0):
    glyphs = []
    cursor = 0
    scale = size / units_per_em
    for char in text:
        glyph_name = cmap.get(ord(char), ".notdef")
        advance, _ = hmtx[glyph_name]
        if char != " ":
            pen = SVGPathPen(glyph_set)
            glyph_set[glyph_name].draw(pen)
            path = pen.getCommands()
            glyphs.append(
                f'<path d="{path}" transform="translate({cursor:.2f} 0)"/>'
            )
        cursor += advance + letter_spacing / scale
    width = cursor * scale
    offset = 0
    if anchor == "middle":
        offset = -width / 2
    elif anchor == "end":
        offset = -width
    return (
        f'<g fill="{fill}" transform="translate({x + offset:.2f} {y:.2f}) '
        f'scale({scale:.6f} {-scale:.6f})">{"".join(glyphs)}</g>'
    )


def svg_shell(title, desc, height, body, defs=""):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(desc)}</desc>
  <defs>
    <pattern id="grid" width="42" height="42" patternUnits="userSpaceOnUse">
      <path d="M 42 0 L 0 0 0 42" fill="none" stroke="#4499c2" stroke-opacity=".07" stroke-width="1"/>
    </pattern>
    <radialGradient id="cyanGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#16c5ff" stop-opacity=".16"/>
      <stop offset="1" stop-color="#16c5ff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="signal" x1="0" x2="1">
      <stop stop-color="#16c5ff"/><stop offset="1" stop-color="#45ed73"/>
    </linearGradient>
    {defs}
  </defs>
  {body}
</svg>
'''
    return "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"


def hero():
    title = display_text("TONIVECHER", 66, 168, 44, letter_spacing=-0.5)
    lab = display_text("AI LAB", 68, 215, 20, fill="#16c5ff", letter_spacing=4)
    body = f'''
  <rect width="1200" height="520" rx="18" fill="#070b0f"/>
  <rect width="1200" height="520" rx="18" fill="url(#grid)"/>
  <ellipse cx="1030" cy="55" rx="310" ry="220" fill="url(#cyanGlow)"/>
  <path d="M0 1H1200M0 519H1200" stroke="#a4cce0" stroke-opacity=".16"/>

  <g transform="translate(66 52)">
    <path d="M0 8H34" stroke="#16c5ff" stroke-width="2"/>
    <text x="48" y="14" fill="#a7bac6" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="16" letter-spacing="2.4">AI PRODUCT ENGINEERING</text>
    <rect x="500" y="-3" width="92" height="25" fill="none" stroke="#16c5ff" stroke-opacity=".48"/>
    <text x="515" y="14" fill="#16c5ff" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="12" letter-spacing="1.4">LAB / 01</text>
  </g>

  {title}
  {lab}
  <text x="66" y="287" fill="#aebdc6" font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="23">
    Делаю продукты, когда одного сайта или бота мало.
  </text>
  <text x="66" y="320" fill="#edf5fa" font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="22" font-weight="650">
    Интерфейс, сервер и автоматизация.
  </text>
  <text x="66" y="350" fill="#edf5fa" font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="22" font-weight="650">
    Запуск тоже беру на себя.
  </text>

  <g transform="translate(66 376)">
    <rect width="256" height="54" fill="#16c5ff"/>
    <text x="24" y="34" fill="#00131a" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="17" font-weight="700" letter-spacing="1.3">OPEN TO REMOTE WORK</text>
    <rect x="272" width="184" height="54" fill="#ffffff" fill-opacity=".025" stroke="#a4cce0" stroke-opacity=".22"/>
    <text x="296" y="34" fill="#c5d2d9" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="17" letter-spacing="1.3">MOSCOW / UTC+3</text>
  </g>

  <g transform="translate(730 62)">
    <rect width="404" height="382" rx="12" fill="#080c10" stroke="#79bedb" stroke-opacity=".34"/>
    <path d="M0 46H404" stroke="#a4cce0" stroke-opacity=".16"/>
    <circle cx="22" cy="23" r="5" fill="#ff4f55"/>
    <circle cx="40" cy="23" r="5" fill="#ffbd18"/>
    <circle cx="58" cy="23" r="5" fill="#45ed73"/>
    <text x="78" y="28" fill="#60717d" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" letter-spacing="1.3">TONIVECHER / SYSTEM FLOW</text>
    <circle cx="337" cy="23" r="4" fill="#45ed73"/>
    <text x="348" y="28" fill="#45ed73" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" letter-spacing="1.2">LIVE</text>

    <g transform="translate(24 74)" font-family="ui-monospace, SFMono-Regular, Menlo, monospace">
      <text x="0" y="12" fill="#16c5ff" font-size="12" letter-spacing="1.8">INPUT SIGNAL</text>
      <rect x="0" y="30" width="356" height="48" fill="#0e151c" stroke="#a4cce0" stroke-opacity=".16"/>
      <text x="16" y="59" fill="#c5d2d9" font-size="15">Telegram · Web · Files · API</text>
      <path d="M178 78V107" stroke="#16c5ff"/>
      <path d="M173 102L178 107L183 102" fill="none" stroke="#16c5ff"/>

      <rect x="0" y="108" width="356" height="82" fill="#111a22" stroke="#16c5ff" stroke-opacity=".5"/>
      <text x="16" y="134" fill="#60717d" font-size="11" letter-spacing="1.5">CONTROL CORE / 02</text>
      <text x="16" y="165" fill="#edf5fa" font-size="19">API · state · access · history</text>
      <circle cx="329" cy="149" r="7" fill="#45ed73"/>
      <path d="M178 190V219" stroke="#45ed73"/>
      <path d="M173 214L178 219L183 214" fill="none" stroke="#45ed73"/>

      <g transform="translate(0 220)">
        <rect width="110" height="66" fill="#0e151c" stroke="#a4cce0" stroke-opacity=".16"/>
        <rect x="123" width="110" height="66" fill="#0e151c" stroke="#a4cce0" stroke-opacity=".16"/>
        <rect x="246" width="110" height="66" fill="#0e151c" stroke="#a4cce0" stroke-opacity=".16"/>
        <text x="14" y="27" fill="#16c5ff" font-size="11">01 / WORK</text><text x="14" y="49" fill="#edf5fa" font-size="14">AGENTS</text>
        <text x="137" y="27" fill="#d248ff" font-size="11">02 / QA</text><text x="137" y="49" fill="#edf5fa" font-size="14">HUMAN</text>
        <text x="260" y="27" fill="#45ed73" font-size="11">03 / SHIP</text><text x="260" y="49" fill="#edf5fa" font-size="14">PROD</text>
      </g>
    </g>
  </g>

  <g transform="translate(66 478)" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13">
    <text fill="#16c5ff">REACT</text><text x="92" fill="#60717d">/</text>
    <text x="116" fill="#edf5fa">FASTAPI</text><text x="230" fill="#60717d">/</text>
    <text x="254" fill="#edf5fa">POSTGRESQL</text><text x="396" fill="#60717d">/</text>
    <text x="420" fill="#edf5fa">TELEGRAM</text><text x="536" fill="#60717d">/</text>
    <text x="560" fill="#45ed73">PRODUCTION</text>
  </g>
'''
    return svg_shell(
        "Tonivecher AI Lab",
        "Продукты для задач, где нужны интерфейс, сервер, автоматизация и запуск.",
        520,
        body,
    )


def system_map():
    stages = [
        ("01", "CHANNELS", "Telegram · Web", "forms · files", "#16c5ff"),
        ("02", "CORE", "API · state", "access · history", "#078cff"),
        ("03", "WORK", "bots · agents", "n8n · documents", "#d248ff"),
        ("04", "CONTROL", "criteria · QA", "human decision", "#ffe016"),
        ("05", "RELEASE", "production", "result · support", "#45ed73"),
    ]
    cards = []
    for i, (num, name, line1, line2, color) in enumerate(stages):
        x = 36 + i * 232
        cards.append(f'''
    <g transform="translate({x} 120)">
      <rect width="204" height="150" fill="#0e151c" stroke="#a4cce0" stroke-opacity=".18"/>
      <path d="M0 0H204" stroke="{color}" stroke-width="3"/>
      <text x="18" y="33" fill="{color}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13" letter-spacing="1.6">{num} / {name}</text>
      <text x="18" y="78" fill="#edf5fa" font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="19" font-weight="650">{line1}</text>
      <text x="18" y="108" fill="#91a1ac" font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="17">{line2}</text>
      <circle cx="180" cy="126" r="5" fill="{color}"/>
    </g>''')
        if i < 4:
            ax = x + 204
            cards.append(f'<path d="M{ax} 195H{ax + 28}" stroke="#60717d"/><path d="M{ax + 22} 190L{ax + 28} 195L{ax + 22} 200" fill="none" stroke="#60717d"/>')
    heading = display_text("SYSTEM ROUTE", 36, 72, 40, letter_spacing=1)
    body = f'''
  <rect width="1200" height="330" rx="18" fill="#070b0f"/>
  <rect width="1200" height="330" rx="18" fill="url(#grid)"/>
  {heading}
  <text x="1164" y="70" text-anchor="end" fill="#60717d" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13" letter-spacing="1.4">FROM SIGNAL TO SHIPPED RESULT</text>
  {''.join(cards)}
  <path d="M36 296H1164" stroke="url(#signal)" stroke-width="2"/>
  <circle cx="36" cy="296" r="5" fill="#16c5ff"/><circle cx="1164" cy="296" r="5" fill="#45ed73"/>
'''
    return svg_shell(
        "Маршрут системы",
        "Каналы передают данные в ядро, затем работа проходит через агентов, контроль человека и выпуск в продакшен.",
        330,
        body,
    )


def section_asset(filename, index, kicker, title, accent="#16c5ff"):
    heading = display_text(title, 44, 93, 44, letter_spacing=0.4)
    body = f'''
  <rect width="1200" height="138" rx="12" fill="#070b0f"/>
  <rect width="1200" height="138" rx="12" fill="url(#grid)"/>
  <path d="M0 1H1200M0 137H1200" stroke="#a4cce0" stroke-opacity=".16"/>
  <path d="M44 34H82" stroke="{accent}" stroke-width="2"/>
  <text x="96" y="39" fill="{accent}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="14" letter-spacing="2">{escape(index)} / {escape(kicker)}</text>
  {heading}
  <circle cx="1138" cy="69" r="7" fill="{accent}"/>
  <circle cx="1138" cy="69" r="18" fill="none" stroke="{accent}" stroke-opacity=".26"/>
'''
    (OUT / filename).write_text(svg_shell(title, kicker, 138, body), encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "hero.svg").write_text(hero(), encoding="utf-8")
    (OUT / "system-route.svg").write_text(system_map(), encoding="utf-8")
    section_asset("section-projects.svg", "01", "SELECTED WORK", "PROJECTS")
    section_asset("section-method.svg", "02", "OPERATING MODEL", "METHOD", "#45ed73")
    section_asset("section-stack.svg", "03", "WORKING SET", "STACK", "#d248ff")
    section_asset("section-contact.svg", "04", "REMOTE / UTC+3", "CONTACT", "#ffe016")


if __name__ == "__main__":
    main()
