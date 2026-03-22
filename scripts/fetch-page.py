# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "playwright",
#     "trafilatura",
# ]
# ///
"""
Fetch and extract clean text from web pages using a real browser.

Usage:
    uv run scripts/fetch-page.py <url>                        # headless fetch, plain text
    uv run scripts/fetch-page.py --format markdown <url>      # headless fetch, markdown
    uv run scripts/fetch-page.py --interactive <url>          # opens visible browser
    uv run scripts/fetch-page.py --wait 5000 <url>            # wait 5s for JS rendering
    uv run scripts/fetch-page.py --setup                      # install browser binaries

One-time setup:
    uv run scripts/fetch-page.py --setup
"""

import argparse
import subprocess
import sys


def setup_browsers():
    """Install Playwright's Chromium browser binary."""
    subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        check=True,
    )
    print("Chromium installed successfully.")


def fetch_page(url: str, *, interactive: bool = False, wait_ms: int = 2000, output_format: str = "txt"):
    from playwright.sync_api import sync_playwright
    import trafilatura

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=not interactive)
        except Exception:
            print(
                "Error: Chromium not found. Run 'uv run scripts/fetch-page.py --setup' first.",
                file=sys.stderr,
            )
            sys.exit(1)

        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            viewport={"width": 1440, "height": 900},
            locale="en-US",
        )
        page = context.new_page()
        # Hide webdriver flag that bot detectors check
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
        except Exception as e:
            browser.close()
            msg = str(e).split("\n")[0]  # first line only
            print(f"Error: could not load {url}: {msg}", file=sys.stderr)
            sys.exit(1)
        page.wait_for_timeout(wait_ms)

        if interactive:
            if sys.stdin.isatty():
                input("Press Enter when ready to extract...")
            else:
                print("Non-interactive terminal detected, extracting after wait period.", file=sys.stderr)
                page.wait_for_timeout(wait_ms)

        html = page.content()
        browser.close()

    result = trafilatura.extract(html, output_format=output_format, include_comments=True, include_links=True)
    if result is None:
        print("Error: trafilatura could not extract content from this page.", file=sys.stderr)
        sys.exit(1)

    print(result)


def main():
    parser = argparse.ArgumentParser(description="Fetch and extract clean text from web pages.")
    parser.add_argument("url", nargs="?", help="URL to fetch")
    parser.add_argument("--setup", action="store_true", help="Install Playwright browser binaries")
    parser.add_argument("--interactive", action="store_true", help="Open a visible browser for manual interaction")
    parser.add_argument("--format", choices=["txt", "markdown"], default="txt", help="Output format (default: txt)")
    parser.add_argument("--wait", type=int, default=2000, help="Extra wait time in ms after page load (default: 2000)")

    args = parser.parse_args()

    if args.setup:
        setup_browsers()
        return

    if not args.url:
        parser.print_help()
        sys.exit(1)

    fetch_page(args.url, interactive=args.interactive, wait_ms=args.wait, output_format=args.format)


if __name__ == "__main__":
    main()
