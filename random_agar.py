import random
import shutil
from pathlib import Path

# --- Config ---
SOURCE_DIR = Path(r"E:\AGAR_dataset\AGAR_dataset\dataset")
TARGET_DIR = Path("AGAR_data")
SEED = 42  # for reproducibility
TOTAL_SAMPLES = 10


# Countable ID ranges per type (inclusive)
COUNTABLE_RANGES = {
    "bright":           (309,   1302),
    "dark":             (2712,  8709),
    "vague":            (11761, 12617),
    "lower-resolution": (12994, 17417),
}


random.seed(SEED)
TARGET_DIR.mkdir(parents=True, exist_ok=True)

# Collect valid IDs per type
valid_ids_per_type = {}
for type_name, (start, end) in COUNTABLE_RANGES.items():
    valid_ids_per_type[type_name] = [
        i for i in range(start, end + 1)
        if (SOURCE_DIR / f"{i}.jpg").exists()
        and (SOURCE_DIR / f"{i}.json").exists()
    ]
    print(f"{type_name}: {len(valid_ids_per_type[type_name])} available")

# --- Allocate samples per type ---
# Step 1: guarantee 1 per type
allocation = {t: 1 for t in COUNTABLE_RANGES}
remaining = TOTAL_SAMPLES - len(COUNTABLE_RANGES)

# Step 2: distribute remaining slots proportionally to pool size
total_pool = sum(len(ids) for ids in valid_ids_per_type.values())
proportional = {
    t: remaining * len(ids) / total_pool
    for t, ids in valid_ids_per_type.items()
}
# Floor each, then hand out leftover slots to types with largest fractional remainder
for t, p in proportional.items():
    allocation[t] += int(p)

leftover = TOTAL_SAMPLES - sum(allocation.values())
fractional_parts = sorted(
    proportional.items(),
    key=lambda kv: kv[1] - int(kv[1]),
    reverse=True,
)
for t, _ in fractional_parts[:leftover]:
    allocation[t] += 1

print(f"\nAllocation: {allocation}")

# --- Sample and copy ---
sampled_all = {}
for type_name, n in allocation.items():
    pool = valid_ids_per_type[type_name]
    n = min(n, len(pool))
    sampled = random.sample(pool, n)
    sampled_all[type_name] = sorted(sampled)

    for img_id in sampled:
        for ext in (".jpg", ".json"):
            src = SOURCE_DIR / f"{img_id}{ext}"
            dst = TARGET_DIR / f"{img_id}{ext}"
            shutil.copy2(src, dst)

print(f"\n[✓] Copied {sum(len(v) for v in sampled_all.values())} image+label pairs")
for t, ids in sampled_all.items():
    print(f"  {t}: {ids}")
print(f"\nOutput folder: {TARGET_DIR.resolve()}")