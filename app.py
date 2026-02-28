import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title('勉強時間管理')
subjects = ['国語', '数学', '英語', '理科', '社会', 'その他']
times = []

for subject in subjects:
    times.append(st.slider(
        f'{subject}の勉強時間',
        min_value=0,
        max_value=300,
        key=subject
    ))

total = sum(times)

st.write('勉強時間の合計:', sum(times), '分')

if total == 0: 
    st.write('何やってるんですか勉強してください！！')
elif total < 60:
    st.write ('勉強足りてなくない？')
elif total < 120:
    st.write('今机に向き合えるかは、自分自身と向き合えるかだぞ')
elif total < 180:
    st.write('もっといける！あなたの人生の主導権を取り戻してください！')
elif total >= 180:
    st.write('お前は勉強の神か')
   


