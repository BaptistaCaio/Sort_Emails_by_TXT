import re

def process_emails():
    print("Cole os e-mails copiados (pressione Enter duas vezes para finalizar):")
    email_text = "\n".join(iter(input, ""))
    
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, email_text)
    
    unique_emails = sorted(set(emails))
    
    formatted_emails = ", ".join(unique_emails)
    
    email_count = len(unique_emails)
    
    print("\nE-mails formatados:")
    print(formatted_emails)
    print(f"\nQuantidade de e-mails únicos: {email_count}")

if __name__ == "__main__":
    process_emails()
