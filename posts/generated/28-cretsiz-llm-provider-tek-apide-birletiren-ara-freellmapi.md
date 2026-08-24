---
title: "28 Ücretsiz LLM Provider'ı Tek API'de Birleştiren Araç: FreeLLMAPI"
slug: "28-cretsiz-llm-provider-tek-apide-birletiren-ara-freellmapi"
author: "coddykit"
source: "devto_ai"
published: "Mon, 24 Aug 2026 18:37:15 +0000"
description: "GitHub Trending'de bugün dikkat çeken bir proje var: FreeLLMAPI . 19,694 yıldız almış bu açık kaynak araç, 34 farklı LLM sağlayıcısının ücretsiz kotasını tek..."
keywords: "bir, freellmapi, provider, tek, api, her, openai, endpoint"
generated: "2026-08-24T18:48:28.655293"
---

# 28 Ücretsiz LLM Provider'ı Tek API'de Birleştiren Araç: FreeLLMAPI

## Overview

GitHub Trending'de bugün dikkat çeken bir proje var: FreeLLMAPI . 19,694 yıldız almış bu açık kaynak araç, 34 farklı LLM sağlayıcısının ücretsiz kotasını tek bir OpenAI-uyumlu API endpoint'inde birleştiriyor. Nedir Bu FreeLLMAPI? Her büyük AI laboratuvarı artık ücretsiz kota sunuyor - ayda birkaç milyon token, günde birkaç bin istek. Tek başına her biri oyuncak gibi. Ama birleştirildiğinde? Ayda 7.4 milyar token çalışan çıkarım kapasitesi ediyor. Sorun şu ki, bunları elle birleştirmek acı verici: otuz dört farklı SDK, otuz dört farklı rate limit, otuz dört farklı hata noktası. FreeLLMAPI bunu tek bir OpenAI-uyumlu endpoint'e indirgiyor. Neden Önemli? 1. Maliyet Sıfır, Güç Maksimum 34 ücretsiz provider (Google, Groq, Cerebras, Mistral, OpenRouter, Cohere, NVIDIA, HuggingFace ve daha fazlası) 474 model ailesi , 635 ücretsiz endpoint Ayda ~7.4 milyar token toplam kapasite 2. Akıllı Yönlendirme Router, her istek için en uygun modeli seçiyor. Bir provider rate limit'e takıldığında otomatik olarak bir sonrakine geçiyor. Her anahtar için kullanım takibi yapıyor, böylece her ücretsiz kotanın altında kalıyorsunuz. 3. Şifreli Anahtar Yönetimi Provider anahtarları SQLite'ta AES-256-GCM ile şifrelenmiş. Uygulamalarınız sadece tek bir birleşik freellmapi-... bearer token görüyor. Nasıl Çalışır? from openai import OpenAI client = OpenAI ( base_url = " http://localhost:3001/v1 " , api_key = " freellmapi-your-unified-key " , ) resp = client . chat . completions . create ( model = " auto " , # router en iyisini seçsin messages = [{ " role " : " user " , " content " : " Roma ' nın çöküşünü bir cümlede özetle. " }], ) print ( resp . choices [ 0 ]. message . content ) print ( " Yönlendirildi: " , resp . headers . get ( " x-routed-via " )) Her yanıt X-Routed-Via: <platform>/<model> header'ı taşıyor, böylece hangi provider'ın hizmet verdiğini görebiliyorsunuz. Kurulum Docker ile tek komut: curl -fsSL https://freellmapi.co/install.sh | bash Bu komut: ~/freellmapi dizinini oluşturur Şifreleme anahtarı üretir Docker imajını çeker Konteynerı başlatır Sonra http://localhost:3001 adresine gidin, Keys sayfasından provider anahtarlarınızı ekleyin, Fallback Chain'i istediğiniz gibi sıralayın ve birleşik API anahtarınızı alın. Desteklenen Araçlar FreeLLMAPI, birçok popüler AI kodlama aracıyla çalışıyor: Claude Code - npx freellmapi setup-claude Codex CLI - npx freellmapi setup-codex Aider - npx freellmapi setup-aider Cline, Roo Code, Continue, OpenCode, Cursor, Zed, JetBrains AI ve daha fazlası Gelişmiş Özellikler Fusion (Çoklu Model Sentezi) Sanal fusion modelini istediğinizde, router prompt'unuzu paralel olarak çeşitli ücretsiz modellere gönderiyor, sonra bir yargıç model taslaklardan tek bir yanıt sentezliyor. Prompt Sıkıştırma Opt-in olarak, paylaşılan bir istek hattı prompt'ları çoğaltabilir, araç çıktısını filtreleyebilir, tekrarlanan JSON'u sıkıştırabilir ve önbellek aramasından önce eski bağlamı kırpabilir. Otomatik Katalog Güncellemesi Router, günde iki kez freellmapi.co 'dan imzalı bir katalog çekiyor: yeni modeller, kota değişiklikleri ve provider uyumluluk düzeltmeleri otomatik olarak geliyor. Desktop Uygulaması Native bir menü çubuğu uygulaması da var: tüm router + dashboard yerel olarak tepsinizden çalışıyor, canlı istek istatistiklerini gösteren bir glass popover ile. Sınırlamalar FreeLLMAPI'nin açıkça belirttiği önemli sınırlamalar var: Frontier modeller yok (GPT-4, Claude 3.5 Sonnet gibi en güçlü modeller ücretsiz değil) Değişken gecikme - farklı provider'lar farklı hızlarda SLA yok - ücretsiz kotalar değişebilir veya kaldırılabilir Gün içinde zeka düşüşü - en iyi modeller günlük kotalarına ulaştıkça, UTC gece yarısında sıfırlanana kadar endpoint'in etkin zekası düşüyor Proje açıkça "kişisel deney ve öğrenme için, üretim için değil" diyor. Gerçek bir şey inşa ediyorsanız, göndermeden önce ücretli API'ye geçin. Mimari Çıkarımlar Bu proje, API tasarımı ve backend geliştirme açısından birçok ders veriyor: API Gateway pattern : Tek endpoint, çoklu backend Rate limiting ve quota yönetimi : Her provider için ayrı takip Failover stratejileri : Otomatik yeniden deneme ve cooldown Şifreleme : Anahtar yönetimi ve güvenlik Mikroservis mimarisi : Modüler provider adaptörleri Bu konularda derinlemesine bilgi için CoddyKit 'in Backend Geliştirme kurslarına göz atabilirsiniz. Sonuç FreeLLMAPI, ücretsiz LLM kotalarını birleştirerek geliştiricilere güçlü bir deney ortamı sunuyor. Tek bir OpenAI-uyumlu endpoint, akıllı yönlendirme, otomatik failover ve şifreli anahtar yönetimi ile, AI prototipleme için etkileyici bir araç. Ancak unutmayın: bu bir öğrenme aracı, üretim altyapısı değil. Gerçek uygulamalar için ücretli API'lere geçiş yapın. GitHub: tashfeenahmed/freellmapi Website: freellmapi.co Lisans: MIT Bu makale, GitHub Trending'deki ilginç açık kaynak projeleri tanıtan serinin bir parçası. Daha fazla teknik içerik için CoddyKit Blog 'u takip edin.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/coddykit/28-ucretsiz-llm-provideri-tek-apide-birlestiren-arac-freellmapi-5967

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
