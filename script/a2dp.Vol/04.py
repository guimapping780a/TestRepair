import uiautomator2 as u2

if __name__ == "__main__":
    d = u2.connect()

    d(resourceId="android:id/text1").click()
    d(text="Delete").click()
    d(text="Find Devices").click()
    assert d(text="Car Dock").exists
