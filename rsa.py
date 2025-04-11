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

    console.print("[bold blue]Step 1:[/] Choose two primes p and q")
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()
    console.print(f"Chosen primes: p = {p}, q = {q}\n")

    console.print("[bold blue]Step 2:[/] Compute n = p * q and φ(n) = (p-1)*(q-1)")
    n = p * q
    phi = (p - 1) * (q - 1)
    console.print(f"n = p × q = {p} × {q} = {n}")
    console.print(f"φ(n) = (p - 1) × (q - 1) = ({p - 1}) × ({q - 1}) = {phi}\n")

    console.print("[bold blue]Step 3:[/] Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1")
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    console.print(f"Chosen e = {e}, since gcd({e}, {phi}) = 1\n")

    console.print("[bold blue]Step 4:[/] Compute d such that d ≡ e⁻¹ mod φ(n)")
    d = modinv(e, phi)
    console.print(f"Computed d such that (d × e) % φ(n) = 1")
    console.print(f"d = {d}, because ({d} × {e}) % {phi} = {(d * e) % phi}\n")

    console.print("[bold blue]Step 5:[/] Final Keys")
    table = Table(title="🔐 RSA Key Components")
    table.add_column("Key", style="cyan", justify="right")
    table.add_column("Value", style="magenta")
    table.add_row("Public Key (e, n)", f"({e}, {n})")
    table.add_row("Private Key (d, n)", f"({d}, {n})")
    console.print(table)

    return (e, n), (d, n)

def encrypt_text(text, public_key):
    e, n = public_key
    console.print("[bold cyan]🔐 Visualizing Encryption (First 10 characters):")

    preview = text[:10]
    preview_encrypted = []

    for ch in track(preview, description="Encrypting..."):
        time.sleep(0.5)
        m = ord(ch)
        c = pow(m, e, n)
        console.print(f"[bold]{ch}[/] → ASCII {m} → Encrypted as (m^e mod n) = ({m}^{e} mod {n}) = {c}")
        preview_encrypted.append(c)

    remaining_encrypted = [pow(ord(ch), e, n) for ch in text[10:]]
    return preview_encrypted + remaining_encrypted

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
    console.print("[bold cyan]🔓 Visualizing Decryption (First 10 characters):")

    preview = cipher[:10]
    preview_decrypted = []

    for c in track(preview, description="Decrypting..."):
        time.sleep(0.5)
        m = pow(c, d, n)
        ch = chr(m)
        console.print(f"Encrypted {c} → Decrypted as (c^d mod n) = ({c}^{d} mod {n}) = {m} → [bold]{ch}[/]")
        preview_decrypted.append(ch)

    remaining_decrypted = [chr(pow(c, d, n)) for c in cipher[10:]]
    return ''.join(preview_decrypted) + ''.join(remaining_decrypted)

def save_decrypted(text, filename="decrypted.dec.txt"):
    with open(filename, "w") as f:
        f.write(text)
    console.print(f"[bold green]Decrypted file saved as {filename}")

def main():
    console.rule("[bold blue]📂 RSA Text Encryptor")

    public_key, private_key = generate_keys()

    with open("input.txt", "r") as f:
        original_text = f.read()

    console.print(f"\n[bold]Original Text Preview:[/] {original_text[:50]}...")

    console.rule("[bold yellow]Encrypting...")
    time.sleep(2)
    cipher = encrypt_text(original_text, public_key)
    save_encrypted(cipher)
    console.rule("[bold yellow]Decrypting...")
    time.sleep(2)
    decrypted = decrypt(cipher, private_key)
    save_decrypted(decrypted)

    console.print(f"\n[bold]Decrypted Preview:[/] {decrypted[:50]}...")

if __name__ == "__main__":
    main()
