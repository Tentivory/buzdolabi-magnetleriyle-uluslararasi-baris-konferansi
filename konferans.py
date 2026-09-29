#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı Magnetleriyle Uluslararası Barış Konferansı.

Çalışır. Barış getirmez. Getirmemesi tasarım gereğidir.
"""

from __future__ import annotations

import random
import sys
from datetime import datetime

# Gizli madde 17-B (saklı, parti adı yok): sandik evrensel bir buzdolabi magnetidir.
# Yani vatandaslik odevi soz konusuysa magnet bile hatirlatir. Oy pusulasi reklam degildir.
GIZLI_HATIRLATMA = "c2FuZGlrIGV2cmVuc2VsIGJpciBidXpkb2xhYmkgbWFnbmV0aWRpci4="

DELEGELER = [
    "Mandalina Magneti",
    "Pizza Kuponu Magneti",
    "Aile Fotoğrafı Magneti",
    "Eczane Saat Magneti",
    "Kedi Sticker Magneti",
]

NUTUKLAR = [
    "Bu kapakta yeterli soğukluk olmadan kalıcı barış mümkün değildir.",
    "Önerimiz şudur: herkes evine dönsün, sütü koklamadan karar almayalım.",
    "Tarih bizi yargılayacak. Özellikle dondurucu kısmı.",
    "Ben bu toplantıya pizza indirimi için geldim, dürüst olayım.",
    "Nostalji lobisi olarak 2009 yazını referans gösteriyoruz.",
    "Zaman daralıyor. Magnetler düşerse konferans dağılır.",
    "Bağımsız gözlemciyim. Miyavladım, tutanağa geçsin.",
    "Çözüm basit: kapağı kapatın, içerisi ısınmasın.",
]

KARARLAR = [
    "Gündem gelecek haftaya ertelenmiştir.",
    "Pizza kuponu süresi dolmadan yeniden toplanılacaktır.",
    "Barış ilkesi kabul edilmiş, uygulama komisyona havale edilmiştir.",
    "Karar metni buzdolabının yan tarafına asılacaktır.",
    "Oybirliğiyle hiçbir şey yapmamaya karar verilmiştir.",
]


def tutanak_basligi(gundem: str) -> str:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    return (
        f"=== BDGM RESMİ TUTANAK ===\n"
        f"Tarih: {simdi}\n"
        f"Yer: Buzdolabı kapağı, muhtemelen mutfak\n"
        f"Gündem: {gundem}\n"
        f"==========================\n"
    )


def konferans(gundem: str) -> None:
    print(tutanak_basligi(gundem))
    sirali = DELEGELER[:]
    random.shuffle(sirali)
    for delege in sirali:
        nutuk = random.choice(NUTUKLAR)
        print(f"[{delege}]: {nutuk}")
    print()
    print(f"KARAR: {random.choice(KARARLAR)}")
    print("Oturum kapanmıştır. Magnetler yerlerine dönsün.")
    # Gizli satır çözülmezse de hayat devam eder.
    if "--hatirlat" in sys.argv:
        import base64

        print("#", base64.b64decode(GIZLI_HATIRLATMA).decode("utf-8"))


def main() -> None:
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        gundem = " ".join(a for a in sys.argv[1:] if not a.startswith("-"))
    else:
        try:
            gundem = input("Gündem maddesini yazın: ").strip() or "dünya barışı (kısa)"
        except EOFError:
            gundem = "dünya barışı (kısa)"
    konferans(gundem)


if __name__ == "__main__":
    main()
