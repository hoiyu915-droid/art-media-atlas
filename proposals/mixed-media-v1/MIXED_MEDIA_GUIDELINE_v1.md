# 混合媒材使用準則 v1

**狀態：** Proposal only / non-executable  
**範圍：** 醫學圖卡、研究摘要卡、機制卡、器官與儀器說明卡  
**來源鎖：** Art Media Atlas `2026.07.23` / blob `ae096ceaf1ff2b0afe9c5c181dab5f51d9e2370c`

## 1. 決策

醫學圖卡預設採「一個主體媒材 + 一個功能性 partner」：

- `base_medium` 決定整張卡的主要視覺語言。
- `partner_medium` 只補線條、解剖、器材、標籤或局部質地。
- 上限為 1 個 base + 2 個 partner；不以隨機換風格製造多樣性。
- atlas 的 `pending` 媒材一律保留 `MANUAL_REVIEW_REQUIRED`，本提案不會把它們偷偷升級為自動候選。

## 2. SEED14 預設配方

| 角色 | 媒材 | 任務 |
|---|---|---|
| Base | M17 色鉛筆 | 溫度、局部色彩、人物與器官表面 |
| Partner | M22 石墨鉛筆 | 解剖結構、儀器輪廓、底稿與細節 |
| Conditional partner | M39 針管筆 | 只有高密度標籤／精細器械需要時，且 resolver 驗證通過 |

這個配方不是由名稱或外觀猜測，而是沿用 canonical SEED14 explicit binding：M17 + M22。

## 3. 混合原則

1. **功能先於裝飾。** Partner 必須回答「它補了哪個缺口」。
2. **濕性與乾性媒材不要同時搶主位。** 濕性媒材只能作受控 base 或局部層次。
3. **背景服從閱讀。** 維持乾淨暖象牙底；禁止整頁泛黃、舊紙、深色 vignette。
4. **證據色與藝術色分離。** CORE / INFERENCE / GAP / CONFLICT 只能用於小標籤、細框或圓點。
5. **逐卡決定。** 同一系列可共享結構，但媒材 proposal 仍需依每卡 anatomy / text / portrait / public-health 任務評估。
6. **只送相關裁切 panel。** 不把完整 75 筆 atlas 或完整九宮格送入 renderer。

## 4. 題材路由

| 題材 | 預設 |
|---|---|
| 醫學機制、解剖、研究摘要 | M17 + M22 |
| 儀器與密集標籤 | M17 + M22；必要時提案 M39 |
| 公衛流程與平塗模組 | M02 + M39 |
| 柔和病人／生活敘事 | M01 + M39，或 M17 + M22 |
| 高對比少色公衛卡 | M50 + M39，或 M74 |
| 高精度數位流程／解剖 | M73 / M74 |
| 歷史、檔案、古典線描 | 只走人工審核的 M06 / M24 / 版畫或攝影工藝支線 |

## 5. 禁止預設

- 以混合媒材數量代替設計品質。
- 大面積水洗、噴槍、厚塗、漆面或工藝表面壓過文字。
- 把 output method 當作繪畫風格。
- 從媒材名稱、seed 名稱、情緒或相似外觀推斷 executable binding。
- 讓 `pending` / family-default 媒材進入自動 runtime。
- 把證據色當器官主色或背景色。

## 6. 本輪 provisional matrix

- BASE：18
- PARTNER：24
- AVOID_DEFAULT：33
- Atlas 自動候選：12
- 保留人工審核：63

`AVOID_DEFAULT` 不是藝術上的否定，而是「不進醫學圖卡的預設自動路由」；仍可在明確題材、人工選擇與 smoke test 後使用。

## 7. Promotion gate

本提案要成為 executable policy，至少需要：

1. 對新增候選媒材完成 4-panel cropped reference。
2. 逐媒材進行文字、數值、解剖與背景污染 smoke test。
3. 將通過者由 `family_default_estimate` 提升為 reviewed pilot profile。
4. 更新 atlas version 與 blob SHA。
5. 更新 seed binding 或 resolver contract，不能只改這份 proposal。
