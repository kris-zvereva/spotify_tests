import time

from selene import be, browser, command


class SpotifyAuthHelper:
    """
    Helper for obtaining Spotify user authorization token via browser.
    This is a workaround - Spotify API doesn't provide user token endpoint.
    Used only for API test setup.
    """

    @staticmethod
    def authorize_and_get_code(email: str, password: str) -> str:
        """
        Performs browser-based login flow and returns authorization code.
        Returns: Authorization code from callback URL
        """
        # UI login flow
        browser.element('//input[@id="username"]').type(email)
        browser.element('//button[@data-testid="login-button"]').click()

        # click "Log in with password" if it appears
        try:
            browser.element(
                '//button[contains(text(), "Log in with a password")]'
            ).click()
        except Exception:
            pass

        browser.element('//input[@id="password"]').type(password)
        browser.element('//button[@type="submit"]').click()
        time.sleep(5)

        # accept permissions if prompt appears
        if browser.element("[data-testid='auth-accept']").matching(be.visible):
            browser.element("[data-testid='auth-accept']").perform(
                command.js.scroll_into_view
            ).click()

        time.sleep(5)

        # extract authorization code from callback URL
        current_url = browser.driver.current_url
        authorization_code = current_url.split("code=")[1].split("&")[0]

        return authorization_code
