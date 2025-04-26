import click

@click.command()
@click.option('--name', prompt='Your name', help='Your full name.')
@click.option('--email', prompt='Your email', help='Your email address.')
@click.option('--message', prompt='Your message', help='Your message or inquiry.')
def contact(name, email, message):
    """
    Command to collect user contact information and message.
    """
    
    print("\nThank you for reaching out to FastAnime!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    print("\nWe will get back to you as soon as possible.")

if __name__ == '__main__':
    contact()