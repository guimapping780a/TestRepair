import uiautomator2 as u2

if __name__ == "__main__":
    d = u2.connect()

    d(resourceId="info.staticfree.SuperGenPass:id/domain_edit").set_text("example.org")
    d(resourceId="info.staticfree.SuperGenPass:id/password_edit").set_text("1234")
    d(text="PIN").click()
    assert d(text="4").exists
