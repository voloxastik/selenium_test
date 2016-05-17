import unittest
from baseTest import BaseTest
from page_objects.PO_start_page import StartPage
from page_objects.PO_player_page import PlayerPage

import time

class TestStartPage(BaseTest):
    # magnet:?xt=urn:btih:88594AAACBDE40EF3E2510C47374EC0AA396C08E&dn=bbb_sunflower_1080p_30fps_normal.mp4&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.publicbt.com%3a80%2fannounce&ws=http%3a%2f%2fdistribution.bbb3d.renderfarming.net%2fvideo%2fmp4%2fbbb_sunflower_1080p_30fps_normal.mp4
    test_magnet_link='magnet:?xt=urn:btih:88594AAACBDE40EF3E2510C47374EC0AA396C08E&dn=bbb_sunflower_1080p_30fps_normal.mp4&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.publicbt.com%3a80%2fannounce&ws=http%3a%2f%2fdistribution.bbb3d.renderfarming.net%2fvideo%2fmp4%2fbbb_sunflower_1080p_30fps_normal.mp4'




    def test_1_emty_magnet_link(self):
        #pressing magnet-enter button with empty page should show error page
        page=StartPage(self.driver)
        page.page_refresh()
        page.enter_magnet_button().click()
        time.sleep(4) #todo   implement wait
        error_message_text=page.error_message()
        self.assertEqual(error_message_text,'Sorry! Something went wrong.')
        page.get_screenshot('test1.png')

    def test_2_wrong_magnet_link(self):
        # type wrong magnet link, press magnet-enter button, get proper error message
        page = StartPage(self.driver)
        page.page_refresh()
        page.input_field().send_keys('&(*%&^$^%#')
        page.enter_magnet_button().click()
        time.sleep(4)  # todo   implement wait
        error_message_text = page.error_message()
        self.assertIn('Failed to parse magnet link',error_message_text)

    def test_3_legal_magnet_link(self):
        # type real magnet link, press magnet-enter button, get animation
        page = PlayerPage(self.driver)
        page.get_player(self.test_magnet_link)
        time.sleep(5)
        self.assertEqual(page.page_title(),'bbb_sunflower_1080p_30fps_normal.mp4')
        page.play()
        time.sleep(5)
        page.pause()




if __name__ == '__main__':
    unittest.main(verbosity=2)