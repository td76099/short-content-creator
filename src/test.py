def convert_json_to_srt(json_data, output_srt):
    with open(output_srt, 'w') as f:
        index = 1
        for word_info in json_data['words']:
          if "start" in word_info:
            start_time = int(word_info['start'] * 1000)
            end_time = int(word_info['end'] * 1000)
            f.write(f"{index}\n")
            f.write(f"{format_time(start_time)} --> {format_time(end_time)}\n")
            f.write(f"{word_info['alignedWord'].upper()}\n\n")
            index += 1

def format_time(milliseconds):
    seconds = milliseconds // 1000
    millis = milliseconds % 1000
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"

# Example usage
import json

json_data = {
  "transcript": "My wife and I are getting a divorce. I don\u2019t want a divorce, I desperately want to try and work things out, but it\u2019s not just up to me. I\u2019m in a bad place right now. She can tell, so she encouraged me to continue going to DnD because she knows how much it means to me. I was reassured that we\u2019re all friends and that no one is taking sides.\r\n\r\nThree days after she broke the news to me, her best friend shelved her old character that she had been playing for years to introduce a new one. The character introduced himself (her first time roleplaying a male character) to the campaign by taunting my former wife\u2019s character with the words, \u201cYou used to have a husband.\u201d For context, my former wife\u2019s character had a fianc\u00e9 who died in combat shortly before the campaign began.\r\n\r\nI blinked. I turned to look at my former wife. In character, I asked when hers had a husband.\r\n\r\n\u201cFianc\u00e9, husband, same thing,\u201d her friend said.\r\n\r\nI started to explain that they\u2019re related, but not the same thing. She said she just misspoke.\r\n\r\nI couldn\u2019t hold it back anymore. I left the room to cry in the hallway. I tried to be as quiet as I could, but I let some sobs escape. They continued to play without me until they needed me to roll for initiative.\r\n\r\nAfter the game, I told my former wife that I don\u2019t think I will be attending the next session. She says that\u2019s ridiculous. She said she talked to her friend after the game. She says her friend and the DM had been planning that character for months. The timing was purely coincidental, and she merely misspoke.\r\n\r\nI was a founding member of this campaign. I have played this character for years. So many hours, days spent. I don\u2019t think I can do it anymore. I feel like I\u2019m losing my wife, my passion, everything.",
  "words": [
    {
      "alignedWord": "my",
      "case": "success",
      "end": 0.23,
      "endOffset": 2,
      "phones": [
        {
          "duration": 0.09,
          "phone": "m_B"
        },
        {
          "duration": 0.1,
          "phone": "ay_E"
        }
      ],
      "start": 0.04,
      "startOffset": 0,
      "word": "My"
    },
    {
      "alignedWord": "wife",
      "case": "success",
      "end": 0.56,
      "endOffset": 7,
      "phones": [
        {
          "duration": 0.1,
          "phone": "w_B"
        },
        {
          "duration": 0.15,
          "phone": "ay_I"
        },
        {
          "duration": 0.08,
          "phone": "f_E"
        }
      ],
      "start": 0.23,
      "startOffset": 3,
      "word": "wife"
    },
    {
      "alignedWord": "and",
      "case": "success",
      "end": 0.74,
      "endOffset": 11,
      "phones": [
        {
          "duration": 0.05,
          "phone": "ah_B"
        },
        {
          "duration": 0.06,
          "phone": "n_I"
        },
        {
          "duration": 0.07,
          "phone": "d_E"
        }
      ],
      "start": 0.56,
      "startOffset": 8,
      "word": "and"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 0.91,
      "endOffset": 13,
      "phones": [
        {
          "duration": 0.17,
          "phone": "ay_S"
        }
      ],
      "start": 0.74,
      "startOffset": 12,
      "word": "I"
    },
    {
      "alignedWord": "are",
      "case": "success",
      "end": 0.99,
      "endOffset": 17,
      "phones": [
        {
          "duration": 0.08,
          "phone": "er_S"
        }
      ],
      "start": 0.91,
      "startOffset": 14,
      "word": "are"
    },
    {
      "alignedWord": "getting",
      "case": "success",
      "end": 1.28,
      "endOffset": 25,
      "phones": [
        {
          "duration": 0.06,
          "phone": "g_B"
        },
        {
          "duration": 0.08,
          "phone": "ih_I"
        },
        {
          "duration": 0.01,
          "phone": "t_I"
        },
        {
          "duration": 0.07,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "ng_E"
        }
      ],
      "start": 0.99,
      "startOffset": 18,
      "word": "getting"
    },
    {
      "alignedWord": "a",
      "case": "success",
      "end": 1.32,
      "endOffset": 27,
      "phones": [
        {
          "duration": 0.04,
          "phone": "ah_S"
        }
      ],
      "start": 1.28,
      "startOffset": 26,
      "word": "a"
    },
    {
      "alignedWord": "divorce",
      "case": "success",
      "end": 1.77,
      "endOffset": 35,
      "phones": [
        {
          "duration": 0.05,
          "phone": "d_B"
        },
        {
          "duration": 0.06,
          "phone": "ih_I"
        },
        {
          "duration": 0.08,
          "phone": "v_I"
        },
        {
          "duration": 0.1,
          "phone": "ao_I"
        },
        {
          "duration": 0.1,
          "phone": "r_I"
        },
        {
          "duration": 0.06,
          "phone": "s_E"
        }
      ],
      "start": 1.32,
      "startOffset": 28,
      "word": "divorce"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 2.33,
      "endOffset": 38,
      "phones": [
        {
          "duration": 0.13,
          "phone": "ay_S"
        }
      ],
      "start": 2.2,
      "startOffset": 37,
      "word": "I"
    },
    {
      "alignedWord": "don't",
      "case": "success",
      "end": 2.5500000000000003,
      "endOffset": 44,
      "phones": [
        {
          "duration": 0.05,
          "phone": "d_B"
        },
        {
          "duration": 0.09,
          "phone": "ow_I"
        },
        {
          "duration": 0.08,
          "phone": "n_E"
        }
      ],
      "start": 2.33,
      "startOffset": 39,
      "word": "don\u2019t"
    },
    {
      "alignedWord": "want",
      "case": "success",
      "end": 2.75,
      "endOffset": 49,
      "phones": [
        {
          "duration": 0.06,
          "phone": "w_B"
        },
        {
          "duration": 0.05,
          "phone": "aa_I"
        },
        {
          "duration": 0.03,
          "phone": "n_I"
        },
        {
          "duration": 0.06,
          "phone": "t_E"
        }
      ],
      "start": 2.55,
      "startOffset": 45,
      "word": "want"
    },
    {
      "alignedWord": "a",
      "case": "success",
      "end": 2.79,
      "endOffset": 51,
      "phones": [
        {
          "duration": 0.04,
          "phone": "ah_S"
        }
      ],
      "start": 2.75,
      "startOffset": 50,
      "word": "a"
    },
    {
      "alignedWord": "divorce",
      "case": "success",
      "end": 3.2800000000000002,
      "endOffset": 59,
      "phones": [
        {
          "duration": 0.05,
          "phone": "d_B"
        },
        {
          "duration": 0.06,
          "phone": "ih_I"
        },
        {
          "duration": 0.09,
          "phone": "v_I"
        },
        {
          "duration": 0.1,
          "phone": "ao_I"
        },
        {
          "duration": 0.11,
          "phone": "r_I"
        },
        {
          "duration": 0.08,
          "phone": "s_E"
        }
      ],
      "start": 2.79,
      "startOffset": 52,
      "word": "divorce"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 3.59,
      "endOffset": 62,
      "phones": [
        {
          "duration": 0.11,
          "phone": "ay_S"
        }
      ],
      "start": 3.48,
      "startOffset": 61,
      "word": "I"
    },
    {
      "alignedWord": "desperately",
      "case": "success",
      "end": 4.109999999999999,
      "endOffset": 74,
      "phones": [
        {
          "duration": 0.09,
          "phone": "d_B"
        },
        {
          "duration": 0.06,
          "phone": "eh_I"
        },
        {
          "duration": 0.07,
          "phone": "s_I"
        },
        {
          "duration": 0.07,
          "phone": "p_I"
        },
        {
          "duration": 0.04,
          "phone": "er_I"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.02,
          "phone": "t_I"
        },
        {
          "duration": 0.05,
          "phone": "l_I"
        },
        {
          "duration": 0.07,
          "phone": "iy_E"
        }
      ],
      "start": 3.59,
      "startOffset": 63,
      "word": "desperately"
    },
    {
      "alignedWord": "want",
      "case": "success",
      "end": 4.28,
      "endOffset": 79,
      "phones": [
        {
          "duration": 0.03,
          "phone": "w_B"
        },
        {
          "duration": 0.07,
          "phone": "ao_I"
        },
        {
          "duration": 0.03,
          "phone": "n_I"
        },
        {
          "duration": 0.04,
          "phone": "t_E"
        }
      ],
      "start": 4.11,
      "startOffset": 75,
      "word": "want"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 4.38,
      "endOffset": 82,
      "phones": [
        {
          "duration": 0.03,
          "phone": "t_B"
        },
        {
          "duration": 0.06,
          "phone": "ih_E"
        }
      ],
      "start": 4.29,
      "startOffset": 80,
      "word": "to"
    },
    {
      "alignedWord": "try",
      "case": "success",
      "end": 4.64,
      "endOffset": 86,
      "phones": [
        {
          "duration": 0.06,
          "phone": "t_B"
        },
        {
          "duration": 0.09,
          "phone": "r_I"
        },
        {
          "duration": 0.11,
          "phone": "ay_E"
        }
      ],
      "start": 4.38,
      "startOffset": 83,
      "word": "try"
    },
    {
      "alignedWord": "and",
      "case": "success",
      "end": 4.77,
      "endOffset": 90,
      "phones": [
        {
          "duration": 0.05,
          "phone": "ah_B"
        },
        {
          "duration": 0.01,
          "phone": "n_I"
        },
        {
          "duration": 0.07,
          "phone": "d_E"
        }
      ],
      "start": 4.64,
      "startOffset": 87,
      "word": "and"
    },
    {
      "alignedWord": "work",
      "case": "success",
      "end": 4.96,
      "endOffset": 95,
      "phones": [
        {
          "duration": 0.06,
          "phone": "w_B"
        },
        {
          "duration": 0.07,
          "phone": "er_I"
        },
        {
          "duration": 0.06,
          "phone": "k_E"
        }
      ],
      "start": 4.77,
      "startOffset": 91,
      "word": "work"
    },
    {
      "alignedWord": "things",
      "case": "success",
      "end": 5.22,
      "endOffset": 102,
      "phones": [
        {
          "duration": 0.08,
          "phone": "th_B"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "ng_I"
        },
        {
          "duration": 0.06,
          "phone": "z_E"
        }
      ],
      "start": 4.96,
      "startOffset": 96,
      "word": "things"
    },
    {
      "alignedWord": "out",
      "case": "success",
      "end": 5.51,
      "endOffset": 106,
      "phones": [
        {
          "duration": 0.18,
          "phone": "aw_B"
        },
        {
          "duration": 0.11,
          "phone": "t_E"
        }
      ],
      "start": 5.22,
      "startOffset": 103,
      "word": "out"
    },
    {
      "alignedWord": "but",
      "case": "success",
      "end": 5.77,
      "endOffset": 111,
      "phones": [
        {
          "duration": 0.06,
          "phone": "b_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.03,
          "phone": "t_E"
        }
      ],
      "start": 5.63,
      "startOffset": 108,
      "word": "but"
    },
    {
      "alignedWord": "it's",
      "case": "success",
      "end": 5.96,
      "endOffset": 116,
      "phones": [
        {
          "duration": 0.04,
          "phone": "ih_B"
        },
        {
          "duration": 0.06,
          "phone": "t_I"
        },
        {
          "duration": 0.09,
          "phone": "s_E"
        }
      ],
      "start": 5.77,
      "startOffset": 112,
      "word": "it\u2019s"
    },
    {
      "alignedWord": "not",
      "case": "success",
      "end": 6.16,
      "endOffset": 120,
      "phones": [
        {
          "duration": 0.02,
          "phone": "n_B"
        },
        {
          "duration": 0.1,
          "phone": "aa_I"
        },
        {
          "duration": 0.08,
          "phone": "t_E"
        }
      ],
      "start": 5.96,
      "startOffset": 117,
      "word": "not"
    },
    {
      "alignedWord": "just",
      "case": "success",
      "end": 6.390000000000001,
      "endOffset": 125,
      "phones": [
        {
          "duration": 0.05,
          "phone": "jh_B"
        },
        {
          "duration": 0.06,
          "phone": "ah_I"
        },
        {
          "duration": 0.05,
          "phone": "s_I"
        },
        {
          "duration": 0.07,
          "phone": "t_E"
        }
      ],
      "start": 6.16,
      "startOffset": 121,
      "word": "just"
    },
    {
      "alignedWord": "up",
      "case": "success",
      "end": 6.529999999999999,
      "endOffset": 128,
      "phones": [
        {
          "duration": 0.07,
          "phone": "ah_B"
        },
        {
          "duration": 0.07,
          "phone": "p_E"
        }
      ],
      "start": 6.39,
      "startOffset": 126,
      "word": "up"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 6.62,
      "endOffset": 131,
      "phones": [
        {
          "duration": 0.03,
          "phone": "t_B"
        },
        {
          "duration": 0.06,
          "phone": "ih_E"
        }
      ],
      "start": 6.53,
      "startOffset": 129,
      "word": "to"
    },
    {
      "alignedWord": "me",
      "case": "success",
      "end": 6.91,
      "endOffset": 134,
      "phones": [
        {
          "duration": 0.07,
          "phone": "m_B"
        },
        {
          "duration": 0.22,
          "phone": "iy_E"
        }
      ],
      "start": 6.62,
      "startOffset": 132,
      "word": "me"
    },
    {
      "alignedWord": "i'm",
      "case": "success",
      "end": 7.74,
      "endOffset": 139,
      "phones": [
        {
          "duration": 0.13,
          "phone": "ay_B"
        },
        {
          "duration": 0.06,
          "phone": "m_E"
        }
      ],
      "start": 7.55,
      "startOffset": 136,
      "word": "I\u2019m"
    },
    {
      "alignedWord": "in",
      "case": "success",
      "end": 7.84,
      "endOffset": 142,
      "phones": [
        {
          "duration": 0.05,
          "phone": "ih_B"
        },
        {
          "duration": 0.05,
          "phone": "n_E"
        }
      ],
      "start": 7.74,
      "startOffset": 140,
      "word": "in"
    },
    {
      "alignedWord": "a",
      "case": "success",
      "end": 7.8999999999999995,
      "endOffset": 144,
      "phones": [
        {
          "duration": 0.06,
          "phone": "ah_S"
        }
      ],
      "start": 7.84,
      "startOffset": 143,
      "word": "a"
    },
    {
      "alignedWord": "bad",
      "case": "success",
      "end": 8.18,
      "endOffset": 148,
      "phones": [
        {
          "duration": 0.08,
          "phone": "b_B"
        },
        {
          "duration": 0.12,
          "phone": "ae_I"
        },
        {
          "duration": 0.07,
          "phone": "d_E"
        }
      ],
      "start": 7.91,
      "startOffset": 145,
      "word": "bad"
    },
    {
      "alignedWord": "place",
      "case": "success",
      "end": 8.489999000000001,
      "endOffset": 154,
      "phones": [
        {
          "duration": 0.06,
          "phone": "p_B"
        },
        {
          "duration": 0.07,
          "phone": "l_I"
        },
        {
          "duration": 0.08,
          "phone": "ey_I"
        },
        {
          "duration": 0.1,
          "phone": "s_E"
        }
      ],
      "start": 8.179999,
      "startOffset": 149,
      "word": "place"
    },
    {
      "alignedWord": "right",
      "case": "success",
      "end": 8.700000000000001,
      "endOffset": 160,
      "phones": [
        {
          "duration": 0.05,
          "phone": "r_B"
        },
        {
          "duration": 0.08,
          "phone": "ay_I"
        },
        {
          "duration": 0.08,
          "phone": "t_E"
        }
      ],
      "start": 8.49,
      "startOffset": 155,
      "word": "right"
    },
    {
      "alignedWord": "now",
      "case": "success",
      "end": 9.03,
      "endOffset": 164,
      "phones": [
        {
          "duration": 0.09,
          "phone": "n_B"
        },
        {
          "duration": 0.24,
          "phone": "aw_E"
        }
      ],
      "start": 8.7,
      "startOffset": 161,
      "word": "now"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 9.54,
      "endOffset": 169,
      "phones": [
        {
          "duration": 0.1,
          "phone": "sh_B"
        },
        {
          "duration": 0.07,
          "phone": "iy_E"
        }
      ],
      "start": 9.37,
      "startOffset": 166,
      "word": "She"
    },
    {
      "alignedWord": "can",
      "case": "success",
      "end": 9.69,
      "endOffset": 173,
      "phones": [
        {
          "duration": 0.05,
          "phone": "k_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.05,
          "phone": "n_E"
        }
      ],
      "start": 9.54,
      "startOffset": 170,
      "word": "can"
    },
    {
      "alignedWord": "tell",
      "case": "success",
      "end": 10.11,
      "endOffset": 178,
      "phones": [
        {
          "duration": 0.08,
          "phone": "t_B"
        },
        {
          "duration": 0.18,
          "phone": "eh_I"
        },
        {
          "duration": 0.16,
          "phone": "l_E"
        }
      ],
      "start": 9.69,
      "startOffset": 174,
      "word": "tell"
    },
    {
      "alignedWord": "so",
      "case": "success",
      "end": 10.339998999999999,
      "endOffset": 182,
      "phones": [
        {
          "duration": 0.13,
          "phone": "s_B"
        },
        {
          "duration": 0.07,
          "phone": "ow_E"
        }
      ],
      "start": 10.139999,
      "startOffset": 180,
      "word": "so"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 10.51,
      "endOffset": 186,
      "phones": [
        {
          "duration": 0.09,
          "phone": "sh_B"
        },
        {
          "duration": 0.08,
          "phone": "iy_E"
        }
      ],
      "start": 10.34,
      "startOffset": 183,
      "word": "she"
    },
    {
      "alignedWord": "encouraged",
      "case": "success",
      "end": 10.98,
      "endOffset": 197,
      "phones": [
        {
          "duration": 0.06,
          "phone": "ih_B"
        },
        {
          "duration": 0.06,
          "phone": "n_I"
        },
        {
          "duration": 0.1,
          "phone": "k_I"
        },
        {
          "duration": 0.07,
          "phone": "er_I"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.07,
          "phone": "jh_I"
        },
        {
          "duration": 0.06,
          "phone": "d_E"
        }
      ],
      "start": 10.51,
      "startOffset": 187,
      "word": "encouraged"
    },
    {
      "alignedWord": "me",
      "case": "success",
      "end": 11.09,
      "endOffset": 200,
      "phones": [
        {
          "duration": 0.04,
          "phone": "m_B"
        },
        {
          "duration": 0.07,
          "phone": "iy_E"
        }
      ],
      "start": 10.98,
      "startOffset": 198,
      "word": "me"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 11.19,
      "endOffset": 203,
      "phones": [
        {
          "duration": 0.06,
          "phone": "t_B"
        },
        {
          "duration": 0.04,
          "phone": "ah_E"
        }
      ],
      "start": 11.09,
      "startOffset": 201,
      "word": "to"
    },
    {
      "alignedWord": "continue",
      "case": "success",
      "end": 11.59,
      "endOffset": 212,
      "phones": [
        {
          "duration": 0.04,
          "phone": "k_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.03,
          "phone": "n_I"
        },
        {
          "duration": 0.07,
          "phone": "t_I"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.05,
          "phone": "n_I"
        },
        {
          "duration": 0.04,
          "phone": "y_I"
        },
        {
          "duration": 0.07,
          "phone": "uw_E"
        }
      ],
      "start": 11.19,
      "startOffset": 204,
      "word": "continue"
    },
    {
      "alignedWord": "going",
      "case": "success",
      "end": 11.83,
      "endOffset": 218,
      "phones": [
        {
          "duration": 0.06,
          "phone": "g_B"
        },
        {
          "duration": 0.06,
          "phone": "ow_I"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.05,
          "phone": "ng_E"
        }
      ],
      "start": 11.61,
      "startOffset": 213,
      "word": "going"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 11.94,
      "endOffset": 221,
      "phones": [
        {
          "duration": 0.05,
          "phone": "t_B"
        },
        {
          "duration": 0.06,
          "phone": "ih_E"
        }
      ],
      "start": 11.83,
      "startOffset": 219,
      "word": "to"
    },
    {
      "alignedWord": "<unk>",
      "case": "success",
      "end": 12.49,
      "endOffset": 225,
      "phones": [
        {
          "duration": 0.32,
          "phone": "oov_S"
        }
      ],
      "start": 12.17,
      "startOffset": 222,
      "word": "DnD"
    },
    {
      "alignedWord": "because",
      "case": "success",
      "end": 12.77,
      "endOffset": 233,
      "phones": [
        {
          "duration": 0.05,
          "phone": "b_B"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "k_I"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.05,
          "phone": "z_E"
        }
      ],
      "start": 12.5,
      "startOffset": 226,
      "word": "because"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 12.93,
      "endOffset": 237,
      "phones": [
        {
          "duration": 0.07,
          "phone": "sh_B"
        },
        {
          "duration": 0.08,
          "phone": "iy_E"
        }
      ],
      "start": 12.78,
      "startOffset": 234,
      "word": "she"
    },
    {
      "alignedWord": "knows",
      "case": "success",
      "end": 13.179999,
      "endOffset": 243,
      "phones": [
        {
          "duration": 0.08,
          "phone": "n_B"
        },
        {
          "duration": 0.1,
          "phone": "ow_I"
        },
        {
          "duration": 0.07,
          "phone": "z_E"
        }
      ],
      "start": 12.929999,
      "startOffset": 238,
      "word": "knows"
    },
    {
      "alignedWord": "how",
      "case": "success",
      "end": 13.329999,
      "endOffset": 247,
      "phones": [
        {
          "duration": 0.06,
          "phone": "hh_B"
        },
        {
          "duration": 0.09,
          "phone": "aw_E"
        }
      ],
      "start": 13.179999,
      "startOffset": 244,
      "word": "how"
    },
    {
      "alignedWord": "much",
      "case": "success",
      "end": 13.52,
      "endOffset": 252,
      "phones": [
        {
          "duration": 0.07,
          "phone": "m_B"
        },
        {
          "duration": 0.06,
          "phone": "ah_I"
        },
        {
          "duration": 0.06,
          "phone": "ch_E"
        }
      ],
      "start": 13.33,
      "startOffset": 248,
      "word": "much"
    },
    {
      "alignedWord": "it",
      "case": "success",
      "end": 13.62,
      "endOffset": 255,
      "phones": [
        {
          "duration": 0.05,
          "phone": "ih_B"
        },
        {
          "duration": 0.05,
          "phone": "t_E"
        }
      ],
      "start": 13.52,
      "startOffset": 253,
      "word": "it"
    },
    {
      "alignedWord": "means",
      "case": "success",
      "end": 13.889999999999999,
      "endOffset": 261,
      "phones": [
        {
          "duration": 0.08,
          "phone": "m_B"
        },
        {
          "duration": 0.06,
          "phone": "iy_I"
        },
        {
          "duration": 0.07,
          "phone": "n_I"
        },
        {
          "duration": 0.06,
          "phone": "z_E"
        }
      ],
      "start": 13.62,
      "startOffset": 256,
      "word": "means"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 13.979999,
      "endOffset": 264,
      "phones": [
        {
          "duration": 0.04,
          "phone": "t_B"
        },
        {
          "duration": 0.05,
          "phone": "ih_E"
        }
      ],
      "start": 13.889999,
      "startOffset": 262,
      "word": "to"
    },
    {
      "alignedWord": "me",
      "case": "success",
      "end": 14.26,
      "endOffset": 267,
      "phones": [
        {
          "duration": 0.08,
          "phone": "m_B"
        },
        {
          "duration": 0.2,
          "phone": "iy_E"
        }
      ],
      "start": 13.98,
      "startOffset": 265,
      "word": "me"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 15.05,
      "endOffset": 270,
      "phones": [
        {
          "duration": 0.13,
          "phone": "ay_S"
        }
      ],
      "start": 14.92,
      "startOffset": 269,
      "word": "I"
    },
    {
      "alignedWord": "was",
      "case": "success",
      "end": 15.229999,
      "endOffset": 274,
      "phones": [
        {
          "duration": 0.04,
          "phone": "w_B"
        },
        {
          "duration": 0.06,
          "phone": "ah_I"
        },
        {
          "duration": 0.08,
          "phone": "z_E"
        }
      ],
      "start": 15.049999,
      "startOffset": 271,
      "word": "was"
    },
    {
      "alignedWord": "reassured",
      "case": "success",
      "end": 15.81,
      "endOffset": 284,
      "phones": [
        {
          "duration": 0.06,
          "phone": "r_B"
        },
        {
          "duration": 0.1,
          "phone": "iy_I"
        },
        {
          "duration": 0.01,
          "phone": "ah_I"
        },
        {
          "duration": 0.14,
          "phone": "sh_I"
        },
        {
          "duration": 0.12,
          "phone": "uh_I"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.09,
          "phone": "d_E"
        }
      ],
      "start": 15.23,
      "startOffset": 275,
      "word": "reassured"
    },
    {
      "alignedWord": "that",
      "case": "success",
      "end": 15.929998999999999,
      "endOffset": 289,
      "phones": [
        {
          "duration": 0.01,
          "phone": "dh_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.06,
          "phone": "t_E"
        }
      ],
      "start": 15.809999,
      "startOffset": 285,
      "word": "that"
    },
    {
      "alignedWord": "we're",
      "case": "success",
      "end": 16.069999,
      "endOffset": 295,
      "phones": [
        {
          "duration": 0.07,
          "phone": "w_B"
        },
        {
          "duration": 0.07,
          "phone": "er_E"
        }
      ],
      "start": 15.929999,
      "startOffset": 290,
      "word": "we\u2019re"
    },
    {
      "alignedWord": "all",
      "case": "success",
      "end": 16.240000000000002,
      "endOffset": 299,
      "phones": [
        {
          "duration": 0.08,
          "phone": "ao_B"
        },
        {
          "duration": 0.09,
          "phone": "l_E"
        }
      ],
      "start": 16.07,
      "startOffset": 296,
      "word": "all"
    },
    {
      "alignedWord": "friends",
      "case": "success",
      "end": 16.619999999999997,
      "endOffset": 307,
      "phones": [
        {
          "duration": 0.09,
          "phone": "f_B"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.11,
          "phone": "eh_I"
        },
        {
          "duration": 0.05,
          "phone": "n_I"
        },
        {
          "duration": 0.07,
          "phone": "z_E"
        }
      ],
      "start": 16.24,
      "startOffset": 300,
      "word": "friends"
    },
    {
      "alignedWord": "and",
      "case": "success",
      "end": 16.759999,
      "endOffset": 311,
      "phones": [
        {
          "duration": 0.02,
          "phone": "ah_B"
        },
        {
          "duration": 0.06,
          "phone": "n_I"
        },
        {
          "duration": 0.05,
          "phone": "d_E"
        }
      ],
      "start": 16.629999,
      "startOffset": 308,
      "word": "and"
    },
    {
      "alignedWord": "that",
      "case": "success",
      "end": 16.91,
      "endOffset": 316,
      "phones": [
        {
          "duration": 0.01,
          "phone": "dh_B"
        },
        {
          "duration": 0.06,
          "phone": "ae_I"
        },
        {
          "duration": 0.08,
          "phone": "t_E"
        }
      ],
      "start": 16.76,
      "startOffset": 312,
      "word": "that"
    },
    {
      "alignedWord": "no",
      "case": "success",
      "end": 17.080000000000002,
      "endOffset": 319,
      "phones": [
        {
          "duration": 0.07,
          "phone": "n_B"
        },
        {
          "duration": 0.1,
          "phone": "ow_E"
        }
      ],
      "start": 16.91,
      "startOffset": 317,
      "word": "no"
    },
    {
      "alignedWord": "one",
      "case": "success",
      "end": 17.24,
      "endOffset": 323,
      "phones": [
        {
          "duration": 0.05,
          "phone": "w_B"
        },
        {
          "duration": 0.07,
          "phone": "ah_I"
        },
        {
          "duration": 0.04,
          "phone": "n_E"
        }
      ],
      "start": 17.08,
      "startOffset": 320,
      "word": "one"
    },
    {
      "alignedWord": "is",
      "case": "success",
      "end": 17.349999999999998,
      "endOffset": 326,
      "phones": [
        {
          "duration": 0.06,
          "phone": "ih_B"
        },
        {
          "duration": 0.05,
          "phone": "z_E"
        }
      ],
      "start": 17.24,
      "startOffset": 324,
      "word": "is"
    },
    {
      "alignedWord": "taking",
      "case": "success",
      "end": 17.69,
      "endOffset": 333,
      "phones": [
        {
          "duration": 0.09,
          "phone": "t_B"
        },
        {
          "duration": 0.07,
          "phone": "ey_I"
        },
        {
          "duration": 0.05,
          "phone": "k_I"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.08,
          "phone": "ng_E"
        }
      ],
      "start": 17.35,
      "startOffset": 327,
      "word": "taking"
    },
    {
      "alignedWord": "sides",
      "case": "success",
      "end": 18.200001,
      "endOffset": 339,
      "phones": [
        {
          "duration": 0.11,
          "phone": "s_B"
        },
        {
          "duration": 0.2,
          "phone": "ay_I"
        },
        {
          "duration": 0.09,
          "phone": "d_I"
        },
        {
          "duration": 0.11,
          "phone": "z_E"
        }
      ],
      "start": 17.690001,
      "startOffset": 334,
      "word": "sides"
    },
    {
      "alignedWord": "three",
      "case": "success",
      "end": 19.149999,
      "endOffset": 349,
      "phones": [
        {
          "duration": 0.09,
          "phone": "th_B"
        },
        {
          "duration": 0.09,
          "phone": "r_I"
        },
        {
          "duration": 0.08,
          "phone": "iy_E"
        }
      ],
      "start": 18.889999,
      "startOffset": 344,
      "word": "Three"
    },
    {
      "alignedWord": "days",
      "case": "success",
      "end": 19.41,
      "endOffset": 354,
      "phones": [
        {
          "duration": 0.07,
          "phone": "d_B"
        },
        {
          "duration": 0.11,
          "phone": "ey_I"
        },
        {
          "duration": 0.08,
          "phone": "z_E"
        }
      ],
      "start": 19.15,
      "startOffset": 350,
      "word": "days"
    },
    {
      "alignedWord": "after",
      "case": "success",
      "end": 19.67,
      "endOffset": 360,
      "phones": [
        {
          "duration": 0.09,
          "phone": "ae_B"
        },
        {
          "duration": 0.06,
          "phone": "f_I"
        },
        {
          "duration": 0.07,
          "phone": "t_I"
        },
        {
          "duration": 0.04,
          "phone": "er_E"
        }
      ],
      "start": 19.41,
      "startOffset": 355,
      "word": "after"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 19.830000000000002,
      "endOffset": 364,
      "phones": [
        {
          "duration": 0.06,
          "phone": "sh_B"
        },
        {
          "duration": 0.08,
          "phone": "iy_E"
        }
      ],
      "start": 19.69,
      "startOffset": 361,
      "word": "she"
    },
    {
      "alignedWord": "broke",
      "case": "success",
      "end": 20.069999999999997,
      "endOffset": 370,
      "phones": [
        {
          "duration": 0.07,
          "phone": "b_B"
        },
        {
          "duration": 0.03,
          "phone": "r_I"
        },
        {
          "duration": 0.08,
          "phone": "ow_I"
        },
        {
          "duration": 0.06,
          "phone": "k_E"
        }
      ],
      "start": 19.83,
      "startOffset": 365,
      "word": "broke"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 20.16,
      "endOffset": 374,
      "phones": [
        {
          "duration": 0.04,
          "phone": "dh_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_E"
        }
      ],
      "start": 20.07,
      "startOffset": 371,
      "word": "the"
    },
    {
      "alignedWord": "news",
      "case": "success",
      "end": 20.38,
      "endOffset": 379,
      "phones": [
        {
          "duration": 0.07,
          "phone": "n_B"
        },
        {
          "duration": 0.1,
          "phone": "uw_I"
        },
        {
          "duration": 0.05,
          "phone": "z_E"
        }
      ],
      "start": 20.16,
      "startOffset": 375,
      "word": "news"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 20.509999999999998,
      "endOffset": 382,
      "phones": [
        {
          "duration": 0.06,
          "phone": "t_B"
        },
        {
          "duration": 0.05,
          "phone": "ih_E"
        }
      ],
      "start": 20.4,
      "startOffset": 380,
      "word": "to"
    },
    {
      "alignedWord": "me",
      "case": "success",
      "end": 20.839999999999996,
      "endOffset": 385,
      "phones": [
        {
          "duration": 0.09,
          "phone": "m_B"
        },
        {
          "duration": 0.24,
          "phone": "iy_E"
        }
      ],
      "start": 20.509999999999998,
      "startOffset": 383,
      "word": "me"
    },
    {
      "alignedWord": "her",
      "case": "success",
      "end": 21.169999999999998,
      "endOffset": 390,
      "phones": [
        {
          "duration": 0.11,
          "phone": "hh_B"
        },
        {
          "duration": 0.05,
          "phone": "er_E"
        }
      ],
      "start": 21.009999999999998,
      "startOffset": 387,
      "word": "her"
    },
    {
      "alignedWord": "best",
      "case": "success",
      "end": 21.48,
      "endOffset": 395,
      "phones": [
        {
          "duration": 0.08,
          "phone": "b_B"
        },
        {
          "duration": 0.08,
          "phone": "eh_I"
        },
        {
          "duration": 0.09,
          "phone": "s_I"
        },
        {
          "duration": 0.06,
          "phone": "t_E"
        }
      ],
      "start": 21.17,
      "startOffset": 391,
      "word": "best"
    },
    {
      "alignedWord": "friend",
      "case": "success",
      "end": 21.79,
      "endOffset": 402,
      "phones": [
        {
          "duration": 0.06,
          "phone": "f_B"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.08,
          "phone": "eh_I"
        },
        {
          "duration": 0.06,
          "phone": "n_I"
        },
        {
          "duration": 0.05,
          "phone": "d_E"
        }
      ],
      "start": 21.48,
      "startOffset": 396,
      "word": "friend"
    },
    {
      "alignedWord": "shelved",
      "case": "success",
      "end": 22.09,
      "endOffset": 410,
      "phones": [
        {
          "duration": 0.09,
          "phone": "sh_B"
        },
        {
          "duration": 0.07,
          "phone": "eh_I"
        },
        {
          "duration": 0.06,
          "phone": "l_I"
        },
        {
          "duration": 0.02,
          "phone": "v_I"
        },
        {
          "duration": 0.06,
          "phone": "d_E"
        }
      ],
      "start": 21.79,
      "startOffset": 403,
      "word": "shelved"
    },
    {
      "alignedWord": "her",
      "case": "success",
      "end": 22.22,
      "endOffset": 414,
      "phones": [
        {
          "duration": 0.06,
          "phone": "hh_B"
        },
        {
          "duration": 0.07,
          "phone": "er_E"
        }
      ],
      "start": 22.09,
      "startOffset": 411,
      "word": "her"
    },
    {
      "alignedWord": "old",
      "case": "success",
      "end": 22.4,
      "endOffset": 418,
      "phones": [
        {
          "duration": 0.07,
          "phone": "ow_B"
        },
        {
          "duration": 0.04,
          "phone": "l_I"
        },
        {
          "duration": 0.07,
          "phone": "d_E"
        }
      ],
      "start": 22.22,
      "startOffset": 415,
      "word": "old"
    },
    {
      "alignedWord": "character",
      "case": "success",
      "end": 22.9,
      "endOffset": 428,
      "phones": [
        {
          "duration": 0.1,
          "phone": "k_B"
        },
        {
          "duration": 0.08,
          "phone": "eh_I"
        },
        {
          "duration": 0.05,
          "phone": "r_I"
        },
        {
          "duration": 0.06,
          "phone": "ih_I"
        },
        {
          "duration": 0.03,
          "phone": "k_I"
        },
        {
          "duration": 0.08,
          "phone": "t_I"
        },
        {
          "duration": 0.1,
          "phone": "er_E"
        }
      ],
      "start": 22.4,
      "startOffset": 419,
      "word": "character"
    },
    {
      "alignedWord": "that",
      "case": "success",
      "end": 23.05,
      "endOffset": 433,
      "phones": [
        {
          "duration": 0.06,
          "phone": "dh_B"
        },
        {
          "duration": 0.04,
          "phone": "ah_I"
        },
        {
          "duration": 0.04,
          "phone": "t_E"
        }
      ],
      "start": 22.91,
      "startOffset": 429,
      "word": "that"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 23.21,
      "endOffset": 437,
      "phones": [
        {
          "duration": 0.08,
          "phone": "sh_B"
        },
        {
          "duration": 0.08,
          "phone": "iy_E"
        }
      ],
      "start": 23.05,
      "startOffset": 434,
      "word": "she"
    },
    {
      "alignedWord": "had",
      "case": "success",
      "end": 23.35,
      "endOffset": 441,
      "phones": [
        {
          "duration": 0.03,
          "phone": "hh_B"
        },
        {
          "duration": 0.06,
          "phone": "ae_I"
        },
        {
          "duration": 0.05,
          "phone": "d_E"
        }
      ],
      "start": 23.21,
      "startOffset": 438,
      "word": "had"
    },
    {
      "alignedWord": "been",
      "case": "success",
      "end": 23.51,
      "endOffset": 446,
      "phones": [
        {
          "duration": 0.04,
          "phone": "b_B"
        },
        {
          "duration": 0.06,
          "phone": "ih_I"
        },
        {
          "duration": 0.06,
          "phone": "n_E"
        }
      ],
      "start": 23.35,
      "startOffset": 442,
      "word": "been"
    },
    {
      "alignedWord": "playing",
      "case": "success",
      "end": 23.83,
      "endOffset": 454,
      "phones": [
        {
          "duration": 0.07,
          "phone": "p_B"
        },
        {
          "duration": 0.08,
          "phone": "l_I"
        },
        {
          "duration": 0.08,
          "phone": "ey_I"
        },
        {
          "duration": 0.02,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "ng_E"
        }
      ],
      "start": 23.509999999999998,
      "startOffset": 447,
      "word": "playing"
    },
    {
      "alignedWord": "for",
      "case": "success",
      "end": 23.959999999999997,
      "endOffset": 458,
      "phones": [
        {
          "duration": 0.05,
          "phone": "f_B"
        },
        {
          "duration": 0.08,
          "phone": "er_E"
        }
      ],
      "start": 23.83,
      "startOffset": 455,
      "word": "for"
    },
    {
      "alignedWord": "years",
      "case": "success",
      "end": 24.310000000000002,
      "endOffset": 464,
      "phones": [
        {
          "duration": 0.12,
          "phone": "y_B"
        },
        {
          "duration": 0.1,
          "phone": "ih_I"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.07,
          "phone": "z_E"
        }
      ],
      "start": 23.96,
      "startOffset": 459,
      "word": "years"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 24.41,
      "endOffset": 467,
      "phones": [
        {
          "duration": 0.04,
          "phone": "t_B"
        },
        {
          "duration": 0.06,
          "phone": "ih_E"
        }
      ],
      "start": 24.31,
      "startOffset": 465,
      "word": "to"
    },
    {
      "alignedWord": "introduce",
      "case": "success",
      "end": 24.830000000000002,
      "endOffset": 477,
      "phones": [
        {
          "duration": 0.04,
          "phone": "ih_B"
        },
        {
          "duration": 0.05,
          "phone": "n_I"
        },
        {
          "duration": 0.05,
          "phone": "t_I"
        },
        {
          "duration": 0.05,
          "phone": "r_I"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.06,
          "phone": "d_I"
        },
        {
          "duration": 0.07,
          "phone": "uw_I"
        },
        {
          "duration": 0.05,
          "phone": "s_E"
        }
      ],
      "start": 24.41,
      "startOffset": 468,
      "word": "introduce"
    },
    {
      "alignedWord": "a",
      "case": "success",
      "end": 24.889999999999997,
      "endOffset": 479,
      "phones": [
        {
          "duration": 0.06,
          "phone": "ah_S"
        }
      ],
      "start": 24.83,
      "startOffset": 478,
      "word": "a"
    },
    {
      "alignedWord": "new",
      "case": "success",
      "end": 25.080000000000002,
      "endOffset": 483,
      "phones": [
        {
          "duration": 0.05,
          "phone": "n_B"
        },
        {
          "duration": 0.08,
          "phone": "y_I"
        },
        {
          "duration": 0.06,
          "phone": "uw_E"
        }
      ],
      "start": 24.89,
      "startOffset": 480,
      "word": "new"
    },
    {
      "alignedWord": "one",
      "case": "success",
      "end": 25.389999999999997,
      "endOffset": 487,
      "phones": [
        {
          "duration": 0.08,
          "phone": "w_B"
        },
        {
          "duration": 0.11,
          "phone": "ah_I"
        },
        {
          "duration": 0.12,
          "phone": "n_E"
        }
      ],
      "start": 25.08,
      "startOffset": 484,
      "word": "one"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 26.240000000000002,
      "endOffset": 492,
      "phones": [
        {
          "duration": 0.09,
          "phone": "dh_B"
        },
        {
          "duration": 0.08,
          "phone": "iy_E"
        }
      ],
      "start": 26.07,
      "startOffset": 489,
      "word": "The"
    },
    {
      "alignedWord": "character",
      "case": "success",
      "end": 26.67,
      "endOffset": 502,
      "phones": [
        {
          "duration": 0.08,
          "phone": "k_B"
        },
        {
          "duration": 0.09,
          "phone": "eh_I"
        },
        {
          "duration": 0.05,
          "phone": "r_I"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.03,
          "phone": "k_I"
        },
        {
          "duration": 0.08,
          "phone": "t_I"
        },
        {
          "duration": 0.05,
          "phone": "er_E"
        }
      ],
      "start": 26.240000000000002,
      "startOffset": 493,
      "word": "character"
    },
    {
      "alignedWord": "introduced",
      "case": "success",
      "end": 27.150000000000002,
      "endOffset": 513,
      "phones": [
        {
          "duration": 0.06,
          "phone": "ih_B"
        },
        {
          "duration": 0.05,
          "phone": "n_I"
        },
        {
          "duration": 0.05,
          "phone": "t_I"
        },
        {
          "duration": 0.05,
          "phone": "r_I"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.07,
          "phone": "d_I"
        },
        {
          "duration": 0.1,
          "phone": "uw_I"
        },
        {
          "duration": 0.01,
          "phone": "s_I"
        },
        {
          "duration": 0.04,
          "phone": "t_E"
        }
      ],
      "start": 26.67,
      "startOffset": 503,
      "word": "introduced"
    },
    {
      "alignedWord": "himself",
      "case": "success",
      "end": 27.709999999999997,
      "endOffset": 521,
      "phones": [
        {
          "duration": 0.04,
          "phone": "hh_B"
        },
        {
          "duration": 0.07,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "m_I"
        },
        {
          "duration": 0.08,
          "phone": "s_I"
        },
        {
          "duration": 0.12,
          "phone": "eh_I"
        },
        {
          "duration": 0.08,
          "phone": "l_I"
        },
        {
          "duration": 0.1,
          "phone": "f_E"
        }
      ],
      "start": 27.15,
      "startOffset": 514,
      "word": "himself"
    },
    {
      "alignedWord": "her",
      "case": "success",
      "end": 27.93,
      "endOffset": 526,
      "phones": [
        {
          "duration": 0.1,
          "phone": "hh_B"
        },
        {
          "duration": 0.07,
          "phone": "er_E"
        }
      ],
      "start": 27.759999999999998,
      "startOffset": 523,
      "word": "her"
    },
    {
      "alignedWord": "first",
      "case": "success",
      "end": 28.199999000000002,
      "endOffset": 532,
      "phones": [
        {
          "duration": 0.07,
          "phone": "f_B"
        },
        {
          "duration": 0.13,
          "phone": "er_I"
        },
        {
          "duration": 0.05,
          "phone": "s_I"
        },
        {
          "duration": 0.02,
          "phone": "t_E"
        }
      ],
      "start": 27.929999000000002,
      "startOffset": 527,
      "word": "first"
    },
    {
      "alignedWord": "time",
      "case": "success",
      "end": 28.5,
      "endOffset": 537,
      "phones": [
        {
          "duration": 0.08,
          "phone": "t_B"
        },
        {
          "duration": 0.12,
          "phone": "ay_I"
        },
        {
          "duration": 0.09,
          "phone": "m_E"
        }
      ],
      "start": 28.21,
      "startOffset": 533,
      "word": "time"
    },
    {
      "alignedWord": "roleplaying",
      "case": "success",
      "end": 29.0,
      "endOffset": 549,
      "phones": [
        {
          "duration": 0.05,
          "phone": "r_B"
        },
        {
          "duration": 0.06,
          "phone": "ow_I"
        },
        {
          "duration": 0.06,
          "phone": "l_I"
        },
        {
          "duration": 0.08,
          "phone": "p_I"
        },
        {
          "duration": 0.07,
          "phone": "l_I"
        },
        {
          "duration": 0.09,
          "phone": "ey_I"
        },
        {
          "duration": 0.01,
          "phone": "ih_I"
        },
        {
          "duration": 0.08,
          "phone": "ng_E"
        }
      ],
      "start": 28.5,
      "startOffset": 538,
      "word": "roleplaying"
    },
    {
      "alignedWord": "a",
      "case": "success",
      "end": 29.05,
      "endOffset": 551,
      "phones": [
        {
          "duration": 0.05,
          "phone": "ah_S"
        }
      ],
      "start": 29.0,
      "startOffset": 550,
      "word": "a"
    },
    {
      "alignedWord": "male",
      "case": "success",
      "end": 29.310000000000002,
      "endOffset": 556,
      "phones": [
        {
          "duration": 0.09,
          "phone": "m_B"
        },
        {
          "duration": 0.1,
          "phone": "ey_I"
        },
        {
          "duration": 0.07,
          "phone": "l_E"
        }
      ],
      "start": 29.05,
      "startOffset": 552,
      "word": "male"
    },
    {
      "alignedWord": "character",
      "case": "success",
      "end": 29.879998999999998,
      "endOffset": 566,
      "phones": [
        {
          "duration": 0.09,
          "phone": "k_B"
        },
        {
          "duration": 0.07,
          "phone": "eh_I"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.06,
          "phone": "ih_I"
        },
        {
          "duration": 0.03,
          "phone": "k_I"
        },
        {
          "duration": 0.09,
          "phone": "t_I"
        },
        {
          "duration": 0.17,
          "phone": "er_E"
        }
      ],
      "start": 29.309998999999998,
      "startOffset": 557,
      "word": "character"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 30.179999,
      "endOffset": 570,
      "phones": [
        {
          "duration": 0.07,
          "phone": "t_B"
        },
        {
          "duration": 0.05,
          "phone": "ih_E"
        }
      ],
      "start": 30.059998999999998,
      "startOffset": 568,
      "word": "to"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 30.279999000000004,
      "endOffset": 574,
      "phones": [
        {
          "duration": 0.06,
          "phone": "dh_B"
        },
        {
          "duration": 0.04,
          "phone": "ah_E"
        }
      ],
      "start": 30.179999000000002,
      "startOffset": 571,
      "word": "the"
    },
    {
      "alignedWord": "campaign",
      "case": "success",
      "end": 30.8,
      "endOffset": 583,
      "phones": [
        {
          "duration": 0.08,
          "phone": "k_B"
        },
        {
          "duration": 0.08,
          "phone": "ae_I"
        },
        {
          "duration": 0.07,
          "phone": "m_I"
        },
        {
          "duration": 0.09,
          "phone": "p_I"
        },
        {
          "duration": 0.13,
          "phone": "ey_I"
        },
        {
          "duration": 0.07,
          "phone": "n_E"
        }
      ],
      "start": 30.28,
      "startOffset": 575,
      "word": "campaign"
    },
    {
      "alignedWord": "by",
      "case": "success",
      "end": 30.929999,
      "endOffset": 586,
      "phones": [
        {
          "duration": 0.06,
          "phone": "b_B"
        },
        {
          "duration": 0.07,
          "phone": "ay_E"
        }
      ],
      "start": 30.799999,
      "startOffset": 584,
      "word": "by"
    },
    {
      "alignedWord": "taunting",
      "case": "success",
      "end": 31.349999000000004,
      "endOffset": 595,
      "phones": [
        {
          "duration": 0.09,
          "phone": "t_B"
        },
        {
          "duration": 0.11,
          "phone": "ao_I"
        },
        {
          "duration": 0.05,
          "phone": "n_I"
        },
        {
          "duration": 0.06,
          "phone": "t_I"
        },
        {
          "duration": 0.04,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "ng_E"
        }
      ],
      "start": 30.929999000000002,
      "startOffset": 587,
      "word": "taunting"
    },
    {
      "alignedWord": "my",
      "case": "success",
      "end": 31.489999,
      "endOffset": 598,
      "phones": [
        {
          "duration": 0.04,
          "phone": "m_B"
        },
        {
          "duration": 0.1,
          "phone": "ay_E"
        }
      ],
      "start": 31.349999,
      "startOffset": 596,
      "word": "my"
    },
    {
      "alignedWord": "former",
      "case": "success",
      "end": 31.830000000000002,
      "endOffset": 605,
      "phones": [
        {
          "duration": 0.09,
          "phone": "f_B"
        },
        {
          "duration": 0.07,
          "phone": "ao_I"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.06,
          "phone": "m_I"
        },
        {
          "duration": 0.06,
          "phone": "er_E"
        }
      ],
      "start": 31.490000000000002,
      "startOffset": 599,
      "word": "former"
    },
    {
      "alignedWord": "wife's",
      "case": "success",
      "end": 32.12,
      "endOffset": 612,
      "phones": [
        {
          "duration": 0.08,
          "phone": "w_B"
        },
        {
          "duration": 0.1,
          "phone": "ay_I"
        },
        {
          "duration": 0.05,
          "phone": "f_I"
        },
        {
          "duration": 0.06,
          "phone": "s_E"
        }
      ],
      "start": 31.83,
      "startOffset": 606,
      "word": "wife\u2019s"
    },
    {
      "alignedWord": "character",
      "case": "success",
      "end": 32.57,
      "endOffset": 622,
      "phones": [
        {
          "duration": 0.1,
          "phone": "k_B"
        },
        {
          "duration": 0.08,
          "phone": "eh_I"
        },
        {
          "duration": 0.04,
          "phone": "r_I"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.04,
          "phone": "k_I"
        },
        {
          "duration": 0.07,
          "phone": "t_I"
        },
        {
          "duration": 0.07,
          "phone": "er_E"
        }
      ],
      "start": 32.12,
      "startOffset": 613,
      "word": "character"
    },
    {
      "alignedWord": "with",
      "case": "success",
      "end": 32.72,
      "endOffset": 627,
      "phones": [
        {
          "duration": 0.06,
          "phone": "w_B"
        },
        {
          "duration": 0.03,
          "phone": "ih_I"
        },
        {
          "duration": 0.06,
          "phone": "th_E"
        }
      ],
      "start": 32.57,
      "startOffset": 623,
      "word": "with"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 32.799999,
      "endOffset": 631,
      "phones": [
        {
          "duration": 0.03,
          "phone": "dh_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_E"
        }
      ],
      "start": 32.719999,
      "startOffset": 628,
      "word": "the"
    },
    {
      "alignedWord": "words",
      "case": "success",
      "end": 33.209998999999996,
      "endOffset": 637,
      "phones": [
        {
          "duration": 0.11,
          "phone": "w_B"
        },
        {
          "duration": 0.15,
          "phone": "er_I"
        },
        {
          "duration": 0.08,
          "phone": "d_I"
        },
        {
          "duration": 0.07,
          "phone": "z_E"
        }
      ],
      "start": 32.799999,
      "startOffset": 632,
      "word": "words"
    },
    {
      "alignedWord": "you",
      "case": "success",
      "end": 33.63,
      "endOffset": 643,
      "phones": [
        {
          "duration": 0.1,
          "phone": "y_B"
        },
        {
          "duration": 0.08,
          "phone": "uw_E"
        }
      ],
      "start": 33.45,
      "startOffset": 640,
      "word": "You"
    },
    {
      "alignedWord": "used",
      "case": "success",
      "end": 33.830000000000005,
      "endOffset": 648,
      "phones": [
        {
          "duration": 0.07,
          "phone": "y_B"
        },
        {
          "duration": 0.06,
          "phone": "uw_I"
        },
        {
          "duration": 0.06,
          "phone": "z_I"
        },
        {
          "duration": 0.01,
          "phone": "d_E"
        }
      ],
      "start": 33.63,
      "startOffset": 644,
      "word": "used"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 33.959998999999996,
      "endOffset": 651,
      "phones": [
        {
          "duration": 0.07,
          "phone": "t_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_E"
        }
      ],
      "start": 33.839999,
      "startOffset": 649,
      "word": "to"
    },
    {
      "alignedWord": "have",
      "case": "success",
      "end": 34.13,
      "endOffset": 656,
      "phones": [
        {
          "duration": 0.06,
          "phone": "hh_B"
        },
        {
          "duration": 0.05,
          "phone": "ae_I"
        },
        {
          "duration": 0.06,
          "phone": "v_E"
        }
      ],
      "start": 33.96,
      "startOffset": 652,
      "word": "have"
    },
    {
      "alignedWord": "a",
      "case": "success",
      "end": 34.169999,
      "endOffset": 658,
      "phones": [
        {
          "duration": 0.04,
          "phone": "ah_S"
        }
      ],
      "start": 34.129999,
      "startOffset": 657,
      "word": "a"
    },
    {
      "alignedWord": "husband",
      "case": "success",
      "end": 34.65,
      "endOffset": 666,
      "phones": [
        {
          "duration": 0.07,
          "phone": "hh_B"
        },
        {
          "duration": 0.08,
          "phone": "ah_I"
        },
        {
          "duration": 0.07,
          "phone": "z_I"
        },
        {
          "duration": 0.01,
          "phone": "b_I"
        },
        {
          "duration": 0.09,
          "phone": "ah_I"
        },
        {
          "duration": 0.07,
          "phone": "n_I"
        },
        {
          "duration": 0.09,
          "phone": "d_E"
        }
      ],
      "start": 34.17,
      "startOffset": 659,
      "word": "husband"
    },
    {
      "alignedWord": "for",
      "case": "success",
      "end": 35.499999,
      "endOffset": 672,
      "phones": [
        {
          "duration": 0.11,
          "phone": "f_B"
        },
        {
          "duration": 0.08,
          "phone": "er_E"
        }
      ],
      "start": 35.309999000000005,
      "startOffset": 669,
      "word": "For"
    },
    {
      "alignedWord": "context",
      "case": "success",
      "end": 36.13,
      "endOffset": 680,
      "phones": [
        {
          "duration": 0.07,
          "phone": "k_B"
        },
        {
          "duration": 0.11,
          "phone": "aa_I"
        },
        {
          "duration": 0.08,
          "phone": "n_I"
        },
        {
          "duration": 0.06,
          "phone": "t_I"
        },
        {
          "duration": 0.12,
          "phone": "eh_I"
        },
        {
          "duration": 0.1,
          "phone": "k_I"
        },
        {
          "duration": 0.01,
          "phone": "s_I"
        },
        {
          "duration": 0.08,
          "phone": "t_E"
        }
      ],
      "start": 35.5,
      "startOffset": 673,
      "word": "context"
    },
    {
      "alignedWord": "my",
      "case": "success",
      "end": 36.429998999999995,
      "endOffset": 684,
      "phones": [
        {
          "duration": 0.11,
          "phone": "m_B"
        },
        {
          "duration": 0.11,
          "phone": "ay_E"
        }
      ],
      "start": 36.209998999999996,
      "startOffset": 682,
      "word": "my"
    },
    {
      "alignedWord": "former",
      "case": "success",
      "end": 36.76,
      "endOffset": 691,
      "phones": [
        {
          "duration": 0.08,
          "phone": "f_B"
        },
        {
          "duration": 0.08,
          "phone": "ao_I"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.05,
          "phone": "m_I"
        },
        {
          "duration": 0.06,
          "phone": "er_E"
        }
      ],
      "start": 36.43,
      "startOffset": 685,
      "word": "former"
    },
    {
      "alignedWord": "wife's",
      "case": "success",
      "end": 37.07,
      "endOffset": 698,
      "phones": [
        {
          "duration": 0.09,
          "phone": "w_B"
        },
        {
          "duration": 0.12,
          "phone": "ay_I"
        },
        {
          "duration": 0.04,
          "phone": "f_I"
        },
        {
          "duration": 0.06,
          "phone": "s_E"
        }
      ],
      "start": 36.76,
      "startOffset": 692,
      "word": "wife\u2019s"
    },
    {
      "alignedWord": "character",
      "case": "success",
      "end": 37.56,
      "endOffset": 708,
      "phones": [
        {
          "duration": 0.11,
          "phone": "k_B"
        },
        {
          "duration": 0.08,
          "phone": "eh_I"
        },
        {
          "duration": 0.05,
          "phone": "r_I"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.03,
          "phone": "k_I"
        },
        {
          "duration": 0.09,
          "phone": "t_I"
        },
        {
          "duration": 0.08,
          "phone": "er_E"
        }
      ],
      "start": 37.07,
      "startOffset": 699,
      "word": "character"
    },
    {
      "alignedWord": "had",
      "case": "success",
      "end": 37.74,
      "endOffset": 712,
      "phones": [
        {
          "duration": 0.08,
          "phone": "hh_B"
        },
        {
          "duration": 0.04,
          "phone": "ae_I"
        },
        {
          "duration": 0.05,
          "phone": "d_E"
        }
      ],
      "start": 37.57,
      "startOffset": 709,
      "word": "had"
    },
    {
      "alignedWord": "a",
      "case": "success",
      "end": 37.81,
      "endOffset": 714,
      "phones": [
        {
          "duration": 0.07,
          "phone": "ah_S"
        }
      ],
      "start": 37.74,
      "startOffset": 713,
      "word": "a"
    },
    {
      "alignedWord": "<unk>",
      "case": "success",
      "end": 38.39,
      "endOffset": 721,
      "phones": [
        {
          "duration": 0.58,
          "phone": "oov_S"
        }
      ],
      "start": 37.81,
      "startOffset": 715,
      "word": "fianc\u00e9"
    },
    {
      "alignedWord": "who",
      "case": "success",
      "end": 38.52,
      "endOffset": 725,
      "phones": [
        {
          "duration": 0.06,
          "phone": "hh_B"
        },
        {
          "duration": 0.07,
          "phone": "uw_E"
        }
      ],
      "start": 38.39,
      "startOffset": 722,
      "word": "who"
    },
    {
      "alignedWord": "died",
      "case": "success",
      "end": 38.790000000000006,
      "endOffset": 730,
      "phones": [
        {
          "duration": 0.1,
          "phone": "d_B"
        },
        {
          "duration": 0.12,
          "phone": "ay_I"
        },
        {
          "duration": 0.05,
          "phone": "d_E"
        }
      ],
      "start": 38.52,
      "startOffset": 726,
      "word": "died"
    },
    {
      "alignedWord": "in",
      "case": "success",
      "end": 38.9,
      "endOffset": 733,
      "phones": [
        {
          "duration": 0.05,
          "phone": "ih_B"
        },
        {
          "duration": 0.06,
          "phone": "n_E"
        }
      ],
      "start": 38.79,
      "startOffset": 731,
      "word": "in"
    },
    {
      "alignedWord": "combat",
      "case": "success",
      "end": 39.349999999999994,
      "endOffset": 740,
      "phones": [
        {
          "duration": 0.06,
          "phone": "k_B"
        },
        {
          "duration": 0.1,
          "phone": "aa_I"
        },
        {
          "duration": 0.06,
          "phone": "m_I"
        },
        {
          "duration": 0.04,
          "phone": "b_I"
        },
        {
          "duration": 0.1,
          "phone": "ae_I"
        },
        {
          "duration": 0.08,
          "phone": "t_E"
        }
      ],
      "start": 38.91,
      "startOffset": 734,
      "word": "combat"
    },
    {
      "alignedWord": "shortly",
      "case": "success",
      "end": 39.769999999999996,
      "endOffset": 748,
      "phones": [
        {
          "duration": 0.1,
          "phone": "sh_B"
        },
        {
          "duration": 0.08,
          "phone": "ao_I"
        },
        {
          "duration": 0.03,
          "phone": "r_I"
        },
        {
          "duration": 0.07,
          "phone": "t_I"
        },
        {
          "duration": 0.06,
          "phone": "l_I"
        },
        {
          "duration": 0.07,
          "phone": "iy_E"
        }
      ],
      "start": 39.36,
      "startOffset": 741,
      "word": "shortly"
    },
    {
      "alignedWord": "before",
      "case": "success",
      "end": 40.06,
      "endOffset": 755,
      "phones": [
        {
          "duration": 0.05,
          "phone": "b_B"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.08,
          "phone": "f_I"
        },
        {
          "duration": 0.05,
          "phone": "ao_I"
        },
        {
          "duration": 0.06,
          "phone": "r_E"
        }
      ],
      "start": 39.77,
      "startOffset": 749,
      "word": "before"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 40.150000000000006,
      "endOffset": 759,
      "phones": [
        {
          "duration": 0.05,
          "phone": "dh_B"
        },
        {
          "duration": 0.04,
          "phone": "ah_E"
        }
      ],
      "start": 40.06,
      "startOffset": 756,
      "word": "the"
    },
    {
      "alignedWord": "campaign",
      "case": "success",
      "end": 40.559999999999995,
      "endOffset": 768,
      "phones": [
        {
          "duration": 0.07,
          "phone": "k_B"
        },
        {
          "duration": 0.06,
          "phone": "ae_I"
        },
        {
          "duration": 0.06,
          "phone": "m_I"
        },
        {
          "duration": 0.07,
          "phone": "p_I"
        },
        {
          "duration": 0.09,
          "phone": "ey_I"
        },
        {
          "duration": 0.06,
          "phone": "n_E"
        }
      ],
      "start": 40.15,
      "startOffset": 760,
      "word": "campaign"
    },
    {
      "alignedWord": "began",
      "case": "success",
      "end": 41.07,
      "endOffset": 774,
      "phones": [
        {
          "duration": 0.04,
          "phone": "b_B"
        },
        {
          "duration": 0.08,
          "phone": "ih_I"
        },
        {
          "duration": 0.08,
          "phone": "g_I"
        },
        {
          "duration": 0.16,
          "phone": "ae_I"
        },
        {
          "duration": 0.15,
          "phone": "n_E"
        }
      ],
      "start": 40.56,
      "startOffset": 769,
      "word": "began"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 41.9,
      "endOffset": 780,
      "phones": [
        {
          "duration": 0.18,
          "phone": "ay_S"
        }
      ],
      "start": 41.72,
      "startOffset": 779,
      "word": "I"
    },
    {
      "alignedWord": "blinked",
      "case": "success",
      "end": 42.41,
      "endOffset": 788,
      "phones": [
        {
          "duration": 0.08,
          "phone": "b_B"
        },
        {
          "duration": 0.05,
          "phone": "l_I"
        },
        {
          "duration": 0.1,
          "phone": "ih_I"
        },
        {
          "duration": 0.11,
          "phone": "ng_I"
        },
        {
          "duration": 0.01,
          "phone": "k_I"
        },
        {
          "duration": 0.16,
          "phone": "t_E"
        }
      ],
      "start": 41.9,
      "startOffset": 781,
      "word": "blinked"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 42.7,
      "endOffset": 791,
      "phones": [
        {
          "duration": 0.13,
          "phone": "ay_S"
        }
      ],
      "start": 42.57,
      "startOffset": 790,
      "word": "I"
    },
    {
      "alignedWord": "turned",
      "case": "success",
      "end": 42.96,
      "endOffset": 798,
      "phones": [
        {
          "duration": 0.1,
          "phone": "t_B"
        },
        {
          "duration": 0.08,
          "phone": "er_I"
        },
        {
          "duration": 0.05,
          "phone": "n_I"
        },
        {
          "duration": 0.03,
          "phone": "d_E"
        }
      ],
      "start": 42.7,
      "startOffset": 792,
      "word": "turned"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 43.06,
      "endOffset": 801,
      "phones": [
        {
          "duration": 0.03,
          "phone": "t_B"
        },
        {
          "duration": 0.07,
          "phone": "uw_E"
        }
      ],
      "start": 42.96,
      "startOffset": 799,
      "word": "to"
    },
    {
      "alignedWord": "look",
      "case": "success",
      "end": 43.230000000000004,
      "endOffset": 806,
      "phones": [
        {
          "duration": 0.05,
          "phone": "l_B"
        },
        {
          "duration": 0.07,
          "phone": "uh_I"
        },
        {
          "duration": 0.05,
          "phone": "k_E"
        }
      ],
      "start": 43.06,
      "startOffset": 802,
      "word": "look"
    },
    {
      "alignedWord": "at",
      "case": "success",
      "end": 43.290000000000006,
      "endOffset": 809,
      "phones": [
        {
          "duration": 0.05,
          "phone": "ae_B"
        },
        {
          "duration": 0.01,
          "phone": "t_E"
        }
      ],
      "start": 43.230000000000004,
      "startOffset": 807,
      "word": "at"
    },
    {
      "alignedWord": "my",
      "case": "success",
      "end": 43.49,
      "endOffset": 812,
      "phones": [
        {
          "duration": 0.07,
          "phone": "m_B"
        },
        {
          "duration": 0.1,
          "phone": "ay_E"
        }
      ],
      "start": 43.32,
      "startOffset": 810,
      "word": "my"
    },
    {
      "alignedWord": "former",
      "case": "success",
      "end": 43.81,
      "endOffset": 819,
      "phones": [
        {
          "duration": 0.07,
          "phone": "f_B"
        },
        {
          "duration": 0.06,
          "phone": "ao_I"
        },
        {
          "duration": 0.07,
          "phone": "r_I"
        },
        {
          "duration": 0.06,
          "phone": "m_I"
        },
        {
          "duration": 0.06,
          "phone": "er_E"
        }
      ],
      "start": 43.49,
      "startOffset": 813,
      "word": "former"
    },
    {
      "alignedWord": "wife",
      "case": "success",
      "end": 44.230000000000004,
      "endOffset": 824,
      "phones": [
        {
          "duration": 0.08,
          "phone": "w_B"
        },
        {
          "duration": 0.17,
          "phone": "ay_I"
        },
        {
          "duration": 0.17,
          "phone": "f_E"
        }
      ],
      "start": 43.81,
      "startOffset": 820,
      "word": "wife"
    },
    {
      "alignedWord": "in",
      "case": "success",
      "end": 44.71,
      "endOffset": 828,
      "phones": [
        {
          "duration": 0.11,
          "phone": "ih_B"
        },
        {
          "duration": 0.07,
          "phone": "n_E"
        }
      ],
      "start": 44.53,
      "startOffset": 826,
      "word": "In"
    },
    {
      "alignedWord": "character",
      "case": "success",
      "end": 45.31,
      "endOffset": 838,
      "phones": [
        {
          "duration": 0.07,
          "phone": "k_B"
        },
        {
          "duration": 0.1,
          "phone": "eh_I"
        },
        {
          "duration": 0.05,
          "phone": "r_I"
        },
        {
          "duration": 0.06,
          "phone": "ih_I"
        },
        {
          "duration": 0.04,
          "phone": "k_I"
        },
        {
          "duration": 0.09,
          "phone": "t_I"
        },
        {
          "duration": 0.18,
          "phone": "er_E"
        }
      ],
      "start": 44.72,
      "startOffset": 829,
      "word": "character"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 45.53,
      "endOffset": 841,
      "phones": [
        {
          "duration": 0.15,
          "phone": "ay_S"
        }
      ],
      "start": 45.38,
      "startOffset": 840,
      "word": "I"
    },
    {
      "alignedWord": "asked",
      "case": "success",
      "end": 45.89,
      "endOffset": 847,
      "phones": [
        {
          "duration": 0.16,
          "phone": "ae_B"
        },
        {
          "duration": 0.09,
          "phone": "s_I"
        },
        {
          "duration": 0.11,
          "phone": "t_E"
        }
      ],
      "start": 45.53,
      "startOffset": 842,
      "word": "asked"
    },
    {
      "alignedWord": "when",
      "case": "success",
      "end": 46.049999,
      "endOffset": 852,
      "phones": [
        {
          "duration": 0.03,
          "phone": "w_B"
        },
        {
          "duration": 0.07,
          "phone": "ih_I"
        },
        {
          "duration": 0.06,
          "phone": "n_E"
        }
      ],
      "start": 45.889999,
      "startOffset": 848,
      "word": "when"
    },
    {
      "alignedWord": "hers",
      "case": "success",
      "end": 46.319998999999996,
      "endOffset": 857,
      "phones": [
        {
          "duration": 0.1,
          "phone": "hh_B"
        },
        {
          "duration": 0.09,
          "phone": "er_I"
        },
        {
          "duration": 0.07,
          "phone": "z_E"
        }
      ],
      "start": 46.059999,
      "startOffset": 853,
      "word": "hers"
    },
    {
      "alignedWord": "had",
      "case": "success",
      "end": 46.48,
      "endOffset": 861,
      "phones": [
        {
          "duration": 0.06,
          "phone": "hh_B"
        },
        {
          "duration": 0.06,
          "phone": "ae_I"
        },
        {
          "duration": 0.04,
          "phone": "d_E"
        }
      ],
      "start": 46.32,
      "startOffset": 858,
      "word": "had"
    },
    {
      "alignedWord": "a",
      "case": "success",
      "end": 46.53,
      "endOffset": 863,
      "phones": [
        {
          "duration": 0.05,
          "phone": "ah_S"
        }
      ],
      "start": 46.480000000000004,
      "startOffset": 862,
      "word": "a"
    },
    {
      "alignedWord": "husband",
      "case": "success",
      "end": 47.03,
      "endOffset": 871,
      "phones": [
        {
          "duration": 0.06,
          "phone": "hh_B"
        },
        {
          "duration": 0.08,
          "phone": "ah_I"
        },
        {
          "duration": 0.08,
          "phone": "z_I"
        },
        {
          "duration": 0.01,
          "phone": "b_I"
        },
        {
          "duration": 0.09,
          "phone": "ah_I"
        },
        {
          "duration": 0.08,
          "phone": "n_I"
        },
        {
          "duration": 0.1,
          "phone": "d_E"
        }
      ],
      "start": 46.53,
      "startOffset": 864,
      "word": "husband"
    },
    {
      "alignedWord": "<unk>",
      "case": "success",
      "end": 48.1,
      "endOffset": 883,
      "phones": [
        {
          "duration": 0.74,
          "phone": "oov_S"
        }
      ],
      "start": 47.36,
      "startOffset": 877,
      "word": "Fianc\u00e9"
    },
    {
      "alignedWord": "husband",
      "case": "success",
      "end": 48.729999,
      "endOffset": 892,
      "phones": [
        {
          "duration": 0.11,
          "phone": "hh_B"
        },
        {
          "duration": 0.07,
          "phone": "ah_I"
        },
        {
          "duration": 0.08,
          "phone": "z_I"
        },
        {
          "duration": 0.01,
          "phone": "b_I"
        },
        {
          "duration": 0.11,
          "phone": "ah_I"
        },
        {
          "duration": 0.07,
          "phone": "n_I"
        },
        {
          "duration": 0.1,
          "phone": "d_E"
        }
      ],
      "start": 48.179999,
      "startOffset": 885,
      "word": "husband"
    },
    {
      "alignedWord": "same",
      "case": "success",
      "end": 49.11,
      "endOffset": 898,
      "phones": [
        {
          "duration": 0.16,
          "phone": "s_B"
        },
        {
          "duration": 0.11,
          "phone": "ey_I"
        },
        {
          "duration": 0.05,
          "phone": "m_E"
        }
      ],
      "start": 48.79,
      "startOffset": 894,
      "word": "same"
    },
    {
      "alignedWord": "thing",
      "case": "success",
      "end": 49.49,
      "endOffset": 904,
      "phones": [
        {
          "duration": 0.07,
          "phone": "th_B"
        },
        {
          "duration": 0.14,
          "phone": "ih_I"
        },
        {
          "duration": 0.17,
          "phone": "ng_E"
        }
      ],
      "start": 49.11,
      "startOffset": 899,
      "word": "thing"
    },
    {
      "alignedWord": "her",
      "case": "success",
      "end": 49.719999,
      "endOffset": 910,
      "phones": [
        {
          "duration": 0.11,
          "phone": "hh_B"
        },
        {
          "duration": 0.06,
          "phone": "er_E"
        }
      ],
      "start": 49.549999,
      "startOffset": 907,
      "word": "her"
    },
    {
      "alignedWord": "friend",
      "case": "success",
      "end": 50.019999,
      "endOffset": 917,
      "phones": [
        {
          "duration": 0.06,
          "phone": "f_B"
        },
        {
          "duration": 0.05,
          "phone": "r_I"
        },
        {
          "duration": 0.08,
          "phone": "eh_I"
        },
        {
          "duration": 0.06,
          "phone": "n_I"
        },
        {
          "duration": 0.05,
          "phone": "d_E"
        }
      ],
      "start": 49.719999,
      "startOffset": 911,
      "word": "friend"
    },
    {
      "alignedWord": "said",
      "case": "success",
      "end": 50.38999999999999,
      "endOffset": 922,
      "phones": [
        {
          "duration": 0.1,
          "phone": "s_B"
        },
        {
          "duration": 0.14,
          "phone": "eh_I"
        },
        {
          "duration": 0.13,
          "phone": "d_E"
        }
      ],
      "start": 50.019999999999996,
      "startOffset": 918,
      "word": "said"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 50.85,
      "endOffset": 928,
      "phones": [
        {
          "duration": 0.18,
          "phone": "ay_S"
        }
      ],
      "start": 50.67,
      "startOffset": 927,
      "word": "I"
    },
    {
      "alignedWord": "started",
      "case": "success",
      "end": 51.19,
      "endOffset": 936,
      "phones": [
        {
          "duration": 0.05,
          "phone": "s_B"
        },
        {
          "duration": 0.05,
          "phone": "t_I"
        },
        {
          "duration": 0.06,
          "phone": "aa_I"
        },
        {
          "duration": 0.02,
          "phone": "r_I"
        },
        {
          "duration": 0.04,
          "phone": "t_I"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.06,
          "phone": "d_E"
        }
      ],
      "start": 50.86,
      "startOffset": 929,
      "word": "started"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 51.29,
      "endOffset": 939,
      "phones": [
        {
          "duration": 0.01,
          "phone": "t_B"
        },
        {
          "duration": 0.09,
          "phone": "ih_E"
        }
      ],
      "start": 51.19,
      "startOffset": 937,
      "word": "to"
    },
    {
      "alignedWord": "explain",
      "case": "success",
      "end": 51.74,
      "endOffset": 947,
      "phones": [
        {
          "duration": 0.01,
          "phone": "ih_B"
        },
        {
          "duration": 0.08,
          "phone": "k_I"
        },
        {
          "duration": 0.04,
          "phone": "s_I"
        },
        {
          "duration": 0.09,
          "phone": "p_I"
        },
        {
          "duration": 0.07,
          "phone": "l_I"
        },
        {
          "duration": 0.09,
          "phone": "ey_I"
        },
        {
          "duration": 0.07,
          "phone": "n_E"
        }
      ],
      "start": 51.29,
      "startOffset": 940,
      "word": "explain"
    },
    {
      "alignedWord": "that",
      "case": "success",
      "end": 51.88,
      "endOffset": 952,
      "phones": [
        {
          "duration": 0.03,
          "phone": "dh_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.06,
          "phone": "t_E"
        }
      ],
      "start": 51.74,
      "startOffset": 948,
      "word": "that"
    },
    {
      "alignedWord": "they're",
      "case": "success",
      "end": 52.02,
      "endOffset": 960,
      "phones": [
        {
          "duration": 0.02,
          "phone": "dh_B"
        },
        {
          "duration": 0.07,
          "phone": "eh_I"
        },
        {
          "duration": 0.05,
          "phone": "r_E"
        }
      ],
      "start": 51.88,
      "startOffset": 953,
      "word": "they\u2019re"
    },
    {
      "alignedWord": "related",
      "case": "success",
      "end": 52.519999999999996,
      "endOffset": 968,
      "phones": [
        {
          "duration": 0.03,
          "phone": "r_B"
        },
        {
          "duration": 0.08,
          "phone": "iy_I"
        },
        {
          "duration": 0.07,
          "phone": "l_I"
        },
        {
          "duration": 0.1,
          "phone": "ey_I"
        },
        {
          "duration": 0.05,
          "phone": "t_I"
        },
        {
          "duration": 0.07,
          "phone": "ah_I"
        },
        {
          "duration": 0.1,
          "phone": "d_E"
        }
      ],
      "start": 52.019999999999996,
      "startOffset": 961,
      "word": "related"
    },
    {
      "alignedWord": "but",
      "case": "success",
      "end": 52.800000000000004,
      "endOffset": 973,
      "phones": [
        {
          "duration": 0.07,
          "phone": "b_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.08,
          "phone": "t_E"
        }
      ],
      "start": 52.6,
      "startOffset": 970,
      "word": "but"
    },
    {
      "alignedWord": "not",
      "case": "success",
      "end": 52.999999,
      "endOffset": 977,
      "phones": [
        {
          "duration": 0.03,
          "phone": "n_B"
        },
        {
          "duration": 0.1,
          "phone": "aa_I"
        },
        {
          "duration": 0.07,
          "phone": "t_E"
        }
      ],
      "start": 52.799999,
      "startOffset": 974,
      "word": "not"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 53.11,
      "endOffset": 981,
      "phones": [
        {
          "duration": 0.05,
          "phone": "dh_B"
        },
        {
          "duration": 0.06,
          "phone": "ah_E"
        }
      ],
      "start": 53.0,
      "startOffset": 978,
      "word": "the"
    },
    {
      "alignedWord": "same",
      "case": "success",
      "end": 53.369999,
      "endOffset": 986,
      "phones": [
        {
          "duration": 0.1,
          "phone": "s_B"
        },
        {
          "duration": 0.09,
          "phone": "ey_I"
        },
        {
          "duration": 0.07,
          "phone": "m_E"
        }
      ],
      "start": 53.109999,
      "startOffset": 982,
      "word": "same"
    },
    {
      "alignedWord": "thing",
      "case": "success",
      "end": 53.729999,
      "endOffset": 992,
      "phones": [
        {
          "duration": 0.07,
          "phone": "th_B"
        },
        {
          "duration": 0.13,
          "phone": "ih_I"
        },
        {
          "duration": 0.15,
          "phone": "ng_E"
        }
      ],
      "start": 53.379999,
      "startOffset": 987,
      "word": "thing"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 54.619999,
      "endOffset": 997,
      "phones": [
        {
          "duration": 0.14,
          "phone": "sh_B"
        },
        {
          "duration": 0.09,
          "phone": "iy_E"
        }
      ],
      "start": 54.389999,
      "startOffset": 994,
      "word": "She"
    },
    {
      "alignedWord": "said",
      "case": "success",
      "end": 54.86,
      "endOffset": 1002,
      "phones": [
        {
          "duration": 0.07,
          "phone": "s_B"
        },
        {
          "duration": 0.07,
          "phone": "eh_I"
        },
        {
          "duration": 0.07,
          "phone": "d_E"
        }
      ],
      "start": 54.65,
      "startOffset": 998,
      "word": "said"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 55.0,
      "endOffset": 1006,
      "phones": [
        {
          "duration": 0.07,
          "phone": "sh_B"
        },
        {
          "duration": 0.07,
          "phone": "iy_E"
        }
      ],
      "start": 54.86,
      "startOffset": 1003,
      "word": "she"
    },
    {
      "alignedWord": "just",
      "case": "success",
      "end": 55.25000000000001,
      "endOffset": 1011,
      "phones": [
        {
          "duration": 0.06,
          "phone": "jh_B"
        },
        {
          "duration": 0.07,
          "phone": "ah_I"
        },
        {
          "duration": 0.05,
          "phone": "s_I"
        },
        {
          "duration": 0.06,
          "phone": "t_E"
        }
      ],
      "start": 55.010000000000005,
      "startOffset": 1007,
      "word": "just"
    },
    {
      "alignedWord": "misspoke",
      "case": "success",
      "end": 55.86,
      "endOffset": 1020,
      "phones": [
        {
          "duration": 0.05,
          "phone": "m_B"
        },
        {
          "duration": 0.07,
          "phone": "ih_I"
        },
        {
          "duration": 0.1,
          "phone": "s_I"
        },
        {
          "duration": 0.1,
          "phone": "p_I"
        },
        {
          "duration": 0.17,
          "phone": "ow_I"
        },
        {
          "duration": 0.12,
          "phone": "k_E"
        }
      ],
      "start": 55.25,
      "startOffset": 1012,
      "word": "misspoke"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 56.300000000000004,
      "endOffset": 1026,
      "phones": [
        {
          "duration": 0.13,
          "phone": "ay_S"
        }
      ],
      "start": 56.17,
      "startOffset": 1025,
      "word": "I"
    },
    {
      "alignedWord": "couldn't",
      "case": "success",
      "end": 56.57,
      "endOffset": 1035,
      "phones": [
        {
          "duration": 0.06,
          "phone": "k_B"
        },
        {
          "duration": 0.06,
          "phone": "uh_I"
        },
        {
          "duration": 0.01,
          "phone": "d_I"
        },
        {
          "duration": 0.07,
          "phone": "ah_I"
        },
        {
          "duration": 0.07,
          "phone": "n_E"
        }
      ],
      "start": 56.3,
      "startOffset": 1027,
      "word": "couldn\u2019t"
    },
    {
      "alignedWord": "hold",
      "case": "success",
      "end": 56.78,
      "endOffset": 1040,
      "phones": [
        {
          "duration": 0.06,
          "phone": "hh_B"
        },
        {
          "duration": 0.05,
          "phone": "ow_I"
        },
        {
          "duration": 0.05,
          "phone": "l_I"
        },
        {
          "duration": 0.05,
          "phone": "d_E"
        }
      ],
      "start": 56.57,
      "startOffset": 1036,
      "word": "hold"
    },
    {
      "alignedWord": "it",
      "case": "success",
      "end": 56.88,
      "endOffset": 1043,
      "phones": [
        {
          "duration": 0.04,
          "phone": "ih_B"
        },
        {
          "duration": 0.06,
          "phone": "t_E"
        }
      ],
      "start": 56.78,
      "startOffset": 1041,
      "word": "it"
    },
    {
      "alignedWord": "back",
      "case": "success",
      "end": 57.120000000000005,
      "endOffset": 1048,
      "phones": [
        {
          "duration": 0.04,
          "phone": "b_B"
        },
        {
          "duration": 0.1,
          "phone": "ae_I"
        },
        {
          "duration": 0.1,
          "phone": "k_E"
        }
      ],
      "start": 56.88,
      "startOffset": 1044,
      "word": "back"
    },
    {
      "alignedWord": "anymore",
      "case": "success",
      "end": 57.62,
      "endOffset": 1056,
      "phones": [
        {
          "duration": 0.05,
          "phone": "eh_B"
        },
        {
          "duration": 0.06,
          "phone": "n_I"
        },
        {
          "duration": 0.07,
          "phone": "iy_I"
        },
        {
          "duration": 0.06,
          "phone": "m_I"
        },
        {
          "duration": 0.08,
          "phone": "ao_I"
        },
        {
          "duration": 0.18,
          "phone": "r_E"
        }
      ],
      "start": 57.12,
      "startOffset": 1049,
      "word": "anymore"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 58.059999999999995,
      "endOffset": 1059,
      "phones": [
        {
          "duration": 0.16,
          "phone": "ay_S"
        }
      ],
      "start": 57.9,
      "startOffset": 1058,
      "word": "I"
    },
    {
      "alignedWord": "left",
      "case": "success",
      "end": 58.300000000000004,
      "endOffset": 1064,
      "phones": [
        {
          "duration": 0.05,
          "phone": "l_B"
        },
        {
          "duration": 0.09,
          "phone": "eh_I"
        },
        {
          "duration": 0.07,
          "phone": "f_I"
        },
        {
          "duration": 0.03,
          "phone": "t_E"
        }
      ],
      "start": 58.06,
      "startOffset": 1060,
      "word": "left"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 58.419999999999995,
      "endOffset": 1068,
      "phones": [
        {
          "duration": 0.05,
          "phone": "dh_B"
        },
        {
          "duration": 0.07,
          "phone": "ah_E"
        }
      ],
      "start": 58.3,
      "startOffset": 1065,
      "word": "the"
    },
    {
      "alignedWord": "room",
      "case": "success",
      "end": 58.68,
      "endOffset": 1073,
      "phones": [
        {
          "duration": 0.09,
          "phone": "r_B"
        },
        {
          "duration": 0.1,
          "phone": "uw_I"
        },
        {
          "duration": 0.07,
          "phone": "m_E"
        }
      ],
      "start": 58.42,
      "startOffset": 1069,
      "word": "room"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 58.79,
      "endOffset": 1076,
      "phones": [
        {
          "duration": 0.04,
          "phone": "t_B"
        },
        {
          "duration": 0.07,
          "phone": "uw_E"
        }
      ],
      "start": 58.68,
      "startOffset": 1074,
      "word": "to"
    },
    {
      "alignedWord": "cry",
      "case": "success",
      "end": 59.06,
      "endOffset": 1080,
      "phones": [
        {
          "duration": 0.08,
          "phone": "k_B"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.13,
          "phone": "ay_E"
        }
      ],
      "start": 58.79,
      "startOffset": 1077,
      "word": "cry"
    },
    {
      "alignedWord": "in",
      "case": "success",
      "end": 59.17,
      "endOffset": 1083,
      "phones": [
        {
          "duration": 0.08,
          "phone": "ih_B"
        },
        {
          "duration": 0.03,
          "phone": "n_E"
        }
      ],
      "start": 59.06,
      "startOffset": 1081,
      "word": "in"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 59.25,
      "endOffset": 1087,
      "phones": [
        {
          "duration": 0.04,
          "phone": "dh_B"
        },
        {
          "duration": 0.04,
          "phone": "ah_E"
        }
      ],
      "start": 59.17,
      "startOffset": 1084,
      "word": "the"
    },
    {
      "alignedWord": "hallway",
      "case": "success",
      "end": 59.77,
      "endOffset": 1095,
      "phones": [
        {
          "duration": 0.05,
          "phone": "hh_B"
        },
        {
          "duration": 0.08,
          "phone": "ao_I"
        },
        {
          "duration": 0.08,
          "phone": "l_I"
        },
        {
          "duration": 0.11,
          "phone": "w_I"
        },
        {
          "duration": 0.2,
          "phone": "ey_E"
        }
      ],
      "start": 59.25,
      "startOffset": 1088,
      "word": "hallway"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 60.19,
      "endOffset": 1098,
      "phones": [
        {
          "duration": 0.12,
          "phone": "ay_S"
        }
      ],
      "start": 60.07,
      "startOffset": 1097,
      "word": "I"
    },
    {
      "alignedWord": "tried",
      "case": "success",
      "end": 60.489999999999995,
      "endOffset": 1104,
      "phones": [
        {
          "duration": 0.09,
          "phone": "t_B"
        },
        {
          "duration": 0.1,
          "phone": "r_I"
        },
        {
          "duration": 0.05,
          "phone": "ay_I"
        },
        {
          "duration": 0.06,
          "phone": "d_E"
        }
      ],
      "start": 60.19,
      "startOffset": 1099,
      "word": "tried"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 60.56,
      "endOffset": 1107,
      "phones": [
        {
          "duration": 0.01,
          "phone": "t_B"
        },
        {
          "duration": 0.06,
          "phone": "ih_E"
        }
      ],
      "start": 60.49,
      "startOffset": 1105,
      "word": "to"
    },
    {
      "alignedWord": "be",
      "case": "success",
      "end": 60.69,
      "endOffset": 1110,
      "phones": [
        {
          "duration": 0.07,
          "phone": "b_B"
        },
        {
          "duration": 0.05,
          "phone": "iy_E"
        }
      ],
      "start": 60.57,
      "startOffset": 1108,
      "word": "be"
    },
    {
      "alignedWord": "as",
      "case": "success",
      "end": 60.839999999999996,
      "endOffset": 1113,
      "phones": [
        {
          "duration": 0.08,
          "phone": "eh_B"
        },
        {
          "duration": 0.07,
          "phone": "z_E"
        }
      ],
      "start": 60.69,
      "startOffset": 1111,
      "word": "as"
    },
    {
      "alignedWord": "quiet",
      "case": "success",
      "end": 61.2,
      "endOffset": 1119,
      "phones": [
        {
          "duration": 0.09,
          "phone": "k_B"
        },
        {
          "duration": 0.08,
          "phone": "w_I"
        },
        {
          "duration": 0.11,
          "phone": "ay_I"
        },
        {
          "duration": 0.06,
          "phone": "ah_I"
        },
        {
          "duration": 0.02,
          "phone": "t_E"
        }
      ],
      "start": 60.84,
      "startOffset": 1114,
      "word": "quiet"
    },
    {
      "alignedWord": "as",
      "case": "success",
      "end": 61.35,
      "endOffset": 1122,
      "phones": [
        {
          "duration": 0.07,
          "phone": "eh_B"
        },
        {
          "duration": 0.08,
          "phone": "z_E"
        }
      ],
      "start": 61.2,
      "startOffset": 1120,
      "word": "as"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 61.46,
      "endOffset": 1124,
      "phones": [
        {
          "duration": 0.11,
          "phone": "ay_S"
        }
      ],
      "start": 61.35,
      "startOffset": 1123,
      "word": "I"
    },
    {
      "alignedWord": "could",
      "case": "success",
      "end": 61.800000000000004,
      "endOffset": 1130,
      "phones": [
        {
          "duration": 0.08,
          "phone": "k_B"
        },
        {
          "duration": 0.17,
          "phone": "uh_I"
        },
        {
          "duration": 0.09,
          "phone": "d_E"
        }
      ],
      "start": 61.46,
      "startOffset": 1125,
      "word": "could"
    },
    {
      "alignedWord": "but",
      "case": "success",
      "end": 62.09,
      "endOffset": 1135,
      "phones": [
        {
          "duration": 0.05,
          "phone": "b_B"
        },
        {
          "duration": 0.06,
          "phone": "ah_I"
        },
        {
          "duration": 0.06,
          "phone": "t_E"
        }
      ],
      "start": 61.92,
      "startOffset": 1132,
      "word": "but"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 62.18000000000001,
      "endOffset": 1137,
      "phones": [
        {
          "duration": 0.09,
          "phone": "ay_S"
        }
      ],
      "start": 62.09,
      "startOffset": 1136,
      "word": "I"
    },
    {
      "alignedWord": "let",
      "case": "success",
      "end": 62.359999,
      "endOffset": 1141,
      "phones": [
        {
          "duration": 0.05,
          "phone": "l_B"
        },
        {
          "duration": 0.07,
          "phone": "eh_I"
        },
        {
          "duration": 0.06,
          "phone": "t_E"
        }
      ],
      "start": 62.179999,
      "startOffset": 1138,
      "word": "let"
    },
    {
      "alignedWord": "some",
      "case": "success",
      "end": 62.56,
      "endOffset": 1146,
      "phones": [
        {
          "duration": 0.06,
          "phone": "s_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.09,
          "phone": "m_E"
        }
      ],
      "start": 62.36,
      "startOffset": 1142,
      "word": "some"
    },
    {
      "alignedWord": "<unk>",
      "case": "success",
      "end": 62.97,
      "endOffset": 1151,
      "phones": [
        {
          "duration": 0.39,
          "phone": "oov_S"
        }
      ],
      "start": 62.58,
      "startOffset": 1147,
      "word": "sobs"
    },
    {
      "alignedWord": "escape",
      "case": "success",
      "end": 63.37,
      "endOffset": 1158,
      "phones": [
        {
          "duration": 0.01,
          "phone": "ih_B"
        },
        {
          "duration": 0.07,
          "phone": "s_I"
        },
        {
          "duration": 0.08,
          "phone": "k_I"
        },
        {
          "duration": 0.16,
          "phone": "ey_I"
        },
        {
          "duration": 0.08,
          "phone": "p_E"
        }
      ],
      "start": 62.97,
      "startOffset": 1152,
      "word": "escape"
    },
    {
      "alignedWord": "they",
      "case": "success",
      "end": 64.23,
      "endOffset": 1164,
      "phones": [
        {
          "duration": 0.09,
          "phone": "dh_B"
        },
        {
          "duration": 0.09,
          "phone": "ey_E"
        }
      ],
      "start": 64.05,
      "startOffset": 1160,
      "word": "They"
    },
    {
      "alignedWord": "continued",
      "case": "success",
      "end": 64.68,
      "endOffset": 1174,
      "phones": [
        {
          "duration": 0.05,
          "phone": "k_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.04,
          "phone": "n_I"
        },
        {
          "duration": 0.06,
          "phone": "t_I"
        },
        {
          "duration": 0.06,
          "phone": "ih_I"
        },
        {
          "duration": 0.05,
          "phone": "n_I"
        },
        {
          "duration": 0.04,
          "phone": "y_I"
        },
        {
          "duration": 0.06,
          "phone": "uw_I"
        },
        {
          "duration": 0.04,
          "phone": "d_E"
        }
      ],
      "start": 64.23,
      "startOffset": 1165,
      "word": "continued"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 64.77999899999999,
      "endOffset": 1177,
      "phones": [
        {
          "duration": 0.04,
          "phone": "t_B"
        },
        {
          "duration": 0.06,
          "phone": "uw_E"
        }
      ],
      "start": 64.679999,
      "startOffset": 1175,
      "word": "to"
    },
    {
      "alignedWord": "play",
      "case": "success",
      "end": 65.03,
      "endOffset": 1182,
      "phones": [
        {
          "duration": 0.07,
          "phone": "p_B"
        },
        {
          "duration": 0.1,
          "phone": "l_I"
        },
        {
          "duration": 0.08,
          "phone": "ey_E"
        }
      ],
      "start": 64.78,
      "startOffset": 1178,
      "word": "play"
    },
    {
      "alignedWord": "without",
      "case": "success",
      "end": 65.39,
      "endOffset": 1190,
      "phones": [
        {
          "duration": 0.06,
          "phone": "w_B"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.08,
          "phone": "th_I"
        },
        {
          "duration": 0.09,
          "phone": "aw_I"
        },
        {
          "duration": 0.08,
          "phone": "t_E"
        }
      ],
      "start": 65.03,
      "startOffset": 1183,
      "word": "without"
    },
    {
      "alignedWord": "me",
      "case": "success",
      "end": 65.56999900000001,
      "endOffset": 1193,
      "phones": [
        {
          "duration": 0.08,
          "phone": "m_B"
        },
        {
          "duration": 0.1,
          "phone": "iy_E"
        }
      ],
      "start": 65.389999,
      "startOffset": 1191,
      "word": "me"
    },
    {
      "alignedWord": "until",
      "case": "success",
      "end": 65.83,
      "endOffset": 1199,
      "phones": [
        {
          "duration": 0.04,
          "phone": "ah_B"
        },
        {
          "duration": 0.08,
          "phone": "n_I"
        },
        {
          "duration": 0.03,
          "phone": "t_I"
        },
        {
          "duration": 0.04,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "l_E"
        }
      ],
      "start": 65.57,
      "startOffset": 1194,
      "word": "until"
    },
    {
      "alignedWord": "they",
      "case": "success",
      "end": 65.95,
      "endOffset": 1204,
      "phones": [
        {
          "duration": 0.05,
          "phone": "dh_B"
        },
        {
          "duration": 0.07,
          "phone": "ey_E"
        }
      ],
      "start": 65.83,
      "startOffset": 1200,
      "word": "they"
    },
    {
      "alignedWord": "needed",
      "case": "success",
      "end": 66.22,
      "endOffset": 1211,
      "phones": [
        {
          "duration": 0.05,
          "phone": "n_B"
        },
        {
          "duration": 0.08,
          "phone": "iy_I"
        },
        {
          "duration": 0.05,
          "phone": "d_I"
        },
        {
          "duration": 0.04,
          "phone": "ah_I"
        },
        {
          "duration": 0.05,
          "phone": "d_E"
        }
      ],
      "start": 65.95,
      "startOffset": 1205,
      "word": "needed"
    },
    {
      "alignedWord": "me",
      "case": "success",
      "end": 66.339999,
      "endOffset": 1214,
      "phones": [
        {
          "duration": 0.04,
          "phone": "m_B"
        },
        {
          "duration": 0.08,
          "phone": "iy_E"
        }
      ],
      "start": 66.219999,
      "startOffset": 1212,
      "word": "me"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 66.45,
      "endOffset": 1217,
      "phones": [
        {
          "duration": 0.05,
          "phone": "t_B"
        },
        {
          "duration": 0.06,
          "phone": "ah_E"
        }
      ],
      "start": 66.34,
      "startOffset": 1215,
      "word": "to"
    },
    {
      "alignedWord": "roll",
      "case": "success",
      "end": 66.68,
      "endOffset": 1222,
      "phones": [
        {
          "duration": 0.08,
          "phone": "r_B"
        },
        {
          "duration": 0.08,
          "phone": "ow_I"
        },
        {
          "duration": 0.07,
          "phone": "l_E"
        }
      ],
      "start": 66.45,
      "startOffset": 1218,
      "word": "roll"
    },
    {
      "alignedWord": "for",
      "case": "success",
      "end": 66.819999,
      "endOffset": 1226,
      "phones": [
        {
          "duration": 0.08,
          "phone": "f_B"
        },
        {
          "duration": 0.06,
          "phone": "er_E"
        }
      ],
      "start": 66.679999,
      "startOffset": 1223,
      "word": "for"
    },
    {
      "alignedWord": "initiative",
      "case": "success",
      "end": 67.36999999999999,
      "endOffset": 1237,
      "phones": [
        {
          "duration": 0.06,
          "phone": "ih_B"
        },
        {
          "duration": 0.05,
          "phone": "n_I"
        },
        {
          "duration": 0.07,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "sh_I"
        },
        {
          "duration": 0.06,
          "phone": "ah_I"
        },
        {
          "duration": 0.05,
          "phone": "t_I"
        },
        {
          "duration": 0.09,
          "phone": "ih_I"
        },
        {
          "duration": 0.1,
          "phone": "v_E"
        }
      ],
      "start": 66.82,
      "startOffset": 1227,
      "word": "initiative"
    },
    {
      "alignedWord": "after",
      "case": "success",
      "end": 68.34,
      "endOffset": 1247,
      "phones": [
        {
          "duration": 0.12,
          "phone": "ae_B"
        },
        {
          "duration": 0.08,
          "phone": "f_I"
        },
        {
          "duration": 0.06,
          "phone": "t_I"
        },
        {
          "duration": 0.05,
          "phone": "er_E"
        }
      ],
      "start": 68.03,
      "startOffset": 1242,
      "word": "After"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 68.43,
      "endOffset": 1251,
      "phones": [
        {
          "duration": 0.04,
          "phone": "dh_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_E"
        }
      ],
      "start": 68.34,
      "startOffset": 1248,
      "word": "the"
    },
    {
      "alignedWord": "game",
      "case": "success",
      "end": 68.86999899999999,
      "endOffset": 1256,
      "phones": [
        {
          "duration": 0.09,
          "phone": "g_B"
        },
        {
          "duration": 0.21,
          "phone": "ey_I"
        },
        {
          "duration": 0.14,
          "phone": "m_E"
        }
      ],
      "start": 68.429999,
      "startOffset": 1252,
      "word": "game"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 69.12,
      "endOffset": 1259,
      "phones": [
        {
          "duration": 0.12,
          "phone": "ay_S"
        }
      ],
      "start": 69.0,
      "startOffset": 1258,
      "word": "I"
    },
    {
      "alignedWord": "told",
      "case": "success",
      "end": 69.39,
      "endOffset": 1264,
      "phones": [
        {
          "duration": 0.08,
          "phone": "t_B"
        },
        {
          "duration": 0.1,
          "phone": "ow_I"
        },
        {
          "duration": 0.01,
          "phone": "l_I"
        },
        {
          "duration": 0.08,
          "phone": "d_E"
        }
      ],
      "start": 69.12,
      "startOffset": 1260,
      "word": "told"
    },
    {
      "alignedWord": "my",
      "case": "success",
      "end": 69.53999900000001,
      "endOffset": 1267,
      "phones": [
        {
          "duration": 0.04,
          "phone": "m_B"
        },
        {
          "duration": 0.11,
          "phone": "ay_E"
        }
      ],
      "start": 69.389999,
      "startOffset": 1265,
      "word": "my"
    },
    {
      "alignedWord": "former",
      "case": "success",
      "end": 69.88,
      "endOffset": 1274,
      "phones": [
        {
          "duration": 0.08,
          "phone": "f_B"
        },
        {
          "duration": 0.07,
          "phone": "ao_I"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.05,
          "phone": "m_I"
        },
        {
          "duration": 0.08,
          "phone": "er_E"
        }
      ],
      "start": 69.53999999999999,
      "startOffset": 1268,
      "word": "former"
    },
    {
      "alignedWord": "wife",
      "case": "success",
      "end": 70.19,
      "endOffset": 1279,
      "phones": [
        {
          "duration": 0.09,
          "phone": "w_B"
        },
        {
          "duration": 0.14,
          "phone": "ay_I"
        },
        {
          "duration": 0.08,
          "phone": "f_E"
        }
      ],
      "start": 69.88,
      "startOffset": 1275,
      "word": "wife"
    },
    {
      "alignedWord": "that",
      "case": "success",
      "end": 70.32999899999999,
      "endOffset": 1284,
      "phones": [
        {
          "duration": 0.04,
          "phone": "dh_B"
        },
        {
          "duration": 0.04,
          "phone": "ah_I"
        },
        {
          "duration": 0.05,
          "phone": "t_E"
        }
      ],
      "start": 70.19999899999999,
      "startOffset": 1280,
      "word": "that"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 70.39999999999999,
      "endOffset": 1286,
      "phones": [
        {
          "duration": 0.07,
          "phone": "ay_S"
        }
      ],
      "start": 70.33,
      "startOffset": 1285,
      "word": "I"
    },
    {
      "alignedWord": "don't",
      "case": "success",
      "end": 70.61999999999999,
      "endOffset": 1292,
      "phones": [
        {
          "duration": 0.05,
          "phone": "d_B"
        },
        {
          "duration": 0.08,
          "phone": "ow_I"
        },
        {
          "duration": 0.05,
          "phone": "n_I"
        },
        {
          "duration": 0.03,
          "phone": "t_E"
        }
      ],
      "start": 70.41,
      "startOffset": 1287,
      "word": "don\u2019t"
    },
    {
      "alignedWord": "think",
      "case": "success",
      "end": 70.849999,
      "endOffset": 1298,
      "phones": [
        {
          "duration": 0.06,
          "phone": "th_B"
        },
        {
          "duration": 0.03,
          "phone": "ih_I"
        },
        {
          "duration": 0.06,
          "phone": "ng_I"
        },
        {
          "duration": 0.07,
          "phone": "k_E"
        }
      ],
      "start": 70.629999,
      "startOffset": 1293,
      "word": "think"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 70.91,
      "endOffset": 1300,
      "phones": [
        {
          "duration": 0.06,
          "phone": "ay_S"
        }
      ],
      "start": 70.85,
      "startOffset": 1299,
      "word": "I"
    },
    {
      "alignedWord": "will",
      "case": "success",
      "end": 71.05,
      "endOffset": 1305,
      "phones": [
        {
          "duration": 0.04,
          "phone": "w_B"
        },
        {
          "duration": 0.06,
          "phone": "ih_I"
        },
        {
          "duration": 0.04,
          "phone": "l_E"
        }
      ],
      "start": 70.91,
      "startOffset": 1301,
      "word": "will"
    },
    {
      "alignedWord": "be",
      "case": "success",
      "end": 71.169999,
      "endOffset": 1308,
      "phones": [
        {
          "duration": 0.05,
          "phone": "b_B"
        },
        {
          "duration": 0.07,
          "phone": "iy_E"
        }
      ],
      "start": 71.049999,
      "startOffset": 1306,
      "word": "be"
    },
    {
      "alignedWord": "attending",
      "case": "success",
      "end": 71.53,
      "endOffset": 1318,
      "phones": [
        {
          "duration": 0.04,
          "phone": "ah_B"
        },
        {
          "duration": 0.08,
          "phone": "t_I"
        },
        {
          "duration": 0.06,
          "phone": "eh_I"
        },
        {
          "duration": 0.04,
          "phone": "n_I"
        },
        {
          "duration": 0.05,
          "phone": "d_I"
        },
        {
          "duration": 0.03,
          "phone": "ih_I"
        },
        {
          "duration": 0.06,
          "phone": "ng_E"
        }
      ],
      "start": 71.17,
      "startOffset": 1309,
      "word": "attending"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 71.609999,
      "endOffset": 1322,
      "phones": [
        {
          "duration": 0.03,
          "phone": "dh_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_E"
        }
      ],
      "start": 71.529999,
      "startOffset": 1319,
      "word": "the"
    },
    {
      "alignedWord": "next",
      "case": "success",
      "end": 71.809999,
      "endOffset": 1327,
      "phones": [
        {
          "duration": 0.07,
          "phone": "n_B"
        },
        {
          "duration": 0.05,
          "phone": "eh_I"
        },
        {
          "duration": 0.07,
          "phone": "k_I"
        },
        {
          "duration": 0.01,
          "phone": "s_E"
        }
      ],
      "start": 71.609999,
      "startOffset": 1323,
      "word": "next"
    },
    {
      "alignedWord": "session",
      "case": "success",
      "end": 72.31999900000001,
      "endOffset": 1335,
      "phones": [
        {
          "duration": 0.15,
          "phone": "s_B"
        },
        {
          "duration": 0.07,
          "phone": "eh_I"
        },
        {
          "duration": 0.1,
          "phone": "sh_I"
        },
        {
          "duration": 0.08,
          "phone": "ah_I"
        },
        {
          "duration": 0.11,
          "phone": "n_E"
        }
      ],
      "start": 71.809999,
      "startOffset": 1328,
      "word": "session"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 73.18,
      "endOffset": 1340,
      "phones": [
        {
          "duration": 0.12,
          "phone": "sh_B"
        },
        {
          "duration": 0.08,
          "phone": "iy_E"
        }
      ],
      "start": 72.98,
      "startOffset": 1337,
      "word": "She"
    },
    {
      "alignedWord": "says",
      "case": "success",
      "end": 73.429999,
      "endOffset": 1345,
      "phones": [
        {
          "duration": 0.07,
          "phone": "s_B"
        },
        {
          "duration": 0.09,
          "phone": "eh_I"
        },
        {
          "duration": 0.06,
          "phone": "z_E"
        }
      ],
      "start": 73.209999,
      "startOffset": 1341,
      "word": "says"
    },
    {
      "alignedWord": "that's",
      "case": "success",
      "end": 73.679999,
      "endOffset": 1352,
      "phones": [
        {
          "duration": 0.06,
          "phone": "dh_B"
        },
        {
          "duration": 0.06,
          "phone": "ae_I"
        },
        {
          "duration": 0.05,
          "phone": "t_I"
        },
        {
          "duration": 0.07,
          "phone": "s_E"
        }
      ],
      "start": 73.439999,
      "startOffset": 1346,
      "word": "that\u2019s"
    },
    {
      "alignedWord": "ridiculous",
      "case": "success",
      "end": 74.27999899999999,
      "endOffset": 1363,
      "phones": [
        {
          "duration": 0.01,
          "phone": "r_B"
        },
        {
          "duration": 0.03,
          "phone": "ih_I"
        },
        {
          "duration": 0.03,
          "phone": "d_I"
        },
        {
          "duration": 0.07,
          "phone": "ih_I"
        },
        {
          "duration": 0.08,
          "phone": "k_I"
        },
        {
          "duration": 0.04,
          "phone": "y_I"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.05,
          "phone": "l_I"
        },
        {
          "duration": 0.11,
          "phone": "ah_I"
        },
        {
          "duration": 0.08,
          "phone": "s_E"
        }
      ],
      "start": 73.72999899999999,
      "startOffset": 1353,
      "word": "ridiculous"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 74.77,
      "endOffset": 1368,
      "phones": [
        {
          "duration": 0.11,
          "phone": "sh_B"
        },
        {
          "duration": 0.1,
          "phone": "iy_E"
        }
      ],
      "start": 74.56,
      "startOffset": 1365,
      "word": "She"
    },
    {
      "alignedWord": "said",
      "case": "success",
      "end": 75.00999999999999,
      "endOffset": 1373,
      "phones": [
        {
          "duration": 0.07,
          "phone": "s_B"
        },
        {
          "duration": 0.07,
          "phone": "eh_I"
        },
        {
          "duration": 0.07,
          "phone": "d_E"
        }
      ],
      "start": 74.8,
      "startOffset": 1369,
      "word": "said"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 75.17,
      "endOffset": 1377,
      "phones": [
        {
          "duration": 0.07,
          "phone": "sh_B"
        },
        {
          "duration": 0.09,
          "phone": "iy_E"
        }
      ],
      "start": 75.01,
      "startOffset": 1374,
      "word": "she"
    },
    {
      "alignedWord": "talked",
      "case": "success",
      "end": 75.42,
      "endOffset": 1384,
      "phones": [
        {
          "duration": 0.05,
          "phone": "t_B"
        },
        {
          "duration": 0.12,
          "phone": "ao_I"
        },
        {
          "duration": 0.05,
          "phone": "k_I"
        },
        {
          "duration": 0.03,
          "phone": "t_E"
        }
      ],
      "start": 75.17,
      "startOffset": 1378,
      "word": "talked"
    },
    {
      "alignedWord": "to",
      "case": "success",
      "end": 75.53,
      "endOffset": 1387,
      "phones": [
        {
          "duration": 0.04,
          "phone": "t_B"
        },
        {
          "duration": 0.07,
          "phone": "uw_E"
        }
      ],
      "start": 75.42,
      "startOffset": 1385,
      "word": "to"
    },
    {
      "alignedWord": "her",
      "case": "success",
      "end": 75.65,
      "endOffset": 1391,
      "phones": [
        {
          "duration": 0.05,
          "phone": "hh_B"
        },
        {
          "duration": 0.07,
          "phone": "er_E"
        }
      ],
      "start": 75.53,
      "startOffset": 1388,
      "word": "her"
    },
    {
      "alignedWord": "friend",
      "case": "success",
      "end": 75.97,
      "endOffset": 1398,
      "phones": [
        {
          "duration": 0.07,
          "phone": "f_B"
        },
        {
          "duration": 0.05,
          "phone": "r_I"
        },
        {
          "duration": 0.09,
          "phone": "eh_I"
        },
        {
          "duration": 0.07,
          "phone": "n_I"
        },
        {
          "duration": 0.04,
          "phone": "d_E"
        }
      ],
      "start": 75.65,
      "startOffset": 1392,
      "word": "friend"
    },
    {
      "alignedWord": "after",
      "case": "success",
      "end": 76.23,
      "endOffset": 1404,
      "phones": [
        {
          "duration": 0.08,
          "phone": "ae_B"
        },
        {
          "duration": 0.06,
          "phone": "f_I"
        },
        {
          "duration": 0.06,
          "phone": "t_I"
        },
        {
          "duration": 0.06,
          "phone": "er_E"
        }
      ],
      "start": 75.97,
      "startOffset": 1399,
      "word": "after"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 76.31,
      "endOffset": 1408,
      "phones": [
        {
          "duration": 0.03,
          "phone": "dh_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_E"
        }
      ],
      "start": 76.23,
      "startOffset": 1405,
      "word": "the"
    },
    {
      "alignedWord": "game",
      "case": "success",
      "end": 76.69,
      "endOffset": 1413,
      "phones": [
        {
          "duration": 0.07,
          "phone": "g_B"
        },
        {
          "duration": 0.19,
          "phone": "ey_I"
        },
        {
          "duration": 0.12,
          "phone": "m_E"
        }
      ],
      "start": 76.31,
      "startOffset": 1409,
      "word": "game"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 77.22,
      "endOffset": 1418,
      "phones": [
        {
          "duration": 0.14,
          "phone": "sh_B"
        },
        {
          "duration": 0.08,
          "phone": "iy_E"
        }
      ],
      "start": 77.0,
      "startOffset": 1415,
      "word": "She"
    },
    {
      "alignedWord": "says",
      "case": "success",
      "end": 77.46,
      "endOffset": 1423,
      "phones": [
        {
          "duration": 0.09,
          "phone": "s_B"
        },
        {
          "duration": 0.1,
          "phone": "eh_I"
        },
        {
          "duration": 0.05,
          "phone": "z_E"
        }
      ],
      "start": 77.22,
      "startOffset": 1419,
      "word": "says"
    },
    {
      "alignedWord": "her",
      "case": "success",
      "end": 77.6,
      "endOffset": 1427,
      "phones": [
        {
          "duration": 0.06,
          "phone": "hh_B"
        },
        {
          "duration": 0.08,
          "phone": "er_E"
        }
      ],
      "start": 77.46,
      "startOffset": 1424,
      "word": "her"
    },
    {
      "alignedWord": "friend",
      "case": "success",
      "end": 77.88,
      "endOffset": 1434,
      "phones": [
        {
          "duration": 0.07,
          "phone": "f_B"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.07,
          "phone": "eh_I"
        },
        {
          "duration": 0.07,
          "phone": "n_I"
        },
        {
          "duration": 0.01,
          "phone": "d_E"
        }
      ],
      "start": 77.6,
      "startOffset": 1428,
      "word": "friend"
    },
    {
      "alignedWord": "and",
      "case": "success",
      "end": 78.00999999999999,
      "endOffset": 1438,
      "phones": [
        {
          "duration": 0.06,
          "phone": "ae_B"
        },
        {
          "duration": 0.04,
          "phone": "n_I"
        },
        {
          "duration": 0.03,
          "phone": "d_E"
        }
      ],
      "start": 77.88,
      "startOffset": 1435,
      "word": "and"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 78.11,
      "endOffset": 1442,
      "phones": [
        {
          "duration": 0.02,
          "phone": "dh_B"
        },
        {
          "duration": 0.08,
          "phone": "ah_E"
        }
      ],
      "start": 78.01,
      "startOffset": 1439,
      "word": "the"
    },
    {
      "alignedWord": "<unk>",
      "case": "success",
      "end": 78.47,
      "endOffset": 1445,
      "phones": [
        {
          "duration": 0.36,
          "phone": "oov_S"
        }
      ],
      "start": 78.11,
      "startOffset": 1443,
      "word": "DM"
    },
    {
      "alignedWord": "had",
      "case": "success",
      "end": 78.66000000000001,
      "endOffset": 1449,
      "phones": [
        {
          "duration": 0.07,
          "phone": "hh_B"
        },
        {
          "duration": 0.06,
          "phone": "ae_I"
        },
        {
          "duration": 0.05,
          "phone": "d_E"
        }
      ],
      "start": 78.48,
      "startOffset": 1446,
      "word": "had"
    },
    {
      "alignedWord": "been",
      "case": "success",
      "end": 78.8,
      "endOffset": 1454,
      "phones": [
        {
          "duration": 0.04,
          "phone": "b_B"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.05,
          "phone": "n_E"
        }
      ],
      "start": 78.66,
      "startOffset": 1450,
      "word": "been"
    },
    {
      "alignedWord": "planning",
      "case": "success",
      "end": 79.17,
      "endOffset": 1463,
      "phones": [
        {
          "duration": 0.07,
          "phone": "p_B"
        },
        {
          "duration": 0.06,
          "phone": "l_I"
        },
        {
          "duration": 0.09,
          "phone": "ae_I"
        },
        {
          "duration": 0.04,
          "phone": "n_I"
        },
        {
          "duration": 0.04,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "ng_E"
        }
      ],
      "start": 78.8,
      "startOffset": 1455,
      "word": "planning"
    },
    {
      "alignedWord": "that",
      "case": "success",
      "end": 79.34,
      "endOffset": 1468,
      "phones": [
        {
          "duration": 0.04,
          "phone": "dh_B"
        },
        {
          "duration": 0.05,
          "phone": "ae_I"
        },
        {
          "duration": 0.08,
          "phone": "t_E"
        }
      ],
      "start": 79.17,
      "startOffset": 1464,
      "word": "that"
    },
    {
      "alignedWord": "character",
      "case": "success",
      "end": 79.78,
      "endOffset": 1478,
      "phones": [
        {
          "duration": 0.06,
          "phone": "k_B"
        },
        {
          "duration": 0.09,
          "phone": "eh_I"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.04,
          "phone": "ih_I"
        },
        {
          "duration": 0.03,
          "phone": "k_I"
        },
        {
          "duration": 0.09,
          "phone": "t_I"
        },
        {
          "duration": 0.07,
          "phone": "er_E"
        }
      ],
      "start": 79.34,
      "startOffset": 1469,
      "word": "character"
    },
    {
      "alignedWord": "for",
      "case": "success",
      "end": 79.9,
      "endOffset": 1482,
      "phones": [
        {
          "duration": 0.06,
          "phone": "f_B"
        },
        {
          "duration": 0.06,
          "phone": "er_E"
        }
      ],
      "start": 79.78,
      "startOffset": 1479,
      "word": "for"
    },
    {
      "alignedWord": "months",
      "case": "success",
      "end": 80.22,
      "endOffset": 1489,
      "phones": [
        {
          "duration": 0.06,
          "phone": "m_B"
        },
        {
          "duration": 0.12,
          "phone": "ah_I"
        },
        {
          "duration": 0.08,
          "phone": "n_I"
        },
        {
          "duration": 0.04,
          "phone": "th_I"
        },
        {
          "duration": 0.02,
          "phone": "s_E"
        }
      ],
      "start": 79.9,
      "startOffset": 1483,
      "word": "months"
    },
    {
      "alignedWord": "the",
      "case": "success",
      "end": 81.19,
      "endOffset": 1494,
      "phones": [
        {
          "duration": 0.09,
          "phone": "dh_B"
        },
        {
          "duration": 0.06,
          "phone": "ah_E"
        }
      ],
      "start": 81.03999999999999,
      "startOffset": 1491,
      "word": "The"
    },
    {
      "alignedWord": "timing",
      "case": "success",
      "end": 81.59,
      "endOffset": 1501,
      "phones": [
        {
          "duration": 0.08,
          "phone": "t_B"
        },
        {
          "duration": 0.13,
          "phone": "ay_I"
        },
        {
          "duration": 0.06,
          "phone": "m_I"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.08,
          "phone": "ng_E"
        }
      ],
      "start": 81.19,
      "startOffset": 1495,
      "word": "timing"
    },
    {
      "alignedWord": "was",
      "case": "success",
      "end": 81.73,
      "endOffset": 1505,
      "phones": [
        {
          "duration": 0.03,
          "phone": "w_B"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.06,
          "phone": "z_E"
        }
      ],
      "start": 81.59,
      "startOffset": 1502,
      "word": "was"
    },
    {
      "alignedWord": "purely",
      "case": "success",
      "end": 82.13,
      "endOffset": 1512,
      "phones": [
        {
          "duration": 0.08,
          "phone": "p_B"
        },
        {
          "duration": 0.01,
          "phone": "y_I"
        },
        {
          "duration": 0.08,
          "phone": "uh_I"
        },
        {
          "duration": 0.07,
          "phone": "r_I"
        },
        {
          "duration": 0.07,
          "phone": "l_I"
        },
        {
          "duration": 0.08,
          "phone": "iy_E"
        }
      ],
      "start": 81.74,
      "startOffset": 1506,
      "word": "purely"
    },
    {
      "alignedWord": "coincidental",
      "case": "success",
      "end": 82.94,
      "endOffset": 1525,
      "phones": [
        {
          "duration": 0.07,
          "phone": "k_B"
        },
        {
          "duration": 0.09,
          "phone": "ow_I"
        },
        {
          "duration": 0.04,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "n_I"
        },
        {
          "duration": 0.07,
          "phone": "s_I"
        },
        {
          "duration": 0.05,
          "phone": "ah_I"
        },
        {
          "duration": 0.07,
          "phone": "d_I"
        },
        {
          "duration": 0.06,
          "phone": "eh_I"
        },
        {
          "duration": 0.05,
          "phone": "n_I"
        },
        {
          "duration": 0.06,
          "phone": "t_I"
        },
        {
          "duration": 0.08,
          "phone": "ah_I"
        },
        {
          "duration": 0.1,
          "phone": "l_E"
        }
      ],
      "start": 82.13,
      "startOffset": 1513,
      "word": "coincidental"
    },
    {
      "alignedWord": "and",
      "case": "success",
      "end": 83.2,
      "endOffset": 1530,
      "phones": [
        {
          "duration": 0.09,
          "phone": "ae_B"
        },
        {
          "duration": 0.06,
          "phone": "n_I"
        },
        {
          "duration": 0.05,
          "phone": "d_E"
        }
      ],
      "start": 83.0,
      "startOffset": 1527,
      "word": "and"
    },
    {
      "alignedWord": "she",
      "case": "success",
      "end": 83.35000000000001,
      "endOffset": 1534,
      "phones": [
        {
          "duration": 0.06,
          "phone": "sh_B"
        },
        {
          "duration": 0.08,
          "phone": "iy_E"
        }
      ],
      "start": 83.21000000000001,
      "startOffset": 1531,
      "word": "she"
    },
    {
      "alignedWord": "merely",
      "case": "success",
      "end": 83.69999899999999,
      "endOffset": 1541,
      "phones": [
        {
          "duration": 0.05,
          "phone": "m_B"
        },
        {
          "duration": 0.11,
          "phone": "ih_I"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.06,
          "phone": "l_I"
        },
        {
          "duration": 0.07,
          "phone": "iy_E"
        }
      ],
      "start": 83.349999,
      "startOffset": 1535,
      "word": "merely"
    },
    {
      "alignedWord": "misspoke",
      "case": "success",
      "end": 84.28,
      "endOffset": 1550,
      "phones": [
        {
          "duration": 0.05,
          "phone": "m_B"
        },
        {
          "duration": 0.07,
          "phone": "ih_I"
        },
        {
          "duration": 0.08,
          "phone": "s_I"
        },
        {
          "duration": 0.1,
          "phone": "p_I"
        },
        {
          "duration": 0.16,
          "phone": "ow_I"
        },
        {
          "duration": 0.12,
          "phone": "k_E"
        }
      ],
      "start": 83.7,
      "startOffset": 1542,
      "word": "misspoke"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 84.72,
      "endOffset": 1556,
      "phones": [
        {
          "duration": 0.14,
          "phone": "ay_S"
        }
      ],
      "start": 84.58,
      "startOffset": 1555,
      "word": "I"
    },
    {
      "alignedWord": "was",
      "case": "success",
      "end": 84.889999,
      "endOffset": 1560,
      "phones": [
        {
          "duration": 0.04,
          "phone": "w_B"
        },
        {
          "duration": 0.07,
          "phone": "ah_I"
        },
        {
          "duration": 0.06,
          "phone": "z_E"
        }
      ],
      "start": 84.719999,
      "startOffset": 1557,
      "word": "was"
    },
    {
      "alignedWord": "a",
      "case": "success",
      "end": 84.969999,
      "endOffset": 1562,
      "phones": [
        {
          "duration": 0.08,
          "phone": "ah_S"
        }
      ],
      "start": 84.889999,
      "startOffset": 1561,
      "word": "a"
    },
    {
      "alignedWord": "founding",
      "case": "success",
      "end": 85.379999,
      "endOffset": 1571,
      "phones": [
        {
          "duration": 0.1,
          "phone": "f_B"
        },
        {
          "duration": 0.1,
          "phone": "aw_I"
        },
        {
          "duration": 0.04,
          "phone": "n_I"
        },
        {
          "duration": 0.05,
          "phone": "d_I"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "ng_E"
        }
      ],
      "start": 84.969999,
      "startOffset": 1563,
      "word": "founding"
    },
    {
      "alignedWord": "member",
      "case": "success",
      "end": 85.66,
      "endOffset": 1578,
      "phones": [
        {
          "duration": 0.02,
          "phone": "m_B"
        },
        {
          "duration": 0.1,
          "phone": "eh_I"
        },
        {
          "duration": 0.05,
          "phone": "m_I"
        },
        {
          "duration": 0.05,
          "phone": "b_I"
        },
        {
          "duration": 0.06,
          "phone": "er_E"
        }
      ],
      "start": 85.38,
      "startOffset": 1572,
      "word": "member"
    },
    {
      "alignedWord": "of",
      "case": "success",
      "end": 85.77,
      "endOffset": 1581,
      "phones": [
        {
          "duration": 0.05,
          "phone": "ah_B"
        },
        {
          "duration": 0.06,
          "phone": "v_E"
        }
      ],
      "start": 85.66,
      "startOffset": 1579,
      "word": "of"
    },
    {
      "alignedWord": "this",
      "case": "success",
      "end": 85.89999999999999,
      "endOffset": 1586,
      "phones": [
        {
          "duration": 0.01,
          "phone": "dh_B"
        },
        {
          "duration": 0.06,
          "phone": "ih_I"
        },
        {
          "duration": 0.06,
          "phone": "s_E"
        }
      ],
      "start": 85.77,
      "startOffset": 1582,
      "word": "this"
    },
    {
      "alignedWord": "campaign",
      "case": "success",
      "end": 86.53,
      "endOffset": 1595,
      "phones": [
        {
          "duration": 0.08,
          "phone": "k_B"
        },
        {
          "duration": 0.07,
          "phone": "ae_I"
        },
        {
          "duration": 0.07,
          "phone": "m_I"
        },
        {
          "duration": 0.06,
          "phone": "p_I"
        },
        {
          "duration": 0.2,
          "phone": "ey_I"
        },
        {
          "duration": 0.13,
          "phone": "n_E"
        }
      ],
      "start": 85.92,
      "startOffset": 1587,
      "word": "campaign"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 86.95,
      "endOffset": 1598,
      "phones": [
        {
          "duration": 0.12,
          "phone": "ay_S"
        }
      ],
      "start": 86.83,
      "startOffset": 1597,
      "word": "I"
    },
    {
      "alignedWord": "have",
      "case": "success",
      "end": 87.11,
      "endOffset": 1603,
      "phones": [
        {
          "duration": 0.06,
          "phone": "hh_B"
        },
        {
          "duration": 0.05,
          "phone": "ae_I"
        },
        {
          "duration": 0.05,
          "phone": "v_E"
        }
      ],
      "start": 86.95,
      "startOffset": 1599,
      "word": "have"
    },
    {
      "alignedWord": "played",
      "case": "success",
      "end": 87.38,
      "endOffset": 1610,
      "phones": [
        {
          "duration": 0.07,
          "phone": "p_B"
        },
        {
          "duration": 0.08,
          "phone": "l_I"
        },
        {
          "duration": 0.06,
          "phone": "ey_I"
        },
        {
          "duration": 0.06,
          "phone": "d_E"
        }
      ],
      "start": 87.11,
      "startOffset": 1604,
      "word": "played"
    },
    {
      "alignedWord": "this",
      "case": "success",
      "end": 87.50999999999999,
      "endOffset": 1615,
      "phones": [
        {
          "duration": 0.01,
          "phone": "dh_B"
        },
        {
          "duration": 0.08,
          "phone": "ih_I"
        },
        {
          "duration": 0.04,
          "phone": "s_E"
        }
      ],
      "start": 87.38,
      "startOffset": 1611,
      "word": "this"
    },
    {
      "alignedWord": "character",
      "case": "success",
      "end": 87.97999899999999,
      "endOffset": 1625,
      "phones": [
        {
          "duration": 0.1,
          "phone": "k_B"
        },
        {
          "duration": 0.08,
          "phone": "eh_I"
        },
        {
          "duration": 0.05,
          "phone": "r_I"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.03,
          "phone": "k_I"
        },
        {
          "duration": 0.09,
          "phone": "t_I"
        },
        {
          "duration": 0.07,
          "phone": "er_E"
        }
      ],
      "start": 87.509999,
      "startOffset": 1616,
      "word": "character"
    },
    {
      "alignedWord": "for",
      "case": "success",
      "end": 88.11,
      "endOffset": 1629,
      "phones": [
        {
          "duration": 0.06,
          "phone": "f_B"
        },
        {
          "duration": 0.07,
          "phone": "er_E"
        }
      ],
      "start": 87.98,
      "startOffset": 1626,
      "word": "for"
    },
    {
      "alignedWord": "years",
      "case": "success",
      "end": 88.50999900000001,
      "endOffset": 1635,
      "phones": [
        {
          "duration": 0.14,
          "phone": "y_B"
        },
        {
          "duration": 0.09,
          "phone": "ih_I"
        },
        {
          "duration": 0.09,
          "phone": "r_I"
        },
        {
          "duration": 0.08,
          "phone": "z_E"
        }
      ],
      "start": 88.109999,
      "startOffset": 1630,
      "word": "years"
    },
    {
      "alignedWord": "so",
      "case": "success",
      "end": 89.13,
      "endOffset": 1639,
      "phones": [
        {
          "duration": 0.14,
          "phone": "s_B"
        },
        {
          "duration": 0.08,
          "phone": "ow_E"
        }
      ],
      "start": 88.91,
      "startOffset": 1637,
      "word": "So"
    },
    {
      "alignedWord": "many",
      "case": "success",
      "end": 89.419999,
      "endOffset": 1644,
      "phones": [
        {
          "duration": 0.06,
          "phone": "m_B"
        },
        {
          "duration": 0.07,
          "phone": "eh_I"
        },
        {
          "duration": 0.06,
          "phone": "n_I"
        },
        {
          "duration": 0.1,
          "phone": "iy_E"
        }
      ],
      "start": 89.129999,
      "startOffset": 1640,
      "word": "many"
    },
    {
      "alignedWord": "hours",
      "case": "success",
      "end": 89.81,
      "endOffset": 1650,
      "phones": [
        {
          "duration": 0.19,
          "phone": "aw_B"
        },
        {
          "duration": 0.11,
          "phone": "er_I"
        },
        {
          "duration": 0.09,
          "phone": "z_E"
        }
      ],
      "start": 89.42,
      "startOffset": 1645,
      "word": "hours"
    },
    {
      "alignedWord": "days",
      "case": "success",
      "end": 90.199999,
      "endOffset": 1656,
      "phones": [
        {
          "duration": 0.12,
          "phone": "d_B"
        },
        {
          "duration": 0.11,
          "phone": "ey_I"
        },
        {
          "duration": 0.08,
          "phone": "z_E"
        }
      ],
      "start": 89.889999,
      "startOffset": 1652,
      "word": "days"
    },
    {
      "alignedWord": "spent",
      "case": "success",
      "end": 90.579999,
      "endOffset": 1662,
      "phones": [
        {
          "duration": 0.01,
          "phone": "s_B"
        },
        {
          "duration": 0.08,
          "phone": "p_I"
        },
        {
          "duration": 0.12,
          "phone": "eh_I"
        },
        {
          "duration": 0.08,
          "phone": "n_I"
        },
        {
          "duration": 0.07,
          "phone": "t_E"
        }
      ],
      "start": 90.219999,
      "startOffset": 1657,
      "word": "spent"
    },
    {
      "case": "not-found-in-audio",
      "endOffset": 1665,
      "startOffset": 1664,
      "word": "I"
    },
    {
      "alignedWord": "don't",
      "case": "success",
      "end": 91.269999,
      "endOffset": 1671,
      "phones": [
        {
          "duration": 0.06,
          "phone": "d_B"
        },
        {
          "duration": 0.08,
          "phone": "ow_I"
        },
        {
          "duration": 0.04,
          "phone": "n_I"
        },
        {
          "duration": 0.03,
          "phone": "t_E"
        }
      ],
      "start": 91.059999,
      "startOffset": 1666,
      "word": "don\u2019t"
    },
    {
      "alignedWord": "think",
      "case": "success",
      "end": 91.479999,
      "endOffset": 1677,
      "phones": [
        {
          "duration": 0.06,
          "phone": "th_B"
        },
        {
          "duration": 0.02,
          "phone": "ih_I"
        },
        {
          "duration": 0.06,
          "phone": "ng_I"
        },
        {
          "duration": 0.06,
          "phone": "k_E"
        }
      ],
      "start": 91.279999,
      "startOffset": 1672,
      "word": "think"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 91.53999999999999,
      "endOffset": 1679,
      "phones": [
        {
          "duration": 0.05,
          "phone": "ay_S"
        }
      ],
      "start": 91.49,
      "startOffset": 1678,
      "word": "I"
    },
    {
      "alignedWord": "can",
      "case": "success",
      "end": 91.69000000000001,
      "endOffset": 1683,
      "phones": [
        {
          "duration": 0.07,
          "phone": "k_B"
        },
        {
          "duration": 0.04,
          "phone": "ah_I"
        },
        {
          "duration": 0.04,
          "phone": "n_E"
        }
      ],
      "start": 91.54,
      "startOffset": 1680,
      "word": "can"
    },
    {
      "alignedWord": "do",
      "case": "success",
      "end": 91.85,
      "endOffset": 1686,
      "phones": [
        {
          "duration": 0.06,
          "phone": "d_B"
        },
        {
          "duration": 0.1,
          "phone": "uw_E"
        }
      ],
      "start": 91.69,
      "startOffset": 1684,
      "word": "do"
    },
    {
      "alignedWord": "it",
      "case": "success",
      "end": 91.96,
      "endOffset": 1689,
      "phones": [
        {
          "duration": 0.05,
          "phone": "ih_B"
        },
        {
          "duration": 0.06,
          "phone": "t_E"
        }
      ],
      "start": 91.85,
      "startOffset": 1687,
      "word": "it"
    },
    {
      "alignedWord": "anymore",
      "case": "success",
      "end": 92.49,
      "endOffset": 1697,
      "phones": [
        {
          "duration": 0.06,
          "phone": "eh_B"
        },
        {
          "duration": 0.08,
          "phone": "n_I"
        },
        {
          "duration": 0.06,
          "phone": "iy_I"
        },
        {
          "duration": 0.07,
          "phone": "m_I"
        },
        {
          "duration": 0.09,
          "phone": "ao_I"
        },
        {
          "duration": 0.17,
          "phone": "r_E"
        }
      ],
      "start": 91.96,
      "startOffset": 1690,
      "word": "anymore"
    },
    {
      "alignedWord": "i",
      "case": "success",
      "end": 92.93,
      "endOffset": 1700,
      "phones": [
        {
          "duration": 0.17,
          "phone": "ay_S"
        }
      ],
      "start": 92.76,
      "startOffset": 1699,
      "word": "I"
    },
    {
      "alignedWord": "feel",
      "case": "success",
      "end": 93.19,
      "endOffset": 1705,
      "phones": [
        {
          "duration": 0.09,
          "phone": "f_B"
        },
        {
          "duration": 0.09,
          "phone": "iy_I"
        },
        {
          "duration": 0.07,
          "phone": "l_E"
        }
      ],
      "start": 92.94,
      "startOffset": 1701,
      "word": "feel"
    },
    {
      "alignedWord": "like",
      "case": "success",
      "end": 93.37,
      "endOffset": 1710,
      "phones": [
        {
          "duration": 0.04,
          "phone": "l_B"
        },
        {
          "duration": 0.07,
          "phone": "ay_I"
        },
        {
          "duration": 0.07,
          "phone": "k_E"
        }
      ],
      "start": 93.19,
      "startOffset": 1706,
      "word": "like"
    },
    {
      "alignedWord": "i'm",
      "case": "success",
      "end": 93.52000000000001,
      "endOffset": 1714,
      "phones": [
        {
          "duration": 0.07,
          "phone": "ay_B"
        },
        {
          "duration": 0.08,
          "phone": "m_E"
        }
      ],
      "start": 93.37,
      "startOffset": 1711,
      "word": "I\u2019m"
    },
    {
      "alignedWord": "losing",
      "case": "success",
      "end": 93.82,
      "endOffset": 1721,
      "phones": [
        {
          "duration": 0.06,
          "phone": "l_B"
        },
        {
          "duration": 0.06,
          "phone": "uw_I"
        },
        {
          "duration": 0.06,
          "phone": "z_I"
        },
        {
          "duration": 0.05,
          "phone": "ih_I"
        },
        {
          "duration": 0.07,
          "phone": "ng_E"
        }
      ],
      "start": 93.52,
      "startOffset": 1715,
      "word": "losing"
    },
    {
      "alignedWord": "my",
      "case": "success",
      "end": 93.97,
      "endOffset": 1724,
      "phones": [
        {
          "duration": 0.05,
          "phone": "m_B"
        },
        {
          "duration": 0.1,
          "phone": "ay_E"
        }
      ],
      "start": 93.82,
      "startOffset": 1722,
      "word": "my"
    },
    {
      "alignedWord": "wife",
      "case": "success",
      "end": 94.4,
      "endOffset": 1729,
      "phones": [
        {
          "duration": 0.1,
          "phone": "w_B"
        },
        {
          "duration": 0.19,
          "phone": "ay_I"
        },
        {
          "duration": 0.14,
          "phone": "f_E"
        }
      ],
      "start": 93.97,
      "startOffset": 1725,
      "word": "wife"
    },
    {
      "alignedWord": "my",
      "case": "success",
      "end": 94.66,
      "endOffset": 1733,
      "phones": [
        {
          "duration": 0.11,
          "phone": "m_B"
        },
        {
          "duration": 0.08,
          "phone": "ay_E"
        }
      ],
      "start": 94.47,
      "startOffset": 1731,
      "word": "my"
    },
    {
      "alignedWord": "passion",
      "case": "success",
      "end": 95.2,
      "endOffset": 1741,
      "phones": [
        {
          "duration": 0.09,
          "phone": "p_B"
        },
        {
          "duration": 0.13,
          "phone": "ae_I"
        },
        {
          "duration": 0.1,
          "phone": "sh_I"
        },
        {
          "duration": 0.09,
          "phone": "ah_I"
        },
        {
          "duration": 0.13,
          "phone": "n_E"
        }
      ],
      "start": 94.66,
      "startOffset": 1734,
      "word": "passion"
    },
    {
      "alignedWord": "everything",
      "case": "success",
      "end": 95.85000000000001,
      "endOffset": 1753,
      "phones": [
        {
          "duration": 0.13,
          "phone": "eh_B"
        },
        {
          "duration": 0.07,
          "phone": "v_I"
        },
        {
          "duration": 0.06,
          "phone": "r_I"
        },
        {
          "duration": 0.06,
          "phone": "iy_I"
        },
        {
          "duration": 0.08,
          "phone": "th_I"
        },
        {
          "duration": 0.09,
          "phone": "ih_I"
        },
        {
          "duration": 0.1,
          "phone": "ng_E"
        }
      ],
      "start": 95.26,
      "startOffset": 1743,
      "word": "everything"
    }
  ]
}

output_srt = "output.srt"
convert_json_to_srt(json_data, output_srt)
