# عروسی جن‌ها | فصل ۲، قسمت ۱ | پرامپت‌ها

روش کار: هر بار یک نما. پرامپت تصویر (ChatGPT) → کاربر عکس را می‌دهد و تأیید می‌شود → ذخیره در `images/` → پرامپت ویدیو (Gemini، image-to-video) → ذخیره در `videos/`.
- همه‌ی پرامپت‌ها با نام مرجع شخصیت در ChatGPT شروع می‌شوند («نفیسه»).
- در پرامپت‌های ویدیو **هیچ موسیقی پس‌زمینه‌ای** نباشد. فقط صدای محیط و دیالوگ. آهنگ‌گذاری را خود کاربر انجام می‌دهد.
- قاب عمودی 9:16 و سوپر رئالیستی.
- ⚠ تصمیم کاربر: نفیسه هیچ‌جا چادر سر نمی‌کنه. به‌جای «چادر سفید خواستگاری»: پیراهن توری سفید شیک + شال حریر سفید خیلی سبک و عقب.

---

## سکانس ۱ | شات ۱ | خواستگاری (تعارف چای)

### پرامپت تصویر (نسخه ۲، با مرجع‌ها)
مرجع‌هایی که باید توی ChatGPT ضمیمه بشن: «نفیسه»، «مادر داماد»، «پذیرایی خونه نفیسه»
```
Use the saved references: «نفیسه» for Nafiseh's face (exact same identity), «مادر داماد» for the groom's mother (exact same face, black gold-embroidered manteau, black silk scarf, heavy gold bangles and rings), and «پذیرایی خونه نفیسه» for the room (same cream-and-gold sofas, red Persian carpet, brass samovar, crystal chandelier, window with the Milad Tower view).

Vertical 9:16 real photograph, not CGI, not illustration.
Khastegari (marriage proposal) evening in Nafiseh's family living room. Nafiseh, 21, wears NO chador — an elegant fitted white lace midi dress with delicate floral French lace, off-the-shoulder neckline showing her collarbones, sheer lace long sleeves, cinched waist (the same chic style as her «نفیسه» reference); a very light sheer white chiffon scarf rests loosely on the back of her head and shoulders, showing most of her long wavy dark-brown hair. Elegant glamorous makeup, shy lowered eyes, a tiny nervous smile. She bends forward slightly, politely offering an ornate silver tray holding clear tulip-shaped Persian tea glasses (estekan) filled with steaming deep amber tea on gold-rimmed saucers.

The groom's mother sits on the cream-and-gold sofa in front of her, sharp appraising hazel-green eyes looking Nafiseh up and down, a polite but cold tight-lipped smile, reaching her heavily gold-bangled hand out toward one tea glass.

Nafiseh's fingers grip the edge of the tray; very faint orange-red henna stains are visible on her fingertips, almost hidden.

Background, softly out of focus: the lit brass samovar with gentle steam, the crystal fruit bowl and pastries on the coffee table, the white gladiolus vase, the crystal chandelier glowing, the window with the night Tehran view.

Candid moment, documentary realism, nobody looks at the camera.
Composition: medium shot from a low side angle at sofa height. The silver tray and the two women's hands are in the center of the frame. Nafiseh's face is in sharp focus in the upper third, and the groom's mother is in three-quarter profile on the right.

Real human imperfections: visible skin pores, fine peach fuzz, natural asymmetry, real lace texture on the dress, fingerprints and reflections on the tea glasses, tiny steam wisps above the tea, realistic reflections on the gold.

Image quality: ultra high resolution, extremely sharp and crisp, natural skin texture (not airbrushed), true-to-life colors, no noise, no grain, no compression artifacts.
Shot on Canon EOS R5 with RF 50mm f/1.2 lens at f/2.8, cinematic warm tungsten lighting with soft shadows, warm amber color tones with slightly cool shadows from the window, tack-sharp focus on the eyes, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no beauty filter, no cartoon look.
```

### پرامپت ویدیو
(بعد از تأیید عکس)

✅ تصویرها تأیید شد: `images/s1_shot1a.webp` (ورود با سینی) و `images/s1_shot1b.webp` (تعارف چای). پرامپت‌های ویدیو توی `shots.json` و صفحه‌ی HTML هستن.

---

## سکانس ۱ | شات ۲ | دست نامرئی مچ نفیسه رو می‌گیره

### پرامپت تصویر
مرجع‌های ضمیمه: «نفیسه»، «سیاهی»، و عکس `s1_shot1b` (برای پیوستگی صحنه)
```
Use the saved references: «نفیسه» for Nafiseh (same face, same white off-shoulder lace dress, same sheer veil, same long wavy dark-brown hair), «سیاهی» for the black smoky hand, and the uploaded khastegari image for the same room, tray, tea glasses and lighting — continuity with the previous shot.

Vertical 9:16 real photograph, cinematic film still, not CGI.
Close-up shot of Nafiseh's right wrist and hand holding the edge of the ornate silver tray with tulip-shaped tea glasses full of hot amber tea. A hand made of living black haze — long thin smoky fingers like black claws, the same substance as «سیاهی», semi-transparent black smoke drifting off its edges — has suddenly wrapped tightly around her wrist out of nowhere, coming from below the frame, with no body visible. The black fingers press into her skin, making it dimple. The tray is starting to tilt sharply toward the right; the tea is sloshing inside the glasses, a little hot tea spilling over a rim, frozen in mid-air droplets, steam swirling.
In the upper part of the frame, slightly softer focus: Nafiseh's face, her eyes wide open in shock and fear, lips parted, the veil slipping.
Faint orange-red henna stains on her fingertips.

Lighting: the same warm tungsten living-room light, but a cold shadow falls over her hand where the black haze touches it; the black smoke absorbs the light.
Mood: sudden supernatural intrusion into a warm family moment, mysterious thriller.

Image quality: ultra high resolution, extremely sharp and crisp, every lace thread and skin pore visible, realistic liquid and steam, realistic volumetric smoke, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 85mm macro lens at f/2.8, tack-sharp focus on the wrist and the black fingers, shallow depth of field, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers on Nafiseh, no plastic skin, no cartoon look.
```

✅ شات ۲ تأیید شد: `images/s1_shot2.webp`.

---

## سکانس ۱ | شات ۳ | چای جوش روی مادر داماد + جیغ + شکستن استکان‌ها

### پرامپت تصویر
مرجع‌های ضمیمه: «مادر داماد»، «نفیسه»، «پذیرایی خونه نفیسه» و عکس `s1_shot1b`
```
Use the saved references: «مادر داماد» for the groom's mother (same face, same black gold-embroidered manteau, black silk scarf with gold border, heavy gold bangles and rings), «نفیسه» for Nafiseh (same face, white off-shoulder lace dress, sheer veil, wavy dark-brown hair), «پذیرایی خونه نفیسه» for the room, and the uploaded khastegari image for continuity (same sofa, tray, tea glasses, lighting).

Vertical 9:16 real photograph, cinematic film still, frozen action moment, not CGI.
The groom's mother, seated on the cream-and-gold sofa, recoils backward screaming — mouth wide open, eyes squeezed half shut in sudden pain and shock, both hands jerked up, her gold bangles flying. Hot amber tea is splashing onto the back of her gold-bangled hand and onto the lap of her black embroidered manteau, the liquid frozen mid-air in glossy arcs and droplets, thick steam rising from the wet black fabric. Her skin on the back of her hand is reddened.
In the foreground the silver tray is tipped almost vertical; two tulip-shaped tea glasses are falling, and one glass is shattering on the edge of the glass coffee table — sharp glass shards and tea droplets frozen in the air, a saucer spinning.
Behind on the left, in slightly softer focus: Nafiseh, horrified, both hands over her mouth, her veil slipping off her hair.
Background: the samovar, the white gladiolus, the chandelier and the night window with the Milad Tower, softly blurred.

Lighting: the same warm tungsten living-room light, specular highlights on the flying tea, glass shards and gold.
Mood: chaotic, sudden, shocking — the warm evening is broken in one second.

Image quality: ultra high resolution, extremely sharp and crisp, realistic liquid physics, realistic shattering glass, every skin pore and wrinkle visible, real fabric texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 35mm lens at f/2.8, high shutter speed freezing the motion, tack-sharp focus on the groom's mother's face and the splash, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look, no blood.
```

✅ شات ۳ تأیید شد: `images/s1_shot3.webp`.

---

## سکانس ۱ | شات ۴ | گوشی نفیسه، شب، «ناشناس»

### پرامپت تصویر
مرجع‌های ضمیمه: «نفیسه»، «اتاق نفیسه»
```
Use the saved references: «نفیسه» for the hand and wrist (same olive skin, a few faint orange-red henna stains on her fingertips, thin gold bracelet) and «اتاق نفیسه» for the room (same bedside lamp, floral bedspread, window with the night view of Tehran and the Milad Tower).

Vertical 9:16 real photograph, cinematic film still, not CGI.
Extreme close-up of a modern smartphone lying on the soft cream rug of Nafiseh's bedroom floor at night, its screen lit and glowing, showing an incoming call: a plain grey default avatar silhouette and the Persian text "ناشناس" (Unknown) in clean white letters, with a green accept and a red decline button. The phone is vibrating — slight motion blur on the edges, tiny ripples in the rug fibers around it.
Beside the phone, in the lower edge of the frame, Nafiseh's trembling hand with faint henna on the fingertips reaching toward it, slightly out of focus.
Background, softly blurred: the bedroom in the dark, a faint warm glow from the bedside lamp, the window with the night skyline and the Milad Tower far away. In the dark glass of the window, almost invisible, a faint smoky black shape with two tiny glowing amber dots — barely noticeable.

Lighting: low-key night, the cold blue-white light of the phone screen on the rug and her fingers, warm amber from the lamp in the background.
Mood: tense, lonely, 2 a.m. dread.

Image quality: ultra high resolution, extremely sharp and crisp, readable screen text, every rug fiber and skin pore visible, true-to-life colors, no noise, no compression artifacts.
Shot on Canon EOS R5 with RF 100mm macro lens at f/2.8, tack-sharp focus on the screen, 8K, hyperrealistic, real photograph, masterpiece.
No extra text besides «ناشناس», no watermark, no logo, no cartoon look.
```

---

## سکانس ۱ | شات ۳ب (جدید) | واکنش همه: تعجب و عصبانیت (بین شات ۳ و شات ۴)

### پرامپت تصویر
مرجع‌های ضمیمه: «مادر نفیسه»، «داماد»، «پدر داماد»، «مادر داماد»، «نفیسه»، «پذیرایی خونه نفیسه» و عکس شات ۳ (برای پیوستگی)
```
Use the saved references: «مادر نفیسه» (Nafiseh's mother, navy headscarf, dark-grey house dress), «داماد» (the handsome groom, wavy brown hair, dark suit, white shirt), «پدر داماد» (the groom's father, grey hair, grey beard, grey suit, light-blue shirt), «مادر داماد» (the groom's mother, black gold-embroidered manteau, black scarf, gold bangles), «نفیسه» (white off-shoulder lace dress, sheer veil), and «پذیرایی خونه نفیسه» for the room; use the uploaded previous image for continuity of the tea mess, broken glass and lighting.

Vertical 9:16 real photograph, cinematic film still, frozen emotional moment, not CGI.
Wide-medium shot of the whole khastegari living room one second after the tea disaster. Everyone reacts at once:
- The groom's mother, seated on the sofa at right, is clutching her red scalded hand, her black manteau soaked with tea, face twisted in pain and furious outrage, glaring straight at Nafiseh.
- The groom's father, standing behind her, one hand on her shoulder, jaw clenched, brows deeply furrowed, cold angry stare, eyes wide in disbelief.
- The groom, standing beside the sofa, eyes wide, mouth slightly open in shock and worry, torn between his mother and Nafiseh, one hand half raised toward his mother.
- Nafiseh's mother, entering the frame from the left, BOTH hands raised and pressed on top of her own head (the classic Iranian gesture of shame and despair, fingers gripping her headscarf), elbows up, face pale with horror and rising fury, mouth open mid-shout, NOT pointing at anyone.
- Nafiseh, at the far left, small and frozen, both hands over her mouth, tears in her eyes, veil slipping.
Foreground: the tipped silver tray on the carpet, broken glass shards and spilled tea on the coffee table and carpet. Background: samovar, gladiolus, chandelier, night window with the Milad Tower.

Lighting: the same warm tungsten living-room light, a little harsher and more dramatic, deep shadows on the angry faces.
Mood: a shocked, humiliating family explosion, tense and chaotic.

Image quality: ultra high resolution, extremely sharp and crisp, every face clearly readable and recognizable, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 35mm lens at f/4, all five faces in sharp focus, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra people, no extra fingers, no plastic skin, no cartoon look.
```


⚠ اصلاح شات ۳ب: مادر نفیسه باید هر دو دستش روی سرش باشه، نه اشاره با انگشت. عکس بقیه خوب بود (ویرایش با پرامپت کوتاه)، هنوز تأیید نشده.

✅ شات ۳ب تأیید شد: `images/s1_shot3b.webp`.

### پرامپت تصویر شات ۴ (نسخه ۲: نفیسه روی صندلی، سیاهی پشت شیشه)
مرجع‌های ضمیمه: «نفیسه»، «اتاق نفیسه»، «سیاهی»
```
Use the saved references: «نفیسه» for Nafiseh (exact same face, long wavy dark-brown hair, the same white off-shoulder lace dress, no veil), «اتاق نفیسه» for the room (same bedside lamp, floral bedspread, big window with the night view of Tehran and the Milad Tower), and «سیاهی» for the dark entity.

Vertical 9:16 real photograph, cinematic film still, not CGI.
Night, Nafiseh's bedroom. Nafiseh sits on a wooden chair at a small wooden desk, seen from the front at a slightly low angle, medium shot from the waist up, in the center of the frame. On the desk in front of her lies her smartphone, screen glowing and vibrating, showing an incoming call with a grey avatar silhouette and the Persian text "ناشناس" with green and red call buttons. She stares at the phone in fear, her trembling hand hovering just above it, faint orange-red henna stains on her fingertips, eyes wide and wet, lips slightly parted, afraid to answer.
Directly BEHIND her, outside the large window, floating in the dark night air, stands «سیاهی»: a tall faceless man-shaped figure made of black smoke, pressed close against the glass, with two glowing amber eyes staring straight at the back of her head. Wisps of black haze curl against the window glass. She does not see it, but the viewer clearly does. The Milad Tower and city lights glow faintly beyond and around the dark figure.

Lighting: low-key night, the cold blue-white light of the phone screen lights her face and hands from below, a warm dim amber glow from the bedside lamp in the background, cold blue moonlight through the window outlining the black figure.
Mood: tense, lonely, 2 a.m. dread, the audience knows someone is watching her.

Image quality: ultra high resolution, extremely sharp and crisp, readable phone text, real skin pores, lace texture, realistic volumetric smoke, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 40mm lens at f/2.8, tack-sharp focus on her face and the phone, the black figure sharp enough to read, 8K, hyperrealistic, real photograph, masterpiece.
No extra text besides «ناشناس», no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

### پرامپت تصویر شات ۴ (نسخه ۳: نفیسه غمگین، سر روی میز، سیاهی پشت شیشه)
مرجع‌های ضمیمه: «نفیسه»، «اتاق نفیسه»، «سیاهی»
```
Use the saved references: «نفیسه» for Nafiseh (exact same face, long wavy dark-brown hair, the same white off-shoulder lace dress, no veil), «اتاق نفیسه» for the room (same bedside lamp, floral bedspread, big window with the night view of Tehran and the Milad Tower), and «سیاهی» for the dark entity.

Vertical 9:16 real photograph, cinematic film still, not CGI.
Night, Nafiseh's bedroom. Nafiseh sits on a wooden chair at a small wooden desk, seen from the front at a slightly high angle, medium shot, in the center of the frame. She is heartbroken and exhausted: she has laid her head down on her folded arms on the desk, her face turned sideways toward the camera, cheek resting on her arm, eyes red and swollen, tears on her cheek and her lashes, wet strands of hair stuck to her face, mascara slightly smudged, a faint red mark on her cheek. Her hair spills over her shoulders and the desk.
On the desk right next to her face lies her smartphone, screen glowing and vibrating, showing an incoming call with a grey avatar silhouette and the Persian text "ناشناس" with green and red buttons. Faint orange-red henna stains on her fingertips. She does not look at the phone.
Directly BEHIND her, outside the large window, floating in the dark night air, stands «سیاهی»: a tall faceless man-shaped figure made of black smoke, pressed close against the glass, with two glowing amber eyes staring straight at the back of her head. Wisps of black haze curl against the window glass. She does not see it, but the viewer clearly does. The Milad Tower and city lights glow faintly around the dark figure.

Lighting: low-key night, the cold blue-white light of the phone screen on her face and arms, a warm dim amber glow from the bedside lamp in the background, cold blue moonlight through the window outlining the black figure.
Mood: heartbroken, lonely, 2 a.m. dread, the audience knows someone is watching her.

Image quality: ultra high resolution, extremely sharp and crisp, readable phone text, real skin pores, lace texture, realistic tears, realistic volumetric smoke, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 40mm lens at f/2.8, tack-sharp focus on her face and the phone, the black figure sharp enough to read, 8K, hyperrealistic, real photograph, masterpiece.
No extra text besides «ناشناس», no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

✅ شات ۴ تأیید شد: `images/s1_shot4.webp`.

---

## سکانس ۱ | شات ۵ | تالار شمع‌ها، زن‌های سُم‌دار، تور سفید

### پرامپت تصویر
مرجع‌های ضمیمه: «نفیسه» (برای زن‌های سُم‌دار مرجع نداریم و توی پرامپت توصیفشون کردم)
```
Use the saved reference «نفیسه» for Nafiseh (exact same face and long wavy dark-brown hair, same white lace dress).

Vertical 9:16 real photograph, cinematic film still, not CGI.
A vast ancient underground hall lit only by hundreds of tall flickering candles of different heights on the floor, on stone ledges and on huge iron candelabras, warm golden flame light and deep black shadows, dripping wax, thin smoke and drifting dust in the air, old carved stone pillars and a dark vaulted ceiling, a mysterious wedding ceremony of jinn.
In the center, Nafiseh stands frozen and terrified, seen in a medium shot from slightly above, wearing her white lace dress, wide wet eyes, trembling lips. Around her, in a slow circle, move several tall, uncanny, beautiful pale women in long dark-red and black flowing dresses, their extremely long black hair hanging down to the floor, their faces half hidden by their hair, with cold glowing eyes — and under the hems of their dresses, instead of feet, they have dark animal hooves clearly visible on the stone floor. Their long thin pale hands are lifting a long, translucent white bridal tulle veil and lowering it over Nafiseh's head; the veil is caught mid-air in a soft sweep, candle flames reflecting in the tulle.

Lighting: candlelight only, warm orange glow on Nafiseh's face and the veil, cold shadows behind the women, deep contrast.
Mood: eerie, ritualistic, dreamlike dread, a bride forced into a ceremony she does not understand.

Image quality: ultra high resolution, extremely sharp and crisp, every candle flame and wax drip visible, realistic skin pores, lace and tulle texture, realistic hooves and long hair, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 35mm lens at f/2.8, tack-sharp focus on Nafiseh's face, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look, no gore, no blood.
```

---

## ✏ تغییر متن سکانس ۴ (تصمیم کاربر): تماس تلفنی حذف می‌شه
- قبلاً: سکانس ۴ شات ۲ و ۳، گوشی روشن می‌شه «ناشناس»، نفیسه جواب می‌ده، صدای بم می‌گه «تو زن منی…» و قطع می‌شه.
- حالا: نفیسه کنار پنجره روی زمین گریه می‌کنه. توی شیشه‌ی پنجره «سیاهی» پشت سرش ظاهر می‌شه و خودش (حضوری) با صدای بم می‌گه: «تو زن منی… دیگه هیچ‌کس جز من حق نداره بهت نگاه کنه.» بعد دودش محو می‌شه و صبح می‌شه (شات ۴: تصادف داماد).
- شات ۴ قلاب (گوشی «ناشناس» + راوی «فقط با یه تماس…») همون‌طور می‌مونه، چون راوی از تماس حرف می‌زنه.
- شات ۶ قلاب: «سیاهی» هنگام گرفتن مچ فقط می‌گه «تو زن منی…» (کوتاه)، تا قدرت جمله‌ی بلند سکانس ۴ کم نشه.

✅ شات ۴ نسخه‌ی بدون گوشی جایگزین شد: `images/s1_shot4.webp`. راوی: «یه شب… با یه تماس ناشناس… ناخواسته رفتم عروسی جن‌ها.»

✏ تصمیم کاربر: شات ۴ قلاب: «سیاهی» می‌گه «تو زن منی… هیچ‌کس حق نداره تو رو بگیره.» و راوی («یه شب… با یه تماس ناشناس… ناخواسته رفتم عروسی جن‌ها… وسط یه مراسم عجیب، یه جن عاشقم شد…») از شات ۵ شروع می‌شه.

✏ راوی نهایی شات ۵ (تصمیم کاربر): «چند سال پیش، یه شب… با یه تماس ناشناس… ناخواسته رفتم عروسی جن‌ها… وسط یه مراسم عجیب، یه جن عاشقم شد و دیگه ولم نکرد.» (حدود ۸ تا ۹ ثانیه؛ شات ۵ باید دو برش از تالار شمع‌ها داشته باشه.)

✅ شات ۵ تأیید شد: `images/s1_shot5.webp`.

---

## سکانس ۱ | شات ۶ | «اون سیاهی» از پله‌ها پایین میاد و مچ نفیسه رو می‌گیره

### پرامپت تصویر
مرجع‌های ضمیمه: «نفیسه»، «سیاهی» و عکس شات ۵ (برای پیوستگی تالار)
```
Use the saved references: «نفیسه» for Nafiseh (exact same face, same long wavy dark-brown hair, same white off-shoulder lace dress, now wearing the long translucent white bridal tulle veil over her head), «سیاهی» for the dark entity, and the uploaded candle-hall image for the same ancient stone hall, candles and lighting.

Vertical 9:16 real photograph, cinematic film still, not CGI.
The same vast ancient candle-lit underground hall. At the back, a wide curved stone staircase leads down into the hall, flanked by tall iron candelabras. Down the staircase, floating just above the steps, descends «سیاهی»: a tall faceless man-shaped figure of living black smoke with long thin smoky arms and two glowing amber eyes, trailing thick black fog down every step, the candle flames bending toward him and dimming as he passes. In the foreground, Nafiseh stands in her lace dress and white tulle veil, tears running down her cheeks, shaking, looking up at him. His long thin smoky hand reaches out and is wrapped around her wrist, black fingers pressing into her skin, the haze mixing with the white tulle. Behind her, the hooved women stand in a silent semi-circle with bowed heads.

Composition: medium-wide shot from a slightly low angle, Nafiseh in the lower center, the black figure towering above her on the stairs, her wrist and his hand in sharp focus.
Lighting: candlelight only, warm orange on Nafiseh and the veil, the black smoke absorbing light, cold blue rim edges on the haze, deep shadows.
Mood: a forced supernatural wedding, helpless fear, a possessive dark groom.

Image quality: ultra high resolution, extremely sharp and crisp, every candle flame, wax drip and thread of tulle visible, realistic volumetric smoke, real skin pores, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 35mm lens at f/2.8, tack-sharp focus on the wrist and Nafiseh's face, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look, no gore, no blood.
```

✅ شات ۴ و ۵ با نسخه‌ی باکیفیت‌تر جایگزین شد و شات ۶ تأیید شد: `images/s1_shot6.webp`.

---

## سکانس ۱ | شات ۷ | اتاق نفیسه، منظره‌ی تهران، سیاهی توی شیشه

### پرامپت تصویر
مرجع‌های ضمیمه: «نفیسه»، «اتاق نفیسه»، «سیاهی»
```
Use the saved references: «نفیسه» for Nafiseh (exact same face, long wavy dark-brown hair, no veil, now wearing a simple soft white cotton nightgown), «اتاق نفیسه» for the room, and «سیاهی» for the dark entity.

Vertical 9:16 real photograph, cinematic film still, not CGI.
Night, Nafiseh's bedroom. Nafiseh stands in front of the big window with her back partly toward the camera, in a close medium shot from behind her shoulder, looking at the night view of Tehran with the Milad Tower glowing in the distance. In the dark window glass we see her faint face reflection — tired, tearful, whispering — and right behind her reflection, clearly visible in the glass, the tall black smoky figure «سیاهی» with two glowing amber eyes standing very close behind her shoulder, its smoky hand hovering just above her neck, its black haze curling around her hair. In the real room behind her there is nothing — only her bed, the dim bedside lamp and empty space — only the reflection shows the entity.

Lighting: low-key night, cold blue city glow and moonlight through the window, a dim warm amber lamp in the room, faint cold breath fog on the glass.
Mood: whispered dread, haunted, he is always with her and never lets go.

Image quality: ultra high resolution, extremely sharp and crisp, realistic glass reflection, real skin pores, realistic volumetric smoke, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 50mm lens at f/2.8, tack-sharp focus on her reflection and the black figure in the glass, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

### پرامپت تصویر شات ۷ (نسخه ۲: سیاهی دقیقاً پشت نفیسه توی اتاق)
مرجع‌های ضمیمه: «نفیسه»، «اتاق نفیسه»، «سیاهی»
```
Use the saved references: «نفیسه» for Nafiseh (exact same face, long wavy dark-brown hair, no veil, now wearing a simple soft white cotton nightgown), «اتاق نفیسه» for the room, and «سیاهی» for the dark entity.

Vertical 9:16 real photograph, cinematic film still, not CGI.
Night, Nafiseh's bedroom. Nafiseh stands in front of the big window, facing the glass, seen from the front-side in a medium shot, her eyes wide open and wet, lips trembling, looking at the night view of Tehran with the Milad Tower glowing far away. DIRECTLY BEHIND HER, inside the room, stands «سیاهی» — the tall faceless man-shaped figure of living black smoke, towering over her, almost touching her back and shoulders, its two long thin smoky arms hanging down on each side of her, one smoky hand resting just above her shoulder, its head bent down toward the back of her head, its two glowing amber eyes fixed on her; thick black haze and fog flows around her feet and curls into her hair. Nafiseh does not turn around, she only senses it, frozen, in her faint reflection in the dark window glass we can see both her face and the glowing eyes right behind her.

Lighting: low-key night, cold blue city glow through the window outlines both figures, a dim warm amber lamp on the nightstand, the black smoke absorbing the light.
Mood: whispered dread, haunted, he is always right behind her and never lets go.

Image quality: ultra high resolution, extremely sharp and crisp, real skin pores, realistic volumetric smoke, realistic glass reflection, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 40mm lens at f/2.8, tack-sharp focus on Nafiseh's face with the black figure sharp behind her, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

✅ شات ۷ تأیید شد: `images/s1_shot7.webp`. تمام تصویرهای سکانس ۱ تموم شد. بعدش: کارت عنوان «عروسی جن‌ها | فصل دوم» (HyperFrames، فونت قرمز خونی روی صفحه‌ی سیاه)، بعد سکانس ۲.

---

# سکانس ۲: «یه هفته قبل»
کارت: «یه هفته قبل» با فونت قرمز خونی روی صفحه‌ی سیاه (HyperFrames، بعداً).

## سکانس ۲ | شات ۱ | حموم، نفیسه حنا رو می‌ساید
(مرجع حموم نداریم؛ توی پرامپت توصیف شده. لباس: راحتی، موی خیس.)

### پرامپت تصویر
مرجع‌های ضمیمه: «نفیسه»
```
Use the saved reference «نفیسه» for Nafiseh (exact same face and the same long dark-brown hair, now soaking wet and slicked back and falling in dark wet strands over her shoulders, no makeup, natural bare face).

Vertical 9:16 real photograph, cinematic film still, not CGI.
A small, plain, slightly old Iranian family apartment bathroom, white and pale-blue ceramic tiles with some wear and a few grout stains, a white porcelain sink with a rusty-edged tap, a mirror above it with small water splashes, a plastic bucket, a worn pink plastic bath scrub brush, steam in the air, cold blue-white fluorescent light, a slightly dirty window of frosted glass.
Nafiseh stands at the sink in a medium close-up from the waist up, wearing only a simple plain white cotton bralette top with a white bath towel wrapped around her waist (modest, natural, not glamorous, not posed). Her skin is damp, tiny water drops on her shoulders and collarbones. She is scrubbing the palms of both hands hard with a stiff bristle brush under the running tap, her palms and fingers are scrubbed red and raw, yet the dark orange-red henna pattern on her palms and fingertips is still vivid and has not faded at all. Her face is tense, eyes wide and wet, jaw clenched, almost desperate, looking down at her hands.
Foreground and in the sharp focus: her hands, the brush, the running water and the stubborn henna on her red skin.

Lighting: cold blue-white bathroom light, soft shadows, damp reflective surfaces, a hint of cold teal in the shadows.
Mood: anxious, desperate, secretive, something she cannot wash away.

Image quality: ultra high resolution, extremely sharp and crisp, every water drop, brush bristle, skin pore and the henna pattern visible, realistic wet hair strands, true-to-life colors, no noise, no compression artifacts.
Shot on Canon EOS R5 with RF 50mm f/1.8 lens, tack-sharp focus on her hands and face, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```
- ⚠ اگه ChatGPT به خاطر «bralette» رد کرد: به‌جاش بنویس `a white cotton tank top`. تغییر لباس تأثیری روی صحنه نداره.

✅ سکانس ۲ شات ۱ تأیید شد: `images/s2_shot1.webp`.

---

## سکانس ۲ | شات ۲ | پذیرایی، مادر عصبانی و نفیسه با دست‌های خیس

### پرامپت تصویر
مرجع‌های ضمیمه: «مادر نفیسه»، «نفیسه»، «پذیرایی خونه نفیسه»
```
Use the saved references: «مادر نفیسه» (Nafiseh's mother, about 50, navy headscarf, dark-grey house dress, same face), «نفیسه» (same face, same long dark-brown hair, now wet and slicked back), and «پذیرایی خونه نفیسه» for the same living room, now in a plain everyday state: the cream-and-gold sofas, the red Persian carpet, the same window, but no tea tray, no fruit bowl and no flowers on the table, everyday light.

Vertical 9:16 real photograph, cinematic film still, not CGI.
Medium-wide shot inside the living room, in the evening. On the left, the mother stands in the middle of the room, having just hung up a landline phone (the phone still in her hand at her side, the cord swinging), her whole face tense with anger and shame, brows furrowed, lips pressed, one hand pointing sideways in mid-scold. On the right, near the hallway door from the bathroom, steam curling out behind her, stands Nafiseh in a loose, plain white short-sleeved cotton house dress, her long dark hair soaking wet and dripping on her shoulders, her bare hands held in front of her in a tense, protective way — both palms and fingers scrubbed bright red and raw with the dark orange-red henna pattern still clearly visible. Nafiseh's face is exhausted, eyes red and teary, pleading, mouth slightly open as if starting to speak.
The two stand about two meters apart facing each other, a tense face-off.

Lighting: soft warm evening light from a lamp, a little cold light and steam from the bathroom door behind Nafiseh, flat realistic household feel.
Mood: shame, gossip, helpless confrontation between a conservative mother and her daughter.

Image quality: ultra high resolution, extremely sharp and crisp, every skin pore, wet hair strand, fabric texture, the henna pattern and the red skin visible, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 35mm lens at f/4, tack-sharp focus on both faces and Nafiseh's hands, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

✅ سکانس ۲ شات ۲ تأیید شد: `images/s2_shot2.webp`.

---

## سکانس ۲ | شات ۳ | نمای نزدیک‌تر مادر و نفیسه: «با این دستا؟!»

### پرامپت تصویر
مرجع‌های ضمیمه: «مادر نفیسه»، «نفیسه» و عکس شات ۲ (برای پیوستگی)
```
Use the saved references: «مادر نفیسه» (same face, navy headscarf, dark floral house dress), «نفیسه» (same face, wet dark hair, white lace-trimmed cotton house dress), and the uploaded previous image for the same living room, window with Milad Tower and lighting (continuity).

Vertical 9:16 real photograph, cinematic film still, not CGI.
Tight medium two-shot, the faces of both women close together in frame, at eye level, the mother on the left in sharp profile-three-quarter, Nafiseh on the right facing her. The mother's face is hard, cold, furious and ashamed: jaw clenched, thin tight lips mid-sentence, narrowed eyes, forehead lines, her finger raised near the frame edge. Nafiseh is crying and desperate, tears and water drops running down her face, wet hair strands stuck to her cheeks, and she is holding both open palms up right in front of her mother's face, filling the foreground — palms and fingers scrubbed bright red and raw with the dark orange-red henna pattern vividly visible, a few water drops dripping from her fingers. The hands are slightly out of focus in front, the two faces sharp behind them.
Background softly blurred: the cream-and-gold sofa, the lamp, the window with the night view and the Milad Tower.

Lighting: soft warm lamp light on the mother, cold bluish steam light on Nafiseh's side, subtle contrast between the two.
Mood: a final confrontation — a mother who only cares what the neighbours say, and a daughter who has no way to explain.

Image quality: ultra high resolution, extremely sharp and crisp, every skin pore, wrinkle, tear, wet hair strand, and the henna pattern visible, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 50mm lens at f/2.8, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

✏ دیالوگ‌های سکانس ۲ (تصمیم کاربر، کوتاه‌شده، زمان: عروسی جن‌ها چند سال پیش بوده و حنا هنوز پاک نشده):
- شات ۲: مادر «همسایه زنگ زد… می‌گه هنوز اون حنا دستته!» / نفیسه «مامان گفتم که… اونجا عروسی جن بود!»
- شات ۳: مادر «بسه جن و پری! پنجشنبه خواستگار میاد. شوهرت می‌دم، دهن مردم بسته شه.» / نفیسه «با این دستا؟!»
- نفیسه دیگه دف نمی‌زنه (دف روی دیوار اتاقش فقط یادگاره).

✅ سکانس ۲ شات ۳ تأیید شد: `images/s2_shot3.webp`.

---

## سکانس ۲ | شات ۴ | مادر دست‌های نفیسه رو پایین می‌کشه

### پرامپت تصویر
مرجع‌های ضمیمه: «مادر نفیسه»، «نفیسه» و عکس شات ۳ (برای پیوستگی)
```
Use the saved references: «مادر نفیسه» (same face, navy headscarf, dark floral house dress), «نفیسه» (same face, wet dark hair, white lace-trimmed cotton house dress), and the uploaded previous image for the same living room, lamp, window with the Milad Tower and lighting (continuity).

Vertical 9:16 real photograph, cinematic film still, not CGI.
Tight medium shot, the two women very close, facing each other. The mother grips both of Nafiseh's wrists in her hands and forcefully pulls them down and away from her face, her knuckles white, her fingers pressing into Nafiseh's skin around the henna; Nafiseh's red henna-covered hands are being forced downward at the lower part of the frame, still dripping. The mother's face is now calm and terrifyingly cold, eyes steady and hard, lips barely moving, speaking quietly and flatly; leaning in close. Nafiseh, tears streaming, stunned and defeated, her head slightly bowed, staring at her own hands, mouth closed, shoulders trembling.
Background softly blurred: the cream-and-gold sofa, the lamp, the window and the Milad Tower.

Lighting: soft warm lamp light on the mother, a cold bluish tint on Nafiseh, deep shadow between them.
Mood: cold, controlling, a mother burying a secret to protect her name; the daughter has no voice.

Image quality: ultra high resolution, extremely sharp and crisp, every skin pore, wrinkle, tear, wet hair strand and the henna pattern visible, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 50mm lens at f/2.8, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

✅ سکانس ۲ شات ۴ تأیید شد: `images/s2_shot4.webp`.

---

## سکانس ۲ | شات ۵ | تماس تصویری نفیسه و سارا (صفحه‌ی دو نیمه)

### پرامپت تصویر
مرجع‌های ضمیمه: «نفیسه»، «اتاق نفیسه»، «سارا»
```
Use the saved references: «نفیسه» for Nafiseh (same face, long dark hair now damp and loose, wearing the same loose white lace-trimmed cotton house dress), «اتاق نفیسه» for her bedroom (same bed, lamp, window with the night view of Tehran), and «سارا» for Sara (same face, same crinkled deep-red scarf, wavy balayage hair showing).

Vertical 9:16 screenshot of a smartphone video call in split-screen layout: two equal frames stacked vertically (top half and bottom half), each with a thin dark divider line between them, with tiny rounded call controls in the corners (mute, camera, red hang-up) — modern realistic video-call UI, but no readable text.
TOP half: Nafiseh in her bedroom at night, sitting on her bed in front of the camera, the dim bedside lamp and the window with the Milad Tower behind her. Her face is exhausted, eyes red and swollen with tears, a bitter, broken half-smile on her lips, a tear rolling down her cheek, her red henna-stained palms visible as she holds the phone.
BOTTOM half: Sara in her own cozy small living room at night, sitting on a sofa with a throw pillow behind her and a warm lamp, a framed picture on the wall. She wears her deep-red scarf and a black embroidered tunic, her face worried and anxious, eyes wide and glossy, leaning toward the camera, lips parted as if urging her friend to speak.

Lighting: top frame low-key, dim amber lamp plus cold blue window light; bottom frame warm, soft living-room light. Real phone-camera look with slight softness at the edges but sharp faces.
Mood: a late-night confession, a friend who wants to help and a girl who cannot tell the truth.

Image quality: ultra high resolution, extremely sharp faces, natural skin texture, real pores, tears, realistic video-call look, true-to-life colors, no noise, no compression artifacts.
8K, hyperrealistic, real photograph, masterpiece.
No readable text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

✅ سکانس ۲ شات ۵ تأیید شد: `images/s2_shot5.webp`. سکانس ۲ تموم شد.

---

# سکانس ۳: «پنجشنبه شب»
کارت: «پنجشنبه شب» با فونت قرمز خونی روی صفحه‌ی سیاه (HyperFrames، بعداً).
⚠ نفیسه چادر نداره (تصمیم کاربر): به‌جاش پیراهن توری سفید + تور سبک. مادر آستین‌های توری رو روی دست‌های حنایی پایین می‌کشه.

## سکانس ۳ | شات ۱ | مادر نفیسه رو جلوی آینه مرتب می‌کنه

### پرامپت تصویر
مرجع‌های ضمیمه: «مادر نفیسه»، «نفیسه»، «پذیرایی خونه نفیسه»
```
Use the saved references: «مادر نفیسه» (same face, navy headscarf, dark floral house dress), «نفیسه» (same face and long wavy dark-brown hair, now dry and styled, wearing the white off-shoulder long-sleeve lace dress with a light sheer white bridal-style veil resting on her hair), and «پذیرایی خونه نفیسه» for the room, now fully prepared for the khastegari: the lit brass samovar, the crystal fruit bowl, pastries, the white gladiolus vase, the large gold-framed wall mirror, the crystal chandelier, evening.

Vertical 9:16 real photograph, cinematic film still, not CGI.
Medium shot in front of the large gold-framed wall mirror in the tidy living room. Nafiseh stands in front of the mirror in her white lace dress with the sheer veil, her eyes lowered and sad, a faint forced half-smile, her hands down at her sides. Her mother stands beside her, a little behind, fixing the long lace sleeves down over Nafiseh's hands to hide the henna: her fingers pull the lace cuffs down hard over Nafiseh's red henna palms, her face stern and tense, whispering a warning into her ear. In the mirror we see both reflections.
Background: the samovar steaming, the glowing chandelier, the neat sofas, the window with the Milad Tower at night.

Lighting: warm evening tungsten light, soft shadows.
Mood: a hidden secret, a nervous mother controlling every detail, a daughter who has no say.

Image quality: ultra high resolution, extremely sharp and crisp, every lace thread, skin pore and wrinkle visible, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 50mm lens at f/2.8, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

✅ سکانس ۳ شات ۱ تأیید شد: `images/s3_shot1.webp`.

✏ دیالوگ شات ۲ سکانس ۳ (با توجه به اینکه نفیسه دیگه دف نمی‌زنه):
- مادر داماد: «شنیدیم عروس خانوم یه زمانی دف می‌زده؟»
- مادر نفیسه (سریع): «نه بابا… یه وقتی، فقط تو مجلسای خانوادگی.»

---

## سکانس ۳ | شات ۲ | خانواده‌ی داماد روی مبل

### پرامپت تصویر
مرجع‌های ضمیمه: «داماد»، «مادر داماد»، «پدر داماد»، «مادر نفیسه»، «پذیرایی خونه نفیسه»
```
Use the saved references: «داماد» (the handsome groom, wavy brown hair, hazel-green eyes, short trimmed beard, dark suit and white open-collar shirt), «مادر داماد» (the groom's mother, black gold-embroidered manteau, black silk scarf with gold border, heavy gold bangles and rings, sharp hazel-green eyes), «پدر داماد» (the groom's father, grey hair, grey beard, dark-grey suit, light-blue shirt, tasbih and red agate ring), «مادر نفیسه» (same face, navy headscarf, dark floral house dress), and «پذیرایی خونه نفیسه» for the room, fully prepared for the khastegari: the lit samovar, fruit bowl, pastries, gladiolus vase, chandelier, the window with the Milad Tower, evening.

Vertical 9:16 real photograph, cinematic film still, not CGI.
Medium-wide shot of the khastegari seating. The groom's family sits in a row on the cream-and-gold sofa: the groom on the left, shy and kind, hands clasped on his knees, a soft polite smile, eyes lowered; the groom's father in the middle, silent and serious, tasbih in his hand, looking slightly away; the groom's mother on the right, sitting very straight, chin lifted, looking over at Nafiseh's mother with a cold appraising look, one eyebrow slightly raised, as she asks a pointed question. Nafiseh's mother sits on the armchair opposite, with a stiff, nervous, forced smile, hands tightly folded in her lap, answering quickly.
On the coffee table between them: fruit bowl, pastries, the vase of white gladiolus. The samovar steams in the background.

Lighting: warm evening tungsten light, soft shadows, the chandelier glowing.
Mood: polite but tense, a social interrogation disguised as small talk.

Image quality: ultra high resolution, extremely sharp and crisp, every face clearly recognizable, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 35mm lens at f/4, all four faces in sharp focus, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra people, no extra fingers, no plastic skin, no cartoon look.
```

✅ سکانس ۳ شات ۲ تأیید شد (همه می‌خندن، فضای گرم و دوستانه): `images/s3_shot2.webp`.

---

## سکانس ۳ | شات ۳ | لبخند داماد و اولین لبخند نفیسه

### پرامپت تصویر
مرجع‌های ضمیمه: «داماد»، «نفیسه»، «پذیرایی خونه نفیسه»
```
Use the saved references: «داماد» (the handsome groom, wavy brown hair, hazel-green eyes, short trimmed beard, dark suit, white open-collar shirt), «نفیسه» (same face, long wavy dark-brown hair, white off-shoulder lace dress with long lace sleeves covering her hands, a light sheer veil on her hair), and «پذیرایی خونه نفیسه» for the room prepared for the khastegari, evening.

Vertical 9:16 real photograph, cinematic film still, not CGI.
Intimate medium two-shot split by a shallow depth of field: in the foreground left, the groom sitting on the sofa, turned toward the camera-right, looking up at Nafiseh with a soft, warm, slightly shy smile that reaches his eyes, the kind of smile that makes a girl's heart race. On the right, standing a few steps away, Nafiseh holding an ornate silver tray with tea glasses, looking at him for the first time, her face softening, a small genuine hopeful smile appearing for the first time on her lips, eyes slightly shining, the veil glowing in the warm light. Their eyes meet across the room, a real moment of quiet attraction.
Background softly blurred: the glowing chandelier, the samovar's steam, the window with the Milad Tower.

Lighting: warm, golden, flattering evening light on both faces.
Mood: a rare moment of tenderness, innocent and hopeful — just before everything goes wrong.

Image quality: ultra high resolution, extremely sharp and crisp, every skin pore, lace thread and eyelash visible, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 85mm lens at f/2, tack-sharp focus on both faces, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra people, no extra fingers, no plastic skin, no cartoon look.
```

✅ سکانس ۳ شات ۳ تأیید شد: `images/s3_shot3.webp`.

---

## سکانس ۳ | شات ۴ | چراغ‌ها چشمک می‌زنن و سیاهی پشت داماد توی شیشه

### پرامپت تصویر
مرجع‌های ضمیمه: «نفیسه»، «داماد»، «سیاهی»، «پذیرایی خونه نفیسه» و عکس شات ۳ (پیوستگی)
```
Use the saved references: «نفیسه» (same face, long wavy dark-brown hair, white off-shoulder lace dress, sheer veil, holding the silver tray with tea glasses), «داماد» (the handsome groom, wavy brown hair, dark suit, white shirt), «سیاهی» for the dark entity, and «پذیرایی خونه نفیسه» for the room; use the uploaded previous image for continuity of the room and lighting.

Vertical 9:16 real photograph, cinematic film still, not CGI.
Medium shot from Nafiseh's point of view slightly behind her shoulder (her veil and a bit of her hair soft in the foreground edge), looking toward the groom who sits on the sofa smiling softly at her, unaware. The chandelier above is flickering — half of its bulbs dark, the warm light dimming and a cold blue tint creeping in. The samovar has stopped steaming. In the large dark window behind the groom, in the reflective glass, directly behind his head and shoulders, stands «سیاهی»: a tall faceless man-shaped figure of black smoke with two glowing amber eyes staring straight at Nafiseh, black haze coiling against the glass. Only the glass shows it — the room behind the groom is empty. Nafiseh's face (in a small sharp view at the frame's side) shows her smile dying, eyes widening in fear.

Lighting: warm light collapsing into cold blue shadows, the amber eyes the brightest point.
Mood: sudden dread, the safe moment is gone.

Image quality: ultra high resolution, extremely sharp and crisp, realistic volumetric smoke, realistic glass reflection, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 50mm lens at f/2.8, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra people, no extra fingers, no plastic skin, no cartoon look.
```

✅ سکانس ۳ شات ۴ تأیید شد: `images/s3_shot4.webp`.

---

## سکانس ۳ | شات ۵ | همون صحنه‌ی قلاب از زاویه‌ی دیگه
تصمیم: شات‌های قلاب (۱ب، ۲، ۳) رو دوباره نمی‌سازیم و فقط یه زاویه‌ی جدید و عریض از لحظه‌ی کج شدن سینی می‌سازیم؛ بقیه‌ش توی ادیت از تصاویر قلاب (s1_shot2 و s1_shot3) استفاده می‌شه.

### پرامپت تصویر
مرجع‌های ضمیمه: «نفیسه»، «مادر داماد»، «داماد»، «سیاهی»، «پذیرایی خونه نفیسه» و عکس s1_shot1b (پیوستگی)
```
Use the saved references: «نفیسه» (same face, long wavy dark-brown hair, white off-shoulder lace dress, sheer veil), «مادر داماد» (black gold-embroidered manteau, black silk scarf, gold bangles), «داماد» (dark suit, white shirt, wavy brown hair), «سیاهی» for the black smoky hand, and «پذیرایی خونه نفیسه» for the room; use the uploaded khastegari image for continuity.

Vertical 9:16 real photograph, cinematic film still, frozen action moment, not CGI.
Wide shot from behind and slightly to the side of the sofa (a completely different angle from the first time), at about shoulder height of a seated person. In the middle, Nafiseh bends forward holding the silver tray of tea glasses; her wrist is suddenly seized by a long thin hand made of black smoke (no body attached, coming from nowhere beside her), the tray tilting violently toward the groom's mother seated on the sofa in the foreground (seen from behind-left), hot amber tea frozen in mid-air arcs spraying toward her, glasses falling. The groom beside his mother turns his head with a startled face; the others are blurred. The chandelier glows above, the window with the Milad Tower in the background.

Lighting: warm tungsten light with a cold shadow around the black smoky hand.
Mood: the exact moment the evening shatters, seen from the guests' side.

Image quality: ultra high resolution, extremely sharp and crisp, realistic liquid and volumetric smoke, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 24mm lens at f/4, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look, no blood.
```

✅ سکانس ۳ شات ۵ تأیید شد: `images/s3_shot5.webp`.

✏ دیالوگ‌های شات ۶ (کوتاه‌شده):
- مادر داماد: «این حنای چیه؟!»
- مادر نفیسه: «واسه عروسی دخترخاله‌ش…»
- مادر داماد: «دروغ نگو! کف دست نمی‌بندن! این دختر عقد کرده‌ست!»

---

## سکانس ۳ | شات ۶ | مادر داماد کف دست نفیسه رو برمی‌گردونه

### پرامپت تصویر
مرجع‌های ضمیمه: «مادر داماد»، «نفیسه»، «مادر نفیسه»، «پذیرایی خونه نفیسه» و عکس شات ۵ (پیوستگی)
```
Use the saved references: «مادر داماد» (same face, black gold-embroidered manteau, black silk scarf, heavy gold bangles, her right hand now red and wet from the hot tea, tea stains on her lap), «نفیسه» (same face, long wavy dark-brown hair, white off-shoulder lace dress, the sheer veil slipping), «مادر نفیسه» (navy headscarf, floral dress), and «پذیرایی خونه نفیسه» for the room; use the uploaded previous image for continuity (tea mess, tray on the floor, glass shards).

Vertical 9:16 real photograph, cinematic film still, not CGI.
Tight medium shot. The groom's mother, furious, standing up from the sofa, grips Nafiseh's wrist with her gold-bangled hand and violently turns Nafiseh's palm upward, pushing it toward the camera: the long lace sleeve has slid back and the palm is covered with the dark orange-red henna pattern, vivid and stubborn. The mother's face is contorted with rage and accusation, mouth open mid-shout. Nafiseh, terrified and trapped, eyes wet, trying to pull away, face turned aside. Behind them, Nafiseh's mother with both hands pressed to her head in horror, the groom standing stunned, the groom's father standing with a hard stare.
Foreground: the henna palm is sharp and central, tea drops and a few glass shards visible on the carpet below.

Lighting: warm tungsten light, harsh and dramatic, deep shadows on the angry faces.
Mood: public humiliation, the secret exposed.

Image quality: ultra high resolution, extremely sharp and crisp, every henna line, skin pore and gold detail visible, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 50mm lens at f/2.8, tack-sharp focus on the henna palm and the mother's face, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

---

## ✏ تغییر (تصمیم کاربر): شات ۶ قبلی (افشای حنا) حذف شد، چون زیادی بود
ترتیب جدید ادامه‌ی سکانس ۳ بعد از حادثه‌ی چای:
- **شات ۶ (جدید):** مادر داماد عصبانی بلند می‌شه: «دختر شما دیوونه‌ست! من همچین عروسی نمی‌خوام!» (دست قرمز و لباس خیس، پدر داماد بازوش رو می‌گیره)
- **شات ۷:** خانواده‌ی داماد با قهر می‌رن. داماد دم در یه نگاه غمگین به نفیسه می‌ندازه و در محکم بسته می‌شه.
- **شات ۸:** سکوت. مادر نفیسه سیلی می‌زنه: «آبرومونو بردی!»
حنا این‌جا برملا نمی‌شه و راز نفیسه تا آخر همون‌طور می‌مونه.

### پرامپت تصویر شات ۶ (جدید)
مرجع‌های ضمیمه: «مادر داماد»، «پدر داماد»، «داماد»، «مادر نفیسه»، «نفیسه»، «پذیرایی خونه نفیسه» و عکس شات ۵ (پیوستگی)
```
Use the saved references: «مادر داماد» (same face, black gold-embroidered manteau, black silk scarf, heavy gold bangles, her right hand red and wet from the hot tea, tea stains soaking her lap), «پدر داماد» (grey hair, grey beard, dark-grey suit, light-blue shirt), «داماد» (wavy brown hair, dark suit, white shirt), «مادر نفیسه» (navy headscarf, floral dress), «نفیسه» (long wavy dark-brown hair, white off-shoulder lace dress, the sheer veil slipping), and «پذیرایی خونه نفیسه» for the room; use the uploaded previous image for continuity (tray and glass shards on the carpet, spilled tea, same lighting).

Vertical 9:16 real photograph, cinematic film still, not CGI.
Medium-wide shot of the aftermath. The groom's mother has just stood up from the sofa, wet black manteau, clutching her scalded red hand against her chest with the other hand, face red and twisted with fury and humiliation, one finger sharply pointing at Nafiseh while she shouts, her gold bangles sliding down her wrist. Beside her, the groom's father grips her upper arm, jaw clenched, cold angry eyes, already steering her toward the door. The groom stands half a step behind, upset and torn, looking at Nafiseh with worried eyes. On the left, Nafiseh stands small and frozen with her hands covered by her lace sleeves, tears running, head lowered in shame, her mother beside her with both hands on her head, pleading, mouth open.
Foreground: the tipped silver tray and glass shards on the red carpet; background: the samovar, the chandelier, the window with the Milad Tower.

Lighting: warm tungsten light, harsh and dramatic, deep shadows on the angry faces.
Mood: public humiliation, an engagement destroyed in seconds.

Image quality: ultra high resolution, extremely sharp and crisp, every face recognizable, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 35mm lens at f/4, all faces in sharp focus, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra people, no extra fingers, no plastic skin, no cartoon look.
```

✅ سکانس ۳ شات ۶ (جدید) تأیید شد: `images/s3_shot6.webp`.

---

## سکانس ۳ | شات ۷ | خانواده‌ی داماد با قهر می‌رن، داماد دم در

### پرامپت تصویر
مرجع‌های ضمیمه: «داماد»، «نفیسه» و عکس شات ۶ (پیوستگی)
```
Use the saved references: «داماد» (wavy brown hair, hazel-green eyes, short trimmed beard, dark suit, white open-collar shirt) and «نفیسه» (long wavy dark-brown hair, white off-shoulder lace dress, sheer veil); use the uploaded previous image for continuity of the living room, lighting and the aftermath.

Vertical 9:16 real photograph, cinematic film still, not CGI.
The apartment's entrance hall seen from inside the living room, at night. The wooden front door is open and the groom's furious parents are already stepping out into the dim stairwell, their backs visible (the mother's black embroidered manteau, the father's grey suit). In the doorway, the groom stands in the centre, one hand on the door edge, turning back for one last look: his face is sad, hurt and regretful, eyes glossy, lips pressed together. In the foreground, slightly out of focus on the left edge, Nafiseh stands small in her white lace dress and veil, face turned toward him, tears on her cheeks, a mixture of grief and longing. Behind her the wrecked living room is softly blurred: chandelier, spilled tea and broken glass on the carpet.

Lighting: cold blue light from the stairwell spilling in through the open door, warm tungsten light from the living room; the groom's face is split between warm and cold.
Mood: a lost chance, a goodbye without a word.

Image quality: ultra high resolution, extremely sharp and crisp, natural skin texture, tears, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 50mm lens at f/2.8, tack-sharp focus on the groom's face, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra people, no extra fingers, no plastic skin, no cartoon look.
```

---

## سکانس ۳ | شات ۸ | سکوت و سیلی مادر

### پرامپت تصویر
مرجع‌های ضمیمه: «مادر نفیسه»، «نفیسه»، «پذیرایی خونه نفیسه» و عکس شات ۶ (پیوستگی)
```
Use the saved references: «مادر نفیسه» (same face, navy headscarf, dark floral house dress), «نفیسه» (same face, long wavy dark-brown hair, white off-shoulder lace dress, the sheer veil half fallen), and «پذیرایی خونه نفیسه» for the wrecked living room; use the uploaded previous image for continuity (tipped tray, spilled tea, glass shards, same lighting).

Vertical 9:16 real photograph, cinematic film still, frozen action moment, not CGI.
The guests are gone and the room is silent. Close medium two-shot, side view. Nafiseh's mother has just slapped her daughter across the face with her right hand: her arm is extended at the end of the swing, palm open, her face a mask of rage, shame and heartbreak, lips pressed, eyes full of tears; Nafiseh's head is snapped sideways by the slap, her long dark-brown hair whipping across her face, the veil sliding off her head, a red handprint blooming on her cheek, eyes wide and welling, mouth slightly open in shock and silence.
Background softly blurred: the tipped silver tray, spilled tea and broken glass on the red carpet, the chandelier, the window with the Milad Tower and the dark empty room.

Lighting: warm tungsten light, a little harsher, deep shadow on one side of each face.
Mood: aftermath, silence, a mother hitting the daughter she cannot protect.

Image quality: ultra high resolution, extremely sharp and crisp, every skin pore, tear and strand of hair visible, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 50mm lens at f/2.8, tack-sharp focus on both faces, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no blood, no extra fingers, no plastic skin, no cartoon look.
```

✅ سکانس ۳ شات ۸ تأیید شد: `images/s3_shot8.webp`. (شات ۷ هنوز ساخته نشده، اختیاری.)

---

# سکانس ۴: قلاب پایانی (بدون تماس تلفنی)

## سکانس ۴ | شات ۱ | نفیسه نیمه‌شب کنار پنجره روی زمین

### پرامپت تصویر
مرجع‌های ضمیمه: «نفیسه»، «اتاق نفیسه»
```
Use the saved references: «نفیسه» (exact same face, long wavy dark-brown hair now messy, wearing the same white off-shoulder lace dress, the sheer veil crumpled on her shoulders, a red slap mark on her cheek) and «اتاق نفیسه» for her bedroom (same bed, bedside lamp, big window with the night skyline of Tehran and the Milad Tower, the cream rug under the window).

Vertical 9:16 real photograph, cinematic film still, not CGI.
Midnight. Nafiseh sits on the cream rug on the floor of her dark bedroom beside the big window, her back against the wall below the windowsill, her knees pulled up to her chest, arms wrapped around them, head slightly tilted back against the wall, eyes red and swollen, tears silently running down her cheek with the red handprint, staring blankly into nothing. Medium-wide shot from across the room at floor level; the window beside her shows the glittering night view of Tehran with the Milad Tower; the dim bedside lamp is off or barely glowing. The room is quiet, empty, lonely.

Lighting: cold blue moonlight and city glow coming through the window onto her face and lace dress, deep soft shadows in the rest of the room.
Mood: broken, exhausted, alone after the worst night of her life.

Image quality: ultra high resolution, extremely sharp and crisp, every lace thread, skin pore and tear visible, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 35mm lens at f/2.8, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

---

## سکانس ۴ | شات ۲ | سیاهی توی شیشه‌ی پنجره پشت نفیسه ظاهر می‌شه (جایگزین تماس تلفنی)

### پرامپت تصویر
مرجع‌های ضمیمه: «نفیسه»، «اتاق نفیسه»، «سیاهی» (و عکس شات ۱ سکانس ۴ برای پیوستگی)
```
Use the saved references: «نفیسه» (exact same face, messy long wavy dark-brown hair, white off-shoulder lace dress, red slap mark on her cheek, tear-streaked), «اتاق نفیسه» for the bedroom and the big window with the Milad Tower, and «سیاهی» for the dark entity; use the previous image for continuity (same position by the window on the cream rug).

Vertical 9:16 real photograph, cinematic film still, not CGI.
Midnight. Nafiseh sits on the floor beside the big window, knees pulled up, but now she has turned her head slowly toward the glass beside her and froze, eyes wide open with a mix of fear and heartbreak, her breath caught, lips parted. In the dark window glass right above her, enormous and close, a tall faceless man-shaped figure made of living black smoke fills most of the glass, pressed against it from outside, two glowing amber eyes staring straight down at her; a long smoky hand lies flat against the glass as if reaching for her. The city lights and the Milad Tower glow faintly behind and through the black haze. Her face and the figure's eyes are both sharp.

Lighting: cold blue moonlight and city glow, deep shadows, the amber eyes the brightest point, a faint cold fog of breath on the glass.
Mood: terror and strange tenderness, someone who will never leave her alone.

Image quality: ultra high resolution, extremely sharp and crisp, realistic volumetric smoke, real skin pores, tears, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 35mm lens at f/2.8, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```

✅ سکانس ۴ شات ۲ و ۳ (یکی شدن): `images/s4_shot2.webp` (سیاهی توی شیشه، دست روی شیشه). شات ۱ (نفیسه روی زمین) اختیاریه؛ می‌شه از ادیت همین شات شروع کرد.

---

## سکانس ۴ | شات ۴ | صبح، مادر پشت تلفن: «داماد تصادف کرده»

### پرامپت تصویر
مرجع‌های ضمیمه: «مادر نفیسه»، «نفیسه»، «پذیرایی خونه نفیسه»
```
Use the saved references: «مادر نفیسه» (same face, navy headscarf, dark floral house dress) and «نفیسه» (same face, long messy dark-brown hair, still in the crumpled white lace dress from last night, faded red mark on her cheek, tired swollen eyes); use «پذیرایی خونه نفیسه» for the color palette and warmth of the apartment, but this is the apartment's small plain kitchen.

Vertical 9:16 real photograph, cinematic film still, not CGI.
Early morning, cold grey daylight through a kitchen window. In the small plain family kitchen, the mother stands pressed against the counter with an old beige landline phone at her ear, face drained of color, pale as paper, eyes wide and unfocused, one hand covering her mouth, shaking, as if she has just heard terrible news. On the counter: unwashed cups, a kettle, a sugar bowl. In the doorway at the back of the frame, slightly out of focus, Nafiseh stands motionless in her crumpled lace dress, watching her mother, hugging her own arms, her face numb with a dawning horrified realization.

Lighting: flat cold grey morning light, a faint blue tint, quiet and bleak.
Mood: shock, dread, the news has arrived.

Image quality: ultra high resolution, extremely sharp and crisp, every skin pore, wrinkle and fabric texture visible, true-to-life colors, no noise, no compression artifacts.
Shot on ARRI Alexa with 35mm lens at f/2.8, tack-sharp focus on the mother's face, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```
- دیالوگ مادر (آروم و لرزون، توی تلفن): «…پسره دیشب، تو راه برگشت… تصادف کرده.»

## سکانس ۴ | شات ۵ | حنای تازه دور انگشت، راوی پایانی

### پرامپت تصویر
مرجع: «نفیسه» (برای دست)
```
Use the saved reference «نفیسه» for her hand (same olive skin tone, the faded orange-red henna pattern still on the palm and fingertips).

Vertical 9:16 real photograph, cinematic film still, not CGI.
Extreme close-up of Nafiseh's open left palm held up in front of her face in soft cold morning light, the camera at a slight angle, fingers lightly curled. Around the base of her ring finger, a fresh, glossy, deep red-orange henna line has just appeared, a thin perfect circle exactly like a ring, still slightly wet and darker than the old faded henna around it, as if freshly painted by an invisible hand. Her other hand trembles near the frame edge. In the soft-focus background, Nafiseh's face — pale, eyes wide with horror, tears welling, lips parted — looking at the new mark.

Lighting: cold grey-blue morning window light, soft shadows, a faint hint of warm amber reflected in the henna.
Mood: a mark of ownership, quiet horror.

Image quality: ultra high resolution, extremely sharp and crisp, every henna line, skin pore and fingerprint visible, natural skin texture, true-to-life colors, no noise, no compression artifacts.
Shot on Canon EOS R5 with RF 100mm macro lens at f/2.8, tack-sharp focus on the ring-shaped henna line, 8K, hyperrealistic, real photograph, masterpiece.
No text, no watermark, no logo, no extra fingers, no plastic skin, no cartoon look.
```
- راوی پایانی (نفیسه، نجوا): «اون شب فهمیدم… اون فقط عاشقم نیست. هر کی به من نزدیک بشه… از بین می‌بره.»
- کارت پایانی: «پارت بعد / ادامه دارد…» با CTA: «به نظرت مادر نفیسه حق داشت؟ 👇 کامنت کن»

✅ سکانس ۴ شات ۴ تأیید شد: `images/s4_shot4.webp`.

✅ سکانس ۴ شات ۵ تأیید شد: `images/s4_shot5.webp`. تمام تصویرهای قسمت ۱ تموم شد (به‌جز شات ۷ سکانس ۳ که اختیاریه). قدم بعدی: ساخت ویدیوها در Gemini، صداها در ElevenLabs، کارت‌ها در HyperFrames، آهنگ‌گذاری و ادیت.

✅ تصاویر نهایی (۲۵ تا) جایگزین شدن. شات ۷ سکانس ۳ هم ساخته شد (`images/s3_shot7.webp`). صفحه‌ی یکپارچه: `episode1_full.html` (۱۳ مگابایت، در Chrome باز بشه؛ پنل داخلی ظرفیتش رو نداره).
- ✏ شات ۱ب قلاب: نفیسه «بفرمایید.» / مادر داماد «ممنون عزیزم.»
