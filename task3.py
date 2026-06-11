import re
import os

# TASK 3: Task Automation — Extract Emails
#         from a .txt file — CodeAlpha


def extract_emails(input_file):
    """Read a .txt file and extract all email addresses using regex."""

    if not os.path.exists(input_file):
        print(f"\n❌ Error: File '{input_file}' not found.")
        return []

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex pattern to match valid email addresses
    email_pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, content)

    # Remove duplicates while preserving order
    seen = set()
    unique_emails = []
    for email in emails:
        if email.lower() not in seen:
            seen.add(email.lower())
            unique_emails.append(email)

    return unique_emails


def save_emails(emails, output_file):
    """Save extracted emails to an output file."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Extracted Emails ({len(emails)} found)\n")
        f.write("=" * 40 + "\n")
        for i, email in enumerate(emails, 1):
            f.write(f"{i:>3}. {email}\n")
    print(f"\n✅ Emails saved to '{output_file}'")


def display_emails(emails):
    """Print emails to console in a formatted table."""
    print("\n" + "=" * 50)
    print("       📧  EXTRACTED EMAIL ADDRESSES")
    print("=" * 50)
    if not emails:
        print("  ⚠️  No email addresses found in the file.")
    else:
        for i, email in enumerate(emails, 1):
            print(f"  {i:>3}. {email}")
    print("=" * 50)
    print(f"  Total found: {len(emails)} email(s)")
    print("=" * 50)


def create_sample_file():
    """Create a sample input file for demo purposes."""
    sample_content = """Hello Team,

Please contact the following people for the project:

- Project Manager: alice.johnson@company.com
- Developer Lead: bob.smith@techcorp.org
- Designer: carol.white@design.io
- QA Engineer: david.brown@testing.net
- Client Contact: eve.martin@client.co.in

For support queries, reach out to support@codealpha.tech
or services.codealpha@gmail.com

Old emails (duplicates for testing):
alice.johnson@company.com
bob.smith@techcorp.org

Invalid ones (should NOT be extracted):
notanemail
missing@
@nodomain.com
just.text.here

Regards,
Team CodeAlpha
info@codealpha.tech
"""
    with open("sample_emails.txt", "w") as f:
        f.write(sample_content)
    print("✅ Created 'sample_emails.txt' for demo.")


def main():
    print("\n" + "=" * 50)
    print("  📧  EMAIL EXTRACTOR — CodeAlpha Internship")
    print("=" * 50)

    print("\nOptions:")
    print("  1. Use your own .txt file")
    print("  2. Create & use a sample file (demo)")
    choice = input("\nChoose (1/2): ").strip()

    if choice == "2":
        create_sample_file()
        input_file = "sample_emails.txt"
    else:
        input_file = input("\nEnter the path to your .txt file: ").strip()
        if not input_file:
            print("⚠️  No file path entered. Exiting.")
            return

    print(f"\n🔍 Scanning '{input_file}' for email addresses...")
    emails = extract_emails(input_file)
    display_emails(emails)

    if emails:
        save_choice = input("\n💾 Save extracted emails to a file? (yes/no): ").strip().lower()
        if save_choice in ("yes", "y"):
            output_file = input("   Output filename (default: extracted_emails.txt): ").strip()
            if not output_file:
                output_file = "extracted_emails.txt"
            save_emails(emails, output_file)

    print("\n👋 Done! Thank you for using Email Extractor.\n")


if __name__ == "__main__":
    main()