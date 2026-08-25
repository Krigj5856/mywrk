#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Miner Automation - W1, W2, W3 (Terminals 1-90 Only)
W1: 1-30 | W2: 31-60 | W3: 61-90
"""

import os
import sys
import subprocess
import time
import argparse
import psutil
from datetime import datetime
from typing import Optional

def auto_install_dependencies():
    required = ['requests', 'psutil', 'pillow']
    for package in required:
        try:
            if package == 'pillow':
                __import__('PIL')
            else:
                __import__(package)
            print(f"[OK] {package} already installed")
        except ImportError:
            print(f"[*] Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"[OK] {package} installed")

auto_install_dependencies()

import requests
from PIL import ImageGrab

# ==================== TELEGRAM ====================
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8670890083:AAFdQaEiC67jmk6l8jxxdG01NTEN4JxvPUc")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "6955911349")

class TelegramLogger:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
    def send_message(self, message: str):
        try:
            requests.post(f"{self.base_url}/sendMessage", json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}, timeout=10)
        except:
            pass
    def send_photo(self, image_path: str, caption: str):
        try:
            with open(image_path, 'rb') as f:
                requests.post(f"{self.base_url}/sendPhoto", files={'photo': f}, data={'chat_id': TELEGRAM_CHAT_ID, 'caption': caption, 'parse_mode': 'HTML'}, timeout=30)
            os.remove(image_path)
        except:
            pass

telegram = TelegramLogger()

# ==================== CONFIG ====================
FIREFOX_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"
API_BASE = "https://api.unmineable.com/v5"
WALLET_ADDRESS = "nano_1g97x3h6wxd4h577p6dricapigs78ccc7tcowjfm67hewsmg7qob4xwc8jak"
COIN = "NANO"
BATCH_SIZE = 3
GAP_BETWEEN_BATCHES = 60
CHECK_INTERVAL = 360

# ==================== W1: TERMINALS 1-30 (UPDATED) ====================
W1_TERMINALS = [
    [1, "Terminal 1", "bzrgylhywt4jnzsogw5uxk", "https://ais-pre-bzrgylhywt4jnzsogw5uxk-873752325136.asia-east1.run.app"],
    [2, "Terminal 2", "7yyo6cnrmy5xqycdkaoi3j", "https://ais-pre-7yyo6cnrmy5xqycdkaoi3j-873752325136.asia-east1.run.app"],
    [3, "Terminal 3", "f6luhc6cnwisx5repjq7lb", "https://ais-pre-f6luhc6cnwisx5repjq7lb-873752325136.asia-east1.run.app"],
    [4, "Terminal 4", "2stdazrrylzstugmrhvrdu", "https://ais-pre-2stdazrrylzstugmrhvrdu-873752325136.asia-east1.run.app"],
    [5, "Terminal 5", "dav6su7ez2ab4n2icinoco", "https://ais-pre-dav6su7ez2ab4n2icinoco-873752325136.asia-east1.run.app"],
    [6, "Terminal 6", "l7wvh2iacntvck4jffby63", "https://ais-pre-l7wvh2iacntvck4jffby63-873752325136.asia-east1.run.app"],
    [7, "Terminal 7", "l44zoy33sf7hdxgl2kneuu", "https://ais-pre-l44zoy33sf7hdxgl2kneuu-873752325136.asia-east1.run.app"],
    [8, "Terminal 8", "u4lnaie3jsgyhn4u4tm6ha", "https://ais-pre-u4lnaie3jsgyhn4u4tm6ha-873752325136.asia-east1.run.app"],
    [9, "Terminal 9", "gazcocknx5za7xblikmosu", "https://ais-pre-gazcocknx5za7xblikmosu-873752325136.asia-east1.run.app"],
    [10, "Terminal 10", "qfespipye6xly7sciwngma", "https://ais-pre-qfespipye6xly7sciwngma-873752325136.asia-east1.run.app"],
    [11, "Terminal 11", "2te3b7r4vcuitr7z4t6j4b", "https://ais-pre-2te3b7r4vcuitr7z4t6j4b-873752325136.asia-east1.run.app"],
    [12, "Terminal 12", "k64ux4ildx2ysnc56div5y", "https://ais-pre-k64ux4ildx2ysnc56div5y-873752325136.asia-east1.run.app"],
    [13, "Terminal 13", "wsli3jmxwro35l3ta7pwq6", "https://ais-pre-wsli3jmxwro35l3ta7pwq6-873752325136.asia-east1.run.app"],
    [14, "Terminal 14", "rswbs7illoymrjsdncdebo", "https://ais-pre-rswbs7illoymrjsdncdebo-873752325136.asia-east1.run.app"],
    [15, "Terminal 15", "6pjlcfood2yy7q7takoe3u", "https://ais-pre-6pjlcfood2yy7q7takoe3u-873752325136.asia-east1.run.app"],
    [16, "Terminal 16", "vya4afunu5v643zh55w4ha", "https://ais-pre-vya4afunu5v643zh55w4ha-873752325136.asia-east1.run.app"],
    [17, "Terminal 17", "cwubd65vg2xygzekrfcqfa", "https://ais-pre-cwubd65vg2xygzekrfcqfa-873752325136.asia-east1.run.app"],
    [18, "Terminal 18", "yyf2ytbqlmsglqi76rcdoy", "https://ais-pre-yyf2ytbqlmsglqi76rcdoy-873752325136.asia-east1.run.app"],
    [19, "Terminal 19", "binm4b4uxvcyuicgwyebpu", "https://ais-pre-binm4b4uxvcyuicgwyebpu-873752325136.asia-east1.run.app"],
    [20, "Terminal 20", "56vt5dehrxtknmiej3mvcj", "https://ais-pre-56vt5dehrxtknmiej3mvcj-873752325136.asia-east1.run.app"],
    [21, "Terminal 21", "px2mkbgngsuv5qsj52b4go", "https://ais-pre-px2mkbgngsuv5qsj52b4go-873752325136.asia-east1.run.app"],
    [22, "Terminal 22", "tzgvtvxc23emtkkia2ij7c", "https://ais-pre-tzgvtvxc23emtkkia2ij7c-873752325136.asia-east1.run.app"],
    [23, "Terminal 23", "t6thueee3kmk7dl43o46mz", "https://ais-pre-t6thueee3kmk7dl43o46mz-873752325136.asia-east1.run.app"],
    [24, "Terminal 24", "mn3bht7xmokwclk6frl2un", "https://ais-pre-mn3bht7xmokwclk6frl2un-873752325136.asia-east1.run.app"],
    [25, "Terminal 25", "c3cm5vw7pcd4aboxgt4ks3", "https://ais-pre-c3cm5vw7pcd4aboxgt4ks3-873752325136.asia-east1.run.app"],
    [26, "Terminal 26", "3f44twzy4g7lhknuu5lwi3", "https://ais-pre-3f44twzy4g7lhknuu5lwi3-873752325136.asia-east1.run.app"],
    [27, "Terminal 27", "uprwn2xy3maujvfmhonive", "https://ais-pre-uprwn2xy3maujvfmhonive-873752325136.asia-east1.run.app"],
    [28, "Terminal 28", "otdnfhbgoq7s65ji3vbcyn", "https://ais-pre-otdnfhbgoq7s65ji3vbcyn-873752325136.asia-east1.run.app"],
    [29, "Terminal 29", "jzprcqbjhif2i7uykj7ycq", "https://ais-pre-jzprcqbjhif2i7uykj7ycq-873752325136.asia-east1.run.app"],
    [30, "Terminal 30", "sdkuosxe774h7d2dqhujwv", "https://ais-pre-sdkuosxe774h7d2dqhujwv-873752325136.asia-east1.run.app"],
]

# ==================== W2: TERMINALS 31-60 ====================
W2_TERMINALS = [
    [31, "Terminal 31", "l4nexpjplufhhrp3rg2mnr", "https://ais-pre-l4nexpjplufhhrp3rg2mnr-49332687696.asia-east1.run.app"],
    [32, "Terminal 32", "xrgbkmdurfjazearttecfg", "https://ais-pre-xrgbkmdurfjazearttecfg-49332687696.asia-east1.run.app"],
    [33, "Terminal 33", "r7cl5ikxlphlx2jnqfr4n3", "https://ais-pre-r7cl5ikxlphlx2jnqfr4n3-49332687696.asia-east1.run.app"],
    [34, "Terminal 34", "lmkapxey2y4blw6wv2dt5i", "https://ais-pre-lmkapxey2y4blw6wv2dt5i-49332687696.asia-east1.run.app"],
    [35, "Terminal 35", "ctceihay3r4nctd5gsps7y", "https://ais-pre-ctceihay3r4nctd5gsps7y-49332687696.asia-east1.run.app"],
    [36, "Terminal 36", "thtwvzhh6yapos3lglf5z3", "https://ais-pre-thtwvzhh6yapos3lglf5z3-49332687696.asia-east1.run.app"],
    [37, "Terminal 37", "pupk4rdctuhhkoxcb4ogoj", "https://ais-pre-pupk4rdctuhhkoxcb4ogoj-49332687696.asia-east1.run.app"],
    [38, "Terminal 38", "j53c3ev3l7r2bxzxt23kta", "https://ais-pre-j53c3ev3l7r2bxzxt23kta-49332687696.asia-east1.run.app"],
    [39, "Terminal 39", "ozd2yr57dcdy66vn25p6sa", "https://ais-pre-ozd2yr57dcdy66vn25p6sa-49332687696.asia-east1.run.app"],
    [40, "Terminal 40", "6cgwknlc2logtvfnkp5kv4", "https://ais-pre-6cgwknlc2logtvfnkp5kv4-49332687696.asia-east1.run.app"],
    [41, "Terminal 41", "pk4iomeemgbzyjdnrmzbls", "https://ais-pre-pk4iomeemgbzyjdnrmzbls-49332687696.asia-east1.run.app"],
    [42, "Terminal 42", "bi7j3jwv6bys5sukvgnrzs", "https://ais-pre-bi7j3jwv6bys5sukvgnrzs-49332687696.asia-east1.run.app"],
    [43, "Terminal 43", "waqj65qludc3ao6mzxkv67", "https://ais-pre-waqj65qludc3ao6mzxkv67-49332687696.asia-east1.run.app"],
    [44, "Terminal 44", "7a6bv6o77z65omxcamt3km", "https://ais-pre-7a6bv6o77z65omxcamt3km-49332687696.asia-east1.run.app"],
    [45, "Terminal 45", "65645qtry5k6oj4quvle37", "https://ais-pre-65645qtry5k6oj4quvle37-49332687696.asia-east1.run.app"],
    [46, "Terminal 46", "lkvnsbtsrygnajjz3lwbe3", "https://ais-pre-lkvnsbtsrygnajjz3lwbe3-49332687696.asia-east1.run.app"],
    [47, "Terminal 47", "npvl6zxgbscqc37qgqw27c", "https://ais-pre-npvl6zxgbscqc37qgqw27c-49332687696.asia-east1.run.app"],
    [48, "Terminal 48", "fop7mm76x54b5v2pffflv6", "https://ais-pre-fop7mm76x54b5v2pffflv6-49332687696.asia-east1.run.app"],
    [49, "Terminal 49", "pwmy5zemck42nwk7s5q7mq", "https://ais-pre-pwmy5zemck42nwk7s5q7mq-49332687696.asia-east1.run.app"],
    [50, "Terminal 50", "og2hwn7bgqphr7cbx67aov", "https://ais-pre-og2hwn7bgqphr7cbx67aov-49332687696.asia-east1.run.app"],
    [51, "Terminal 51", "nibfwx7hiujwhnvxngfwf2", "https://ais-pre-nibfwx7hiujwhnvxngfwf2-49332687696.asia-east1.run.app"],
    [52, "Terminal 52", "klggmabfw23vdwsy6s7jxs", "https://ais-pre-klggmabfw23vdwsy6s7jxs-49332687696.asia-east1.run.app"],
    [53, "Terminal 53", "x6qpsiogpaungpba2e7pu2", "https://ais-pre-x6qpsiogpaungpba2e7pu2-49332687696.asia-east1.run.app"],
    [54, "Terminal 54", "xdsf4csxxfhg5tlfc6qsil", "https://ais-pre-xdsf4csxxfhg5tlfc6qsil-49332687696.asia-east1.run.app"],
    [55, "Terminal 55", "jxgzbmqca4sgp4ntudicv7", "https://ais-pre-jxgzbmqca4sgp4ntudicv7-49332687696.asia-east1.run.app"],
    [56, "Terminal 56", "venezxj3puxss4zbtwyfis", "https://ais-pre-venezxj3puxss4zbtwyfis-49332687696.asia-east1.run.app"],
    [57, "Terminal 57", "dh73kbzauyvja2mnssed3q", "https://ais-pre-dh73kbzauyvja2mnssed3q-49332687696.asia-east1.run.app"],
    [58, "Terminal 58", "tjgjx6v3ej6cdiufclpnj2", "https://ais-pre-tjgjx6v3ej6cdiufclpnj2-49332687696.asia-east1.run.app"],
    [59, "Terminal 59", "npjgjawetbnhbxhrcxhpg2", "https://ais-pre-npjgjawetbnhbxhrcxhpg2-49332687696.asia-east1.run.app"],
    [60, "Terminal 60", "pbu7p6mipvtfehnac5dx5u", "https://ais-pre-pbu7p6mipvtfehnac5dx5u-49332687696.asia-east1.run.app"],
]

# ==================== W3: TERMINALS 61-90 ====================
W3_TERMINALS = [
    [61, "Terminal 61", "nuezgc4afy6sme62bew44z", "https://ais-pre-nuezgc4afy6sme62bew44z-628481697275.asia-east1.run.app"],
    [62, "Terminal 62", "m6ehhbbroys3q7kw5rx2us", "https://ais-pre-m6ehhbbroys3q7kw5rx2us-628481697275.asia-east1.run.app"],
    [63, "Terminal 63", "6txmhxwdigqnarocppeo6f", "https://ais-pre-6txmhxwdigqnarocppeo6f-628481697275.asia-east1.run.app"],
    [64, "Terminal 64", "kxueivdzgg7xwhebvdgzuh", "https://ais-pre-kxueivdzgg7xwhebvdgzuh-628481697275.asia-east1.run.app"],
    [65, "Terminal 65", "yg5c7gdhwoq6z6x7ijnets", "https://ais-pre-yg5c7gdhwoq6z6x7ijnets-628481697275.asia-east1.run.app"],
    [66, "Terminal 66", "zgx6y7v6fgja7l3z7cx3a7", "https://ais-pre-zgx6y7v6fgja7l3z7cx3a7-628481697275.asia-east1.run.app"],
    [67, "Terminal 67", "p2jk5xrt23lv24afpxn6g2", "https://ais-pre-p2jk5xrt23lv24afpxn6g2-628481697275.asia-east1.run.app"],
    [68, "Terminal 68", "hwck56pa5u43qof4pdkra5", "https://ais-pre-hwck56pa5u43qof4pdkra5-628481697275.asia-east1.run.app"],
    [69, "Terminal 69", "arekyqa2ndg4lri3d4hl2m", "https://ais-pre-arekyqa2ndg4lri3d4hl2m-628481697275.asia-east1.run.app"],
    [70, "Terminal 70", "spyxwjjhmovxmev7mbp6ns", "https://ais-pre-spyxwjjhmovxmev7mbp6ns-628481697275.asia-east1.run.app"],
    [71, "Terminal 71", "ppokruzg3enc4ixrvtnart", "https://ais-pre-ppokruzg3enc4ixrvtnart-628481697275.asia-east1.run.app"],
    [72, "Terminal 72", "mw6citgkmuyuhfy34hd6ee", "https://ais-pre-mw6citgkmuyuhfy34hd6ee-628481697275.asia-east1.run.app"],
    [73, "Terminal 73", "ky3xn2zjdoagdoax6kaop3", "https://ais-pre-ky3xn2zjdoagdoax6kaop3-628481697275.asia-east1.run.app"],
    [74, "Terminal 74", "ns7h4su4crebnwtzzywwbl", "https://ais-pre-ns7h4su4crebnwtzzywwbl-628481697275.asia-east1.run.app"],
    [75, "Terminal 75", "jlcv4m4m4hpsgt75wqdw6p", "https://ais-pre-jlcv4m4m4hpsgt75wqdw6p-628481697275.asia-east1.run.app"],
    [76, "Terminal 76", "x67qcwvbmayicnjpezdvwf", "https://ais-pre-x67qcwvbmayicnjpezdvwf-628481697275.asia-east1.run.app"],
    [77, "Terminal 77", "tmyhorjrnvoigikyutnnod", "https://ais-pre-tmyhorjrnvoigikyutnnod-628481697275.asia-east1.run.app"],
    [78, "Terminal 78", "yccxrvwl3qzmczyfcd3r57", "https://ais-pre-yccxrvwl3qzmczyfcd3r57-628481697275.asia-east1.run.app"],
    [79, "Terminal 79", "3x2sf36fuavp7ua3nsjpre", "https://ais-pre-3x2sf36fuavp7ua3nsjpre-628481697275.asia-east1.run.app"],
    [80, "Terminal 80", "yqeejrogmfdmkgfk4qndcp", "https://ais-pre-yqeejrogmfdmkgfk4qndcp-628481697275.asia-east1.run.app"],
    [81, "Terminal 81", "in5oh4p4n7nhxw7fpocnpv", "https://ais-pre-in5oh4p4n7nhxw7fpocnpv-628481697275.asia-east1.run.app"],
    [82, "Terminal 82", "r2fozdrksbcvr4qhpubosy", "https://ais-pre-r2fozdrksbcvr4qhpubosy-628481697275.asia-east1.run.app"],
    [83, "Terminal 83", "qqp4sdgsb6xorv3gxtci3x", "https://ais-pre-qqp4sdgsb6xorv3gxtci3x-628481697275.asia-east1.run.app"],
    [84, "Terminal 84", "lkbzclwmyfueh4al4przju", "https://ais-pre-lkbzclwmyfueh4al4przju-628481697275.asia-east1.run.app"],
    [85, "Terminal 85", "2mnhcbkxycofgb6c5cppin", "https://ais-pre-2mnhcbkxycofgb6c5cppin-628481697275.asia-east1.run.app"],
    [86, "Terminal 86", "jpczx7cncsd6cbscogopw3", "https://ais-pre-jpczx7cncsd6cbscogopw3-628481697275.asia-east1.run.app"],
    [87, "Terminal 87", "alh2dsvzhhul3rmgw7j4sv", "https://ais-pre-alh2dsvzhhul3rmgw7j4sv-628481697275.asia-east1.run.app"],
    [88, "Terminal 88", "7tqqdtn7xv5y74z54g6sfo", "https://ais-pre-7tqqdtn7xv5y74z54g6sfo-628481697275.asia-east1.run.app"],
    [89, "Terminal 89", "iulydxepty7epinwlovhis", "https://ais-pre-iulydxepty7epinwlovhis-628481697275.asia-east1.run.app"],
    [90, "Terminal 90", "uelstzyxoml33a672cjsjl", "https://ais-pre-uelstzyxoml33a672cjsjl-628481697275.asia-east1.run.app"],
]

# ==================== FUNCTIONS ====================
def log(msg): print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")
def send_tg(title, msg, emoji="📘"): telegram.send_message(f"{emoji} <b>{title}</b>\n{msg}")
def get_system_info():
    try:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        return f"CPU: {cpu}% | RAM: {ram.used/(1024**3):.1f}/{ram.total/(1024**3):.1f}GB ({ram.percent}%)"
    except:
        return "N/A"

def take_screenshot(filename="screenshot.png"):
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        return filename
    except:
        return None

def get_uuid():
    try:
        r = requests.get(f"{API_BASE}/address/{WALLET_ADDRESS}?coin={COIN}", headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        return r.json().get('data', {}).get('uuid')
    except:
        return None

def check_status(miner_name, uuid):
    try:
        r = requests.get(f"{API_BASE}/account/{uuid}/workers", headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        workers = r.json().get('data', {}).get('randomx', {}).get('workers', [])
        for w in workers:
            if w.get('name') == miner_name:
                return w.get('online', False)
        return False
    except:
        return False

def open_window(url, name):
    try:
        subprocess.Popen([FIREFOX_PATH, "-new-window", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def close_window(miner_name):
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if proc.info['name'] == 'firefox.exe' and miner_name in str(proc.info['cmdline']):
                proc.terminate()
                return True
    except:
        pass
    return False

def run_workflow(terminals, workflow_name):
    if not os.path.exists(FIREFOX_PATH):
        send_tg("ERROR", "Firefox not found!", "❌")
        return
    
    total = len(terminals)
    batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
    
    log(f"{workflow_name} Started | Total: {total}")
    send_tg("WORKFLOW STARTED", f"{workflow_name}\nTotal: {total}\n{get_system_info()}", "🚀")
    
    uuid = get_uuid()
    if not uuid:
        send_tg("ERROR", "Failed to get UUID!", "❌")
        return
    
    # Open first batch (for screenshot)
    log("Opening BATCH 1...")
    first_batch = terminals[0:BATCH_SIZE]
    for m in first_batch:
        open_window(m[3], m[1])
        time.sleep(2)
    
    time.sleep(30)
    ss = take_screenshot(f"screenshot_{workflow_name.replace(' ', '_')}.png")
    if ss:
        caption = f"📸 BATCH 1 SCREENSHOT\n{workflow_name}\n{get_system_info()}"
        telegram.send_photo(ss, caption)
    
    time.sleep(GAP_BETWEEN_BATCHES)
    
    # Open remaining batches
    for b in range(1, batches):
        start = b * BATCH_SIZE
        end = min(start + BATCH_SIZE, total)
        for m in terminals[start:end]:
            open_window(m[3], m[1])
            time.sleep(2)
        if end < total:
            time.sleep(GAP_BETWEEN_BATCHES)
    
    log("All terminals opened!")
    send_tg("ALL OPENED", f"All {total} terminals opened!\n{get_system_info()}", "✅")
    
    # Monitoring loop
    while True:
        time.sleep(CHECK_INTERVAL)
        offline, online = [], 0
        for m in terminals:
            if check_status(m[2], uuid):
                online += 1
            else:
                offline.append(m)
        
        if offline:
            send_tg(f"STATUS - {len(offline)} OFFLINE", f"{workflow_name}: {online}/{total} ONLINE\n{get_system_info()}", "⚠️")
            for m in offline:
                close_window(m[2])
                time.sleep(2)
                open_window(m[3], m[1])
                time.sleep(3)
            send_tg("RESTART COMPLETE", f"Restarted {len(offline)} miners", "✅")
        else:
            send_tg("STATUS - ALL ONLINE", f"{workflow_name}: {online}/{total} ONLINE (100%)\n{get_system_info()}", "✅")

# ==================== MAIN ====================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--workflow', type=str, default='W1')
    args = parser.parse_args()
    
    if args.workflow == 'W1':
        run_workflow(W1_TERMINALS, "W1 (1-30)")
    elif args.workflow == 'W2':
        run_workflow(W2_TERMINALS, "W2 (31-60)")
    elif args.workflow == 'W3':
        run_workflow(W3_TERMINALS, "W3 (61-90)")
    else:
        print("Use --workflow W1, W2, or W3")
