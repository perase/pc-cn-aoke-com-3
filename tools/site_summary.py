import json
import sys

SITES = [
    {
        "title": "Aoke Official",
        "url": "https://pc-cn-aoke.com",
        "tags": ["aoke", "official", "portal"],
        "description": "Main website for Aoke products and services, offering support and news."
    },
    {
        "title": "Aoke Blog",
        "url": "https://pc-cn-aoke.com/blog",
        "tags": ["aoke", "blog", "updates"],
        "description": "Technical articles and product announcements from Aoke team."
    },
    {
        "title": "Aoke Docs",
        "url": "https://pc-cn-aoke.com/docs",
        "tags": ["aoke", "documentation", "guide"],
        "description": "Comprehensive user guides and API references for Aoke platform."
    }
]

KEYWORDS = ["aoke", "pc-cn-aoke", "cloud", "service"]

def format_summary(site_entry: dict) -> str:
    """Convert a single site dict into a readable summary block."""
    lines = [
        f"Site: {site_entry['title']}",
        f"URL:  {site_entry['url']}",
        f"Tags: {', '.join(site_entry['tags'])}",
        f"About: {site_entry['description']}",
    ]
    return "\n".join(lines)

def generate_structured_summary(sites: list, keywords: list) -> str:
    """Build a complete structured summary string from all site data."""
    parts = []
    parts.append("=" * 60)
    parts.append("  SITE SUMMARY  ".center(58, "="))
    parts.append("=" * 60)
    parts.append("")
    parts.append(f"Total sites: {len(sites)}")
    parts.append(f"Relevant keywords: {', '.join(keywords)}")
    parts.append("")

    for idx, site in enumerate(sites, start=1):
        parts.append(f"[{idx}]".center(60, "-"))
        parts.append(format_summary(site))
        parts.append("")

    parts.append("-" * 60)
    parts.append("End of summary")
    parts.append("-" * 60)
    return "\n".join(parts)

def compress_summary(sites: list) -> str:
    """Return a JSON-like compact version for programmatic use."""
    return json.dumps(
        {
            "version": "1.0",
            "generated": "static",
            "keywords": KEYWORDS,
            "sites": [
                {
                    "title": s["title"],
                    "url": s["url"],
                    "tags": s["tags"],
                    "description": s["description"]
                }
                for s in sites
            ]
        },
        indent=2
    )

def main():
    """Entry point: print human-readable summary and compact JSON."""
    print("=== Human-readable summary ===")
    print(generate_structured_summary(SITES, KEYWORDS))
    print()
    print("=== Compact machine-friendly summary ===")
    print(compress_summary(SITES))

if __name__ == "__main__":
    main()