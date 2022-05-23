python -m PyInstaller --distpath=.. --onefile --hidden-import=pytube --add-data=../config.json;config --name=Pyracy -i=../assets/images/pyracy-icon.ico --clean Main.py
del /P Pyracy.spec
cmd /k
