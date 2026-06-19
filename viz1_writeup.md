# Visualization 1: TTC Subway Delay Heatmap

**Dataset:** TTC Subway Delay Data 2024, City of Toronto Open Data Portal
**Link:** https://open.toronto.ca/dataset/ttc-subway-delay-data/


## 1. Software used

Python 3 with 'pandas', 'seaborn', and 'matplotlib'. Output: 'viz1_heatmap.png'

## 2. Intended audience

Toronto subway riders and transit researchers wanting to understand whether delay severity varies by time of day or day of week.

## 3. Message / information conveyed

TTC subway delays are surprisingly consistent across all hours and days. Most cells average 6–10 minutes regardless of when you travel. The dark band around 3–5am reflects reduced overnight service frequency, not safer travel. A single outlier (Friday 4am, avg 77 min from ~6 incidents) is capped in the colour scale and noted in the caption, because I didn't want it to overshadow the rest.

## 4. Design considerations

**Chart type:** A heatmap uses colour to show a two-dimensional pattern (day × hour) at a glance, which is right for "exploring" or when the goal is spoting where any time slot stands out.

**Colour:** viridis goes from dark purple (low) to yellow (high). It works for people with colour-vision deficiency and prints clearly in greyscale, unlike a rainbow palette.

**Colour scale cap:** Friday 4am (avg 77 min, n ~ 6) is an outlier; Capping at 20 min prevents the outlier from making every other cell look identical. The outlier is noted in the caption.

**Title:** States the finding rather than describing the axes.

**Ticks:** Every-other-hour x-ticks reduce clutter without losing readability.

## 5. Reproducibility

'viz1_heatmap.py' runs from the repo root with standard pip-installable libraries. All settings (file name, palette, scale cap) are named constants at the top of the file.

## 6. Accessibility

**Colorblind safety:** viridis is distinguishable under deuteranopia and protanopia.

**Contrast:** Chart elements meet WCAG contrast standards.

**Alt text:** Heatmap of average TTC delay (min) by hour (0-23) and day (Mon–Sun), 2024. Delays are broadly uniform at 6-10 minutes. Cells around 3-5am appear darker due to lower overnight service volume.

## 7. Individuals and communities impacted

This matters most to people who rely on the TTC with no alternative, like lower-income riders, shift workers, and people without car access. For these riders a consistent 6–10 minute delay on every trip adds up, and the finding that there is no "safe" time to avoid delays is itself an important result.

## 8. Feature inclusion / exclusion rationale

**Included:** Day, hour, average Min Delay (the variables that answer "when is the subway delayed and by how much."). **Excluded:** Min Delay = 0 rows (no measurable disruption); station/line/cause (require a third dimension, which is addressed in Viz 2).

## 9. Underwater labour

Before making the chart, there was filtering of 17,073 zero-delay rows; the time column was parsed to extract the hour; the Friday 4am outlier was investigated and handled (deciding to cap rather than drop it). TTC staff who entered delay records and the City's open data team are invisible contributors whose work makes this visualization possible.
