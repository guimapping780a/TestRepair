import uiautomator2 as u2

if __name__ == "__main__":
    d = u2.connect()

    d(className="android.widget.ImageButton", instance=0).click()
    d(resourceId="android:id/title", instance=1).click()
    d(resourceId="android:id/summary", instance=2).click()