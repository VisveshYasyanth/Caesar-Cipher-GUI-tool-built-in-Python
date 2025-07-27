# 🛡️ PixelVault - Image Encryption Tool

A beautiful Python GUI application that encrypts and decrypts images using **Swap-based** and **XOR-based (Math)** methods. Built with `tkinter` and `Pillow`.

> 🎨 Stylish UI • 🔐 Image Security • 🧠 Beginner-Friendly

---

## ✨ Features

- 🔐 Encrypt and Decrypt Images  
- 🔁 Two Modes: `Swap` and `Math (XOR)`  
- 🖼️ View image preview  
- 🧠 Easy-to-use GUI built with `tkinter`  
- 💾 Swap encryption saves key data for perfect decryption  

---

## 🧠 How It Works

### 🔁 Swap Encryption:
Randomly swaps pixel positions using a numeric key.  
A `.swp` file is saved to reverse the encryption.

### ✖️ XOR Math Encryption:
Each pixel value is XORed with the key — simple and effective.  
Same function used for encryption & decryption.

---

## 🧪 Usage

1. Run the app:
   ```bash
   python pixel_vault.py
