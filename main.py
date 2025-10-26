import json

input_file = "sites.txt"
output_file = "sites.json"

results = []
current_group = None
group_counter = {}

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        if line.startswith("#"):
            current_group = line.lstrip("#").strip()
            group_counter[current_group] = 0
            continue

        if current_group:
            group_counter[current_group] += 1
            hostname = f"{current_group} ({group_counter[current_group]})"
        else:
            hostname = None

        results.append({
            "hostname": line,
            "ip": hostname
        })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print(f"Done. Created file {output_file} with {len(results)} sites.")
