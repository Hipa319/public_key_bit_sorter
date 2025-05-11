# Public Key Bit Sorter

This tool sorts ECDSA uncompressed public keys (format `04...`, 130 characters) into separate files based on their effective bit lengths. Four different bit-counting strategies are supported to analyze the entropy or structure of public keys.

---

## 📊 Bit-Counting Methods Comparison

| Method             | Description                                                              | Usefulness                                                     |
|--------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------|
| **1. Classic**     | Total bits = HEX length × 4                                               | Basic structural grouping; includes all leading zeroes         |
| **2. Dynamic**     | Sum of X + Y binary lengths, skipping leading `0`s                        | Realistic entropy measure; ideal for detecting weak keys       |
| **3. Legacy**      | MAX of X or Y HEX length (no leading `0`s), × 4                           | Crude but fast; good for identifying dominant coordinate       |
| **4. Binary-Max**  | MAX of X or Y binary bit length (no leading `0`s)                         | Most accurate per-coordinate entropy estimation                |

---

## ⚙️ Features

- Supports 4 key analysis methods
- Uses `multiprocessing` for fast sorting
- `tqdm` progress bar
- Automatically writes grouped keys to `output/` folder
- Compatible with Linux and Windows (`clear` / `cls`)

---

## 🧪 Requirements

Install required Python dependency:

```bash
pip install tqdm
```

## 📂 Usage (Terminal)

```bash
python3 public_key_bit_sorter.py
```

Follow the interactive prompts:
1. Input file name (default: `publickeys.txt`)
2. Choose bit-counting method (1–4)
3. Select number of CPU threads

Grouped keys will be saved in files like:
```
output/publickeys_256bit.txt
output/publickeys_253bit.txt
...
```

---

## 📜 License

MIT License — see [LICENSE](LICENSE)

---

## ⚠️ Disclaimer

- 🚫 This software is for **educational use only**
- ⚠️ Do not use it with real cryptocurrency addresses / key pairs
- ❗️ The author takes no responsibility for damage or misuse
- 🛡️ Use responsibly and at your own risk

---

## 🏱 Support

⭐ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

⭐ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

⭐ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

🫐 We also appreciate older privacy coins like **Bytecoin (BCN)**  
`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

🙏 *Thank you for supporting independent research and ethical technology.*

---

Created with dedication to education, blockchain analysis, and ethical research.  
*“I morph bits not to break, but to understand.” — BitMorphX*
