# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
      Bad Visualization: "Ser-Sub-Category Sale 3D Cylindrical Chart". (Tableau Public, https://public.tableau.com/app/profile/shaq4030/viz/Ser-Sub-Category3DCylindricalChart/CylinderChart ). This visualization is bad for three main reasons.
      
      Reason 1: The 3D cylinders make it hard to read the actual values. The class slides cover the principle "No 3D without Cause", and there's no cause here. Because each bar is a cylinder, it's unclear where exactly the value ends: the front of the curve? The back? The middle? This is what the slide deck 4 calls "approximate interpretation", which is harder on the brain than simply reading a flat bar at a baseline. The 3D adds nothing useful and it only makes things harder to read.
      
      Reason 2: The colours mean nothing. Every bar gets a different random colour, but none of those colours actually encode any information. There's no grouping or pattern behind them. According to Wong (2010), the Gestalt principles tell us that viewers will automatically look for meaning in colour. When there isn't any, it's just confusing noise. On top of that, 17 different colours on a black background is a real accessibility problem for anyone with colour blindness, which goes against creating equitable visualizations.
      
      Reason 3: This chart type is the wrong tool for the job. The whole point of this chart is to compare sales across sub-categories, which is a ranking task. The Financial Times Visual Vocabulary, which we covered in class, tells me that a plain bar chart is the right choice here. Instead, this uses an unusual 3D cylinder format that the course specifically flags as increasing cognitive load. The story (which sub-categories sell the most) gets completely buried in the visual noise.

      Good Visualization: "AI/AN Unemployment Rates Over Time". (Tableau Public, https://public.tableau.com/app/profile/britnee.johnston3127/viz/AI-ANUnemploymentRatesOverTime/Fig3). This visualization is a "good" classification for three main reasons.
      
      Reason 1: It picks the right chart type and tells a clear story. The chart compares unemployment trends across five racial groups over two decades, which is a "change over time" task, and a multi-line chart is exactly what the Financial Times Visual Vocabulary recommends for it. The chart type is also familiar, which as we noted in class, keeps cognitive load low. Also, the title is informative: "During recessions and recoveries, American Indian/Alaska Natives' unemployment rate is higher than white, Latinx, and Asians." You don't have to guess what the point is. In class we talked about how a good visualization clearly conveys what message the maker is attempting to convey.
      
      Reason 2: It hits all four of Kennedy et al.'s (2016) conventions. The four design choices that make audiences trust a visualization more are a 2D image, a clean layout, geometric shapes and lines, and a cited data source. This chart checks every box. It's uncluttered, uses simple lines, and credits the U.S. Bureau of Labor Statistics at the bottom. In class we talked about "provenance rhetoric", which is the idea that citing your source signals transparency and makes viewers more likely to trust what they're seeing (slide 47 in slide deck 4).
      
      Reason 3: The colour works. it uses "Gestalt similarity" meaningfully. Each racial group gets a distinct, consistent colour that runs throughout the chart. According to Wong (2010), the Gestalt principle means viewers automatically group things that look alike, and here, that instinct is actually helpful. Your eye follows each line as a single continuous story without getting confused. This is the opposite of the bad visualization, where 17 random colours encoded nothing. The colour palette also uses muted, distinguishable tones rather than neon colours, making it more accessible across different viewing contexts.


      ```
    - How could this data visualization have been improved?  
      ```
      For the BAD visualization:
      Improvement 1: Switch to a simple horizontal bar chart, sorted by value. Sorting bars from highest to lowest makes the ranking obvious at a glance. No 3D needed and no confusion about where to read the value.
      Improvement 2: Use one colour, or use colour with purpose. A single colour for all bars, or one highlight colour for the top performer, would be far cleaner and accessible to all viewers, addressing our focus on equitable design.

      For the GOOD visualization:
      Improvement 1: Add direct line labels instead of a separate legend. Right now the legend sits below the chart, forcing the viewer to move their eyes back and forth to figure out which line is which. Labelling each line directly at its endpoint would reduce that back-and-forth and lower cognitive load.
      
      Improvement 2: Highlight the AI/AN line more prominently. Since that group is literally the subject of the title, it could be bolder or a slightly thicker line weight to draw the eye there first. This would strengthen the storytelling and make the visualization even more intentional in guiding the audience.
      
      ```
- Word count should not exceed (as a maximum) 500 words for each visualization (i.e. 
300 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 -  2026-06-09`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
