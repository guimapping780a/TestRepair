import uiautomator2 as u2

if __name__ == "__main__":
    d = u2.connect()

    d(description="More options").click()
    d(text="Settings").click()
    d(text="Theme").click()
    d(text="Accent Color").click()
    assert d(text="Accent Color").exists
