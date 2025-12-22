import allure
import requests
from allure_commons.types import AttachmentType


def attach_bstack_video(session_id, username, access_key, is_mobile=False):
    """Attach BrowserStack video to Allure report"""
    import time

    time.sleep(5)  # Ждём пока видео сгенерируется

    # Разные API для web и mobile
    if is_mobile:
        api_url = (
            f"https://api.browserstack.com/app-automate/sessions/{session_id}.json"
        )
    else:
        api_url = f"https://api.browserstack.com/automate/sessions/{session_id}.json"

    try:
        response = requests.get(api_url, auth=(username, access_key))
        response.raise_for_status()
        video_url = response.json()["automation_session"]["video_url"]

        allure.attach(
            f'<a href="{video_url}">BrowserStack Video</a>',
            name="Video",
            attachment_type=allure.attachment_type.HTML,
        )
    except requests.exceptions.RequestException as e:
        print(f"Failed to get BrowserStack video: {e}")


def add_screenshot(browser):
    """Attach screenshot to Allure report"""
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name="screenshot",
        attachment_type=AttachmentType.PNG,
        extension=".png",
    )
