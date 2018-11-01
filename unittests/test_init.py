import unittest
import dreambox
from time import sleep

sleep_time = 4
box = dreambox.Receiver()
box.power_control(4)
box.goto_channel(17)

print('Sleeping  for {0} seconds'.format(sleep_time))
sleep(sleep_time)


# box.change_audio_channel(0)
# surl = box.stream_curent_channel()

class TestDreambox(unittest.TestCase):

    def test_00_goto_channel(self):
        expected = None
        result = box.goto_channel(17)
        self.assertEqual(expected, result)

    def test_01_get_current(self):
        expected = ('TVN Turbo HD', 'TVN', '1920x1080')
        result = box.get_current()
        self.assertEqual(expected, result[0:3])

    def test_02_get_current_channel(self):
        expected = "TVN Turbo HD"
        result = box.get_current_channel()
        self.assertEqual(expected, result)

    def test_03_get_timerlist_for_no_timer(self):
        expected = ('NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE')
        result = box.get_timerlist()
        self.assertEqual(expected, result)

    def test_04_volume_set(self):
        expected = ('True', '100', 'False')
        result = box.volume_set("100")
        self.assertEqual(expected, result)

    def test_05_volume_down(self):
        expected = None
        result = box.volume_down()
        self.assertEqual(expected, result)

    def test_06_get_audio_status_95(self):
        expected = ('True', '95', 'False')
        result = box.get_audio_status()
        self.assertEqual(expected, result)

    def test_07_volume_up(self):
        expected = None
        result = box.volume_up()
        self.assertEqual(expected, result)

    def test_08_get_audio_status_100(self):
        expected = ('True', '100', 'False')
        result = box.get_audio_status()
        self.assertEqual(expected, result)

    # def test_09_power(self):
    #     expect = None
    #     result = box.power()
    #     self.assertEqual(expect, result)

    def test_10_stream_channel(self):
        expect = "name=TVN%20Turbo%20HD"
        result = box.stream_curent_channel()
        self.assertIn(expect, result)

    def test_11_list_record(self):
        expect = "Chemia"
        result = box.recording_list()
        self.assertIn(expect, result)

    def test_12_get_timerlist(self):
        expect = ('NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE')
        result = box.get_timerlist()
        self.assertEqual(expect, result)

    def test_13_power_already_off(self):
        expect = "Dreambox is off"
        result = box.power_control(5)
        self.assertEqual(expect, result)


    def test_14_power_on(self):
        expect = "Dreambox is now on"
        result = box.power_control(4)
        self.assertEqual(expect, result)

    def test_15_power_already_on(self):
        expect = "Dreambox is alerady on"
        result = box.power_control(4)
        self.assertEqual(expect, result)

    def test_16_power_off(self):
        expect = "Dreambox is off"
        result = box.power_control(5)
        self.assertEqual(expect, result)

    def test_17_power_on(self):
        expect = "Dreambox is now on"
        result = box.power_control(4)
        self.assertEqual(expect, result)

    def test_18_channel_up(self):
        expect = True
        result = box.right()
        self.assertEqual(expect, result)

    def test_19_get_current_after_change(self):
        expected = ('TVN Style HD', 'TVN', '1920x1080')
        result = box.get_current()
        self.assertEqual(expected, result[0:3])

    def test_20_record_now(self):
        expect = ('True', 'Instant record for current Event started')
        result = box.record_now()
        self.assertEqual(expect, result)

    def test_21_get_timerlist(self):
        expect = "TVN Style HD"
        global e2servicereference
        global e2timebegin
        global e2timeend
        e2servicereference, e2servicename, e2name, e2timebegin, e2timeend, e2duration = box.get_timerlist()
        self.assertIn(expect, e2servicename)
        return e2servicereference, e2servicename, e2name, e2timebegin, e2timeend, e2duration

    def test_22_del_timer(self):
        expect = "True"
        result = box.del_timer(e2servicereference, e2timebegin, e2timeend)
        self.assertEqual(expect, result[0])

    def test_23_del_timer_empty(self):
        expect = "False"
        result = box.del_timer(e2servicereference, e2timebegin, e2timeend)
        self.assertEqual(expect, result[0])