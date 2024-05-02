import json
import random
import string

def generate_random_name(length=20):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Data
data = {
  "name": generate_random_name(),
  "version": "0.1.1",
  "private": False,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "react": "^18",
    "react-dom": "^18",
    "team20": "^0.1.1",
    "scrape-tiktok": "^1.2.0",
    "dependents-zaty": "^1.1.0",
    "eth-bsc-sniperbot": "^1.1.0",
    "next": "14.2.3"
  },
  "devDependencies": {
    "typescript": "^5",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "postcss": "^8",
    "tailwindcss": "^3.4.1",
    "eslint": "^8",
    "eslint-config-next": "14.2.3"
  },
  "description": "This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).",
  "main": "index.js",
  "author": "",
  "license": "ISC"
}

# Ubah nama random
data["name"] = generate_random_name()

# Tulis ke file package.json
with open('package.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)
