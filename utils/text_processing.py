import opencc
from paddleocr import TextRecognition

# #### DEMO
# s2t_converter = opencc.OpenCC('s2t.json')
# t2s_converter = opencc.OpenCC('t2s.json')
# converted_2s = s2t_converter.convert('汉语')
# converted_2t = t2s_converter.convert(converted_2s)
#
# print(f"Traditional text: {converted_2s} | Simplified text: {converted_2t}")
# > Traditional text: 漢語 | Simplified text: 汉语
# ####

simp2trad_converter = opencc.OpenCC('s2t.json')
trad2simp_converter = opencc.OpenCC('t2s.json')
text_recognition_model = TextRecognition()

def convert_to_simplified(text: str) -> str:
    return trad2simp_converter.convert(text)

def convert_to_traditional(text: str) -> str:
    return simp2trad_converter.convert(text)

def read_text_from_image(img):
    output = text_recognition_model.predict(img)
    return output