import uiautomator2 as u2

if __name__ == "__main__":
    d = u2.connect()

    d(description="open").click()
    d(text="Settings").click()
    d(text="Shopping List").click()
    assert d(text="Shopping").exists
