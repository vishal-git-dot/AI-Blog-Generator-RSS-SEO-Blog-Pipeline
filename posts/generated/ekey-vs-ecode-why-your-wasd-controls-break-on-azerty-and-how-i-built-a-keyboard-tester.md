---
title: "e.key vs e.code: Why Your WASD Controls Break on AZERTY (and How I Built a Keyboard Tester)"
slug: "ekey-vs-ecode-why-your-wasd-controls-break-on-azerty-and-how-i-built-a-keyboard-tester"
author: "Arelvox"
source: "devto_webdev"
published: "Wed, 04 Nov 2026 14:00:00 +0000"
description: "If you have ever built keyboard shortcuts or a game in the browser, you have probably used e.key . Then someone with a French or German keyboard tells you yo..."
keywords: "key, code, keyboard, tester, you, function, keycode, layout"
generated: "2026-11-04T14:06:42.005075"
---

# e.key vs e.code: Why Your WASD Controls Break on AZERTY (and How I Built a Keyboard Tester)

## Overview

If you have ever built keyboard shortcuts or a game in the browser, you have probably used e.key . Then someone with a French or German keyboard tells you your WASD controls are broken. The fix is one property you may not be using: e.code . Here is the difference, and what I learned building a keyboard tester. 👉 Live demo: arelvox.com/keyboard-tester key vs code vs keyCode Press the key to the right of Tab on three different layouts: Layout e.key e.code e.keyCode US (QWERTY) q KeyQ 81 French (AZERTY) a KeyQ 65 German (QWERTZ) q KeyQ 81 e.key is the character the key produces. It depends on the layout, Shift, Caps Lock and so on. e.code is the physical position of the key, named after the US layout. It never changes with the layout. e.keyCode is deprecated and inconsistent between browsers. Avoid it in new code. Rule of thumb Typing text, shortcuts that show a letter in the UI (like Ctrl+S): use e.key . Game controls and anything about where the key is (WASD, a keyboard tester): use e.code . document . addEventListener ( ' keydown ' , function ( e ) { if ( e . code === ' KeyW ' ) moveUp (); // works on AZERTY too (it is the Z key there) }); Building a keyboard tester A keyboard tester is a nice exercise because it forces you to use e.code . Each key on the virtual keyboard has its code as a data attribute: var ROWS = [ [[ ' Escape ' , ' Esc ' ], [ ' F1 ' , ' F1 ' ], /* ... */ ], [[ ' Backquote ' , ' ` ' ], [ ' Digit1 ' , ' 1 ' ], /* ... */ [ ' Backspace ' , ' Backspace ' , 2 ]], // [code, label, width] ]; On keydown , I look up the element by code and mark it as tested: document . addEventListener ( ' keydown ' , function ( e ) { e . preventDefault (); // stop Tab, Space, arrows from scrolling var el = root . querySelector ( ' [data-c=" ' + e . code + ' "] ' ); if ( el ) el . className = ' key done down ' ; }); document . addEventListener ( ' keyup ' , function ( e ) { var el = root . querySelector ( ' [data-c=" ' + e . code + ' "] ' ); if ( el ) el . className = ' key done ' ; }); Gotchas I hit 1. Left and right modifiers are different codes. ShiftLeft and ShiftRight , ControlLeft and ControlRight , AltLeft and AltRight . Great for a tester, but remember it if you check e.code === 'ShiftLeft' and the user presses the right one. 2. Some keys never reach the page. Fn is handled inside the keyboard itself, so no website can detect it. Print Screen, media keys and some Windows key combinations are often eaten by the operating system. A tester should say so, or people think their key is broken. 3. Stuck "pressed" keys after Alt+Tab. If the window loses focus while a key is down, you never get the keyup . Clear the pressed state on blur : window . addEventListener ( ' blur ' , function () { root . querySelectorAll ( ' .key.down ' ). forEach ( function ( k ) { k . className = ' key done ' ; }); }); 4. Do not block F5 and F12. Calling preventDefault() on everything also blocks refresh and dev tools, which annoys people. Let those through. 5. Ghosting is a hardware limit. If you press several keys at once and some never fire, that is the keyboard's rollover limit, not a bug in your code. Cheap keyboards often fail on combinations like A+S+D+F. It is a fun thing to test. Try it Press every key and see which ones work: Keyboard tester → . It shows key , code and keyCode live, so it is also handy when you are debugging shortcuts.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/arelvox/ekey-vs-ecode-why-your-wasd-controls-break-on-azerty-and-how-i-built-a-keyboard-tester-c50

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
