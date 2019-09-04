# coding: utf-8
"""
This file contain, for each range a name associated with for Unicode.
Scrapped from https://unicode-table.com/
"""
from codecs import BOM_UTF8, BOM_UTF16_BE, BOM_UTF16_LE, BOM_UTF32_BE, BOM_UTF32_LE

UNICODE_RANGES = [
    "0000−001F",
    "0020−007F",
    "0080−00FF",
    "0100−017F",
    "0180−024F",
    "0250−02AF",
    "02B0−02FF",
    "0300−036F",
    "0370−03FF",
    "0400−04FF",
    "0500−052F",
    "0530−058F",
    "0590−05FF",
    "0600−06FF",
    "0700−074F",
    "0750−077F",
    "0780−07BF",
    "07C0−07FF",
    "0800−083F",
    "0840−085F",
    "0860−086F",
    "08A0−08FF",
    "0900−097F",
    "0980−09FF",
    "0A00−0A7F",
    "0A80−0AFF",
    "0B00−0B7F",
    "0B80−0BFF",
    "0C00−0C7F",
    "0C80−0CFF",
    "0D00−0D7F",
    "0D80−0DFF",
    "0E00−0E7F",
    "0E80−0EFF",
    "0F00−0FFF",
    "1000−109F",
    "10A0−10FF",
    "1100−11FF",
    "1200−137F",
    "1380−139F",
    "13A0−13FF",
    "1400−167F",
    "1680−169F",
    "16A0−16FF",
    "1700−171F",
    "1720−173F",
    "1740−175F",
    "1760−177F",
    "1780−17FF",
    "1800−18AF",
    "18B0−18FF",
    "1900−194F",
    "1950−197F",
    "1980−19DF",
    "19E0−19FF",
    "1A00−1A1F",
    "1A20−1AAF",
    "1AB0−1AFF",
    "1B00−1B7F",
    "1B80−1BBF",
    "1BC0−1BFF",
    "1C00−1C4F",
    "1C50−1C7F",
    "1C80−1C8F",
    "1CC0−1CCF",
    "1CD0−1CFF",
    "1D00−1D7F",
    "1D80−1DBF",
    "1DC0−1DFF",
    "1E00−1EFF",
    "1F00−1FFF",
    "2000−206F",
    "2070−209F",
    "20A0−20CF",
    "20D0−20FF",
    "2100−214F",
    "2150−218F",
    "2190−21FF",
    "2200−22FF",
    "2300−23FF",
    "2400−243F",
    "2440−245F",
    "2460−24FF",
    "2500−257F",
    "2580−259F",
    "25A0−25FF",
    "2600−26FF",
    "2700−27BF",
    "27C0−27EF",
    "27F0−27FF",
    "2800−28FF",
    "2900−297F",
    "2980−29FF",
    "2A00−2AFF",
    "2B00−2BFF",
    "2C00−2C5F",
    "2C60−2C7F",
    "2C80−2CFF",
    "2D00−2D2F",
    "2D30−2D7F",
    "2D80−2DDF",
    "2DE0−2DFF",
    "2E00−2E7F",
    "2E80−2EFF",
    "2F00−2FDF",
    "2FF0−2FFF",
    "3000−303F",
    "3040−309F",
    "30A0−30FF",
    "3100−312F",
    "3130−318F",
    "3190−319F",
    "31A0−31BF",
    "31C0−31EF",
    "31F0−31FF",
    "3200−32FF",
    "3300−33FF",
    "3400−4DBF",
    "4DC0−4DFF",
    "4E00−9FFF",
    "A000−A48F",
    "A490−A4CF",
    "A4D0−A4FF",
    "A500−A63F",
    "A640−A69F",
    "A6A0−A6FF",
    "A700−A71F",
    "A720−A7FF",
    "A800−A82F",
    "A830−A83F",
    "A840−A87F",
    "A880−A8DF",
    "A8E0−A8FF",
    "A900−A92F",
    "A930−A95F",
    "A960−A97F",
    "A980−A9DF",
    "A9E0−A9FF",
    "AA00−AA5F",
    "AA60−AA7F",
    "AA80−AADF",
    "AAE0−AAFF",
    "AB00−AB2F",
    "AB30−AB6F",
    "AB70−ABBF",
    "ABC0−ABFF",
    "AC00−D7AF",
    "D7B0−D7FF",
    "D800−DB7F",
    "DB80−DBFF",
    "DC00−DFFF",
    "E000−F8FF",
    "F900−FAFF",
    "FB00−FB4F",
    "FB50−FDFF",
    "FE00−FE0F",
    "FE10−FE1F",
    "FE20−FE2F",
    "FE30−FE4F",
    "FE50−FE6F",
    "FE70−FEFF",
    "FF00−FFEF",
    "FFF0−FFFF",
    "10000−1007F",
    "10080−100FF",
    "10100−1013F",
    "10140−1018F",
    "10190−101CF",
    "101D0−101FF",
    "10280−1029F",
    "102A0−102DF",
    "102E0−102FF",
    "10300−1032F",
    "10330−1034F",
    "10350−1037F",
    "10380−1039F",
    "103A0−103DF",
    "10400−1044F",
    "10450−1047F",
    "10480−104AF",
    "104B0−104FF",
    "10500−1052F",
    "10530−1056F",
    "10600−1077F",
    "10800−1083F",
    "10840−1085F",
    "10860−1087F",
    "10880−108AF",
    "108E0−108FF",
    "10900−1091F",
    "10920−1093F",
    "10980−1099F",
    "109A0−109FF",
    "10A00−10A5F",
    "10A60−10A7F",
    "10A80−10A9F",
    "10AC0−10AFF",
    "10B00−10B3F",
    "10B40−10B5F",
    "10B60−10B7F",
    "10B80−10BAF",
    "10C00−10C4F",
    "10C80−10CFF",
    "10E60−10E7F",
    "11000−1107F",
    "11080−110CF",
    "110D0−110FF",
    "11100−1114F",
    "11150−1117F",
    "11180−111DF",
    "111E0−111FF",
    "11200−1124F",
    "11280−112AF",
    "112B0−112FF",
    "11300−1137F",
    "11400−1147F",
    "11480−114DF",
    "11580−115FF",
    "11600−1165F",
    "11660−1167F",
    "11680−116CF",
    "11700−1173F",
    "118A0−118FF",
    "11A00−11A4F",
    "11A50−11AAF",
    "11AC0−11AFF",
    "11C00−11C6F",
    "11C70−11CBF",
    "11D00−11D5F",
    "12000−123FF",
    "12400−1247F",
    "12480−1254F",
    "13000−1342F",
    "14400−1467F",
    "16800−16A3F",
    "16A40−16A6F",
    "16AD0−16AFF",
    "16B00−16B8F",
    "16F00−16F9F",
    "16FE0−16FFF",
    "17000−187FF",
    "18800−18AFF",
    "1B000−1B0FF",
    "1B100−1B12F",
    "1B170−1B2FF",
    "1BC00−1BC9F",
    "1BCA0−1BCAF",
    "1D000−1D0FF",
    "1D100−1D1FF",
    "1D200−1D24F",
    "1D300−1D35F",
    "1D360−1D37F",
    "1D400−1D7FF",
    "1D800−1DAAF",
    "1E000−1E02F",
    "1E800−1E8DF",
    "1E900−1E95F",
    "1EE00−1EEFF",
    "1F000−1F02F",
    "1F030−1F09F",
    "1F0A0−1F0FF",
    "1F100−1F1FF",
    "1F200−1F2FF",
    "1F300−1F5FF",
    "1F600−1F64F",
    "1F650−1F67F",
    "1F680−1F6FF",
    "1F700−1F77F",
    "1F780−1F7FF",
    "1F800−1F8FF",
    "1F900−1F9FF",
    "20000−2A6DF",
    "2A700−2B73F",
    "2B740−2B81F",
    "2B820−2CEAF",
    "2CEB0−2EBEF",
    "2F800−2FA1F",
    "E0000−E007F",
    "E0100−E01EF"
]

UNICODE_RANGES_NAMES = [
  "Control character",
  "Basic Latin",
  "Latin-1 Supplement",
  "Latin Extended-A",
  "Latin Extended-B",
  "IPA Extensions",
  "Spacing Modifier Letters",
  "Combining Diacritical Marks",
  "Greek and Coptic",
  "Cyrillic",
  "Cyrillic Supplement",
  "Armenian",
  "Hebrew",
  "Arabic",
  "Syriac",
  "Arabic Supplement",
  "Thaana",
  "NKo",
  "Samaritan",
  "Mandaic",
  "Syriac Supplement",
  "Arabic Extended-A",
  "Devanagari",
  "Bengali",
  "Gurmukhi",
  "Gujarati",
  "Oriya",
  "Tamil",
  "Telugu",
  "Kannada",
  "Malayalam",
  "Sinhala",
  "Thai",
  "Lao",
  "Tibetan",
  "Myanmar",
  "Georgian",
  "Hangul Jamo",
  "Ethiopic",
  "Ethiopic Supplement",
  "Cherokee",
  "Unified Canadian Aboriginal Syllabics",
  "Ogham",
  "Runic",
  "Tagalog",
  "Hanunoo",
  "Buhid",
  "Tagbanwa",
  "Khmer",
  "Mongolian",
  "Unified Canadian Aboriginal Syllabics Extended",
  "Limbu",
  "Tai Le",
  "New Tai Lue",
  "Khmer Symbols",
  "Buginese",
  "Tai Tham",
  "Combining Diacritical Marks Extended",
  "Balinese",
  "Sundanese",
  "Batak",
  "Lepcha",
  "Ol Chiki",
  "Cyrillic Extended C",
  "Sundanese Supplement",
  "Vedic Extensions",
  "Phonetic Extensions",
  "Phonetic Extensions Supplement",
  "Combining Diacritical Marks Supplement",
  "Latin Extended Additional",
  "Greek Extended",
  "General Punctuation",
  "Superscripts and Subscripts",
  "Currency Symbols",
  "Combining Diacritical Marks for Symbols",
  "Letterlike Symbols",
  "Number Forms",
  "Arrows",
  "Mathematical Operators",
  "Miscellaneous Technical",
  "Control Pictures",
  "Optical Character Recognition",
  "Enclosed Alphanumerics",
  "Box Drawing",
  "Block Elements",
  "Geometric Shapes",
  "Miscellaneous Symbols",
  "Dingbats",
  "Miscellaneous Mathematical Symbols-A",
  "Supplemental Arrows-A",
  "Braille Patterns",
  "Supplemental Arrows-B",
  "Miscellaneous Mathematical Symbols-B",
  "Supplemental Mathematical Operators",
  "Miscellaneous Symbols and Arrows",
  "Glagolitic",
  "Latin Extended-C",
  "Coptic",
  "Georgian Supplement",
  "Tifinagh",
  "Ethiopic Extended",
  "Cyrillic Extended-A",
  "Supplemental Punctuation",
  "CJK Radicals Supplement",
  "Kangxi Radicals",
  "Ideographic Description Characters",
  "CJK Symbols and Punctuation",
  "Hiragana",
  "Katakana",
  "Bopomofo",
  "Hangul Compatibility Jamo",
  "Kanbun",
  "Bopomofo Extended",
  "CJK Strokes",
  "Katakana Phonetic Extensions",
  "Enclosed CJK Letters and Months",
  "CJK Compatibility",
  "CJK Unified Ideographs Extension A",
  "Yijing Hexagram Symbols",
  "CJK Unified Ideographs",
  "Yi Syllables",
  "Yi Radicals",
  "Lisu",
  "Vai",
  "Cyrillic Extended-B",
  "Bamum",
  "Modifier Tone Letters",
  "Latin Extended-D",
  "Syloti Nagri",
  "Common Indic Number Forms",
  "Phags-pa",
  "Saurashtra",
  "Devanagari Extended",
  "Kayah Li",
  "Rejang",
  "Hangul Jamo Extended-A",
  "Javanese",
  "Myanmar Extended-B",
  "Cham",
  "Myanmar Extended-A",
  "Tai Viet",
  "Meetei Mayek Extensions",
  "Ethiopic Extended-A",
  "Latin Extended-E",
  "Cherokee Supplement",
  "Meetei Mayek",
  "Hangul Syllables",
  "Hangul Jamo Extended-B",
  "High Surrogates",
  "High Private Use Surrogates",
  "Low Surrogates",
  "Private Use Area",
  "CJK Compatibility Ideographs",
  "Alphabetic Presentation Forms",
  "Arabic Presentation Forms-A",
  "Variation Selectors",
  "Vertical Forms",
  "Combining Half Marks",
  "CJK Compatibility Forms",
  "Small Form Variants",
  "Arabic Presentation Forms-B",
  "Halfwidth and Fullwidth Forms",
  "Specials",
  "Linear B Syllabary",
  "Linear B Ideograms",
  "Aegean Numbers",
  "Ancient Greek Numbers",
  "Ancient Symbols",
  "Phaistos Disc",
  "Lycian",
  "Carian",
  "Coptic Epact Numbers",
  "Old Italic",
  "Gothic",
  "Old Permic",
  "Ugaritic",
  "Old Persian",
  "Deseret",
  "Shavian",
  "Osmanya",
  "Osage",
  "Elbasan",
  "Caucasian Albanian",
  "Linear A",
  "Cypriot Syllabary",
  "Imperial Aramaic",
  "Palmyrene",
  "Nabataean",
  "Hatran",
  "Phoenician",
  "Lydian",
  "Meroitic Hieroglyphs",
  "Meroitic Cursive",
  "Kharoshthi",
  "Old South Arabian",
  "Old North Arabian",
  "Manichaean",
  "Avestan",
  "Inscriptional Parthian",
  "Inscriptional Pahlavi",
  "Psalter Pahlavi",
  "Old Turkic",
  "Old Hungarian",
  "Rumi Numeral Symbols",
  "Brahmi",
  "Kaithi",
  "Sora Sompeng",
  "Chakma",
  "Mahajani",
  "Sharada",
  "Sinhala Archaic Numbers",
  "Khojki",
  "Multani",
  "Khudawadi",
  "Grantha",
  "Newa",
  "Tirhuta",
  "Siddham",
  "Modi",
  "Mongolian Supplement",
  "Takri",
  "Ahom",
  "Warang Citi",
  "Zanabazar Square",
  "Soyombo",
  "Pau Cin Hau",
  "Bhaiksuki",
  "Marchen",
  "Masaram Gondi",
  "Cuneiform",
  "Cuneiform Numbers and Punctuation",
  "Early Dynastic Cuneiform",
  "Egyptian Hieroglyphs",
  "Anatolian Hieroglyphs",
  "Bamum Supplement",
  "Mro",
  "Bassa Vah",
  "Pahawh Hmong",
  "Miao",
  "Ideographic Symbols and Punctuation",
  "Tangut",
  "Tangut Components",
  "Kana Supplement",
  "Kana Extended-A",
  "Nushu",
  "Duployan",
  "Shorthand Format Controls",
  "Byzantine Musical Symbols",
  "Musical Symbols",
  "Ancient Greek Musical Notation",
  "Tai Xuan Jing Symbols",
  "Counting Rod Numerals",
  "Mathematical Alphanumeric Symbols",
  "Sutton SignWriting",
  "Glagolitic Supplement",
  "Mende Kikakui",
  "Adlam",
  "Arabic Mathematical Alphabetic Symbols",
  "Mahjong Tiles",
  "Domino Tiles",
  "Playing Cards",
  "Enclosed Alphanumeric Supplement",
  "Enclosed Ideographic Supplement",
  "Miscellaneous Symbols and Pictographs",
  "Emoticons (Emoji)",
  "Ornamental Dingbats",
  "Transport and Map Symbols",
  "Alchemical Symbols",
  "Geometric Shapes Extended",
  "Supplemental Arrows-C",
  "Supplemental Symbols and Pictographs",
  "CJK Unified Ideographs Extension B",
  "CJK Unified Ideographs Extension C",
  "CJK Unified Ideographs Extension D",
  "CJK Unified Ideographs Extension E",
  "CJK Unified Ideographs Extension F",
  "CJK Compatibility Ideographs Supplement",
  "Tags",
  "Variation Selectors Supplement"
]

BYTE_ORDER_MARK = {
    'utf_8': BOM_UTF8,
    'utf_7': [
        b'\x2b\x2f\x76\x38',
        b'\x2b\x2f\x76\x39',
        b'\x2b\x2f\x76\x2b',
        b'\x2b\x2f\x76\x2f',
        b'\x2b\x2f\x76\x38\x2d'
    ],
    'gb18030': b'\x84\x31\x95\x33',
    'utf_32_be': BOM_UTF32_BE,
    'utf_32_le': BOM_UTF32_LE,
    'utf_16_be': BOM_UTF16_BE,
    'utf_16_le': BOM_UTF16_LE
}

UNICODE_RANGES_ZIP = dict(
    zip(
        UNICODE_RANGES_NAMES,
        [
            range(
                int(el[0], 16),
                int(el[1], 16)+1
            ) for el in map(lambda x: x.split('−'), UNICODE_RANGES)
        ]
    )
)
