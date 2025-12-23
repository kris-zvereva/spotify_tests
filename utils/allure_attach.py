import time

import allure
import requests
from allure_commons.types import AttachmentType


def attach_bstack_video(
    session_id, username, access_key, is_mobile=False, retries=5, delay=5
):
    """Attach BrowserStack video to Allure report"""
    if is_mobile:
        api_url = (
            f"https://api.browserstack.com/app-automate/sessions/{session_id}.json"
        )
    else:
        api_url = f"https://api.browserstack.com/automate/sessions/{session_id}.json"

    video_url = None
    for attempt in range(retries):
        try:
            response = requests.get(api_url, auth=(username, access_key))
            response.raise_for_status()
            video_url = response.json()["automation_session"].get("video_url")
            if video_url:
                break
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1}: Failed to get BrowserStack video: {e}")
        time.sleep(delay)

    if video_url:
        allure.attach(
            f'<a href="{video_url}">BrowserStack Video</a>',
            name="Video",
            attachment_type=AttachmentType.HTML,
        )
    else:
        print("BrowserStack video not available after retries")


def add_screenshot(browser):
    """Attach screenshot to Allure report"""
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name="screenshot",
        attachment_type=AttachmentType.PNG,
        extension=".png",
    )


def add_logs(browser):
    try:
        logs_raw = browser.driver.execute("getLog", {"type": "browser"})["value"]
        if logs_raw:
            log = "\n".join(str(entry) for entry in logs_raw)
            allure.attach(log, name="browser_logs", attachment_type=AttachmentType.TEXT)
    except Exception as e:
        print(f"Browser logs not available: {e}")
