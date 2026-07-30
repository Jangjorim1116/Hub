import random

TIPS = {
    "토마토": {
        "ko": [
            "토마토는 곁순을 제때 따줘야 원가지에 영양이 집중돼서 열매가 잘 자라요.",
            "물은 흙 표면이 마른 뒤에 흠뻑 주는 게 좋아요. 과습하면 뿌리가 썩기 쉬워요.",
            "꽃이 필 때 통풍이 잘 되면 착과율이 높아져요.",
            "잎이 한낮에 살짝 처지는 건 정상이에요. 저녁에 다시 살아나면 괜찮아요.",
            "완전히 빨갛게 익기 전, 색이 절반쯤 올라왔을 때 따서 실온에서 후숙해도 좋아요.",
            "칼슘이 부족하면 열매 밑부분이 검게 썩는 배꼽썩음병이 생길 수 있어요.",
        ],
        "en": [
            "Remove tomato side shoots (suckers) promptly so nutrients concentrate on the main stem and fruit grows well.",
            "Water thoroughly only after the soil surface has dried out. Overwatering can easily cause root rot.",
            "Good airflow while flowers are blooming improves fruit set.",
            "It's normal for leaves to droop slightly at midday. If they perk back up in the evening, everything's fine.",
            "You can pick tomatoes when they're about half-colored, before fully ripening, and let them ripen at room temperature.",
            "A calcium deficiency can cause blossom end rot, where the bottom of the fruit turns black and rots.",
        ],
        "ja": [
            "トマトは脇芽を早めに摘み取ると、主枝に栄養が集中して実がよく育ちます。",
            "水は土の表面が乾いてからたっぷり与えましょう。過湿だと根が腐りやすくなります。",
            "開花時に風通しが良いと着果率が高まります。",
            "日中に葉が少ししおれるのは正常です。夕方に元に戻れば問題ありません。",
            "完全に赤く熟す前、色づきが半分程度の時に収穫し、室温で追熟させても良いです。",
            "カルシウムが不足すると、実の下部が黒く腐る尻腐れ病が発生することがあります。",
        ],
        "zh": [
            "要及时摘除番茄的侧芽，这样养分才能集中到主枝，果实才能长得更好。",
            "等土壤表面变干后再浇透水。浇水过多容易导致烂根。",
            "开花期间通风良好可以提高坐果率。",
            "叶片在中午稍微下垂是正常现象，只要傍晚能恢复就没关系。",
            "在完全变红之前，颜色到一半左右时采摘，放在室温下继续后熟也可以。",
            "缺钙可能导致脐腐病，即果实底部发黑腐烂。",
        ],
        "fr": [
            "Retirez rapidement les gourmands de la tomate pour que les nutriments se concentrent sur la tige principale et que les fruits se développent bien.",
            "Arrosez abondamment seulement après que la surface du sol ait séché. Un excès d'eau peut facilement faire pourrir les racines.",
            "Une bonne circulation d'air pendant la floraison améliore la nouaison.",
            "Il est normal que les feuilles s'affaissent légèrement à midi. Si elles reprennent leur forme le soir, tout va bien.",
            "Vous pouvez cueillir les tomates lorsqu'elles sont colorées à moitié, avant maturité complète, et les laisser mûrir à température ambiante.",
            "Une carence en calcium peut provoquer la nécrose apicale, où le bas du fruit noircit et pourrit.",
        ],
    },
    "가지": {
        "ko": [
            "가지는 물을 좋아하는 작물이라 흙이 마르지 않게 신경 써주세요.",
            "첫 꽃(첫물가지)을 따주면 나무가 튼튼해지고 이후 수확량이 늘어나요.",
            "곁가지를 정리해주면 통풍이 좋아져 병 발생이 줄어요.",
            "가지 색이 흐려지고 윤기가 없어지면 수확 시기를 놓친 신호예요.",
            "고온다습한 환경에서 진딧물·응애가 잘 생기니 잎 뒷면을 자주 확인해주세요.",
            "비료는 꽃이 피기 시작할 때부터 2주 간격으로 주면 좋아요.",
        ],
        "en": [
            "Eggplants love water, so make sure the soil doesn't dry out.",
            "Pinching off the first flower (first fruit) helps the plant grow stronger and increases later yield.",
            "Pruning side branches improves airflow and reduces disease.",
            "If the eggplant's color fades and loses its shine, that's a sign you've missed the harvest window.",
            "Aphids and mites thrive in hot, humid conditions, so check the undersides of leaves often.",
            "Start fertilizing once flowers begin to bloom, and repeat every two weeks.",
        ],
        "ja": [
            "ナスは水を好む作物なので、土が乾かないように気をつけてください。",
            "最初の花（一番花）を摘み取ると株が丈夫になり、その後の収穫量が増えます。",
            "脇枝を整理すると風通しが良くなり、病気の発生が減ります。",
            "ナスの色が薄くなり、つやがなくなったら収穫時期を逃したサインです。",
            "高温多湿の環境ではアブラムシ・ハダニが発生しやすいので、葉の裏をこまめに確認してください。",
            "肥料は花が咲き始めた時から2週間おきに与えると良いです。",
        ],
        "zh": [
            "茄子喜水，要注意别让土壤变干。",
            "摘除第一朵花（头茬果）能让植株更健壮，之后的产量也会增加。",
            "修剪侧枝可以改善通风，减少病害发生。",
            "如果茄子颜色变淡、失去光泽，说明已经错过了最佳采收期。",
            "高温潮湿的环境容易滋生蚜虫和螨虫，请经常检查叶片背面。",
            "从开花开始，每两周施一次肥效果较好。",
        ],
        "fr": [
            "L'aubergine aime l'eau, veillez donc à ce que le sol ne sèche pas.",
            "Pincer la première fleur (premier fruit) renforce la plante et augmente le rendement ultérieur.",
            "Tailler les branches latérales améliore la circulation de l'air et réduit les maladies.",
            "Si la couleur de l'aubergine pâlit et perd son brillant, c'est le signe que vous avez manqué le moment de la récolte.",
            "Les pucerons et acariens prolifèrent en conditions chaudes et humides, vérifiez donc souvent le dessous des feuilles.",
            "Commencez à fertiliser dès le début de la floraison, et répétez toutes les deux semaines.",
        ],
    },
    "고추": {
        "ko": [
            "고추는 과습에 약해서 물빠짐이 좋은 흙을 써야 해요.",
            "바람이 강하면 가지가 부러지기 쉬우니 지지대로 단단히 고정해주세요.",
            "고추가 잘 안 열리면 질소 비료를 줄이고 인산·칼륨 비료 비중을 늘려보세요.",
            "탄저병 예방을 위해 잎에 물이 튀지 않게 밑동에 물을 주세요.",
            "짙은 초록색일 때도 수확 가능하고, 빨갛게 익히면 매운맛과 단맛이 더 강해져요.",
            "잎이 오글쪼글해지면 담배가루이 등 진딧물류 피해를 의심해보세요.",
        ],
        "en": [
            "Chili peppers are sensitive to overwatering, so use well-draining soil.",
            "Strong wind can easily snap the branches, so secure the plant firmly with a stake.",
            "If peppers aren't setting well, reduce nitrogen fertilizer and increase phosphorus and potassium.",
            "To prevent anthracnose, water at the base so water doesn't splash onto the leaves.",
            "You can harvest while it's still dark green, but letting it ripen red intensifies both the spiciness and sweetness.",
            "If the leaves curl and wrinkle, suspect damage from whiteflies or aphid-type pests.",
        ],
        "ja": [
            "唐辛子は過湿に弱いので、水はけの良い土を使いましょう。",
            "風が強いと枝が折れやすいので、支柱でしっかり固定してください。",
            "実がつきにくい場合は、窒素肥料を減らしてリン酸・カリ肥料の割合を増やしてみましょう。",
            "炭疽病を防ぐため、葉に水が跳ねないよう株元に水を与えてください。",
            "濃い緑色の時でも収穫可能で、赤く熟すと辛味と甘みがより強くなります。",
            "葉が縮れてきたら、コナジラミなどのアブラムシ類の被害を疑いましょう。",
        ],
        "zh": [
            "辣椒不耐涝，要使用排水良好的土壤。",
            "大风容易折断枝条，请用支架牢固固定。",
            "如果辣椒结果不好，可以减少氮肥，增加磷钾肥的比例。",
            "为预防炭疽病，请从植株根部浇水，避免水溅到叶片上。",
            "深绿色时也可以采摘，如果熟成红色，辣味和甜味都会更浓。",
            "如果叶片卷曲皱缩，可能是烟粉虱等蚜虫类害虫造成的伤害。",
        ],
        "fr": [
            "Les piments sont sensibles à l'excès d'eau, utilisez donc un sol bien drainé.",
            "Un vent fort peut facilement casser les branches, fixez donc solidement la plante avec un tuteur.",
            "Si les piments ne se forment pas bien, réduisez l'azote et augmentez le phosphore et le potassium.",
            "Pour prévenir l'anthracnose, arrosez à la base pour éviter les éclaboussures sur les feuilles.",
            "Vous pouvez récolter quand il est encore vert foncé, mais le laisser mûrir en rouge intensifie le piquant et la douceur.",
            "Si les feuilles se recroquevillent, soupçonnez des dégâts causés par les aleurodes ou des pucerons.",
        ],
    },
    "상추": {
        "ko": [
            "상추는 서늘한 날씨를 좋아해서 한여름엔 꽃대가 올라오고 잎이 써질 수 있어요.",
            "바깥쪽 잎부터 뜯어서 수확하면 속잎이 계속 자라 오래 수확할 수 있어요.",
            "직사광선이 너무 강하면 잎이 질겨지니 반그늘도 괜찮아요.",
            "뿌리가 얕아서 흙이 금방 말라요. 물은 자주, 조금씩 주는 게 좋아요.",
            "잎에 쓴맛이 강해지면 수확 시기가 늦은 신호예요.",
            "심은 지 20일쯤 촘촘한 곳은 솎아줘야 서로 자리를 안 뺏어요.",
        ],
        "en": [
            "Lettuce prefers cool weather, so in midsummer it may bolt (send up a flower stalk) and taste bitter.",
            "Harvest the outer leaves first and the inner leaves will keep growing, letting you harvest for longer.",
            "Strong direct sunlight can toughen the leaves, so partial shade is fine too.",
            "Because the roots are shallow, the soil dries out quickly. Water often, a little at a time.",
            "If the leaves taste noticeably bitter, that's a sign you've harvested too late.",
            "Around 20 days after planting, thin out crowded spots so plants don't compete for space.",
        ],
        "ja": [
            "レタスは涼しい気候を好むため、真夏はとう立ちして葉が苦くなることがあります。",
            "外側の葉から摘み取ると、内側の葉が育ち続け長く収穫できます。",
            "直射日光が強すぎると葉が硬くなるので、半日陰でも大丈夫です。",
            "根が浅いため土がすぐ乾きます。水はこまめに少しずつ与えましょう。",
            "葉の苦味が強くなったら収穫時期が遅れているサインです。",
            "植えてから20日ほどで、密集している場所は間引いてお互いの場所を奪わないようにしましょう。",
        ],
        "zh": [
            "生菜喜欢凉爽的天气，盛夏可能会抽薹，叶片也会变苦。",
            "从外叶开始采摘，内叶会持续生长，可以延长采收期。",
            "直射阳光过强会使叶片变老变硬，半阴环境也可以。",
            "由于根系较浅，土壤很快就会变干，建议少量多次浇水。",
            "如果叶片苦味变浓，说明采收时间已经偏晚。",
            "种植大约20天后，要给过密的地方间苗，避免植株互相争夺空间。",
        ],
        "fr": [
            "La laitue préfère les climats frais ; en plein été, elle peut monter en graine et devenir amère.",
            "Récoltez d'abord les feuilles extérieures : les feuilles intérieures continueront à pousser, ce qui prolonge la récolte.",
            "Un soleil direct trop fort peut durcir les feuilles, une mi-ombre convient donc aussi.",
            "Les racines étant peu profondes, le sol sèche vite. Arrosez souvent, un peu à la fois.",
            "Si les feuilles ont un goût amer prononcé, c'est le signe que la récolte est tardive.",
            "Environ 20 jours après la plantation, éclaircissez les zones denses pour que les plants ne se disputent pas l'espace.",
        ],
    },
    "오이": {
        "ko": [
            "오이는 물을 아주 좋아해서 흙이 마르지 않게 자주 물을 줘야 해요.",
            "덩굴 식물이라 지지대나 유인줄을 미리 설치해주는 게 좋아요.",
            "곁순을 적당히 정리해줘야 통풍이 잘 되고 병에 덜 걸려요.",
            "오이는 자라는 속도가 빨라서 하루만 늦어도 씨가 굵어지고 맛이 떨어져요.",
            "잎에 흰가루병(흰 곰팡이 같은 반점)이 잘 생기니 통풍과 배수를 신경 써주세요.",
            "아침 시간에 수확하면 수분감이 가장 좋아요.",
        ],
        "en": [
            "Cucumbers love water a lot, so water frequently to keep the soil from drying out.",
            "It's a vining plant, so it's best to set up a stake or trellis string in advance.",
            "Trimming side shoots appropriately improves airflow and reduces disease.",
            "Cucumbers grow fast — even one day late and the seeds thicken and the taste declines.",
            "Powdery mildew (white, mold-like spots) often appears on the leaves, so pay attention to airflow and drainage.",
            "Harvesting in the morning gives the best water content and crispness.",
        ],
        "ja": [
            "キュウリは水をとても好むので、土が乾かないようこまめに水を与えましょう。",
            "つる性植物なので、支柱や誘引ひもを事前に設置しておくと良いです。",
            "脇芽を適度に整理すると風通しが良くなり、病気にかかりにくくなります。",
            "キュウリは成長が早いため、一日収穫が遅れるだけで種が太くなり味が落ちます。",
            "葉にうどんこ病（白いカビのような斑点）ができやすいので、風通しと排水に気をつけてください。",
            "朝の時間に収穫すると水分感が最も良いです。",
        ],
        "zh": [
            "黄瓜非常喜水，要经常浇水以防止土壤变干。",
            "黄瓜是藤蔓植物，最好提前搭好支架或引蔓绳。",
            "适当整理侧芽能改善通风，减少病害。",
            "黄瓜生长很快，哪怕晚采一天，种子都会变粗，口感也会变差。",
            "叶片容易长白粉病（像白色霉斑），请注意通风和排水。",
            "早上采摘水分感最好。",
        ],
        "fr": [
            "Le concombre adore l'eau, arrosez donc fréquemment pour éviter que le sol ne sèche.",
            "C'est une plante grimpante, il est donc préférable d'installer un tuteur ou un fil de palissage à l'avance.",
            "Tailler modérément les pousses latérales améliore la circulation de l'air et réduit les maladies.",
            "Le concombre pousse vite : un seul jour de retard et les graines épaississent, altérant le goût.",
            "L'oïdium (taches blanches semblables à de la moisissure) apparaît souvent sur les feuilles, faites donc attention à l'aération et au drainage.",
            "La récolte le matin offre la meilleure teneur en eau.",
        ],
    },
}

GENERAL_TIPS = {
    "ko": [
        "새로 심은 모종은 며칠간 직사광선을 피하고 서서히 적응시켜주세요.",
        "물은 아침 일찍 주는 게 좋아요. 저녁에 주면 습기가 오래 남아 병에 걸리기 쉬워요.",
        "화분 밑 물빠짐 구멍이 막히지 않았는지 가끔 확인해주세요.",
        "잎 색이 연해지면 비료 부족, 잎이 노랗게 처지면 과습을 의심해보세요.",
        "통풍이 잘 되는 곳에 두면 병충해가 훨씬 줄어들어요.",
        "매일 잠깐씩이라도 식물 상태를 관찰하는 습관이 가장 중요해요.",
    ],
    "en": [
        "For newly planted seedlings, avoid direct sunlight for a few days and let them acclimate gradually.",
        "It's best to water early in the morning. Watering in the evening leaves moisture lingering, which invites disease.",
        "Occasionally check that the drainage hole at the bottom of the pot isn't clogged.",
        "Pale leaves suggest a fertilizer shortage; yellow, drooping leaves suggest overwatering.",
        "Placing plants somewhere with good airflow greatly reduces pests and disease.",
        "The most important habit is checking on your plants for even a few minutes every day.",
    ],
    "ja": [
        "新しく植えた苗は数日間直射日光を避け、徐々に慣らしてあげましょう。",
        "水は朝早くに与えるのが良いです。夕方に与えると湿気が長く残り、病気にかかりやすくなります。",
        "鉢底の水はけ穴が詰まっていないか時々確認してください。",
        "葉の色が薄くなったら肥料不足、葉が黄色く垂れたら過湿を疑いましょう。",
        "風通しの良い場所に置くと病害虫がかなり減ります。",
        "毎日少しずつでも植物の状態を観察する習慣が最も大切です。",
    ],
    "zh": [
        "新栽的幼苗应避开直射阳光几天，让它逐渐适应环境。",
        "最好在清晨浇水。傍晚浇水会让湿气滞留过久，容易引发病害。",
        "请偶尔检查花盆底部的排水孔是否堵塞。",
        "叶色变浅可能是缺肥，叶片发黄下垂则可能是浇水过多。",
        "放在通风良好的地方能大大减少病虫害。",
        "最重要的是养成每天哪怕只花几分钟观察植株状态的习惯。",
    ],
    "fr": [
        "Pour les jeunes plants récemment plantés, évitez le soleil direct pendant quelques jours et laissez-les s'acclimater progressivement.",
        "Il est préférable d'arroser tôt le matin. Arroser le soir laisse l'humidité stagner, ce qui favorise les maladies.",
        "Vérifiez de temps en temps que le trou de drainage au fond du pot n'est pas bouché.",
        "Des feuilles pâles suggèrent un manque d'engrais ; des feuilles jaunes et affaissées suggèrent un excès d'eau.",
        "Placer les plantes dans un endroit bien ventilé réduit considérablement les parasites et les maladies.",
        "L'habitude la plus importante est d'observer l'état de vos plantes, ne serait-ce que quelques minutes chaque jour.",
    ],
}


def get_tip(species_list: list, language: str = "ko"):
    """사용자가 키우는 작물 목록을 받아 (작물명 또는 None, 팁 문자열)을 무작위로 반환."""
    general_pool = GENERAL_TIPS.get(language) or GENERAL_TIPS["ko"]
    if species_list:
        species = random.choice(species_list)
        species_tips = TIPS.get(species, {})
        pool = species_tips.get(language) or species_tips.get("ko") or general_pool
        return species, random.choice(pool)
    return None, random.choice(general_pool)
