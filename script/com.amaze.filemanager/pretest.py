import time
import uiautomator2 as u2

if __name__ == "__main__":
    d = u2.connect()

    d(description="Navigate up").click()
    time.sleep(0.5)
    d(textContains="Storage").click()
    time.sleep(0.5)