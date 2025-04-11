# RSA_Crypto
# 🔐 RSA Text Encryptor (Terminal-based)

A Python CLI tool that demonstrates RSA encryption and decryption with rich terminal visualization. Built with the [`rich`](https://github.com/Textualize/rich) library for colorful output, this script:
- Generates RSA keys
- Encrypts a text file (`input.txt`)
- Saves the encrypted data
- Decrypts it back to original
- Displays key steps with animations

---

## 📁 Project Structure

```
rsa_encryptor/
├── input.txt           # Text file to encrypt
├── encrypted.enc.txt       # Output: Encrypted text (numeric form)
├── decrypted.dec.txt   # Output: Decrypted plaintext
├── rsa.py             # RSA logic with rich visuals
```

---

## ⚙️ Requirements

- Python 3.7+
- `rich` (install via pip)

```bash
pip install rich
```

---

## 🚀 How to Run

1. **Prepare your input**  
   Edit or create a file named `input.txt` with the text you want to encrypt.

2. **Run the script**

```bash
python rsa.py
```

3. **See the results**
   - 📜 RSA key generation with colorful breakdown
   - 🔐 First 10 characters visualized during encryption
   - 🔓 First 10 characters visualized during decryption
   - 💾 Files `encrypted.enc.txt` and `decrypted.dec.txt` are saved automatically

---

## ✨ Features

- ✅ RSA key generation with `p`, `q`, `n`, `ϕ(n)`, `e`, `d` breakdown
- ✅ Interactive encryption/decryption visualization (first 10 chars)
- ✅ Uses `pow(m, e, n)` and `pow(c, d, n)` for modular arithmetic
- ✅ Stylish and animated using `rich.console`, `rich.table`, and `rich.progress`

---

## 📷 Example Terminal Output

```
─────────────────────────────
         📂 RSA Text Encryptor
─────────────────────────────

Step 1: Choose two primes p and q
Chosen primes: p = 113, q = 179

Step 2: Compute n and φ(n)
n = 20227, φ(n) = 19936

Step 3: Choose e such that gcd(e, φ(n)) = 1
e = 7

Step 4: Compute d such that d × e ≡ 1 mod φ(n)
d = 17023

🔐 Visualizing Encryption:
H → ASCII 72 → (72^7 mod 20227) = 8452
...

🔓 Visualizing Decryption:
8452 → (8452^17023 mod 20227) = 72 → H
...
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.