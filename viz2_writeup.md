# Visualization 2 - TTC Delay Events by Incident Category and Line

**Dataset:** TTC Subway Delay Data 2024 - City of Toronto Open Data Portal
**Link:** https://open.toronto.ca/dataset/ttc-subway-delay-data/

## 1. Software used

Microsoft Excel. Clustered horizontal bar chart built from a data table. Submitted as '.xlsx' and '.png'. I included a 'how to' excel file to retrace my steps.

## 2. Intended audience

Transit advocates and TTC planners who need to know what causes delays and which lines are worst.

## 3. Message / information conveyed

People-related incidents dominate on all lines. Disruptive passengers, passenger injuries, and false alarms make up the majority of delay events. Door malfunctions are the top technical cause on Line 1 but absent from Line 2. Line 4 has far fewer events, but it also has far fewer stations (6 vs. 38 on Line 1), so raw counts aren't directly comparable.

## 4. Design considerations

**Chart type:** Horizontal clustered bars for comparing counts across 8 categories × 3 groups. 

**Colour:** Okabe-Ito (blue '#0072B2', orange '#E69F00', sky-blue '#56B4E9') - hue is right for categorical data, avoids red/green, works under all common colour-vision deficiencies.

**Data labels:** Counts on bars so readers don't have to estimate from the axis.

**Sorting:** Descending by total count.

**Labels:** Plain English so any reader can follow without knowing TTC codes.

## 5. Reproducibility

The '.xlsx' file contains the data table and chart. Excel charts are not reproducible in the same way code is. Formatting depends on the Excel version, but the data table is included so the chart can be recreated if needed. Refer to the 'how to' excel document to reproduce.

## 6. Accessibility

Okabe-Ito avoids red/green and is readable under deuteranopia. Data labels eliminate reliance on colour alone.

**Alt text:** Horizontal grouped bar chart of TTC delay event counts, top 8 categories by line. Disruptive passengers and passenger injuries most common. Door malfunctions high on Line 1, absent on Line 2. Line 4 counts low throughout.

## 7. Individuals and communities impacted

Most delay causes are people-related, not mechanical. This reflects a transit system serving many vulnerable riders. Surfacing this supports advocacy for social services, not just operational fixes. As in Visualization 1, the most affected riders are those with no alternative to the TTC.

## 8. Feature inclusion / exclusion rationale

**Included:** Category, line, count. MUIR + MUI merged (same event, different outcomes) — combined they are the #2 cause. Top 8 covers the bulk of events.

**Excluded:** Min Delay = 0 rows; average duration (outliers dominate); per-station normalisation (stations vary too much, which is a limitation noted in Question 3).

## 9. Underwater labour

PUT0 was missing from the Code Descriptions file and labelled manually. Seventeen line-name variants collapsed to three. The two injury codes identified as the same event and merged into one label. TTC staff, City open data maintainers, and incident coders are invisible contributors whose work is necessary for this chart.
