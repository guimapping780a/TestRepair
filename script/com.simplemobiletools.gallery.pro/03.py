import uiautomator2 as u2

if __name__ == "__main__":
    d = u2.connect()

    d(description="More options").click()
    d(text="Filter media").click()
    assert d(text="Filter media").exists
    d(text="CANCEL").click()
