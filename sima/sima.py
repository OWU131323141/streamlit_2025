import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: 	#CAE8E2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("旅行先におすすめの島診断🗾")

st.markdown('<p style="font-size:30px; font-weight:bold;">Q1. どの季節に旅行したいですか？</p>', unsafe_allow_html=True)
kisetu = st.radio("旅行したい季節は？",["春🌸","夏🌳","秋🍂","冬⛄"])
print(kisetu)

kotoba = st.radio("この中で一番惹かれる言葉は？",["神秘的✨","のんびり🐢","ワイルド💪"])
print(kotoba)

motimono = st.radio("この中で１つだけ持っていけるとしたら？",["カメラ📸","水着👙","スニーカー👟"])
print(motimono)

if st.button("旅行先を診断する..."):
    if kotoba == "のんびり🐢" and motimono in ["カメラ📸","スニーカー👟"] and kisetu in ["春🌸","秋🍂"]:
        st.markdown('<h3 style="color:#267CA7;">あなたにおすすめの島は…男木島(香川県)！</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        with col1:
            st.image("sima/10000963.jpg", caption="男木島")
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        男木島はアートと猫の島。迷路のような路地や坂道が魅力的で、瀬戸内国際芸術祭の作品をめぐるのにもぴったり。<br><br>
                        **こんな人におすすめ** :<br>
                        ・静かに過ごしたい<br>
                        ・写真が好き<br>
                        ・一人旅や友達との気ままな旅行がしたい<br><br>
                        **おすすめの季節** : 春・秋
                        """, unsafe_allow_html=True)
            
    elif kotoba in ["神秘的✨", "のんびり🐢"] and motimono in ["カメラ📸", "水着👙"] and kisetu in ["夏🌳","冬⛄"]:
        st.markdown('<h3 style="color:#267CA7;">あなたにおすすめの島は…与論島(鹿児島県)！"</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        with col1:
            st.image("sima/download-wallpaper-01.jpg", caption="与論島")
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        透き通る海と白浜の百合ヶ浜で、恋人や自分と向き合う時間を。<br><br>
                        **こんな人におすすめ** :<br>
                        ・透き通る海でロマンティックな時間を過ごしたい<br>
                        ・恋人と特別な思い出を過ごしたい<br>
                        ・SNS映えする風景に浸りたい<br><br>
                        **おすすめの季節** : 夏、冬
                        """, unsafe_allow_html=True)
    elif kotoba == "のんびり🐢" and motimono == "水着👙" and kisetu in ["春🌸","秋🍂"]:
        st.markdown('<h3 style="color:#267CA7;">あなたにおすすめの島は…久米島(沖縄県)！"</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        with col1:
            st.image("sima/038T0A7375_s.jpg", caption="久米島")
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        はての浜の美しさに心奪われる。穏やかに海と暮らす旅。<br><br>
                        **こんな人におすすめ** :<br>
                        ・穏やかな海で心を解放したい<br>
                        ・水着でリゾート気分を満喫したい<br>
                        ・ちょっと人が少ない静かな沖縄を味わいたい<br><br>
                        **おすすめの季節** : 春、秋
                        """, unsafe_allow_html=True)
    elif kotoba == "ワイルド💪" and motimono in ["スニーカー👟", "水着👙","カメラ📸"] and kisetu in ["夏🌳","秋🍂"]:
        st.markdown('<h3 style="color:#267CA7;">あなたにおすすめの島は…青ヶ島(東京都)！"</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        with col1:
            st.image("sima/landscape_img25.jpg", caption="青ヶ島")
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        絶海の火山島。冒険や非日常を求めるあなたに。<br><br>
                        **こんな人におすすめ** :<br>
                        ・人里離れた冒険的な旅がしたい<br>
                        ・火山やダイナミックな自然に興味がある<br>
                        ・自分だけの秘境を見つけたい<br><br>
                        **おすすめの季節** : 夏～秋
                        """, unsafe_allow_html=True)

    elif kotoba == "神秘的✨" and motimono == "カメラ📸" and kisetu in ["春🌸","秋🍂"]:
        st.markdown('<h3 style="color:#267CA7;">あなたにおすすめの島は…屋久島(鹿児島県)！"</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        with col1:
            st.image("sima/pic-wilson-dr.jpg", caption="屋久島")
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        樹齢数千年の杉と苔むす森、神秘的な自然の中で深呼吸できる島。<br><br>
                        **こんな人におすすめ** :<br>
                        ・もののけ姫の世界に浸りたい<br>
                        ・苔や巨樹などをカメラでじっくり撮影したい<br>
                        ・トレッキングやハイキングを楽しみたい<br><br>
                        **おすすめの季節** : 春、秋
                        """, unsafe_allow_html=True)
    elif kotoba == "神秘的✨" and motimono == "水着👙" and kisetu in ["春🌸","秋🍂"]:
        st.markdown('<h3 style="color:#267CA7;">あなたにおすすめの島は…与那国島(沖縄県)！"</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("sima/019aozora_02397A_TP_V.jpg", caption="与那国島")
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        日本最西端の地で、謎めいた海底遺跡と出会える神秘の島。<br><br>
                        **こんな人におすすめ** :<br>
                        ・ロマンあふれる海底遺跡に惹かれる<br>
                        ・非日常を味わえる秘境に行ってみたい<br>
                        ・歩いて回れる小さな島でのんびりしたい<br><br>
                        **おすすめの季節** : 夏、秋
                        """, unsafe_allow_html=True)
    elif kotoba in ["神秘的✨", "ワイルド💪"] and motimono == "スニーカー👟" and kisetu in ["春🌸","冬⛄"]:
        st.markdown('<h3 style="color:#267CA7;">あなたにおすすめの島は…奥尻島(北海道)！"</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("sima/AdobeStock_567979284_Preview.jpeg", caption="奥尻島")
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        北海道の離島・奥尻島は、澄んだ海とダイナミックな断崖、静かな集落が広がる“秘境感”のある島。<br>
                        海の幸と自然を満喫できる、ちょっと特別な時間を味わえます。<br><br>
                        **こんな人におすすめ** :<br>
                        ・静けさの中で自然や景色をじっくり楽しみたい<br>
                        ・観光地化されていない、地元の暮らしが感じられる場所を旅したい<br>
                        ・スニーカーで岬や海岸線を歩きたい<br><br>
                        **おすすめの季節** : 春、冬
                        """, unsafe_allow_html=True)
    elif kotoba == "ワイルド💪" and motimono in ["カメラ📸", "水着👙"] and kisetu in ["春🌸", "冬⛄"]:
        st.markdown('<h3 style="color:#267CA7;">あなたにおすすめの島は…種子島(鹿児島県)！"</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("sima/332.jpg", caption="種子島")
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        鹿児島県の種子島は、サーフィンの名所として知られ、手つかずの自然と広大な海岸線が魅力の島。<br>
                        宇宙センターもあり、ダイナミックな体験ができるユニークな場所です。<br>
                        海も山も満喫でき、カメラ片手に絶景を追いかけたくなるようなスポットが満載。<br><br>
                        **こんな人におすすめ** :<br>
                        ・ワイルドな自然の中でアクティブに過ごしたい<br>
                        ・ローカルな雰囲気を感じながら島の暮らしを見てみたい<br>
                        ・水着で海を満喫しつつ、カメラで風景も楽しみたい<br><br>
                        **おすすめの季節** : 春、冬
                        """, unsafe_allow_html=True)
    elif kotoba == "神秘的✨" and motimono == "スニーカー👟" and kisetu in ["夏🌳", "秋🍂"]:
        st.markdown('<h3 style="color:#267CA7;">あなたにおすすめの島は…礼文島(北海道)！"</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("sima/kanko_50_l.jpg", caption="礼文島")
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        北海道の最北に位置する礼文島は、「花の浮島」とも呼ばれる高山植物の宝庫。<br>
                        夏から秋にかけて、幻想的な霧とともに咲き誇る花々、荒々しい断崖が織りなす神秘的な風景が魅力です。<br>
                        島内には整備されたトレッキングコースがあり、スニーカーで自然の美しさをたっぷり味わえます。<br><br>
                        **こんな人におすすめ** :<br>
                        ・幻想的な風景や自然の神秘に惹かれる<br>
                        ・静かな時間の中で、花や風景を丁寧に味わいたい<br>
                        ・スニーカーで軽やかに島を歩き回りたい<br><br>
                        **おすすめの季節** : 夏、秋
                        """, unsafe_allow_html=True)
    elif kotoba == "のんびり🐢" and motimono == "スニーカー👟" and kisetu in ["夏🌳", "冬⛄"]:
        st.markdown('<h3 style="color:#267CA7;">あなたにおすすめの島は…利尻島(北海道)！"</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("sima/りしぷら-夜空㈫.jpg", caption="利尻島")
        with col2:
            st.markdown("""
                        **島の紹介** :<br>
                        利尻昆布で有名な利尻島は、利尻富士を中心とした美しい自然が広がる静かな島。<br>
                        釣りや温泉、地元グルメも楽しめ、夏は涼しく、冬は人も少なくゆったりとした島時間が流れます。<br>
                        島の道は歩きやすく、スニーカーでのんびり散策にぴったりです。<br><br>
                        **こんな人におすすめ** :<br>
                        ・観光客が少ない場所で静かに過ごしたい<br>
                        ・自然の中でリラックスしながら景色を味わいたい<br>
                        ・スニーカーでのんびり歩きながら地元の雰囲気を感じたい<br><br>
                        **おすすめの季節** : 夏、冬
                        """, unsafe_allow_html=True)
            
