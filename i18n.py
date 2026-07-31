LANGUAGES = [
    ("ko", "한국어"),
    ("en", "English"),
    ("ja", "日本語"),
    ("zh", "中文"),
    ("fr", "Français"),
]

DEFAULT_LANGUAGE = "ko"

LANGUAGE_NAMES_FOR_AI = {
    "ko": "Korean",
    "en": "English",
    "ja": "Japanese",
    "zh": "Simplified Chinese",
    "fr": "French",
}

TRANSLATIONS = {
    "nav_home": {"ko": "홈", "en": "Home", "ja": "ホーム", "zh": "首页", "fr": "Accueil"},
    "nav_chat": {"ko": "대화", "en": "Chat", "ja": "チャット", "zh": "聊天", "fr": "Discussion"},
    "nav_settings": {"ko": "설정", "en": "Settings", "ja": "設定", "zh": "设置", "fr": "Paramètres"},

    "today_tasks_pot": {
        "ko": "오늘 할 일 (화분)", "en": "Today's tasks (Pots)", "ja": "今日のタスク（鉢植え）",
        "zh": "今日待办（花盆）", "fr": "Tâches du jour (Pots)",
    },
    "month_tasks_plot": {
        "ko": "이번달 할 일 (텃밭)", "en": "This month's tasks (Gardens)", "ja": "今月のタスク（菜園）",
        "zh": "本月待办（菜园）", "fr": "Tâches du mois (Jardins)",
    },
    "no_tasks_today": {
        "ko": "오늘 할 일이 없어요.", "en": "No tasks for today.", "ja": "今日のタスクはありません。",
        "zh": "今天没有待办事项。", "fr": "Aucune tâche pour aujourd'hui.",
    },
    "no_tasks_month": {
        "ko": "이번달 할 일이 없어요.", "en": "No tasks this month.", "ja": "今月のタスクはありません。",
        "zh": "本月没有待办事项。", "fr": "Aucune tâche ce mois-ci.",
    },
    "view_details": {
        "ko": "📖 자세히 보기", "en": "📖 View details", "ja": "📖 詳細を見る",
        "zh": "📖 查看详情", "fr": "📖 Voir les détails",
    },
    "write_review": {
        "ko": "후기 쓰기", "en": "Write a review", "ja": "レビューを書く",
        "zh": "写评价", "fr": "Rédiger un avis",
    },
    "my_pots": {"ko": "보유중인 화분", "en": "My pots", "ja": "保有中の鉢植え", "zh": "我的花盆", "fr": "Mes pots"},
    "my_plots": {"ko": "보유중인 텃밭", "en": "My gardens", "ja": "保有中の菜園", "zh": "我的菜园", "fr": "Mes jardins"},
    "no_pots": {
        "ko": "등록된 화분이 없어요. 첫 화분을 등록해보세요!", "en": "No pots yet. Register your first pot!",
        "ja": "登録された鉢植えがありません。最初の鉢植えを登録してみましょう！",
        "zh": "还没有花盆，快去登记第一个花盆吧！", "fr": "Aucun pot enregistré. Ajoutez votre premier pot !",
    },
    "no_plots": {
        "ko": "등록된 텃밭이 없어요. 첫 텃밭을 등록해보세요!", "en": "No gardens yet. Register your first garden!",
        "ja": "登録された菜園がありません。最初の菜園を登録してみましょう！",
        "zh": "还没有菜园，快去登记第一个菜园吧！", "fr": "Aucun jardin enregistré. Ajoutez votre premier jardin !",
    },
    "add_pot": {"ko": "＋ 화분 등록하기", "en": "＋ Add a pot", "ja": "＋ 鉢植えを登録", "zh": "＋ 添加花盆", "fr": "＋ Ajouter un pot"},
    "add_plot": {"ko": "＋ 텃밭 등록하기", "en": "＋ Add a garden", "ja": "＋ 菜園を登録", "zh": "＋ 添加菜园", "fr": "＋ Ajouter un jardin"},
    "today_tip": {"ko": "오늘의 TIP", "en": "Tip of the day", "ja": "今日のヒント", "zh": "今日小贴士", "fr": "Astuce du jour"},

    "chat_users": {"ko": "사용자 대화", "en": "Community chat", "ja": "ユーザーチャット", "zh": "用户聊天", "fr": "Discussion communauté"},
    "chat_ai_1on1": {"ko": "1:1", "en": "1:1", "ja": "1:1", "zh": "1对1", "fr": "1:1"},
    "chat_send": {"ko": "보내기", "en": "Send", "ja": "送信", "zh": "发送", "fr": "Envoyer"},
    "chat_message_placeholder": {
        "ko": "메시지를 입력하세요", "en": "Type a message", "ja": "メッセージを入力してください",
        "zh": "请输入消息", "fr": "Écrivez un message",
    },
    "chat_no_messages": {
        "ko": "아직 메시지가 없어요. 첫 메시지를 남겨보세요!", "en": "No messages yet. Be the first to say hi!",
        "ja": "まだメッセージがありません。最初のメッセージを送ってみましょう！",
        "zh": "还没有消息，快来发第一条吧！", "fr": "Pas encore de messages. Soyez le premier à écrire !",
    },
    "chat_ai_placeholder": {
        "ko": "물어보세요", "en": "Ask anything", "ja": "何でも聞いてください",
        "zh": "请随意提问", "fr": "Posez votre question",
    },
    "chat_suggested_label": {
        "ko": "추천 질문", "en": "Suggested questions", "ja": "おすすめの質問",
        "zh": "推荐问题", "fr": "Questions suggérées",
    },
    "chat_suggested_q1": {
        "ko": "물은 얼마나 자주 줘야 해요?", "en": "How often should I water?",
        "ja": "水はどのくらいの頻度で与えればいいですか？", "zh": "多久浇一次水？",
        "fr": "À quelle fréquence dois-je arroser ?",
    },
    "chat_suggested_q2": {
        "ko": "비료는 언제 줘야 해요?", "en": "When should I fertilize?",
        "ja": "肥料はいつ与えればいいですか？", "zh": "什么时候该施肥？",
        "fr": "Quand dois-je fertiliser ?",
    },
    "chat_suggested_q3": {
        "ko": "잎이 시들었어요, 왜 그럴까요?", "en": "My leaves are wilting — why?",
        "ja": "葉がしおれています。なぜでしょうか？", "zh": "叶子蔫了，是什么原因？",
        "fr": "Mes feuilles flétrissent, pourquoi ?",
    },
    "chat_room_title": {
        "ko": "{kind} 사용자 대화방", "en": "{kind} community chat room", "ja": "{kind}ユーザーチャットルーム",
        "zh": "{kind}用户聊天室", "fr": "Salon de discussion communautaire {kind}",
    },
    "chat_room_desc": {
        "ko": "{kind}을 키우는 다른 사용자와 자유롭게 대화해보세요. (매일 초기화돼요)",
        "en": "Chat freely with other users growing {kind}. (Resets daily)",
        "ja": "{kind}を育てている他のユーザーと自由に会話してみましょう。（毎日リセットされます）",
        "zh": "和其他种植{kind}的用户自由聊天吧。（每天重置）",
        "fr": "Discutez librement avec d'autres utilisateurs qui cultivent des {kind}. (Réinitialisé chaque jour)",
    },
    "bot_name_pot": {"ko": "화분봇", "en": "PotBot", "ja": "鉢植えボット", "zh": "花盆助手", "fr": "PotBot"},
    "bot_name_garden": {"ko": "텃밭봇", "en": "GardenBot", "ja": "菜園ボット", "zh": "菜园助手", "fr": "GardenBot"},
    "chat_ai_title": {
        "ko": "{bot}과 1:1 상담", "en": "1:1 chat with {bot}", "ja": "{bot}との1:1相談",
        "zh": "与{bot}的1对1咨询", "fr": "Consultation 1:1 avec {bot}",
    },
    "chat_bot_toggle_help": {
        "ko": "탭하면 화분봇/텃밭봇 전환", "en": "Tap to switch between PotBot/GardenBot",
        "ja": "タップすると鉢植えボット/菜園ボットを切り替えます", "zh": "点击可切换花盆助手/菜园助手",
        "fr": "Appuyez pour basculer entre PotBot/GardenBot",
    },
    "chat_room_toggle_help": {
        "ko": "탭하면 화분/텃밭 대화방 전환", "en": "Tap to switch between Pot/Garden chat rooms",
        "ja": "タップすると鉢植え/菜園のチャットルームを切り替えます", "zh": "点击可切换花盆/菜园聊天室",
        "fr": "Appuyez pour basculer entre les salons Pot/Jardin",
    },
    "chat_ai_desc": {
        "ko": "나만 볼 수 있는 대화입니다. {kind} 관리에 대해 무엇이든 물어보세요. (매일 초기화돼요)",
        "en": "This chat is private to you. Ask anything about {kind} care. (Resets daily)",
        "ja": "自分だけが見られる会話です。{kind}の管理について何でも聞いてみましょう。（毎日リセットされます）",
        "zh": "这是只有你能看到的对话。可以随意询问关于{kind}养护的任何问题。（每天重置）",
        "fr": "Cette discussion est privée. Posez toutes vos questions sur l'entretien de {kind}. (Réinitialisé chaque jour)",
    },
    "chat_me_label": {"ko": "나", "en": "Me", "ja": "自分", "zh": "我", "fr": "Moi"},
    "chat_ai_thinking": {
        "ko": "{bot}이 답변을 생각하고 있어요... (약 5~10초 정도 걸려요)",
        "en": "{bot} is thinking of a reply... (about 5-10 seconds)",
        "ja": "{bot}が返信を考えています...（約5〜10秒かかります）",
        "zh": "{bot}正在思考回复...（大约需要5-10秒）",
        "fr": "{bot} réfléchit à une réponse... (environ 5 à 10 secondes)",
    },
    "ai_reply_fallback_error": {
        "ko": "죄송해요, 지금은 AI 서버가 혼잡해서 답변을 받지 못했어요. 잠시 후 다시 시도해주세요.",
        "en": "Sorry, the AI server is busy right now and couldn't respond. Please try again shortly.",
        "ja": "申し訳ありません、現在AIサーバーが混雑しており返信を受け取れませんでした。しばらくしてからもう一度お試しください。",
        "zh": "抱歉，AI服务器当前繁忙，未能收到回复。请稍后再试。",
        "fr": "Désolé, le serveur IA est actuellement surchargé et n'a pas pu répondre. Veuillez réessayer dans un instant.",
    },
    "message_input_label": {
        "ko": "메시지 입력", "en": "Message input", "ja": "メッセージ入力",
        "zh": "消息输入", "fr": "Saisie du message",
    },
    "ai_message_input_label": {
        "ko": "AI에게 메시지", "en": "Message to AI", "ja": "AIへのメッセージ",
        "zh": "给AI的消息", "fr": "Message à l'IA",
    },
    "memo_label": {"ko": "메모", "en": "Memo", "ja": "メモ", "zh": "备注", "fr": "Mémo"},
    "weather_risk_checking": {
        "ko": "텃밭 지역에 날씨 긴급 위기가 없는지 확인하고 있어요...",
        "en": "Checking for urgent weather risks in your garden's area...",
        "ja": "菜園の地域で気象上の緊急リスクがないか確認しています...",
        "zh": "正在检查菜园所在地区是否有紧急天气风险...",
        "fr": "Vérification des risques météo urgents dans la zone de votre jardin...",
    },
    "browser_notification_title": {
        "ko": "허브 알림", "en": "Hub notification", "ja": "Hub通知",
        "zh": "Hub通知", "fr": "Notification Hub",
    },

    "settings_title": {"ko": "설정", "en": "Settings", "ja": "設定", "zh": "设置", "fr": "Paramètres"},
    "setting_icon": {"ko": "아이콘 변경", "en": "Change icon", "ja": "アイコン変更", "zh": "更改头像", "fr": "Changer l'icône"},
    "setting_alarm": {"ko": "알람 설정", "en": "Alarm settings", "ja": "アラーム設定", "zh": "提醒设置", "fr": "Paramètres d'alerte"},
    "setting_language": {"ko": "언어 설정", "en": "Language", "ja": "言語設定", "zh": "语言设置", "fr": "Langue"},
    "setting_email": {"ko": "이메일 변경", "en": "Change email", "ja": "メールアドレス変更", "zh": "更改邮箱", "fr": "Changer l'e-mail"},
    "setting_password": {
        "ko": "비밀번호 변경", "en": "Change password", "ja": "パスワード変更",
        "zh": "更改密码", "fr": "Changer le mot de passe",
    },
    "setting_logout": {"ko": "로그아웃", "en": "Log out", "ja": "ログアウト", "zh": "退出登录", "fr": "Déconnexion"},
    "setting_delete": {"ko": "계정 삭제", "en": "Delete account", "ja": "アカウント削除", "zh": "删除账户", "fr": "Supprimer le compte"},

    "current_email_prefix": {
        "ko": "현재 이메일: ", "en": "Current email: ", "ja": "現在のメール: ",
        "zh": "当前邮箱：", "fr": "E-mail actuel : ",
    },
    "new_email_label": {"ko": "새 이메일", "en": "New email", "ja": "新しいメールアドレス", "zh": "新邮箱", "fr": "Nouvel e-mail"},
    "password_label": {"ko": "비밀번호", "en": "Password", "ja": "パスワード", "zh": "密码", "fr": "Mot de passe"},
    "password_confirm_label": {
        "ko": "비밀번호 확인", "en": "Confirm password", "ja": "パスワード確認",
        "zh": "确认密码", "fr": "Confirmer le mot de passe",
    },
    "password_mismatch_msg": {
        "ko": "비밀번호가 일치하지 않아요.", "en": "Passwords don't match.", "ja": "パスワードが一致しません。",
        "zh": "密码不匹配。", "fr": "Les mots de passe ne correspondent pas.",
    },
    "change_submit": {"ko": "변경하기", "en": "Change", "ja": "変更する", "zh": "更改", "fr": "Modifier"},
    "current_password_label": {
        "ko": "현재 비밀번호", "en": "Current password", "ja": "現在のパスワード",
        "zh": "当前密码", "fr": "Mot de passe actuel",
    },
    "new_password_label": {
        "ko": "새 비밀번호", "en": "New password", "ja": "新しいパスワード",
        "zh": "新密码", "fr": "Nouveau mot de passe",
    },
    "new_password_confirm_label": {
        "ko": "새 비밀번호 확인", "en": "Confirm new password", "ja": "新しいパスワード確認",
        "zh": "确认新密码", "fr": "Confirmer le nouveau mot de passe",
    },
    "new_password_mismatch_msg": {
        "ko": "새 비밀번호가 일치하지 않아요.", "en": "New passwords don't match.", "ja": "新しいパスワードが一致しません。",
        "zh": "新密码不匹配。", "fr": "Les nouveaux mots de passe ne correspondent pas.",
    },
    "delete_account_warning": {
        "ko": "계정을 삭제하면 화분·텃밭·채팅 기록을 포함한 모든 데이터가 영구적으로 삭제되며 되돌릴 수 없어요.",
        "en": "Deleting your account permanently removes all data, including pots, gardens, and chat history, and cannot be undone.",
        "ja": "アカウントを削除すると、鉢植え・菜園・チャット履歴を含むすべてのデータが完全に削除され、元に戻せません。",
        "zh": "删除账户将永久删除包括花盆、菜园和聊天记录在内的所有数据，且无法恢复。",
        "fr": "La suppression de votre compte efface définitivement toutes les données, y compris les pots, jardins et l'historique de discussion, et ne peut pas être annulée.",
    },
    "delete_account_confirm_button": {
        "ko": "계정 영구 삭제", "en": "Permanently delete account", "ja": "アカウントを完全に削除",
        "zh": "永久删除账户", "fr": "Supprimer définitivement le compte",
    },

    "alarm_title": {"ko": "알람 설정", "en": "Alarm settings", "ja": "アラーム設定", "zh": "提醒设置", "fr": "Paramètres d'alerte"},
    "back": {"ko": "← 뒤로가기", "en": "← Back", "ja": "← 戻る", "zh": "← 返回", "fr": "← Retour"},
    "alarm_desc": {
        "ko": (
            "오늘 할 일(당일 목록)은 이미 홈 화면에 표시되니 별도로 알리지 않아요. "
            "대신 가이드라인에 있는 다음 중요 일정(지지대 설치, 웃거름, 수확 시작 등)의 날짜가 되면 "
            "브라우저 알림으로 알려드려요."
        ),
        "en": (
            "Today's tasks are already shown on the home screen, so we won't notify you separately for those. "
            "Instead, we'll send a browser notification when the next important milestone in your guideline "
            "(staking, fertilizing, harvest start, etc.) comes due."
        ),
        "ja": (
            "今日のタスクはすでにホーム画面に表示されているため、別途通知はしません。"
            "代わりに、ガイドラインの次の重要な予定（支柱設置、追肥、収穫開始など）の日になったら"
            "ブラウザ通知でお知らせします。"
        ),
        "zh": (
            "今日待办已在首页显示，因此不会另行提醒。"
            "但当指南中下一个重要节点（立支架、追肥、开始收获等）到期时，会通过浏览器通知提醒你。"
        ),
        "fr": (
            "Les tâches du jour sont déjà affichées sur l'écran d'accueil, donc nous ne les notifions pas séparément. "
            "En revanche, nous vous enverrons une notification du navigateur lorsque la prochaine étape importante "
            "de votre guide (tuteurage, engrais, début de récolte, etc.) arrivera à échéance."
        ),
    },
    "alarm_checkbox": {
        "ko": "가이드라인 중요 일정 알림 받기", "en": "Receive guideline milestone alerts",
        "ja": "ガイドラインの重要な予定の通知を受け取る", "zh": "接收指南重要日程提醒",
        "fr": "Recevoir les alertes des étapes importantes du guide",
    },
    "alarm_permission_info": {
        "ko": "브라우저에서 알림 권한을 요청할 거예요. 허용해주셔야 알림이 보여요.",
        "en": "Your browser will ask for notification permission. Please allow it to see alerts.",
        "ja": "ブラウザが通知の許可を求めます。許可しないと通知が表示されません。",
        "zh": "浏览器会请求通知权限，请允许后才能看到提醒。",
        "fr": "Votre navigateur va demander l'autorisation d'envoyer des notifications. Merci de l'accepter.",
    },

    "kind_pot": {"ko": "화분", "en": "Pot", "ja": "鉢植え", "zh": "花盆", "fr": "Pot"},
    "kind_garden": {"ko": "텃밭", "en": "Garden", "ja": "菜園", "zh": "菜园", "fr": "Jardin"},
    "back_to_home": {"ko": "← 홈으로", "en": "← Home", "ja": "← ホームへ", "zh": "← 返回首页", "fr": "← Accueil"},
    "save": {"ko": "저장", "en": "Save", "ja": "保存", "zh": "保存", "fr": "Enregistrer"},
    "cancel": {"ko": "취소", "en": "Cancel", "ja": "キャンセル", "zh": "取消", "fr": "Annuler"},
    "select_button": {"ko": "선택", "en": "Select", "ja": "選択", "zh": "选择", "fr": "Sélectionner"},

    "task_not_found": {
        "ko": "작업 정보를 찾을 수 없습니다.", "en": "Couldn't find this task.", "ja": "タスク情報が見つかりません。",
        "zh": "找不到该任务信息。", "fr": "Tâche introuvable.",
    },
    "info_not_found": {
        "ko": "정보를 찾을 수 없습니다.", "en": "Couldn't find this information.", "ja": "情報が見つかりません。",
        "zh": "找不到相关信息。", "fr": "Informations introuvables.",
    },
    "task_done_checkbox": {
        "ko": "작업 완료", "en": "Mark as done", "ja": "作業完了", "zh": "标记完成", "fr": "Marquer comme terminé",
    },
    "one_line_summary": {
        "ko": "한 줄 요약", "en": "Summary", "ja": "一言まとめ", "zh": "一句话总结", "fr": "Résumé",
    },

    "new_pot_title": {
        "ko": "새 화분 등록", "en": "Register a new pot", "ja": "新しい鉢植えを登録",
        "zh": "登记新花盆", "fr": "Enregistrer un nouveau pot",
    },
    "new_plot_title": {
        "ko": "새 텃밭 등록", "en": "Register a new garden", "ja": "新しい菜園を登録",
        "zh": "登记新菜园", "fr": "Enregistrer un nouveau jardin",
    },
    "other_species": {"ko": "기타", "en": "Other", "ja": "その他", "zh": "其他", "fr": "Autre"},
    "species_to_plant": {
        "ko": "심을 작물", "en": "Crop to plant", "ja": "植える作物", "zh": "要种植的作物", "fr": "Culture à planter",
    },
    "custom_species_prompt": {
        "ko": "작물 이름을 입력해주세요", "en": "Enter the crop name", "ja": "作物の名前を入力してください",
        "zh": "请输入作物名称", "fr": "Entrez le nom de la culture",
    },
    "pot_size_label": {"ko": "화분 크기", "en": "Pot size", "ja": "鉢のサイズ", "zh": "花盆大小", "fr": "Taille du pot"},
    "plot_size_label": {"ko": "텃밭 크기", "en": "Garden size", "ja": "菜園のサイズ", "zh": "菜园大小", "fr": "Taille du jardin"},
    "pot_name_label": {
        "ko": "화분 이름 (별명)", "en": "Pot name (nickname)", "ja": "鉢植えの名前（ニックネーム）",
        "zh": "花盆名称（昵称）", "fr": "Nom du pot (surnom)",
    },
    "plot_name_label": {
        "ko": "텃밭 이름 (별명)", "en": "Garden name (nickname)", "ja": "菜園の名前（ニックネーム）",
        "zh": "菜园名称（昵称）", "fr": "Nom du jardin (surnom)",
    },
    "register_button": {"ko": "등록하기", "en": "Register", "ja": "登録する", "zh": "登记", "fr": "Enregistrer"},
    "register_warning_pot": {
        "ko": "화분 이름과 작물을 입력해주세요.", "en": "Please enter a pot name and crop.",
        "ja": "鉢植えの名前と作物を入力してください。", "zh": "请输入花盆名称和作物。",
        "fr": "Veuillez saisir un nom de pot et une culture.",
    },
    "register_warning_plot": {
        "ko": "텃밭 이름과 작물을 입력해주세요.", "en": "Please enter a garden name and crop.",
        "ja": "菜園の名前と作物を入力してください。", "zh": "请输入菜园名称和作物。",
        "fr": "Veuillez saisir un nom de jardin et une culture.",
    },
    "duplicate_pot_name": {
        "ko": "이미 같은 이름의 화분이 있어요. 다른 이름을 써주세요.",
        "en": "You already have a pot with this name. Please use a different name.",
        "ja": "同じ名前の鉢植えがすでにあります。別の名前を使ってください。",
        "zh": "已存在同名的花盆，请使用其他名称。",
        "fr": "Vous avez déjà un pot portant ce nom. Veuillez utiliser un autre nom.",
    },
    "duplicate_plot_name": {
        "ko": "이미 같은 이름의 텃밭이 있어요. 다른 이름을 써주세요.",
        "en": "You already have a garden with this name. Please use a different name.",
        "ja": "同じ名前の菜園がすでにあります。別の名前を使ってください。",
        "zh": "已存在同名的菜园，请使用其他名称。",
        "fr": "Vous avez déjà un jardin portant ce nom. Veuillez utiliser un autre nom.",
    },
    "generating_guide_spinner": {
        "ko": "AI가 나만의 재배 가이드를 만들고 있어요... (약 15초 정도 걸려요)",
        "en": "AI is creating your personalized growing guide... (about 15 seconds)",
        "ja": "AIがあなた専用の栽培ガイドを作成しています…（約15秒かかります）",
        "zh": "AI正在为你生成专属的种植指南……（大约需要15秒）",
        "fr": "L'IA prépare votre guide de culture personnalisé... (environ 15 secondes)",
    },
    "pot_registered_flash": {
        "ko": "'{name}' 화분이 등록됐어요! 수확까지의 가이드를 만들었어요.",
        "en": "'{name}' has been registered! We've created a guide through harvest.",
        "ja": "「{name}」の鉢植えが登録されました！収穫までのガイドを作成しました。",
        "zh": "「{name}」花盆已登记！已为你生成到收获为止的指南。",
        "fr": "« {name} » a été enregistré ! Un guide jusqu'à la récolte a été créé.",
    },
    "plot_registered_flash": {
        "ko": "'{name}' 텃밭이 등록됐어요! 수확까지의 가이드를 만들었어요.",
        "en": "'{name}' has been registered! We've created a guide through harvest.",
        "ja": "「{name}」の菜園が登録されました！収穫までのガイドを作成しました。",
        "zh": "「{name}」菜园已登记！已为你生成到收获为止的指南。",
        "fr": "« {name} » a été enregistré ! Un guide jusqu'à la récolte a été créé.",
    },
    "cancel_and_back": {
        "ko": "← 취소하고 돌아가기", "en": "← Cancel and go back", "ja": "← キャンセルして戻る",
        "zh": "← 取消并返回", "fr": "← Annuler et revenir",
    },

    "pot_not_found": {
        "ko": "화분 정보를 찾을 수 없습니다.", "en": "Couldn't find this pot.", "ja": "鉢植え情報が見つかりません。",
        "zh": "找不到花盆信息。", "fr": "Pot introuvable.",
    },
    "plot_not_found": {
        "ko": "텃밭 정보를 찾을 수 없습니다.", "en": "Couldn't find this garden.", "ja": "菜園情報が見つかりません。",
        "zh": "找不到菜园信息。", "fr": "Jardin introuvable.",
    },
    "edit_name": {"ko": "이름 수정", "en": "Edit name", "ja": "名前を編集", "zh": "编辑名称", "fr": "Modifier le nom"},
    "new_pot_name_label": {
        "ko": "새 화분 이름", "en": "New pot name", "ja": "新しい鉢植えの名前",
        "zh": "新的花盆名称", "fr": "Nouveau nom du pot",
    },
    "new_plot_name_label": {
        "ko": "새 텃밭 이름", "en": "New garden name", "ja": "新しい菜園の名前",
        "zh": "新的菜园名称", "fr": "Nouveau nom du jardin",
    },
    "guide_ai_caption": {
        "ko": "AI가 이 작물에 맞게 생성한 가이드입니다", "en": "This guide was generated by AI for this crop",
        "ja": "AIがこの作物に合わせて生成したガイドです", "zh": "这是AI为该作物生成的指南",
        "fr": "Ce guide a été généré par l'IA pour cette culture",
    },
    "guide_default_caption": {
        "ko": "기본 가이드입니다 (AI 생성 실패 시 대체)", "en": "This is the default guide (used when AI generation fails)",
        "ja": "基本ガイドです（AI生成に失敗した場合の代替）", "zh": "这是默认指南（AI生成失败时使用）",
        "fr": "Ceci est le guide par défaut (utilisé en cas d'échec de l'IA)",
    },
    "current_status_memo": {
        "ko": "현재 상태 메모", "en": "Current status note", "ja": "現在の状態メモ", "zh": "当前状态备注", "fr": "Note sur l'état actuel",
    },
    "memo_placeholder": {
        "ko": "예: 꽃이 피기 시작함, 아랫잎이 노랗게 변함",
        "en": "e.g. flowers starting to bloom, lower leaves turning yellow",
        "ja": "例：花が咲き始めた、下葉が黄色くなった",
        "zh": "例：开始开花了、下部叶片变黄了",
        "fr": "ex. : les fleurs commencent à s'ouvrir, les feuilles du bas jaunissent",
    },
    "guideline_title": {"ko": "가이드라인", "en": "Guideline", "ja": "ガイドライン", "zh": "指南", "fr": "Guide"},
    "guideline_progress": {
        "ko": "{done}/{total}단계 완료", "en": "{done}/{total} steps done", "ja": "{done}/{total}段階完了",
        "zh": "已完成 {done}/{total} 个阶段", "fr": "{done}/{total} étapes terminées",
    },
    "photo_diagnosis_title": {
        "ko": "사진으로 정밀검사", "en": "Photo checkup", "ja": "写真で精密検査", "zh": "照片精密检测", "fr": "Diagnostic par photo",
    },
    "photo_diagnosis_caption": {
        "ko": "화분/식물 사진을 올리면 AI가 상태를 분석하고 가이드라인을 조정해줘요.",
        "en": "Upload a photo of your plant and AI will analyze its condition and adjust the guideline.",
        "ja": "鉢植え・植物の写真をアップロードすると、AIが状態を分析してガイドラインを調整します。",
        "zh": "上传花盆/植物照片，AI会分析状态并调整指南。",
        "fr": "Téléchargez une photo de votre plante et l'IA analysera son état pour ajuster le guide.",
    },
    "upload_photo": {"ko": "사진 업로드", "en": "Upload photo", "ja": "写真をアップロード", "zh": "上传照片", "fr": "Télécharger une photo"},
    "start_ai_diagnosis": {
        "ko": "AI 정밀검사 시작", "en": "Start AI checkup", "ja": "AI精密検査を開始", "zh": "开始AI精密检测", "fr": "Démarrer le diagnostic IA",
    },
    "analyzing_photo_spinner": {
        "ko": "AI가 사진을 분석하고 있어요... (약 10~15초 정도 걸려요)",
        "en": "AI is analyzing the photo... (about 10-15 seconds)",
        "ja": "AIが写真を分析しています…（約10〜15秒かかります）",
        "zh": "AI正在分析照片……（大约需要10-15秒）",
        "fr": "L'IA analyse la photo... (environ 10 à 15 secondes)",
    },
    "diagnosis_failed": {
        "ko": "AI 서버가 혼잡해서 분석에 실패했어요. 잠시 후 다시 시도해주세요.",
        "en": "The AI server is busy and the analysis failed. Please try again shortly.",
        "ja": "AIサーバーが混雑していて分析に失敗しました。しばらくしてからもう一度お試しください。",
        "zh": "AI服务器繁忙，分析失败，请稍后重试。",
        "fr": "Le serveur IA est surchargé et l'analyse a échoué. Veuillez réessayer sous peu.",
    },
    "adjusted_guide_preview": {
        "ko": "조정된 가이드라인 미리보기", "en": "Preview of adjusted guideline", "ja": "調整後のガイドラインプレビュー",
        "zh": "调整后的指南预览", "fr": "Aperçu du guide ajusté",
    },
    "update_guide_button": {
        "ko": "이 가이드라인으로 업데이트하기", "en": "Update to this guideline", "ja": "このガイドラインに更新する",
        "zh": "更新为此指南", "fr": "Mettre à jour avec ce guide",
    },
    "guide_updated_flash": {
        "ko": "가이드라인이 업데이트됐어요!", "en": "The guideline has been updated!", "ja": "ガイドラインが更新されました！",
        "zh": "指南已更新！", "fr": "Le guide a été mis à jour !",
    },
    "growth_history_title": {
        "ko": "성장 기록 ({n}건)", "en": "Growth history ({n})", "ja": "成長記録（{n}件）",
        "zh": "生长记录（{n}条）", "fr": "Historique de croissance ({n})",
    },
    "days_since_planted": {
        "ko": "심은 지 {n}일째", "en": "day {n} since planting", "ja": "植えてから{n}日目",
        "zh": "种下第{n}天", "fr": "jour {n} depuis la plantation",
    },
    "soil_title": {"ko": "추천 흙", "en": "Recommended soil", "ja": "おすすめの土", "zh": "推荐土壤", "fr": "Sol recommandé"},
    "fertilizer_title": {
        "ko": "추천 비료", "en": "Recommended fertilizer", "ja": "おすすめの肥料", "zh": "推荐肥料", "fr": "Engrais recommandé",
    },
    "homemade_fertilizer_title": {
        "ko": "천연비료 만들기", "en": "Making natural fertilizer", "ja": "天然肥料の作り方",
        "zh": "自制天然肥料", "fr": "Fabriquer un engrais naturel",
    },
    "harvest_review_title": {
        "ko": "수확 후기", "en": "Harvest review", "ja": "収穫レビュー", "zh": "收获评价", "fr": "Avis de récolte",
    },
    "difficulty_label": {
        "ko": "난이도: {value}", "en": "Difficulty: {value}", "ja": "難易度：{value}",
        "zh": "难度：{value}", "fr": "Difficulté : {value}",
    },
    "no_recommendation": {
        "ko": "추천 정보가 없어요.", "en": "No recommendation available.", "ja": "推薦情報がありません。",
        "zh": "暂无推荐信息。", "fr": "Aucune recommandation disponible.",
    },
    "harvest_reached_caption": {
        "ko": "수확 시기에 도달했어요! 후기를 남기면 AI가 다음 작물을 추천해줘요.",
        "en": "It's harvest time! Leave a review and AI will recommend your next crop.",
        "ja": "収穫時期になりました！レビューを残すとAIが次の作物を推薦してくれます。",
        "zh": "已经到收获期啦！留下评价后AI会为你推荐下一个作物。",
        "fr": "C'est l'heure de la récolte ! Laissez un avis et l'IA vous recommandera votre prochaine culture.",
    },
    "go_write_review": {
        "ko": "후기 쓰러 가기", "en": "Write a review", "ja": "レビューを書きに行く", "zh": "去写评价", "fr": "Rédiger un avis",
    },
    "delete_button": {"ko": "삭제하기", "en": "Delete", "ja": "削除する", "zh": "删除", "fr": "Supprimer"},
    "confirm_delete_pot": {
        "ko": "정말로 '{name}' 화분을 삭제하시겠어요? 되돌릴 수 없어요.",
        "en": "Are you sure you want to delete the pot '{name}'? This can't be undone.",
        "ja": "本当に「{name}」の鉢植えを削除しますか？元に戻せません。",
        "zh": "确定要删除花盆「{name}」吗？此操作无法撤销。",
        "fr": "Voulez-vous vraiment supprimer le pot « {name} » ? Cette action est irréversible.",
    },
    "confirm_delete_plot": {
        "ko": "정말로 '{name}' 텃밭을 삭제하시겠어요? 되돌릴 수 없어요.",
        "en": "Are you sure you want to delete the garden '{name}'? This can't be undone.",
        "ja": "本当に「{name}」の菜園を削除しますか？元に戻せません。",
        "zh": "确定要删除菜园「{name}」吗？此操作无法撤销。",
        "fr": "Voulez-vous vraiment supprimer le jardin « {name} » ? Cette action est irréversible.",
    },
    "yes_delete": {"ko": "네, 삭제합니다", "en": "Yes, delete it", "ja": "はい、削除します", "zh": "是的，删除", "fr": "Oui, supprimer"},
    "pot_deleted_flash": {
        "ko": "'{name}' 화분을 삭제했어요.", "en": "Deleted the pot '{name}'.", "ja": "「{name}」の鉢植えを削除しました。",
        "zh": "已删除花盆「{name}」。", "fr": "Le pot « {name} » a été supprimé.",
    },
    "plot_deleted_flash": {
        "ko": "'{name}' 텃밭을 삭제했어요.", "en": "Deleted the garden '{name}'.", "ja": "「{name}」の菜園を削除しました。",
        "zh": "已删除菜园「{name}」。", "fr": "Le jardin « {name} » a été supprimé.",
    },

    "weather_check_title": {
        "ko": "위치로 날씨 정밀검사", "en": "Weather check by location", "ja": "位置情報による天気精密検査",
        "zh": "按位置进行天气检测", "fr": "Vérification météo par localisation",
    },
    "weather_check_caption": {
        "ko": (
            "텃밭 위치를 선택하면 AI가 그 지역의 실시간 날씨(비·구름·기온 등)를 검색해서 가이드라인을 조정해줘요. "
            "한 번 실행해두면 이후 이 위치를 기준으로 폭염·한파·태풍 등 긴급 위기가 있을 때 매일 자동으로 알려드려요."
        ),
        "en": (
            "Select your garden's location and AI will look up real-time weather there (rain, clouds, temperature, etc.) "
            "to adjust the guideline. Once you run this, we'll automatically check this location every day and alert you "
            "if there's a heatwave, cold snap, typhoon, or other emergency."
        ),
        "ja": (
            "菜園の位置を選択すると、AIがその地域のリアルタイムの天気（雨・曇り・気温など）を検索してガイドラインを調整します。"
            "一度実行しておくと、以後この位置を基準に猛暑・寒波・台風などの緊急事態を毎日自動で確認してお知らせします。"
        ),
        "zh": (
            "选择菜园位置后，AI会搜索该地区的实时天气（降雨、多云、气温等）并调整指南。"
            "运行一次后，之后会以此位置为基准每天自动检查是否有高温、寒潮、台风等紧急天气并提醒你。"
        ),
        "fr": (
            "Sélectionnez l'emplacement de votre jardin et l'IA recherchera la météo en temps réel de cette zone "
            "(pluie, nuages, température, etc.) pour ajuster le guide. Une fois exécuté, nous vérifierons "
            "automatiquement cet emplacement chaque jour et vous alerterons en cas de canicule, vague de froid, "
            "typhon ou autre urgence."
        ),
    },
    "set_location_now": {
        "ko": "지금 텃밭 위치를 입력할게요", "en": "I'll enter the garden's location now",
        "ja": "今、菜園の位置を入力します", "zh": "现在输入菜园位置",
        "fr": "Je vais indiquer l'emplacement du jardin maintenant",
    },
    "province_label": {"ko": "시/도", "en": "Province/City", "ja": "都道府県", "zh": "省/市", "fr": "Province/Ville"},
    "district_label": {"ko": "시/군/구", "en": "District", "ja": "市区町村", "zh": "区/县", "fr": "Arrondissement"},
    "start_weather_check": {
        "ko": "AI 날씨 정밀검사 시작", "en": "Start AI weather check", "ja": "AI天気精密検査を開始",
        "zh": "开始AI天气检测", "fr": "Démarrer la vérification météo IA",
    },
    "weather_searching_spinner": {
        "ko": "AI가 '{location}'의 날씨를 검색하고 있어요... (약 20~30초 정도 걸려요)",
        "en": "AI is looking up the weather in '{location}'... (about 20-30 seconds)",
        "ja": "AIが「{location}」の天気を検索しています…（約20〜30秒かかります）",
        "zh": "AI正在搜索「{location}」的天气……（大约需要20-30秒）",
        "fr": "L'IA recherche la météo à « {location} »... (environ 20 à 30 secondes)",
    },
    "sources_title": {
        "ko": "참고한 출처", "en": "Sources referenced", "ja": "参考にした出典", "zh": "参考来源", "fr": "Sources consultées",
    },

    "harvest_review_heading": {
        "ko": "{name} 수확 후기", "en": "{name} — Harvest review", "ja": "{name} 収穫レビュー",
        "zh": "{name} 收获评价", "fr": "{name} — Avis de récolte",
    },
    "difficulty_section_title": {
        "ko": "1. 난이도", "en": "1. Difficulty", "ja": "1. 難易度", "zh": "1. 难度", "fr": "1. Difficulté",
    },
    "difficulty_question": {
        "ko": "이번 작물, 키우기 어떠셨나요?", "en": "How was growing this crop?", "ja": "今回の作物、育ててみていかがでしたか？",
        "zh": "这次种植感觉难度如何？", "fr": "Comment s'est passée la culture de cette plante ?",
    },
    "difficulty_easy": {"ko": "쉬웠어요", "en": "Easy", "ja": "簡単でした", "zh": "很简单", "fr": "Facile"},
    "difficulty_hard": {"ko": "어려웠어요", "en": "Hard", "ja": "難しかったです", "zh": "很难", "fr": "Difficile"},
    "review_section_title": {
        "ko": "2. 후기", "en": "2. Review", "ja": "2. レビュー", "zh": "2. 评价", "fr": "2. Avis",
    },
    "review_textarea_label": {
        "ko": "지금까지 관리하면서 느꼈던 생각이나 느낌을 자유롭게 적어주세요.",
        "en": "Write freely about your thoughts and experience while growing this.",
        "ja": "これまで育ててきて感じたことを自由に書いてください。",
        "zh": "请自由写下你在种植过程中的想法和感受。",
        "fr": "Écrivez librement vos réflexions et votre expérience pendant la culture.",
    },
    "review_placeholder_pot": {
        "ko": "예: 별 탈 없이 잘 자라서 뿌듯했어요 / 물 주는 타이밍을 못 맞춰서 잎이 시든 적도 있었어요",
        "en": "e.g. It grew well without issues and I felt proud / The leaves wilted once because I missed watering",
        "ja": "例：特に問題なく育って嬉しかった／水やりのタイミングを逃して葉がしおれたこともあった",
        "zh": "例：一直长得很好，很有成就感 / 有一次没掌握好浇水时机导致叶子蔫了",
        "fr": "ex. : Elle a bien poussé sans problème, j'étais fier / Les feuilles ont flétri une fois que j'ai raté l'arrosage",
    },
    "review_placeholder_plot": {
        "ko": "예: 텃밭 흙이 좋아서 생각보다 잘 자랐어요 / 비 예보를 못 챙겨서 물이 넘친 적이 있었어요",
        "en": "e.g. The soil was good so it grew better than expected / It got overwatered once because I missed the rain forecast",
        "ja": "例：菜園の土が良くて思ったより育った／雨予報を見逃して水が溢れたこともあった",
        "zh": "例：菜园土壤好，长得比预想的还好 / 有一次没注意天气预报导致积水",
        "fr": "ex. : Le sol du jardin était bon, elle a mieux poussé que prévu / Elle a été trop arrosée une fois car j'ai manqué les prévisions de pluie",
    },
    "submit_review_button": {
        "ko": "후기 제출하고 다음 작물 추천받기", "en": "Submit review and get a crop recommendation",
        "ja": "レビューを送信して次の作物のおすすめを受け取る", "zh": "提交评价并获取下一个作物推荐",
        "fr": "Envoyer l'avis et obtenir une recommandation de culture",
    },
    "review_warning_empty": {
        "ko": "후기를 입력해주세요.", "en": "Please write a review.", "ja": "レビューを入力してください。",
        "zh": "请输入评价。", "fr": "Veuillez rédiger un avis.",
    },
    "recommend_spinner": {
        "ko": "AI가 다음 작물을 추천하고 있어요... (약 5~10초 정도 걸려요)",
        "en": "AI is recommending your next crop... (about 5-10 seconds)",
        "ja": "AIが次の作物を推薦しています…（約5〜10秒かかります）",
        "zh": "AI正在推荐下一个作物……（大约需要5-10秒）",
        "fr": "L'IA recommande votre prochaine culture... (environ 5 à 10 secondes)",
    },
    "recommend_failed": {
        "ko": "AI 서버가 혼잡해서 추천을 생성하지 못했어요.", "en": "The AI server is busy and couldn't generate a recommendation.",
        "ja": "AIサーバーが混雑していて推薦を生成できませんでした。", "zh": "AI服务器繁忙，未能生成推荐。",
        "fr": "Le serveur IA est surchargé et n'a pas pu générer de recommandation.",
    },
    "analyzing_review_spinner": {
        "ko": "AI가 후기를 문장별로 살펴보고 있어요... (약 10~20초 정도 걸려요)",
        "en": "AI is looking through your review sentence by sentence... (about 10-20 seconds)",
        "ja": "AIが後記を文章ごとに確認しています…（約10〜20秒かかります）",
        "zh": "AI正在逐句分析你的后记……（大约需要10-20秒）",
        "fr": "L'IA examine votre avis phrase par phrase... (environ 10 à 20 secondes)",
    },
    "review_analysis_heading": {
        "ko": "{name} 후기 분석", "en": "{name} — Review breakdown", "ja": "{name} 後記分析",
        "zh": "{name} 后记分析", "fr": "{name} — Analyse de l'avis",
    },
    "recommend_label": {"ko": "추천:", "en": "Recommended:", "ja": "おすすめ:", "zh": "推荐:", "fr": "Recommandé :"},
    "overall_recommend_heading": {
        "ko": "종합 추천", "en": "Overall recommendation", "ja": "総合おすすめ",
        "zh": "综合推荐", "fr": "Recommandation globale",
    },
    "no_points_found": {
        "ko": "후기에서 뚜렷한 포인트를 찾지 못했어요.", "en": "Couldn't find clear points in the review.",
        "ja": "後記から明確なポイントを見つけられませんでした。", "zh": "未能从后记中找到明确的要点。",
        "fr": "Aucun point clair n'a pu être identifié dans l'avis.",
    },

    "icon_change_title": {
        "ko": "아이콘 변경", "en": "Change icon", "ja": "アイコン変更", "zh": "更改头像", "fr": "Changer l'icône",
    },
    "reset_to_default_icon": {
        "ko": "기본 아이콘으로 되돌리기", "en": "Reset to default icon", "ja": "デフォルトアイコンに戻す",
        "zh": "恢复默认头像", "fr": "Rétablir l'icône par défaut",
    },
    "photo_set_title": {
        "ko": "사진으로 설정", "en": "Set from photo", "ja": "写真で設定", "zh": "使用照片设置", "fr": "Définir à partir d'une photo",
    },
    "photo_preview_caption": {
        "ko": "미리보기 (동그란 아이콘 안에 어떻게 보일지)", "en": "Preview (how it will look inside the round icon)",
        "ja": "プレビュー（丸いアイコンの中でどう見えるか）", "zh": "预览（在圆形头像中的效果）",
        "fr": "Aperçu (rendu dans l'icône ronde)",
    },
    "save_this_photo": {
        "ko": "이 사진으로 저장하기", "en": "Save this photo", "ja": "この写真で保存する",
        "zh": "保存此照片", "fr": "Enregistrer cette photo",
    },
    "icon_saved_flash": {
        "ko": "아이콘이 저장됐어요!", "en": "Your icon has been saved!", "ja": "アイコンが保存されました！",
        "zh": "头像已保存！", "fr": "Votre icône a été enregistrée !",
    },
    "generating_explanation_spinner": {
        "ko": "AI가 자세한 설명을 만들고 있어요... (약 20초 정도 걸려요)",
        "en": "AI is preparing a detailed explanation... (about 20 seconds)",
        "ja": "AIが詳しい説明を作成しています…（約20秒かかります）",
        "zh": "AI正在生成详细说明……（大约需要20秒）",
        "fr": "L'IA prépare une explication détaillée... (environ 20 secondes)",
    },
    "explanation_failed_fallback": {
        "ko": "AI 서버가 혼잡해서 자세한 설명을 불러오지 못했어요. 우선 위 요약 설명을 참고해서 진행해보세요: {desc}",
        "en": "The AI server is busy and couldn't load a detailed explanation. For now, please refer to the summary above: {desc}",
        "ja": "AIサーバーが混雑していて詳しい説明を読み込めませんでした。まずは上記の要約を参考に進めてみてください：{desc}",
        "zh": "AI服务器繁忙，未能加载详细说明。请先参考上面的摘要说明进行操作：{desc}",
        "fr": "Le serveur IA est surchargé et n'a pas pu charger d'explication détaillée. Pour l'instant, référez-vous au résumé ci-dessus : {desc}",
    },
    "feature_label": {"ko": "특징", "en": "Feature", "ja": "特徴", "zh": "特点", "fr": "Caractéristique"},
    "cultivation_tip_label": {
        "ko": "{kind} 재배 팁", "en": "{kind} growing tip", "ja": "{kind}栽培のコツ",
        "zh": "{kind}种植小贴士", "fr": "Astuce de culture ({kind})",
    },
    "base_fertilizer_label": {"ko": "밑거름", "en": "Base fertilizer", "ja": "元肥", "zh": "基肥", "fr": "Engrais de fond"},
    "top_fertilizer_label": {"ko": "웃거름", "en": "Top dressing", "ja": "追肥", "zh": "追肥", "fr": "Engrais d'appoint"},
    "caution_label": {
        "ko": "주의·보충", "en": "Caution / supplement", "ja": "注意・補足", "zh": "注意事项/补充", "fr": "Attention / complément",
    },
    "fertilizer_unavailable": {
        "ko": "비료 추천 정보를 불러오지 못했어요.", "en": "Couldn't load fertilizer recommendations.",
        "ja": "肥料の推薦情報を読み込めませんでした。", "zh": "未能加载肥料推荐信息。",
        "fr": "Impossible de charger les recommandations d'engrais.",
    },
    "common_fertilizer_expander": {
        "ko": "모든 채소에 무난한 기타 비료 추천", "en": "Other fertilizers that suit any crop",
        "ja": "どの野菜にも使える万能肥料の紹介", "zh": "适合所有蔬菜的通用肥料推荐",
        "fr": "Autres engrais adaptés à toutes les cultures",
    },

    "terms_title": {"ko": "이용약관", "en": "Terms of Service", "ja": "利用規約", "zh": "服务条款", "fr": "Conditions d'utilisation"},
    "terms_agree_checkbox": {
        "ko": "이용약관에 동의합니다", "en": "I agree to the Terms of Service",
        "ja": "利用規約に同意します", "zh": "我同意服务条款",
        "fr": "J'accepte les conditions d'utilisation",
    },
    "terms_required_warning": {
        "ko": "이용약관에 동의해야 가입할 수 있어요.", "en": "You must agree to the Terms of Service to sign up.",
        "ja": "利用規約に同意しないと登録できません。", "zh": "必须同意服务条款才能注册。",
        "fr": "Vous devez accepter les conditions d'utilisation pour vous inscrire.",
    },
    "terms_text": {
        "ko": (
            "제1조 (목적)\n"
            "이 약관은 '허브'(이하 '서비스')가 제공하는 AI 기반 재배 가이드 서비스의 이용 조건과 절차를 정합니다.\n\n"
            "제2조 (서비스의 내용)\n"
            "서비스는 이용자가 입력한 작물 정보를 바탕으로 Anthropic Claude API를 통해 재배 가이드, 사진 진단, "
            "날씨 기반 관리 조언을 생성합니다. AI가 생성한 정보는 참고용이며, 실제 재배 결과를 보장하지 않습니다.\n\n"
            "제3조 (이용자의 의무)\n"
            "이용자는 가입 시 정확한 정보를 입력해야 하며, 본인 계정과 비밀번호를 안전하게 관리할 책임이 있습니다. "
            "타인의 정보를 도용하거나 서비스를 부정한 목적으로 사용해서는 안 됩니다.\n\n"
            "제4조 (미성년자 이용)\n"
            "만 14세 미만 이용자는 법정대리인의 동의 없이 개인정보를 제공해서는 안 됩니다. "
            "만 14세 미만임이 확인될 경우 서비스 이용이 제한될 수 있습니다.\n\n"
            "제5조 (서비스 변경 및 중단)\n"
            "서비스는 운영상·기술상 필요에 따라 사전 공지 후 변경되거나 일시 중단될 수 있습니다.\n\n"
            "제6조 (책임의 제한)\n"
            "서비스가 제공하는 정보는 AI가 생성한 참고 자료이며, 이를 활용한 재배 결과에 대해 서비스는 책임을 지지 않습니다."
        ),
        "en": (
            "Article 1 (Purpose)\n"
            "These Terms set out the conditions and procedures for using the AI-based growing guide service "
            "provided by 'Hub' (the \"Service\").\n\n"
            "Article 2 (Service Description)\n"
            "Based on the crop information you enter, the Service uses the Anthropic Claude API to generate "
            "growing guides, photo diagnoses, and weather-based care advice. AI-generated information is for "
            "reference only and does not guarantee actual growing results.\n\n"
            "Article 3 (User Obligations)\n"
            "Users must enter accurate information when signing up and are responsible for keeping their "
            "account and password secure. Users must not impersonate others or use the Service for improper "
            "purposes.\n\n"
            "Article 4 (Use by Minors)\n"
            "Users under the age of 14 must not provide personal information without the consent of a legal "
            "guardian. Service use may be restricted if a user is confirmed to be under 14.\n\n"
            "Article 5 (Changes to and Suspension of the Service)\n"
            "The Service may be changed or temporarily suspended, with prior notice, as operationally or "
            "technically necessary.\n\n"
            "Article 6 (Limitation of Liability)\n"
            "Information provided by the Service is AI-generated reference material, and the Service is not "
            "liable for growing outcomes based on its use."
        ),
        "ja": (
            "第1条（目的）\n"
            "本規約は、「Hub」（以下「サービス」）が提供するAIベースの栽培ガイドサービスの利用条件および"
            "手続きを定めます。\n\n"
            "第2条（サービスの内容）\n"
            "サービスは、利用者が入力した作物情報をもとにAnthropic Claude APIを通じて栽培ガイド、写真診断、"
            "天気に基づく管理アドバイスを生成します。AIが生成した情報は参考用であり、実際の栽培結果を保証する"
            "ものではありません。\n\n"
            "第3条（利用者の義務）\n"
            "利用者は登録時に正確な情報を入力する必要があり、自身のアカウントとパスワードを安全に管理する責任が"
            "あります。他人の情報を盗用したり、サービスを不正な目的で使用してはなりません。\n\n"
            "第4条（未成年者の利用）\n"
            "満14歳未満の利用者は、法定代理人の同意なしに個人情報を提供してはなりません。満14歳未満であることが"
            "確認された場合、サービスの利用が制限されることがあります。\n\n"
            "第5条（サービスの変更および中断）\n"
            "サービスは、運営上・技術上の必要に応じて事前告知の上、変更または一時中断されることがあります。\n\n"
            "第6条（責任の制限）\n"
            "サービスが提供する情報はAIが生成した参考資料であり、これを活用した栽培結果についてサービスは責任を"
            "負いません。"
        ),
        "zh": (
            "第1条（目的）\n"
            "本条款规定了\"Hub\"（以下简称\"服务\"）提供的AI种植指南服务的使用条件和程序。\n\n"
            "第2条（服务内容）\n"
            "服务会根据用户输入的作物信息，通过Anthropic Claude API生成种植指南、照片诊断和基于天气的养护建议。"
            "AI生成的信息仅供参考，不保证实际种植结果。\n\n"
            "第3条（用户义务）\n"
            "用户注册时必须输入准确信息，并对自己的账户和密码的安全负责。用户不得盗用他人信息，也不得将服务用于"
            "不正当目的。\n\n"
            "第4条（未成年人使用）\n"
            "未满14周岁的用户不得在未经法定监护人同意的情况下提供个人信息。如确认用户未满14周岁，服务使用可能"
            "受到限制。\n\n"
            "第5条（服务的变更及中断）\n"
            "服务可能因运营或技术需要，在事先通知后进行变更或暂时中断。\n\n"
            "第6条（责任限制）\n"
            "服务提供的信息是AI生成的参考资料，对于据此产生的种植结果，服务不承担责任。"
        ),
        "fr": (
            "Article 1 (Objet)\n"
            "Les présentes conditions définissent les modalités et procédures d'utilisation du service de guide "
            "de culture basé sur l'IA fourni par « Hub » (le « Service »).\n\n"
            "Article 2 (Description du service)\n"
            "Sur la base des informations sur les cultures que vous saisissez, le Service utilise l'API Claude "
            "d'Anthropic pour générer des guides de culture, des diagnostics par photo et des conseils "
            "d'entretien basés sur la météo. Les informations générées par l'IA sont fournies à titre indicatif "
            "uniquement et ne garantissent pas les résultats réels de culture.\n\n"
            "Article 3 (Obligations de l'utilisateur)\n"
            "L'utilisateur doit saisir des informations exactes lors de l'inscription et est responsable de la "
            "sécurité de son compte et de son mot de passe. Il est interdit d'usurper l'identité d'autrui ou "
            "d'utiliser le Service à des fins inappropriées.\n\n"
            "Article 4 (Utilisation par des mineurs)\n"
            "Les utilisateurs de moins de 14 ans ne doivent pas fournir de données personnelles sans le "
            "consentement d'un représentant légal. L'utilisation du Service peut être restreinte si l'utilisateur "
            "est confirmé comme ayant moins de 14 ans.\n\n"
            "Article 5 (Modification et interruption du service)\n"
            "Le Service peut être modifié ou temporairement interrompu, avec préavis, selon les besoins "
            "opérationnels ou techniques.\n\n"
            "Article 6 (Limitation de responsabilité)\n"
            "Les informations fournies par le Service sont des données de référence générées par l'IA, et le "
            "Service décline toute responsabilité quant aux résultats de culture obtenus à partir de leur "
            "utilisation."
        ),
    },
    "setting_privacy": {
        "ko": "개인정보처리방침", "en": "Privacy Policy", "ja": "プライバシーポリシー",
        "zh": "隐私政策", "fr": "Politique de confidentialité",
    },
    "privacy_policy_text": {
        "ko": (
            "'허브'는 다음과 같이 개인정보를 처리합니다.\n\n"
            "1. 수집하는 개인정보 항목\n"
            "- 필수: 이름, 이메일, 비밀번호(암호화 저장)\n"
            "- 선택: 프로필 사진, 텃밭 위치(시/도·시/군/구), 업로드한 식물 사진\n\n"
            "2. 개인정보의 수집 및 이용 목적\n"
            "- 회원 식별 및 로그인\n"
            "- AI 재배 가이드·사진 진단·날씨 기반 조언 생성\n"
            "- 커뮤니티·1:1 AI 채팅 기능 제공\n\n"
            "3. 개인정보의 제3자 제공\n"
            "사진, 작물 정보, 위치, 대화 내용 등은 AI 응답 생성을 위해 Anthropic(Claude API)에 전송될 수 있습니다. "
            "그 외의 목적으로 제3자에게 제공하지 않습니다.\n\n"
            "4. 개인정보의 보관 및 파기\n"
            "비밀번호는 PBKDF2-SHA256으로 암호화하여 저장합니다. 이용자가 계정을 삭제하면 화분·텃밭·채팅 기록을 "
            "포함한 모든 개인정보가 즉시 영구 삭제됩니다.\n\n"
            "5. 이용자의 권리\n"
            "이용자는 언제든 설정에서 이메일·비밀번호를 변경하거나 계정을 삭제해 개인정보 이용을 중단할 수 있습니다.\n\n"
            "6. 문의\n"
            "서비스 이용 중 개인정보 관련 문의는 팀 운영자에게 연락해 주세요."
        ),
        "en": (
            "'Hub' processes personal information as follows.\n\n"
            "1. Personal information collected\n"
            "- Required: name, email, password (stored encrypted)\n"
            "- Optional: profile photo, garden location (province/district), uploaded plant photos\n\n"
            "2. Purpose of collection and use\n"
            "- Member identification and login\n"
            "- Generating AI growing guides, photo diagnoses, and weather-based advice\n"
            "- Providing community and 1:1 AI chat features\n\n"
            "3. Provision of personal information to third parties\n"
            "Photos, crop information, location, and chat content may be sent to Anthropic (Claude API) to "
            "generate AI responses. Information is not provided to third parties for any other purpose.\n\n"
            "4. Retention and destruction of personal information\n"
            "Passwords are encrypted and stored using PBKDF2-SHA256. When a user deletes their account, all "
            "personal information — including pots, gardens, and chat history — is immediately and permanently "
            "deleted.\n\n"
            "5. User rights\n"
            "Users can change their email or password, or delete their account at any time in Settings to stop "
            "the use of their personal information.\n\n"
            "6. Contact\n"
            "For questions about personal information while using the Service, please contact the team."
        ),
        "ja": (
            "「Hub」は以下のように個人情報を取り扱います。\n\n"
            "1. 収集する個人情報の項目\n"
            "必須：氏名、メールアドレス、パスワード（暗号化して保存）\n"
            "任意：プロフィール写真、菜園の位置（都道府県・市区町村）、アップロードした植物の写真\n\n"
            "2. 個人情報の収集および利用目的\n"
            "会員識別およびログイン\n"
            "AI栽培ガイド・写真診断・天気に基づくアドバイスの生成\n"
            "コミュニティ・1対1 AIチャット機能の提供\n\n"
            "3. 個人情報の第三者提供\n"
            "写真、作物情報、位置、会話内容などはAI応答生成のためAnthropic（Claude API）に送信される場合が"
            "あります。それ以外の目的で第三者に提供することはありません。\n\n"
            "4. 個人情報の保管および破棄\n"
            "パスワードはPBKDF2-SHA256で暗号化して保存します。利用者がアカウントを削除すると、鉢植え・菜園・"
            "チャット履歴を含むすべての個人情報が直ちに完全に削除されます。\n\n"
            "5. 利用者の権利\n"
            "利用者はいつでも設定画面からメールアドレス・パスワードを変更したり、アカウントを削除して個人情報の"
            "利用を停止することができます。\n\n"
            "6. お問い合わせ\n"
            "サービス利用中の個人情報に関するお問い合わせはチーム運営者までご連絡ください。"
        ),
        "zh": (
            "\"Hub\"按以下方式处理个人信息。\n\n"
            "1. 收集的个人信息项目\n"
            "必填：姓名、邮箱、密码（加密存储）\n"
            "选填：头像照片、菜园位置（省/市及区/县）、上传的植物照片\n\n"
            "2. 个人信息的收集和使用目的\n"
            "会员身份识别及登录\n"
            "生成AI种植指南、照片诊断及基于天气的建议\n"
            "提供社区及一对一AI聊天功能\n\n"
            "3. 个人信息向第三方提供\n"
            "照片、作物信息、位置、聊天内容等可能会为生成AI回复而发送给Anthropic（Claude API）。除此之外不会以"
            "其他目的提供给第三方。\n\n"
            "4. 个人信息的保存及销毁\n"
            "密码使用PBKDF2-SHA256加密存储。用户删除账户后，包括花盆、菜园、聊天记录在内的所有个人信息将立即"
            "永久删除。\n\n"
            "5. 用户权利\n"
            "用户可随时在设置中更改邮箱、密码，或删除账户以停止个人信息的使用。\n\n"
            "6. 联系方式\n"
            "在使用服务过程中如有个人信息相关问题，请联系团队负责人。"
        ),
        "fr": (
            "« Hub » traite les données personnelles comme suit.\n\n"
            "1. Données personnelles collectées\n"
            "Obligatoires : nom, e-mail, mot de passe (stocké de manière chiffrée)\n"
            "Facultatives : photo de profil, emplacement du jardin (province/arrondissement), photos de plantes "
            "téléchargées\n\n"
            "2. Finalités de la collecte et de l'utilisation\n"
            "Identification des membres et connexion\n"
            "Génération de guides de culture par IA, de diagnostics par photo et de conseils basés sur la météo\n"
            "Fourniture des fonctionnalités de communauté et de discussion individuelle avec l'IA\n\n"
            "3. Transmission des données personnelles à des tiers\n"
            "Les photos, les informations sur les cultures, la localisation et le contenu des discussions "
            "peuvent être transmis à Anthropic (API Claude) afin de générer les réponses de l'IA. Aucune donnée "
            "n'est transmise à des tiers à d'autres fins.\n\n"
            "4. Conservation et suppression des données personnelles\n"
            "Les mots de passe sont chiffrés et stockés à l'aide de PBKDF2-SHA256. Lorsqu'un utilisateur "
            "supprime son compte, toutes ses données personnelles — y compris les pots, jardins et l'historique "
            "de discussion — sont immédiatement et définitivement supprimées.\n\n"
            "5. Droits de l'utilisateur\n"
            "Les utilisateurs peuvent à tout moment modifier leur e-mail ou mot de passe, ou supprimer leur "
            "compte dans les Paramètres pour cesser l'utilisation de leurs données personnelles.\n\n"
            "6. Contact\n"
            "Pour toute question relative aux données personnelles pendant l'utilisation du Service, veuillez "
            "contacter l'équipe."
        ),
    },
}


def t(key: str, language: str = DEFAULT_LANGUAGE) -> str:
    entry = TRANSLATIONS.get(key)
    if not entry:
        return key
    return entry.get(language) or entry.get(DEFAULT_LANGUAGE) or key


SPECIES_NAMES = {
    "토마토": {"ko": "토마토", "en": "Tomato", "ja": "トマト", "zh": "番茄", "fr": "Tomate"},
    "가지": {"ko": "가지", "en": "Eggplant", "ja": "ナス", "zh": "茄子", "fr": "Aubergine"},
    "고추": {"ko": "고추", "en": "Chili pepper", "ja": "唐辛子", "zh": "辣椒", "fr": "Piment"},
    "상추": {"ko": "상추", "en": "Lettuce", "ja": "レタス", "zh": "生菜", "fr": "Laitue"},
    "오이": {"ko": "오이", "en": "Cucumber", "ja": "キュウリ", "zh": "黄瓜", "fr": "Concombre"},
    "깻잎": {"ko": "깻잎", "en": "Perilla leaf", "ja": "エゴマの葉", "zh": "紫苏叶", "fr": "Feuille de périlla"},
    "파": {"ko": "파", "en": "Green onion", "ja": "ネギ", "zh": "大葱", "fr": "Oignon vert"},
    "애호박": {"ko": "애호박", "en": "Zucchini", "ja": "ズッキーニ", "zh": "西葫芦", "fr": "Courgette"},
    "감자": {"ko": "감자", "en": "Potato", "ja": "ジャガイモ", "zh": "土豆", "fr": "Pomme de terre"},
    "당근": {"ko": "당근", "en": "Carrot", "ja": "ニンジン", "zh": "胡萝卜", "fr": "Carotte"},
    "고구마": {"ko": "고구마", "en": "Sweet potato", "ja": "サツマイモ", "zh": "红薯", "fr": "Patate douce"},
    "마늘": {"ko": "마늘", "en": "Garlic", "ja": "ニンニク", "zh": "大蒜", "fr": "Ail"},
    "바질": {"ko": "바질", "en": "Basil", "ja": "バジル", "zh": "罗勒", "fr": "Basilic"},
}

SIZE_NAMES = {
    "소형 (지름 20cm 이하)": {
        "ko": "소형 (지름 20cm 이하)", "en": "Small (≤20cm diameter)", "ja": "小型（直径20cm以下）",
        "zh": "小型（直径20cm以下）", "fr": "Petit (≤20cm de diamètre)",
    },
    "중형 (지름 20~40cm)": {
        "ko": "중형 (지름 20~40cm)", "en": "Medium (20-40cm diameter)", "ja": "中型（直径20-40cm）",
        "zh": "中型（直径20-40cm）", "fr": "Moyen (20-40cm de diamètre)",
    },
    "대형 (지름 40cm 이상)": {
        "ko": "대형 (지름 40cm 이상)", "en": "Large (≥40cm diameter)", "ja": "大型（直径40cm以上）",
        "zh": "大型（直径40cm以上）", "fr": "Grand (≥40cm de diamètre)",
    },
    "소형 (1평 이하)": {
        "ko": "소형 (1평 이하)", "en": "Small (≤3.3m²)", "ja": "小型（約3.3m²以下）",
        "zh": "小型（约3.3平方米以下）", "fr": "Petit (≤3,3m²)",
    },
    "중형 (1~3평)": {
        "ko": "중형 (1~3평)", "en": "Medium (3.3-10m²)", "ja": "中型（約3.3-10m²）",
        "zh": "中型（约3.3-10平方米）", "fr": "Moyen (3,3-10m²)",
    },
    "대형 (3평 이상)": {
        "ko": "대형 (3평 이상)", "en": "Large (≥10m²)", "ja": "大型（約10m²以上）",
        "zh": "大型（约10平方米以上）", "fr": "Grand (≥10m²)",
    },
}


def species_name(species: str, language: str = DEFAULT_LANGUAGE) -> str:
    entry = SPECIES_NAMES.get(species)
    if not entry:
        return species
    return entry.get(language) or entry.get(DEFAULT_LANGUAGE) or species


def size_name(size: str, language: str = DEFAULT_LANGUAGE) -> str:
    entry = SIZE_NAMES.get(size)
    if not entry:
        return size
    return entry.get(language) or entry.get(DEFAULT_LANGUAGE) or size
