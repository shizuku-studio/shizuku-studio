# しずく AI Studio | AIモデル募集導線 改修ブリーフ

---

## ブランド情報（必須厳守）

- **ブランド名**：しずく AI Studio（英: Shizuku AI Studio）
- **株式会社This is Me の名称は一切使用禁止**（LP・X・LINE・契約書すべて）
- ロゴ表記：`💧 しずく AI Studio`（「AI Studio」は金色 `#C8A84B`）
- Copyright表記：`© 2026 Shizuku AI Studio. All rights reserved.`

---

## 現状ファイル構成

| ファイル | 役割 | 状態 |
|---|---|---|
| `shizuku-studio/lp-recruit.html` | AIモデル募集LP（ダークテーマ） | ブランド名更新が必要 |
| `shizuku-studio/index.html` | メインLP（ライト/パープル系） | 更新済み |
| `shizuku-studio/lp-new.html` | 美容系LP（別軸） | 更新済み |
| `shizuku-studio/add_cta.py` | X投稿動画CTA合成スクリプト | ブランド名更新が必要 |

---

## lp-recruit.html 現状構成

### デザイン
- 背景：`#0A0A0F`（ほぼ黒）
- アクセント：`#C8A84B`（ゴールド）
- フォント：Noto Serif JP（見出し）+ Noto Sans JP
- CSS変数：`--gold`, `--deep`, `--text`, `--gray`, `--line-green`

### セクション構成
1. **HERO** — メインキャッチ＋CTAボタン
2. **PERSONA** — 6つのターゲット像（会社員/主婦/学生/バツイチ/育休中/地方在住）
3. **FEATURES** — 3つの特徴（顔出し不要/撮影だけ/ストック型収益）
4. **INCOME** — 収益テーブル（スタート3〜10万/成長10〜30万/安定30〜100万円以上）
5. **HOW IT WORKS** — 参加フロー4ステップ
6. **FAQ** — 6問（顔バレ/未経験/副業バレ/退出/報酬/撮影内容）
7. **CTA** — LINEボタン（`#apply`セクション）
8. **FOOTER**

### 現状の問題点
- [ ] hero内 `<p class="hero-brand serif">しずくStudio</p>` → `しずく AI Studio` に変更必要
- [ ] FEATURES内 "すべてしずくStudioが担当します" → ブランド名更新
- [ ] Copyright `© 2026 Shizuku Studio.` → `© 2026 Shizuku AI Studio.` に変更
- [ ] LINE URL `lin.ee/XXXXXXX` → 本番URLに差し替え
- [ ] CTA文言「あなたの物語を、しずくに。」→ 魅力度向上の余地あり

---

## 改修方針（優先順）

### Phase 1：即日修正（ブランド統一）
- [ ] lp-recruit.html の「しずくStudio」→「しずく AI Studio」全置換
- [ ] add_cta.py の「しずくStudio」テキスト更新
- [ ] Copyright更新

### Phase 2：導線強化（今週中）
- [ ] **ウォームアップCTAの追加**：LINEボタン前に「今すぐ応募できない方へ」→ Xフォロー誘導ボタンを追加
- [ ] **FAQの充実**：「どんな撮影か」に「指示書あり/強要なし」をより具体的に記載
- [ ] **FLOW追加**：契約書にAI顔置換同意条項が含まれることを明示
- [ ] **LINE URL本番化**：`lin.ee/XXXXXXX` を正式URLに変更

### Phase 3：コンバージョン向上（来週以降）
- [ ] **ビフォーアフター画像/動画セクション追加**（index.htmlに実装済みのコンポーネントを流用）
- [ ] **社会的証明の強化**：収益実績の説得力アップ（事例数・期間・職種の多様性）
- [ ] **スクロールアニメーション**：既存のfade-up効果強化
- [ ] **モバイルファースト最適化**：CTAボタンの固定フッター化（スクロール中常時表示）

---

## 改修アドバイス

### 1. CTAの二段階設計
LINE相談への心理的ハードルを下げるため、以下の二段階構造を推奨：
```
[今すぐ相談] LINEで無料相談する   ← メインCTA
[まずは詳しく] Xをフォローして事例を見る  ← サブCTA
```

### 2. 安心感の視覚的演出
- **証明ロゴバー**：「クラウドサイン契約」「AV新法対応」「電子署名」などのバッジを並べる
- **数字で示す実績**：「累計○○名参加」「平均月収○万円」などを hero に入れる
- 現状は文字情報のみ → バッジ/アイコン/数字での可視化が効果的

### 3. ペルソナページへのLINEアンカー
各ペルソナカードに「これが私かも → 相談してみる↓」のマイクロCTAを追加すると
離脱防止になる（FEATURESまで読まなくてもLINEに飛べる）

### 4. Instagram/X連携への誘導追加
現状はLINEのみ。講義13回の「2アカ体制/Ponto」設計に合わせて：
- **Ponto経由のリンク集**を使い、LINE・IG・Xをまとめて提示
- LPフッターに「Instagramで活動リポート公開中 →」リンクを追加

### 5. ダークテーマの活用
現lp-recruit.htmlのダークデザインは「秘密感・特別感」を演出しており、
モデル募集LPとして差別化効果がある。**index.htmlのライトテーマとの使い分けは正しい**。
ただしデザイン統一感のため以下を揃えること：
- ロゴ表記の統一（`💧 しずく AI Studio`）
- ゴールドカラー `#C8A84B` の統一

---

## ツール・システム連携

| 用途 | ツール/プラットフォーム |
|---|---|
| 電子契約 | クラウドサイン |
| AI顔置換 | ACUL (Acool) — クラシックモデル、年齢補正+15〜20 |
| AI顔生成 | ChatGPT — 1名あたり15〜30パターン |
| モザイク編集 | CapCut Pro（月2,500円）|
| 販売 | OnlyFans（海外）+ MyFans（国内）|
| LINE募集導線 | LINE公式アカウント |
| リンク集約 | Ponto（IG→OF/MyFans間接誘導）|
| X招集 | メイン+サブ2アカ体制（BAN対策）|

---

## 収益モデル（LP掲載用）

| ステージ | 目安月収（モデル取り分30%） | 目安期間 |
|---|---|---|
| スタート期 | 3万〜10万円 | 1〜2ヶ月目 |
| 成長期 | 10万〜30万円 | 3〜6ヶ月目 |
| 安定期 | 30万〜100万円以上 | 6ヶ月〜 |

**補足（内部用）**：講義事例では Sara熟女アカウントが月874万円達成（モデル取り分30%で約262万円相当）

---

## 改修ログ

| 日付 | 作業内容 | 担当 |
|---|---|---|
| 2026-06-11 | brief作成、現状整理、改修方針策定 | Claude |
| 2026-06-11 | Phase 1完了：lp-recruit.html ブランド名全更新、add_cta.py更新 | Claude |
| 2026-06-11 | **優先順位1完了**：`lp-monitor.html` 新規作成（顔出しなしAI映像モニター募集LP） | Claude |

### lp-monitor.html 仕様
- URL候補：`https://shizuku-studio.github.io/shizuku-studio/lp-monitor.html`
- ダークテーマ（lp-recruit.htmlと同系統）
- セクション：HERO → WHAT IS THIS → SAFETY PROMISE → HOW IT WORKS → FAQ → CTA
- 固定LINE誘導ボタン（スクロール時に画面下部に常時表示）
- HEROを過ぎたらスティッキーLINEボタン表示
- フェードインアニメーション実装済み
- 禁止表現：高収入煽り・誰でも稼げる断定・成人向け要素・一切なし

---

## 関連ファイル

- `D:\Claude-MyProject\subscguild\講義ノート全17回.md` — 全講義サマリー
- `D:\Claude-MyProject\shizuku-studio\lp-recruit.html` — 改修対象メインファイル
- `D:\Claude-MyProject\shizuku-studio\index.html` — メインLP（参照用）
- `C:\Users\user\.claude\projects\d--Claude-MyProject\memory\project_subscguild.md` — 事業メモリ
