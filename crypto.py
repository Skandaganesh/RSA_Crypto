from rich.console import Console
from rich.progress import track
from rich.table import Table
import random, time

console = Console()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_prime():
    primes = [x for x in range(100, 300) if is_prime(x)]
    return random.choice(primes)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(e, phi):
    m0, x0, x1 = phi, 0, 1
    while e > 1:
        q = e // phi
        e, phi = phi, e % phi
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keys():
    console.rule("[bold green]RSA Key Generation")
    for _ in track(range(10), description="Generating primes..."):
        time.sleep(0.05)

    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()

    n = p * q
    phi = (p-1)*(q-1)

    e = 3
    while gcd(e, phi) != 1:
        e += 2

    d = modinv(e, phi)

    table = Table(title="🔐 Key Details")
    table.add_column("Name", style="cyan")
    table.add_column("Value", style="magenta")
    table.add_row("p", str(p))
    table.add_row("q", str(q))
    table.add_row("n", str(n))
    table.add_row("phi(n)", str(phi))
    table.add_row("e (public key)", str(e))
    table.add_row("d (private key)", str(d))
    console.print(table)

    return (e, n), (d, n)


def encrypt_text(text, public_key):
    e, n = public_key
    return [pow(ord(ch), e, n) for ch in text]

def save_encrypted(cipher, filename="encrypted.enc"):
    with open(filename, "w") as f:
        f.write(" ".join(map(str, cipher)))
    console.print(f"[bold green]Encrypted file saved as {filename}")


def load_encrypted(filename="encrypted.enc"):
    with open(filename, "r") as f:
        cipher = list(map(int, f.read().split()))
    return cipher

def decrypt(cipher, private_key):
    d, n = private_key
    return ''.join([chr(pow(c, d, n)) for c in cipher])

def save_decrypted(text, filename="decrypted.dec.txt"):
    with open(filename, "w") as f:
        f.write(text)
    console.print(f"[bold green]Decrypted file saved as {filename}")


def main():
    console.rule("[bold blue]📂 RSA Text Encryptor")

    public_key, private_key = generate_keys()

    with open("input.txt", "r") as f:
        original_text = f.read()

    console.print(f"\n[bold]Original Text:[/] {original_text[:50]}...")

    console.rule("[bold yellow]Encrypting...")
    cipher = encrypt_text(original_text, public_key)
    save_encrypted(cipher)

    console.rule("[bold yellow]Decrypting...")
    decrypted = decrypt(cipher, private_key)
    save_decrypted(decrypted)

    console.print(f"\n[bold]Decrypted Preview:[/] {decrypted[:50]}...")

if __name__ == "__main__":
    main()
