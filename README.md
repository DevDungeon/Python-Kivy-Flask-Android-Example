# Kivy App with Flask Example

This is a template application that shows how Flask and Kivy
can work together. This example runs on Android.
It starts Flask in a background thread and logs
incoming requests to a text output on the Android screen.

ALso see these relevant tutorials:

- [Kivy Flask App on Android Example]() - More details and instructions about this project
- [Python Flask Tutorial]()
- [Kivy Tutorial]()
- [How to Publish Android Apps to Google Play Store](https://www.devdungeon.com/content/how-publish-android-apps-google-play-store)
- [PyInstaller Tutorial]() - For packaging desktop apps as .exe and Linux/Mac equivalents

## Setup

You need Kivy and Buildozer. You must be on Linux for Android build to work.

```
python3 -m pip install kivy buildozer
```

## Build

Use buildozer to create Android APKs

```bash
# Build
python3 -m buildozer android debug
# Build and install
python3 -m buildozer android debug deploy
# Build, install, and run
python3 -m buildozer android debug deploy run
```


## Get the IP address of the device

```bash
python3 -m buildozer -v android adb -- shell ifconfig wlan0
```

## Run curl from Android

Running `curl` from the Android device can be useful for testing Flask.

```bash
python3 -m buildozer -v android adb -- shell "curl localhost:5000"
```
