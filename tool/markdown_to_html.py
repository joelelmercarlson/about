# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "markdown>=3.10.1",
# ]
# ///
import markdown
import sys
import os

__author__  = "Joel E Carlson"
__credits__ = [ "joel.elmer.carlson@outlook.com" ]
__email__   = __credits__[0]

def markdown_to_html(md_text: str) -> str:
    """
    Convert Markdown text to HTML.
    """
    if not isinstance(md_text, str):
        raise TypeError("Markdown input must be a string.")
    return markdown.markdown(md_text, extensions=["extra", "toc", "tables"])

def convert_file(md_file_path: str, output_html_path: str):
    """
    Convert a Markdown file to an HTML file.
    """
    if not os.path.isfile(md_file_path):
        raise FileNotFoundError(f"Markdown file not found: {md_file_path}")

    with open(md_file_path, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()

    html_header = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>loki</title>
    </head>
    """
    html_footer = """</body></html>"""

    html_content = markdown_to_html(md_content)

    with open(output_html_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_header + html_content + html_footer)

    print(f"- HTML file created: {output_html_path}")

if __name__ == "__main__":
    # Example usage from command line:
    # python md_to_html.py input.md output.html
    if len(sys.argv) == 3:
        convert_file(sys.argv[1], sys.argv[2])
    else:
        # Example inline conversion
        sample_md = """
# Hello World
This is **Markdown** converted to HTML.

- Item 1
- Item 2

[Click here](http://loki.jharris.com)
"""
        print(markdown_to_html(sample_md))

