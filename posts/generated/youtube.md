---
title: "क्या YouTube के ऑटो-जनरेटेड कैप्शन इतने सही हैं कि उन्हें कोट किया जा सके?"
slug: "youtube"
author: "Hanako H."
source: "devto_python"
published: "Thu, 05 Nov 2026 14:17:34 +0000"
description: "ज़्यादातर YouTube वीडियो में ट्रांसक्रिप्ट होती है, और उनमें से अधिकतर को स्पीच रिकग्निशन ने लिखा होता है। वीडियो के साथ चलने के लिए यह ठीक है। लेकिन किसी पे..."
keywords: "tracks, youtube, because, they, willing, not, hard, kind"
generated: "2026-11-05T14:31:30.068109"
---

# क्या YouTube के ऑटो-जनरेटेड कैप्शन इतने सही हैं कि उन्हें कोट किया जा सके?

## Overview

ज़्यादातर YouTube वीडियो में ट्रांसक्रिप्ट होती है, और उनमें से अधिकतर को स्पीच रिकग्निशन ने लिखा होता है। वीडियो के साथ चलने के लिए यह ठीक है। लेकिन किसी पेपर, न्यूज़ स्टोरी या क़ानूनी नोट में कोट देने के लिए सवाल यह है कि ऑटोमैटिक टेक्स्ट असल में कही गई बात से कितना दूर है, और उसके टाइमस्टैम्प सही सेकंड पर इशारा करते हैं या नहीं। जिस वीडियो में दोनों तरह के कैप्शन हों, वह इसका सीधा जवाब देता है। वीडियो NASA का अपलोड किया हुआ राष्ट्रपति कैनेडी का 1962 का राइस यूनिवर्सिटी वाला भाषण है ( WZyRbnpGyzQ , 18 मिनट)। इसमें दो अंग्रेज़ी ट्रैक हैं: एक किसी इंसान का लिखा हुआ और एक YouTube का बनाया हुआ। दोनों को Python पैकेज youtube-transcript-api से लिस्ट और डाउनलोड किया जा सकता है: from youtube_transcript_api import YouTubeTranscriptApi tracks = YouTubeTranscriptApi (). list ( " WZyRbnpGyzQ " ) for t in tracks : print ( t . language_code , t . is_generated , t . language ) # en False English - Caption # en True English (auto-generated) manual = tracks . find_manually_created_transcript ([ " en " ]). fetch (). to_raw_data () auto = tracks . find_generated_transcript ([ " en " ]). fetch (). to_raw_data () हर एंट्री टेक्स्ट की एक लाइन होती है, जिसके साथ स्टार्ट टाइम और सेकंड में अवधि होती है। दोनों ट्रैक में कितना फ़र्क है शब्द-दर-शब्द तुलना करने पर (लोअरकेस, विराम चिह्न हटाकर, Python के difflib.SequenceMatcher से अलाइन करके) दोनों ट्रैक भाषण के लगभग 95% हिस्से पर एक जैसे हैं: इंसान का लिखा ऑटो-जनरेटेड लाइनें 183 332 शब्द 2,233 2,211 विराम चिह्न 255 4 अलग शब्द लगभग 143 (6%) छह प्रतिशत छोटा लगता है, जब तक यह न देखें कि वे कौन से शब्द हैं। स्पीच रिकग्निशन आम शब्दों पर अच्छा करता है और नामों, संख्याओं और तकनीकी शब्दों पर बुरा, और कोट अक्सर इन्हीं हिस्सों पर टिका होता है: इंसान का लिखा ऑटो-जनरेटेड President Pitzer President pit launched John Glenn launched John gland a Saturn C-1 booster rocket a satin C1 Cape Canaveral (second mention) canabal we are willing to accept we're willing to accept एक खाली जगह भी है। लगभग 4:47 पर ऑटोमैटिक ट्रैक "both must be" से सीधे "determined and cannot be deterred" पर कूद जाता है। बीच के 28 शब्द, "enterprised and overcome with answerable courage. If this capsule history of our progress teaches us anything, it is that man, in his quest for knowledge and progress, is", उसमें हैं ही नहीं। ऑटोमैटिक ट्रैक में कुछ भी इस खाली जगह को चिह्नित नहीं करता। मशहूर लाइन का क्या होता है इस भाषण की जो लाइन लोग कोट करते हैं, वह 9:18 पर है। इंसानी ट्रैक में यह एक लाइन है, विराम चिह्नों के साथ और एक स्टार्ट टाइम के साथ: 558.90 3.65 not because they are easy, but because they are hard, ऑटोमैटिक ट्रैक में यह तीन ओवरलैप होती लाइनों में फैली है, और पहला शब्द पिछली लाइन का है: 555.64 4.80 decade and do the other things not 558.20 6.52 because they are easy but because they 560.44 7.04 are hard because that goal will serve to ऑटोमैटिक कैप्शन रोलिंग डिस्प्ले के लिए बने होते हैं, एक बार में कुछ शब्द, इसलिए उनकी लाइनें वाक्यों की जगह बोलने के टाइमिंग का पीछा करती हैं। कोट करने के लिए इससे दो बातें निकलती हैं। 9:18 वाली लाइन कॉपी करने पर ऐसा टुकड़ा मिलता है जो वाक्य के बीच से शुरू होता है, और "not" वाली लाइन का स्टार्ट टाइम 9:15 है, यानी कोट से तीन सेकंड पहले। कैप्शन के तौर पर दोनों में कुछ ग़लत नहीं; सायटेशन के तौर पर दोनों ग़लत हैं। इस मामले में व्याकरण बचा रहा, "they are", उस वर्शन के उलट जो ज़्यादातर लोगों को याद है ("because it is hard")। लेकिन कुछ लाइनों बाद "we are willing" बन गया "we're willing", और ऑटोमैटिक ट्रैक से लिया गया कोट कैनेडी के मुँह में ऐसा संक्षिप्त रूप डाल देगा जो उन्होंने कहा ही नहीं। ट्रैक चुनना, और लिंक osFoundry डेस्कटॉप ऐप का ट्रांसक्रिप्ट टूल, जो उसी कंप्यूटर से कैप्शन लाता है जिस पर वह चल रहा है, यह चुनाव Rust की कुछ लाइनों में करता है। YouTube ऑटोमैटिक ट्रैक को kind: "asr" से चिह्नित करता है, और ऐप पहले इंसान का लिखा अंग्रेज़ी ट्रैक लेता है, फिर कोई भी अंग्रेज़ी ट्रैक, फिर कोई भी इंसानी ट्रैक, और फिर जो भी मौजूद हो: fn pick_track ( tracks : & [ CaptionTrack ]) -> Option <& CaptionTrack > { tracks .iter () .find (| t | t .language_code .starts_with ( "en" ) && t .kind != "asr" ) .or_else (|| tracks .iter () .find (| t | t .language_code .starts_with ( "en" ))) .or_else (|| tracks .iter () .find (| t | t .kind != "asr" )) .or_else (|| tracks .first ()) } जब कोई लाइन रेफ़रेंस के रूप में सेव होती है, तो उसका स्टार्ट टाइम लिंक का t पैरामीटर बन जाता है। समय नीचे की ओर राउंड किया जाता है, ताकि वीडियो शब्दों से सेकंड के एक हिस्से पहले शुरू हो, पहले शब्द के बाद नहीं: url : `https://www.youtube.com/watch?v= ${ transcript . video_id } &t= ${ Math . floor ( segment . start )} s` 9:18 वाली लाइन के लिए यह &t=558s है, उस लाइन के लिए जो 558.9 सेकंड पर शुरू होती है। जब सिर्फ़ ऑटोमैटिक ट्रैक हो बहुत से वीडियो में सिर्फ़ ऑटोमैटिक ट्रैक होता है। तब वह सर्च इंडेक्स है, स्रोत नहीं: उससे मोटे तौर पर पता करें कि बात कहाँ कही गई, वह हिस्सा चलाएँ और कोट ऑडियो सुनकर लिखें। नाम और संख्याएँ किसी दूसरे स्रोत से जाँचें, और ऐसे हिस्सों की उम्मीद रखें जो बिना किसी निशान के ग़ायब हैं। सेकंड तक पहुँचने वाला लिंक फिर भी रखने लायक़ है, क्योंकि उससे पाठक वही जाँच कुछ सेकंड में दोहरा सकता है। यहाँ इस्तेमाल हुआ डेस्कटॉप ऐप osFoundry डाउनलोड पेज से मुफ़्त है।

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bestaitools-hi/kyaa-youtube-ke-ontto-jnrettedd-kaipshn-itne-shii-hain-ki-unhen-kott-kiyaa-jaa-ske-4lon

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
