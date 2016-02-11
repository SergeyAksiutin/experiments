########################################################################
#
# SYNOPSIS
#   test_usecase -- Smoke test for School Major Match API
#
# AUTHOR
#   Serhii Aksiutin (saksiutin@chegg.com)
#
# DATE
#  Thursday August 6th, 2015
#
# DESCRIPTION
#   Smoke test for Schools on ODIN
#
# USAGE
#   normal run: nosetests match.py
#   debug  run: nosetests match.py --nocapture
#
# EXIT STATUS
#
# FILES
#
# INDENTATION STYLE
#   One tab = four spaces
#
# LICENSE/COPYRIGHT
#   (c) 2015 Chegg, Inc. All rights reserved
#
########################################################################
from api_utils import Calls
from unittest import TestCase
import httplib


class TestClass(TestCase):

    # DESCRIPTION
    #   School Major Match. List of all possible test cases
    #
    # ENDPOINT
    #   git 
    #
    # INPUT
    #   match request input object
    # JSON:{"majorIds": ["{majorIds}"]}
    #
    # OUTPUT
    #   list of major IDs with school ID
    #
    # EXAMPLE
    #   n/a
    #
    @classmethod
    def setUpClass(cls):
        cls.calls = Calls()
# School has L1

    # ask level 1 major
    def test_a_l1_in_l1(self):
        actual = self.calls.match_majors(
            majorIds='9d556d90-4819-4b33-a265-6c2076bb28aa',
            schoolid='00051799-5a99-4d82-a7c1-180bb987ced6')
        assert actual.http_code == httplib.OK

    # ask level 2 major
    def test_b_l2_in_l1(self):
        actual = self.calls.match_majors(
            majorIds='70606d5e-eba3-43c4-9409-5d5db7db9dd4',
            schoolid='29817beb-21fb-4fa9-9a45-b1c26765c57e')
        assert actual.http_code == httplib.OK

    # ask level 3 major
    def test_c_l3_in_l1(self):
        actual = self.calls.match_majors(
            majorIds='84d8797e-d610-44b6-a6bd-31fa45dc0091',
            schoolid='29817beb-21fb-4fa9-9a45-b1c26765c57e')
        assert actual.http_code == httplib.OK
# School has L2

    # ask level 1 major
    def test_d_l1_in_l2(self):
        actual = self.calls.match_majors(
            majorIds='8e4e9405-2426-44aa-af78-4b31252095a0',
            schoolid='2e5b8511-c934-4eff-b368-e4d40dc0f3e1')
        assert actual.http_code == httplib.OK

    # ask level 2 major
    def test_e_l2_in_l2(self):
        actual = self.calls.match_majors(
            majorIds='6629f299-54df-43e0-8b56-e1bc0088433e',
            schoolid='2e5b8511-c934-4eff-b368-e4d40dc0f3e1')
        assert actual.http_code == httplib.OK

    # ask level 3 major
    def test_f_l3_in_l2(self):
        actual = self.calls.match_majors(
            majorIds='c7b12888-dcbf-46b6-9ca1-397720f5e230',
            schoolid='328f842b-05dd-428e-8d46-f25d59add53c')
        assert actual.http_code == httplib.OK
# School has L3

    # ask level 1 major
    def test_g_l1_in_l3(self):
        actual = self.calls.match_majors(
            majorIds='ecac43f1-30cb-4745-b031-b3db8f59ac62',
            schoolid='328f842b-05dd-428e-8d46-f25d59add53c')
        assert actual.http_code == httplib.OK

    # ask level 2 major
    def test_h_l2_in_l3(self):
        actual = self.calls.match_majors(
            majorIds='97b0f8d5-f53a-4aa5-b858-b36d77afd79f',
            schoolid='38d878e7-7235-4d88-9190-0f4263ea4383')
        assert actual.http_code == httplib.OK

    # ask level 3 major
    def test_i_l3_in_l3(self):
        actual = self.calls.match_majors(
            majorIds='a5509984-a5a8-403a-97eb-46f395786db4',
            schoolid='39ace496-ba72-4106-981b-12bd2f3356f0')
        assert actual.http_code == httplib.OK
# School has L2 and L3

    # ask level 1 major
    def test_j_l1_in_l2_l3(self):
        actual = self.calls.match_majors(
            majorIds='fa8eeb15-5c64-456c-873f-a44849be9f2c',
            schoolid='0d7db9ac-0c40-4495-941f-50cf553b14bf')
        assert actual.http_code == httplib.OK
# School doesn't have L1, L2 and L3

    # ask level 1 major
    def test_k_l1_in_l0(self):
        actual = self.calls.match_majors(
            majorIds='d7eddaac-5264-4f2c-8ae5-610f46d52c5f',
            schoolid='3dea9b86-f2cb-44d3-93ee-e4e312e5b74d')
        assert actual.http_code == httplib.OK
