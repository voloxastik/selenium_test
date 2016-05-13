import unittest
from baseTest import BaseTest
from page_objects.basePage import BasePage   #todo do we need it??????
from page_objects.PO_start_page import StartPage
from page_objects.PO_player_page import PlayerPage

import time

class TestStartPage(BaseTest):
    # magnet:?xt=urn:btih:88594AAACBDE40EF3E2510C47374EC0AA396C08E&dn=bbb_sunflower_1080p_30fps_normal.mp4&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.publicbt.com%3a80%2fannounce&ws=http%3a%2f%2fdistribution.bbb3d.renderfarming.net%2fvideo%2fmp4%2fbbb_sunflower_1080p_30fps_normal.mp4
    test_magnet_link='magnet:?xt=urn:btih:88594AAACBDE40EF3E2510C47374EC0AA396C08E&dn=bbb_sunflower_1080p_30fps_normal.mp4&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.publicbt.com%3a80%2fannounce&ws=http%3a%2f%2fdistribution.bbb3d.renderfarming.net%2fvideo%2fmp4%2fbbb_sunflower_1080p_30fps_normal.mp4'

    def test_legal_magnet_link(self):
        # type real magnet link, press magnet-enter button, get animation
        page = PlayerPage(self.driver)
        time.sleep(10)
        print(page.page_title())
        page.get_player(self.test_magnet_link)

        print(page.page_title())
        time.sleep(100)

'''
    def test_emty_magnet_link(self):
        #pressing magnet-enter button with empty page should show error page
        page=StartPage(self.driver)
        page.page_refresh()
        page.enter_magnet_button().click()
        time.sleep(2) #todo   implement wait
        error_message_text=page.error_message()
        self.assertEqual(error_message_text,'Sorry! Something went wrong.')

    def test_wrong_magnet_link(self):
        # type wrong magnet link, press magnet-enter button, get proper error message
        page = StartPage(self.driver)
        page.page_refresh()
        page.input_field().send_keys('&(*%&^$^%#')
        page.enter_magnet_button().click()
        time.sleep(2)  # todo   implement wait
        error_message_text = page.error_message()
        self.assertIn('Failed to parse magnet link',error_message_text)
        '''





if __name__ == '__main__':
    unittest.main(verbosity=2)