"""
Command-line interface for Cinematic Prompt Formatter.
"""

import argparse
import csv
import sys
from typing import List, Optional

from formatter.formatter import format_prompt, format_batch
from formatter.presets import list_presets, get_preset_names


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        prog="cpf",
        description="Cinematic Prompt Formatter - Translate cinematic language into AI prompts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  cpf format "dolly in, rim light, cyberpunk mood"
  cpf format "anamorphic lens, noir lighting" --model flux
  cpf batch input.csv --output formatted.csv
  cpf presets
  cpf search neon
  cpf terms
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Format command
    format_parser = subparsers.add_parser(
        "format",
        help="Format a cinematic description into an AI prompt",
    )
    format_parser.add_argument(
        "description",
        help="Cinematic description to format",
    )
    format_parser.add_argument(
        "--model", "-m",
        choices=["sdxl", "flux", "sd15"],
        default="sdxl",
        help="Target model (default: sdxl)",
    )
    format_parser.add_argument(
        "--style", "-s",
        help="Preset style to apply",
    )
    format_parser.add_argument(
        "--list-styles",
        action="store_true",
        help="List available styles",
    )

    # Batch command
    batch_parser = subparsers.add_parser(
        "batch",
        help="Batch format cinematic descriptions from a CSV file",
    )
    batch_parser.add_argument(
        "input",
        help="Input CSV file with 'description' column",
    )
    batch_parser.add_argument(
        "--output", "-o",
        help="Output CSV file (default: stdout)",
    )
    batch_parser.add_argument(
        "--model", "-m",
        choices=["sdxl", "flux", "sd15"],
        default="sdxl",
        help="Target model (default: sdxl)",
    )
    batch_parser.add_argument(
        "--style", "-s",
        help="Preset style to apply",
    )

    # Presets command
    subparsers.add_parser(
        "presets",
        help="List available preset styles",
    )

    # Terms command
    terms_parser = subparsers.add_parser(
        "terms",
        help="List available cinematic terms",
    )
    terms_parser.add_argument(
        "--category", "-c",
        choices=["lens", "lighting", "camera", "mood", "color"],
        help="Filter by category",
    )

    # Search command
    search_parser = subparsers.add_parser(
        "search",
        help="Search for cinematic terms",
    )
    search_parser.add_argument(
        "query",
        help="Search query",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "format":
        handle_format(args)
    elif args.command == "batch":
        handle_batch(args)
    elif args.command == "presets":
        handle_presets()
    elif args.command == "terms":
        handle_terms(args)
    elif args.command == "search":
        handle_search(args)


def handle_format(args):
    """Handle the format command."""
    if args.list_styles:
        handle_presets()
        return

    result = format_prompt(
        args.description,
        style=args.style,
        model=args.model,
    )
    print(result)


def handle_batch(args):
    """Handle the batch command."""
    try:
        with open(args.input, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if "description" not in reader.fieldnames:
                print("Error: Input CSV must have a 'description' column", file=sys.stderr)
                sys.exit(1)

            descriptions = [row["description"] for row in reader]

        results = format_batch(
            descriptions,
            style=args.style,
            model=args.model,
        )

        if args.output:
            with open(args.output, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["description", "formatted_prompt"])
                for desc, result in zip(descriptions, results):
                    writer.writerow([desc, result])
            print(f"Formatted {len(results)} prompts to {args.output}")
        else:
            for desc, result in zip(descriptions, results):
                print(f"{desc} -> {result}")

    except FileNotFoundError:
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def handle_presets():
    """Handle the presets command."""
    presets = list_presets()
    print("Available presets:")
    print("-" * 60)
    for name, desc in presets.items():
        print(f"  {name:25} {desc}")
    print("-" * 60)
    print(f"Total: {len(presets)} presets")


def handle_terms(args):
    """Handle the terms command."""
    from formatter.mapper import get_all_terms

    terms = get_all_terms()

    if args.category:
        if args.category in terms:
            print(f"Available {args.category} terms:")
            print("-" * 60)
            for term in sorted(terms[args.category]):
                print(f"  {term}")
            print("-" * 60)
            print(f"Total: {len(terms[args.category])} terms")
        else:
            print(f"Unknown category: {args.category}")
    else:
        print("Available cinematic terms by category:")
        print("=" * 60)
        for category, category_terms in sorted(terms.items()):
            print(f"\n{category.upper()}")
            print("-" * 60)
            for term in sorted(category_terms):
                print(f"  {term}")
            print(f"\n  ({len(category_terms)} terms)")
        print("=" * 60)
        total = sum(len(t) for t in terms.values())
        print(f"Total: {total} terms")


def handle_search(args):
    """Handle the search command."""
    from formatter.mapper import search_terms as mapper_search

    results = mapper_search(args.query)

    if results:
        print(f"Search results for '{args.query}':")
        print("-" * 60)
        for category, matches in results.items():
            print(f"\n{category.upper()}:")
            for match in matches:
                print(f"  {match}")
        total = sum(len(m) for m in results.values())
        print("-" * 60)
        print(f"Found {total} matches")
    else:
        print(f"No results found for '{args.query}'")


if __name__ == "__main__":
    main()