import unittest
from TestUtils import TestUtils


class TestSymbolTable(unittest.TestCase):

    def test_0(self):
        input = ["INSERT a number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10000))

    def test_1(self):
        input = ["INSERT bE2 string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10001))

    def test_2(self):
        input = ["INSERT bE_2 number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10002))

    def test_3(self):
        input = ["INSERT bE_2 string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10003))

    def test_4(self):
        input = ["INSERT b2_ number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10004))

    def test_5(self):
        input = ["INSERT string string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10005))

    def test_6(self):
        input = ["INSERT B string"]
        expected = ["Invalid: INSERT B string"]
        self.assertTrue(TestUtils.check(input, expected, 10006))

    def test_7(self):
        input = ["INSERT B number"]
        expected = ["Invalid: INSERT B number"]
        self.assertTrue(TestUtils.check(input, expected, 10007))

    def test_8(self):
        input = ["INSERT _b number"]
        expected = ["Invalid: INSERT _b number"]
        self.assertTrue(TestUtils.check(input, expected, 10008))

    def test_9(self):
        input = ["INSERT 3e string"]
        expected = ["Invalid: INSERT 3e string"]
        self.assertTrue(TestUtils.check(input, expected, 10009))

    def test_10(self):
        input = ["INSERT 3e number"]
        expected = ["Invalid: INSERT 3e number"]
        self.assertTrue(TestUtils.check(input, expected, 10010))

    def test_11(self):
        input = [" INSERT abc string"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10011))

    def test_12(self):
        input = ["INSERT  abc string"]
        expected = ["Invalid: INSERT  abc string"]
        self.assertTrue(TestUtils.check(input, expected, 10012))

    def test_13(self):
        input = ["INSERT abc string "]
        expected = ["Invalid: INSERT abc string "]
        self.assertTrue(TestUtils.check(input, expected, 10013))

    def test_14(self):
        input = ["INSERT bc ed string"]
        expected = ["Invalid: INSERT bc ed string"]
        self.assertTrue(TestUtils.check(input, expected, 10014))

    def test_15(self):
        input = ["INSERT bc~ed number"]
        expected = ["Invalid: INSERT bc~ed number"]
        self.assertTrue(TestUtils.check(input, expected, 10015))

    def test_16(self):
        input = ["INSERT bced Number"]
        expected = ["Invalid: INSERT bced Number"]
        self.assertTrue(TestUtils.check(input, expected, 10016))

    def test_17(self):
        input = ["INSERT bced String"]
        expected = ["Invalid: INSERT bced String"]
        self.assertTrue(TestUtils.check(input, expected, 10017))

    def test_18(self):
        input = ["INSERT number bced"]
        expected = ["Invalid: INSERT number bced"]
        self.assertTrue(TestUtils.check(input, expected, 10018))

    def test_19(self):
        input = ["INSERT  string"]
        expected = ["Invalid: INSERT  string"]
        self.assertTrue(TestUtils.check(input, expected, 10019))

    def test_20(self):
        input = ["INSERT  number"]
        expected = ["Invalid: INSERT  number"]
        self.assertTrue(TestUtils.check(input, expected, 10020))

    def test_21(self):
        input = ["INSERT "]
        expected = ["Invalid: INSERT "]
        self.assertTrue(TestUtils.check(input, expected, 10021))

    def test_22(self):
        input = ["INSERT"]
        expected = ["Invalid: INSERT"]
        self.assertTrue(TestUtils.check(input, expected, 10022))

    def test_23(self):
        input = ["INSERT abc number", "INSERT abcd string"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10023))

    def test_24(self):
        input = ["INSERT abc number", "INSERT abc string"]
        expected = ["Redeclared: INSERT abc string"]
        self.assertTrue(TestUtils.check(input, expected, 10024))

    def test_25(self):
        input = ["INSERT x number", "ASSIGN x 1"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10025))

    def test_26(self):
        input = ["INSERT x number", "ASSIGN x 12"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10026))

    def test_27(self):
        input = ["INSERT x number", "ASSIGN x -122"]
        expected = ["Invalid: ASSIGN x -122"]
        self.assertTrue(TestUtils.check(input, expected, 10027))

    def test_28(self):
        input = ["INSERT x string", "ASSIGN x 'a'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10028))

    def test_29(self):
        input = ["INSERT x string", "ASSIGN x '1bc'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10029))

    def test_30(self):
        input = ["INSERT x string", "ASSIGN x '1bC'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10030))

    def test_31(self):
        input = ["INSERT x string", "ASSIGN x 'a_a'"]
        expected = ["Invalid: ASSIGN x 'a_a'"]
        self.assertTrue(TestUtils.check(input, expected, 10031))

    def test_32(self):
        input = ["INSERT x string", "ASSIGN x 'a@a'"]
        expected = ["Invalid: ASSIGN x 'a@a'"]
        self.assertTrue(TestUtils.check(input, expected, 10032))

    def test_33(self):
        input = ["ASSIGN Ba 1"]
        expected = ["Invalid: ASSIGN Ba 1"]
        self.assertTrue(TestUtils.check(input, expected, 10033))

    def test_34(self):
        input = ["ASSIGN B2 1"]
        expected = ["Invalid: ASSIGN B2 1"]
        self.assertTrue(TestUtils.check(input, expected, 10034))

    def test_35(self):
        input = ["ASSIGN bc~ed 1"]
        expected = ["Invalid: ASSIGN bc~ed 1"]
        self.assertTrue(TestUtils.check(input, expected, 10035))

    def test_36(self):
        input = ["INSERT x number", "ASSIGN x Ba"]
        expected = ["Invalid: ASSIGN x Ba"]
        self.assertTrue(TestUtils.check(input, expected, 10036))

    def test_37(self):
        input = ["INSERT x number", "ASSIGN x _"]
        expected = ["Invalid: ASSIGN x _"]
        self.assertTrue(TestUtils.check(input, expected, 10037))

    def test_38(self):
        input = ["INSERT x number", "ASSIGN x bc@ed"]
        expected = ["Invalid: ASSIGN x bc@ed"]
        self.assertTrue(TestUtils.check(input, expected, 10038))

    def test_39(self):
        input = ["INSERT x string", "ASSIGN x bc@ed"]
        expected = ["Invalid: ASSIGN x bc@ed"]
        self.assertTrue(TestUtils.check(input, expected, 10039))

    def test_40(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x y"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10040))

    def test_41(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x number"]
        expected = ["Undeclared: ASSIGN x number"]
        self.assertTrue(TestUtils.check(input, expected, 10041))

    def test_42(self):
        input = ["INSERT x number", "INSERT y number", "ASSIGN x string"]
        expected = ["Undeclared: ASSIGN x string"]
        self.assertTrue(TestUtils.check(input, expected, 10042))

    def test_43(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN y number"]
        expected = ["Undeclared: ASSIGN y number"]
        self.assertTrue(TestUtils.check(input, expected, 10043))

    def test_44(self):
        input = ["INSERT x string", "INSERT y number", "ASSIGN x y"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10044))

    def test_45(self):
        input = ["INSERT number number", "INSERT string string", "ASSIGN number string"]
        expected = ["TypeMismatch: ASSIGN number string"]
        self.assertTrue(TestUtils.check(input, expected, 10045))

    def test_46(self):
        input = ["INSERT string string", "INSERT number number", "ASSIGN string number"]
        expected = ["TypeMismatch: ASSIGN string number"]
        self.assertTrue(TestUtils.check(input, expected, 10046))

    def test_47(self):
        input = ["ASSIGN a 1"]
        expected = ["Undeclared: ASSIGN a 1"]
        self.assertTrue(TestUtils.check(input, expected, 10047))

    def test_48(self):
        input = ["ASSIGN b2 'string'"]
        expected = ["Undeclared: ASSIGN b2 'string'"]
        self.assertTrue(TestUtils.check(input, expected, 10048))

    def test_49(self):
        input = ["INSERT x string", "ASSIGN x 1"]
        expected = ["TypeMismatch: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10049))

    def test_50(self):
        input = ["INSERT x string", "ASSIGN x 12"]
        expected = ["TypeMismatch: ASSIGN x 12"]
        self.assertTrue(TestUtils.check(input, expected, 10050))

    def test_51(self):
        input = ["INSERT x number", "ASSIGN x 'a'"]
        expected = ["TypeMismatch: ASSIGN x 'a'"]
        self.assertTrue(TestUtils.check(input, expected, 10051))

    def test_52(self):
        input = ["INSERT x number", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10052))

    def test_53(self):
        input = ["INSERT x number", "ASSIGN x 'azAZ09'"]
        expected = ["TypeMismatch: ASSIGN x 'azAZ09'"]
        self.assertTrue(TestUtils.check(input, expected, 10053))

    def test_54(self):
        input = ["INSERT x string", "INSERT y string", " ASSIGN x y"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10054))

    def test_55(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN  x y"]
        expected = ["Invalid: ASSIGN  x y"]
        self.assertTrue(TestUtils.check(input, expected, 10055))

    def test_56(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x y "]
        expected = ["Invalid: ASSIGN x y "]
        self.assertTrue(TestUtils.check(input, expected, 10056))

    def test_57(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x  'y'"]
        expected = ["Invalid: ASSIGN x  'y'"]
        self.assertTrue(TestUtils.check(input, expected, 10057))

    def test_58(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x"]
        expected = ["Invalid: ASSIGN x"]
        self.assertTrue(TestUtils.check(input, expected, 10058))

    def test_59(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN  "]
        expected = ["Invalid: ASSIGN  "]
        self.assertTrue(TestUtils.check(input, expected, 10059))

    def test_60(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN "]
        expected = ["Invalid: ASSIGN "]
        self.assertTrue(TestUtils.check(input, expected, 10060))

    def test_61(self):
        input = ["BEGIN", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10061))

    def test_62(self):
        input = ["BEGIN ", "END"]
        expected = ["Invalid: BEGIN "]
        self.assertTrue(TestUtils.check(input, expected, 10062))

    def test_63(self):
        input = [" BEGIN", "END"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10063))

    def test_64(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10064))

    def test_65(self):
        input = ["INSERT x number", "BEGIN", "INSERT x string", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10065))

    def test_66(self):
        input = ["INSERT x string", "BEGIN", "INSERT x string", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10066))

    def test_67(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "ASSIGN x 1", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10067))

    def test_68(self):
        input = ["BEGIN", "BEGIN", "END", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10068))

    def test_69(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END", "END", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10069))

    def test_70(self):
        input = ["BEGIN", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10070))

    def test_71(self):
        input = ["BEGIN", "BEGIN", "END", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10071))

    def test_72(self):
        input = ["END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10072))

    def test_73(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "END", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10073))

    def test_74(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10074))

    def test_75(self):
        input = ["BEGIN", "INSERT x number", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10075))

    def test_76(self):
        input = ["BEGIN"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10076))

    def test_77(self):
        input = ["BEGIN", "BEGIN"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10077))

    def test_78(self):
        input = ["BEGIN", "BEGIN", "BEGIN"]
        expected = ["UnclosedBlock: 3"]
        self.assertTrue(TestUtils.check(input, expected, 10078))

    def test_79(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END", "END"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10079))

    def test_80(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10080))

    def test_81(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10081))

    def test_82(self):
        input = ["INSERT x number", "BEGIN", "BEGIN", "INSERT x number", "END", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10082))

    def test_83(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10083))

    def test_84(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "INSERT x number", "END"]
        expected = ["Redeclared: INSERT x number"]
        self.assertTrue(TestUtils.check(input, expected, 10084))

    def test_85(self):
        input = ["INSERT x number", "INSERT y string", "BEGIN", "INSERT x number", "INSERT y string", "END", "BEGIN", "INSERT x number", "INSERT y string", "END"]
        expected = ["success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10085))

    def test_86(self):
        input = ["INSERT x string", "BEGIN", "INSERT y number", "BEGIN", "ASSIGN x y", "END", "END"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10086))

    def test_87(self):
        input = ["INSERT x number", "BEGIN", "INSERT y string", "BEGIN", "INSERT z number", "ASSIGN x y", "END", "END"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10087))

    def test_88(self):
        input = ["BEGIN", "INSERT x string", "INSERT y number", "BEGIN", "END", "END", "ASSIGN x y"]
        expected = ["Undeclared: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10088))

    def test_89(self):
        input = ["BEGIN", "INSERT x number", "INSERT y number", "ASSIGN x y", "END", "BEGIN", "INSERT x number", "INSERT y number", "ASSIGN y x", "END", "ASSIGN x y"]
        expected = ["Undeclared: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10089))

    def test_90(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10090))

    def test_91(self):
        input = ["BEGIN", "ASSIGN x 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["Undeclared: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10091))

    def test_92(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "ASSIGN y 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["TypeMismatch: ASSIGN y 1"]
        self.assertTrue(TestUtils.check(input, expected, 10092))

    def test_93(self):
        input = ["LOOKUP B"]
        expected = ["Invalid: LOOKUP B"]
        self.assertTrue(TestUtils.check(input, expected, 10093))

    def test_94(self):
        input = ["LOOKUP Ba"]
        expected = ["Invalid: LOOKUP Ba"]
        self.assertTrue(TestUtils.check(input, expected, 10094))

    def test_95(self):
        input = ["LOOKUP _b"]
        expected = ["Invalid: LOOKUP _b"]
        self.assertTrue(TestUtils.check(input, expected, 10095))

    def test_96(self):
        input = ["LOOKUP 3e"]
        expected = ["Invalid: LOOKUP 3e"]
        self.assertTrue(TestUtils.check(input, expected, 10096))

    def test_97(self):
        input = ["LOOKUP bc~ed"]
        expected = ["Invalid: LOOKUP bc~ed"]
        self.assertTrue(TestUtils.check(input, expected, 10097))

    def test_98(self):
        input = ["LOOKUP a"]
        expected = ["Undeclared: LOOKUP a"]
        self.assertTrue(TestUtils.check(input, expected, 10098))

    def test_99(self):
        input = ["LOOKUP bE_2"]
        expected = ["Undeclared: LOOKUP bE_2"]
        self.assertTrue(TestUtils.check(input, expected, 10099))

    def test_100(self):
        input = ["LOOKUP b_"]
        expected = ["Undeclared: LOOKUP b_"]
        self.assertTrue(TestUtils.check(input, expected, 10100))

    def test_101(self):
        input = ["LOOKUP number"]
        expected = ["Undeclared: LOOKUP number"]
        self.assertTrue(TestUtils.check(input, expected, 10101))

    def test_102(self):
        input = ["LOOKUP x "]
        expected = ["Invalid: LOOKUP x "]
        self.assertTrue(TestUtils.check(input, expected, 10102))

    def test_103(self):
        input = [" LOOKUP x"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10103))

    def test_104(self):
        input = ["INSERT x number", "LOOKUP x"]
        expected = ["success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10104))

    def test_105(self):
        input = ["INSERT x string", "INSERT y number", "LOOKUP x"]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10105))

    def test_106(self):
        input = ["INSERT x number", "BEGIN", "LOOKUP x", "END"]
        expected = ["success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10106))

    def test_107(self):
        input = ["BEGIN", "INSERT x number", "LOOKUP x", "END"]
        expected = ["success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10107))

    def test_108(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "2"]
        self.assertTrue(TestUtils.check(input, expected, 10108))

    def test_109(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10109))

    def test_110(self):
        input = ["BEGIN", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "END", "LOOKUP x", "END"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10110))

    def test_111(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "LOOKUP x", "INSERT x number", "END", "END"]
        expected = ["success", "1", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10111))

    def test_112(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "LOOKUP x", "END"]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10112))

    def test_113(self):
        input = ["PRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 10113))

    def test_114(self):
        input = ["PRINT "]
        expected = ["Invalid: PRINT "]
        self.assertTrue(TestUtils.check(input, expected, 10114))

    def test_115(self):
        input = ["PRINT  "]
        expected = ["Invalid: PRINT  "]
        self.assertTrue(TestUtils.check(input, expected, 10115))

    def test_116(self):
        input = ["PRINT number"]
        expected = ["Invalid: PRINT number"]
        self.assertTrue(TestUtils.check(input, expected, 10116))

    def test_117(self):
        input = ["INSERT x number", "INSERT y number", "PRINT"]
        expected = ["success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10117))

    def test_118(self):
        input = ["BEGIN", "INSERT x string", "INSERT y string", "PRINT", "END"]
        expected = ["success", "success", "x//1 y//1"]
        self.assertTrue(TestUtils.check(input, expected, 10118))

    def test_119(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "PRINT", "END"]
        expected = ["success", "success", "success", "y//0 x//1"]
        self.assertTrue(TestUtils.check(input, expected, 10119))

    def test_120(self):
        input = ["INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10120))

    def test_121(self):
        input = ["INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10121))

    def test_122(self):
        input = ["INSERT x string", "INSERT y string", "INSERT z string", "PRINT"]
        expected = ["success", "success", "success", "x//0 y//0 z//0"]
        self.assertTrue(TestUtils.check(input, expected, 10122))

    def test_123(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "INSERT y string", "INSERT z string", "PRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "x//1 y//2 z//2"]
        self.assertTrue(TestUtils.check(input, expected, 10123))

    def test_124(self):
        input = ["RPRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 10124))

    def test_125(self):
        input = ["RPRINT "]
        expected = ["Invalid: RPRINT "]
        self.assertTrue(TestUtils.check(input, expected, 10125))

    def test_126(self):
        input = ["RPRINT  "]
        expected = ["Invalid: RPRINT  "]
        self.assertTrue(TestUtils.check(input, expected, 10126))

    def test_127(self):
        input = ["RPRINT number"]
        expected = ["Invalid: RPRINT number"]
        self.assertTrue(TestUtils.check(input, expected, 10127))

    def test_128(self):
        input = ["INSERT x number", "INSERT y number", "RPRINT"]
        expected = ["success", "success", "y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10128))

    def test_129(self):
        input = ["BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", ""]
        self.assertTrue(TestUtils.check(input, expected, 10129))

    def test_130(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "RPRINT", "END"]
        expected = ["success", "success", "success", "x//1 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10130))

    def test_131(self):
        input = ["INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10131))

    def test_132(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "INSERT z string", "RPRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "z//2 x//1 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10132))

    def test_133(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "RPRINT", "INSERT z string", "END", "END"]
        expected = ["success", "success", "success", "success", "x//1 y//0 z//0", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10133))

    def test_134(self):
        input = [""]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10134))

    def test_135(self):
        input = [" "]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10135))

    def test_136(self):
        input = ["  "]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10136))

    def test_137(self):
        input = []
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10137))

    def test_138(self):
        input = ["INSERT x number", ""]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10138))

    def test_139(self):
        input = ["INSERT x number", "", "INSERT x number"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10139))

    def test_140(self):
        input = ["INSErT x number"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10140))

    def test_141(self):
        input = ["x INSERT number"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10141))

    def test_142(self):
        input = ["INSERT x", "number INSERT y number"]
        expected = ["Invalid: INSERT x"]
        self.assertTrue(TestUtils.check(input, expected, 10142))

    def test_143(self):
        input = ["INSERT x number INSERT y number"]
        expected = ["Invalid: INSERT x number INSERT y number"]
        self.assertTrue(TestUtils.check(input, expected, 10143))

    def test_144(self):
        input = ["INSERT x number", " "]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10144))

    def test_145(self):
        input = ["INSERT x number", "  "]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10145))

    def test_146(self):
        input = ["PRINT"] * 100
        expected = [""]*100
        self.assertTrue(TestUtils.check(input, expected, 10146))

    def test_147(self):
        input = ["INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10147))

    def test_148(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "success","x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10148))

    def test_149(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "success","y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10149))

    def test_150(self):
        input = ["INSERT x number", "ASSIGN x 123"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10150))