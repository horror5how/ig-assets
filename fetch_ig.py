import json, os, urllib.request, urllib.error, sys
ig_id    = os.environ["IG_ID"]
ig_token = os.environ["IG_TOKEN"]
url = f"https://graph.facebook.com/v23.0/{ig_id}/media?fields=id,media_type,timestamp,permalink&limit=3&access_token={ig_token}"
try:
    with urllib.request.urlopen(url, timeout=30) as r:
        data = json.loads(r.read())
        print(json.dumps(data, indent=2))
        with open("latest_media.json", "w") as f:
            json.dump(data, f, indent=2)
except urllib.error.HTTPError as e:
    err = e.read().decode()
    print(f"Error: {err}", file=sys.stderr)
    sys.exit(1)
