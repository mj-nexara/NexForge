# core/config.py
import json
import os

CONFIG_FILE = "nexforge_config.json"

default_config = {
    "offline_mode": True,
    "logging_level": "info",
    "enable_ipfs": True,
    "use_did": True
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(default_config)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
