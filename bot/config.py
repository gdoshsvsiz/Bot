#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = 6620972
    DEV = 1664850827
    OWNER = config("OWNER", "6047510747")
    API_HASH = "3f6835286b03e000ab6d71b37cc35b92"
    BOT_TOKEN = config("BOT_TOKEN", "6672385958:AAHhRjtPPxQc9ZwCZDf8enRNnOnnUZ4Ek1k")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By TGVid-Comp (https://github.com/Zylern/TGVid-Comp)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = "https://telegra.ph/file/e67c2bb851ee37be37b5f.jpg"
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
