# Fractional Distillation Lab

An interactive web lab that shows Grade 6 students how a refinery tower sorts crude oil into petrol, jet fuel, diesel, bitumen and more. Available in English and Thai.

ห้องทดลองแบบโต้ตอบ สอนเรื่องการกลั่นลำดับส่วนของน้ำมันดิบ สำหรับนักเรียนชั้น ป.6 ใช้ได้ทั้งภาษาไทยและภาษาอังกฤษ

**Open the lab:** <https://ssutee.github.io/fractional-distillation-lab/>
**เปิดเป็นภาษาไทย:** <https://ssutee.github.io/fractional-distillation-lab/#th>

## What students can do

- **Heat the crude oil.** Drag the furnace slider and watch which molecules boil, rise up the tower and condense on each tray, and which stay liquid and sink.
- **Follow one molecule.** Ride along with a single molecule and read its story as it passes each tray, with a live comparison of the tray temperature and its boiling point.
- **Meet the fractions.** Tap a tank to see each fraction's carbon atoms, boiling range and everyday uses.
- **Look inside a real tower.** A 3D cut-away shows the furnace, trays, bubble caps, downcomers, side draw-off pipes, condenser, reflux drum, steam inlet, platforms and a worker for scale.
- **Zoom into one tray.** Watch vapor bubble through the liquid on a real draw-off tray: heavy molecules condense, light ones boil off and rise, and kerosene leaves through the side pipe.
- **Test themselves.** A 7-question quiz explains every answer.

## Using it in class

- Runs in any modern browser on computers, tablets and phones. Nothing to install and no sign-in.
- Switch language with the **English / ไทย** buttons. Add `#th` or `#en` to the link to open one language directly.
- The 3D section needs WebGL. On a device without it, the list of parts and their explanations still work.
- If a device is set to reduce motion, the animations start paused and can be played with a button.

## About the science

This is a simplified model for Grade 6. The tray temperatures (30, 120, 180, 260 and 340 °C), carbon numbers and the 350–400 °C furnace range are rounded. Boiling points come from straight-chain hydrocarbons (alkanes), so every molecule lands on the tray its boiling point predicts. Real towers have 30 to 50 trays, and real fractions overlap a little.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The page GitHub Pages serves. It is built from `fractional-distillation.html`, so don't edit it by hand. |
| `fractional-distillation.html` | The source of the lab. It is also published as a Claude artifact, which adds its own page wrapper. |
| `build-index.py` | Wraps the source in a complete HTML document, adds the link-preview tags, and writes `index.html`. |
| `social-preview.png` | The 1280×640 card shown when the live link or the repository is shared. |

## Editing the lab

1. Edit `fractional-distillation.html`.
2. Rebuild the page:

   ```bash
   python3 build-index.py
   ```

3. Preview it locally, then open <http://localhost:8000>:

   ```bash
   python3 -m http.server 8000
   ```

4. Commit and push to `main`. GitHub Pages republishes the site about a minute later.

## Built with

Plain HTML, CSS and JavaScript with no build tools. The 2D lab is drawn in SVG, the 3D model uses [Three.js](https://threejs.org/) r128 from cdnjs, and the type is set in Google Fonts (Bricolage Grotesque, Lexend, IBM Plex Mono, Anuphan and IBM Plex Sans Thai Looped).

## License

The lab is released under the [MIT License](LICENSE). You are free to use, copy, change and share it, including in your own classes and websites, as long as you keep the copyright notice.

Three.js (MIT License) and the fonts (SIL Open Font License) are loaded from their CDNs and keep their own licenses.
