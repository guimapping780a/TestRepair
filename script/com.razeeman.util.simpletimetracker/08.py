import uiautomator2 as u2

if __name__ == "__main__":
    d = u2.connect()

    d(className="android.widget.ImageView", instance=2).click()
    d(
        resourceId="com.razeeman.util.simpletimetracker:id/btnStatisticsContainerToday"
    ).click()
    d(text="This month").click()
    assert d(text="THIS MONTH").exists
