from scholarly import scholarly
import datetime

# === CONFIG ===
SCHOLAR_ID = "9PIpzCgAAAAJ"  # Replace with your Google Scholar ID
AUTHOR = scholarly.search_author_id(SCHOLAR_ID)
AUTHOR = scholarly.fill(AUTHOR, sections=["publications"])

# === HTML HEADER ===
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Publications | {AUTHOR['name']}</title>
  <link rel="stylesheet" href="style.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
</head>
<body>
  <header class="topbar">
    <div class="brand"><a href="index.html">{AUTHOR['name']}</a></div>
    <nav>
      <a href="index.html">About</a>
      <a href="publications.html" class="active">Publications</a>
      <a href="projects.html">Projects</a>
      <a href="cv.html">CV</a>
      <a href="contact.html">Contact</a>
    </nav>
  </header>

  <section class="hero">
    <h1>Publications</h1>
    <p>Selected works from <a href="https://scholar.google.com/citations?user={SCHOLAR_ID}" target="_blank">Google Scholar</a></p>
  </section>

  <main class="pubs-container">
"""

# === ADD EACH PUBLICATION ===
for pub in AUTHOR["publications"]:
    bib = pub.get("bib", {})
    title = bib.get("title", "Untitled")
    authors = bib.get("author", "")
    venue = bib.get("venue", "")
    year = bib.get("pub_year", "")

    # 🔗 Correct and direct Google Scholar link
    citation_id = pub.get("author_pub_id", "")
    if citation_id:
        link = f"https://scholar.google.com/citations?view_op=view_citation&hl=en&user={SCHOLAR_ID}&citation_for_view={citation_id}"
    else:
        link = f"https://scholar.google.com/scholar?cluster={citation_id}"

    html += f"""
    <article class="pub-card">
      <div class="pub-header">
        <a href="{link}" target="_blank" rel="noopener noreferrer" class="pub-title">{title}</a>
        <span class="pub-year">{year}</span>
      </div>
      <p class="pub-authors">{authors}</p>
      <p class="pub-venue">{venue}</p>
    </article>
    """

# === FOOTER ===
html += f"""
  </main>

  <footer>
    <p>Last updated: {datetime.date.today()} | &copy; {datetime.date.today().year} {AUTHOR['name']}</p>
  </footer>
</body>
</html>
"""

# === SAVE FILE ===
with open("publications.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ publications.html generated successfully with working Google Scholar links.")
