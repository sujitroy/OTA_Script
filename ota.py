import os.path, json, re, io, time, hashlib, sys

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# constants
donate_url = "https://www.paypal.me/nitinchobhe"
website_url = "https://plus.google.com/communities/111037372581335961267"
developer = "nitin.chobhe"
developer_url = "https://forum.xda-developers.com/member.php?u=5044214"
forum_url= "https://forum.xda-developers.com/pixel-2-xl/development/rom-colt-os-enigma-taimen-t3911826"
url= "https://sourceforge.net/projects/coltos/files/taimen/"
device = sys.argv[1]
filename = "ColtOS-Enigma-4.1_OFFICIAL-" + time.strftime('%Y%m%d') + "-" + device + ".zip"
zip_path = os.path.expanduser("~") + "/colt/out/target/product/" + device + "/"
error = "false"

ota_data = {}
md5file = zip_path + filename + ".md5sum"
changelog = zip_path + "ColtOS-Enigma-4.1_OFFICIAL-" + time.strftime('%Y%m%d') + "-" + device + "-Changelog.txt"

# generate addons nested dict
addons = {"addons":[]}
tmp_addons1 = {}
tmp_addons2 = {}
tmp_addons1["title"] = "Magisk"
tmp_addons1["summary"] = "Magisk"
tmp_addons1["url"] = "https://github.com/topjohnwu/Magisk/releases/download/v19.0/Magisk-v19.0.zip"
tmp_addons2["title"] = "Magisk"
tmp_addons2["summary"] = "Magisk Uninstaller"
tmp_addons2["url"] = "https://github.com/topjohnwu/Magisk/releases/download/v19.0/Magisk-uninstaller-20190328.zip"
addons.get ("addons").append(tmp_addons1)
addons.get ("addons").append(tmp_addons2)

# read some data from files
raw_changelog = io.open(changelog,"r", encoding="cp866").read()

# fill json struct
ota_data=addons
ota_data["donate_url"] = donate_url
ota_data["website_url"] = website_url
ota_data["developer"] = developer
ota_data["developer_url"] = developer_url
ota_data["forum_url"] = forum_url
ota_data["filename"] = filename
ota_data["build_date"] = time.strftime('%Y%m%d')
ota_data["filesize"] = str(getSize(zip_path + filename))
ota_data["md5"] = md5(zip_path + filename)
ota_data["url"] = url + filename + "/download"
ota_data["changelog"] = raw_changelog
ota_data["error"] = error
print("Writting json data to " + device + ".json")
with open("colt_official_devices/" + device + ".json", "w") as f:
  json.dump(ota_data, f, indent=2)
