import streamlit as st

st.header("旅行先におすすめの島診断🗾")

kisetu = st.radio("旅行したい季節は？",["春🌸","夏🌳","秋🍂","冬⛄"])
print(kisetu)

yosan = st.selectbox("予算の目安は？",("格安で抑えたい","ほどほどに楽しみたい","贅沢OK!"))
print(yosan)

kotoba = st.radio("この中で一番惹かれる言葉は？",["神秘的","にぎやか","ロマンチック","のんびり","ワイルド","アート"])
print(kotoba)

motimono = st.radio("この中で１つだけ持っていけるとしたら？",["カメラ","本","水着","スニーカー","スマホ","お弁当"])
print(motimono)

if st.button("旅行先を診断する..."):
    if kotoba in ["アート", "のんびり"] and motimono in ["カメラ", "スマホ"] and kisetu in ["春🌸","秋🍂"]:
        st.subheader("あなたにおすすめの島は… **男木島（香川県）**！")
        col1, col2 = st.columns([1,2])
        with col1:
            st.image("10000963.jpg", caption="男木島", use_column_width = True)
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        男木島はアートと猫の島。迷路のような路地や坂道が魅力的で、瀬戸内国際芸術祭の作品をめぐるのにもぴったり。<br>
                        **こんな人におすすめ** :<br>
                        ・静かに過ごしたい<br>
                        ・写真が好き<br>
                        ・一人旅や友達との気ままな旅行がしたい<br>
                        **おすすめの季節** : 春・秋
                        """, unsafe_allow_html=True)
            
    elif kotoba in ["神秘的", "ロマンチック"] and motimono in ["カメラ", "水着", "スマホ"] and kisetu in ["夏🌳"]:
        st.subheader("あなたにおすすめの島は… **与論島（鹿児島県）**！")
        col1, col2 = st.columns([1,2])
        with col1:
            st.image("download-wallpaper-01.jpg", caption="与論島", use_column_width = True)
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        透き通る海と白浜の百合ヶ浜で、恋人や自分と向き合う時間を。<br>
                        **こんな人におすすめ** :<br>
                        ・透き通る海でロマンティックな時間を過ごしたい<br>
                        ・恋人と特別な思い出を過ごしたい<br>
                        ・SNS映えする風景に浸りたい<br>
                        **おすすめの季節** : 夏
                        """, unsafe_allow_html=True)
    elif kotoba == "のんびり" and motimono in ["水着", "本"] and kisetu in ["夏🌳"]:
        st.subheader("あなたにおすすめの島は… **久米島（沖縄県）**！")
        col1, col2 = st.columns([1,2])
        with col1:
            st.image("038T0A7375_s.jpg", caption="久米島", use_column_width = True)
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        はての浜の美しさに心奪われる。穏やかに海と暮らす旅。<br>
                        **こんな人におすすめ** :<br>
                        ・穏やかな海で心を解放したい<br>
                        ・水着でリゾート気分を満喫したい<br>
                        ・ちょっと人が少ない静かな沖縄を味わいたい<br>
                        **おすすめの季節** : 夏
                        """, unsafe_allow_html=True)
    elif kotoba in ["ワイルド", "神秘的"] and motimono in ["スニーカー", "カメラ"] and kisetu in ["夏🌳","秋🍂"]:
        st.subheader("あなたにおすすめの島は… **青ヶ島（東京都）**！")
        col1, col2 = st.columns([1,2])
        with col1:
            st.image("landscape_img25.jpg", caption="青ヶ島", use_column_width = True)
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        絶海の火山島。冒険や非日常を求めるあなたに。<br>
                        **こんな人におすすめ** :<br>
                        ・人里離れた冒険的な旅がしたい<br>
                        ・火山やダイナミックな自然に興味がある<br>
                        ・自分だけの秘境を見つけたい<br>
                        **おすすめの季節** : 夏～秋
                        """, unsafe_allow_html=True)
    elif kotoba == "にぎやか" and motimono == "お弁当" and kisetu in ["春🌸","冬⛄"]:
        st.subheader("あなたにおすすめの島は… **天草諸島（熊本県）**！")
        col1, col2 = st.columns([1,2])
        with col1:
            st.image("20210601175138-21900e42-me.jpg", caption="天草諸島", use_column_width = True)
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        イルカウォッチングや海鮮など、アクティブでおいしい旅に。<br>
                        **こんな人におすすめ** :<br>
                        ・おいしい魚介やイルカウォッチングを楽しみたい<br>
                        ・観光地化されすぎていない島を探している<br>
                        ・カメラ片手にダイナミックな風景を撮りたい<br>
                        **おすすめの季節** : 冬～春
                        """, unsafe_allow_html=True)

                        
    else:
        st.info("診断ロジックに合う島がまだ登録されていません。ほかの条件もお試しください！")
            