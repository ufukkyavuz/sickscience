---
name: reference-session-archive-access
description: How to recover archived/other sessions: search_session_transcripts skips archived ones; read ~/.claude/projects/<proj>/*.jsonl; unarchive_session tool
metadata:
  type: reference
---

Kullanıcı arşivlediği oturumlardaki konuşmaların (Drive linkleri, Pinterest panosu, kararlar) hatırlanmasını bekler ve "bu geçmişi göremiyor musun" diye sinirlenir (2026-11-13).

- `search_session_transcripts` ve `list_sessions` arşivli oturumları ARAMAZ.
- Doğrusu: `~/.claude/projects/-Users-ufo-…-SickScience/*.jsonl` dosyalarını `grep`/python ile tara (aranan kelime + Drive link); ya da `list_events` ile oturum geçmişi.
- Kullanıcı "arşivden çıkar" derse `mcp__ccd_session_mgmt__unarchive_session` (ToolSearch ile yükle); auto mode hook'u ilk çağrıda input'u değiştirir, aynı input ile bir kez daha çağır.
- Çocuk oturumu arşivlenince bitirdiği işi bu oturum devralır; önce geçmişi oku.
