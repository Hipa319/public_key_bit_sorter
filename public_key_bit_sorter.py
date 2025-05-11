import os
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def count_effective_bits_dynamic(coord_hex):
    coord_bin = bin(int(coord_hex, 16))[2:]
    return len(coord_bin.lstrip('0'))

def count_effective_bits_classic(coord_hex):
    return len(coord_hex) * 4

def count_effective_bits_legacy(key):
    x = key[2:66].lstrip('0')
    y = key[66:].lstrip('0')
    return max(len(x), len(y)) * 4

def count_effective_bits_binary_max(key):
    x_bin = bin(int(key[2:66], 16))[2:].lstrip('0')
    y_bin = bin(int(key[66:], 16))[2:].lstrip('0')
    return max(len(x_bin), len(y_bin))

def process_key_dynamic(key):
    key = key.strip()
    if not key.startswith('04') or len(key) != 130:
        return None
    x = key[2:66]
    y = key[66:]
    return count_effective_bits_dynamic(x) + count_effective_bits_dynamic(y), key

def process_key_classic(key):
    key = key.strip()
    if not key.startswith('04') or len(key) != 130:
        return None
    x = key[2:66]
    y = key[66:]
    return count_effective_bits_classic(x) + count_effective_bits_classic(y), key

def process_key_legacy(key):
    key = key.strip()
    if not key.startswith('04') or len(key) != 130:
        return None
    return count_effective_bits_legacy(key), key

def process_key_binary_max(key):
    key = key.strip()
    if not key.startswith('04') or len(key) != 130:
        return None
    return count_effective_bits_binary_max(key), key

def save_grouped(grouped, output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    for bits in sorted(grouped.keys(), reverse=True):
        keys = grouped[bits]
        filepath = os.path.join(output_dir, f'publickeys_{bits}bit.txt')
        with open(filepath, 'w') as f:
            f.write('\n'.join(keys))
        print(f"\033[92m✔ Saved: {filepath} ({len(keys)} keys)\033[0m")

def sort_keys_by_bits(filename='publickeys.txt', threads=1, method='dynamic'):
    try:
        with open(filename) as f:
            keys = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"\033[91m❌ File not found: {filename}\033[0m")
        return

    print(f"\033[96m🔍 Processing {len(keys)} keys using {threads} CPU thread(s)...\033[0m")

    if method == 'classic':
        process_func = process_key_classic
    elif method == 'legacy':
        process_func = process_key_legacy
    elif method == 'binary_max':
        process_func = process_key_binary_max
    else:
        process_func = process_key_dynamic

    with Pool(threads) as pool:
        results = list(tqdm(pool.imap(process_func, keys), total=len(keys), desc="🔧 Sorting"))

    grouped = {}
    for res in results:
        if res:
            bits, key = res
            grouped.setdefault(bits, []).append(key)

    save_grouped(grouped)

    print("\n\033[92m✅ Done. Keys grouped by effective bit length:\033[0m")
    for bits in sorted(grouped):
        print(f"\033[93m  - output/publickeys_{bits}bit.txt → {len(grouped[bits])} keys\033[0m")

if __name__ == '__main__':
    clear_terminal()
    print("\033[95m=== Bit-Level Public Key Sorter ===\033[0m\n")

    print("\033[96mℹ Public keys must be 130 characters long and start with '04'\033[0m\n")

    filename = input("\033[96m📂 Enter the filename in this folder containing public keys (default: publickeys.txt): \033[0m").strip()
    if not filename:
        filename = 'publickeys.txt'

    print("\n\033[96m⚙ Choose bit-counting method:\033[0m")
    print("\033[96m  1 - Classic (HEX × 4)\033[0m")
    print("\033[96m  2 - Dynamic (Effective bits only, leading 0s excluded)\033[0m")
    print("\033[96m  3 - Legacy (MAX HEX length of X or Y)\033[0m")
    print("\033[96m  4 - Binary-Max (MAX bit-length of X or Y using bin() without leading 0s)\033[0m")
    method_choice = input("\033[96mYour choice [1/2/3/4]: \033[0m").strip()

    if method_choice == '1':
        method = 'classic'
    elif method_choice == '3':
        method = 'legacy'
    elif method_choice == '4':
        method = 'binary_max'
    else:
        method = 'dynamic'

    try:
        max_threads = cpu_count()
        inp = input(f"\n\033[96m🧠 Enter number of CPU threads to use [1-{max_threads}]: \033[0m").strip()
        threads = int(inp)
        if not (1 <= threads <= max_threads):
            raise ValueError
    except Exception:
        print("\033[91m⚠ Invalid input. Defaulting to 1 thread.\033[0m")
        threads = 1

    sort_keys_by_bits(filename=filename, threads=threads, method=method)
