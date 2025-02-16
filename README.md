<div align="center">

# AI Agents: Create Blender Scripts 🎨🖥️  
**The most powerful AI-powered Blender scripting tool.**  
[![Website][website-shield]][website-url]  
[![Support][support-shield]][support-url]  
[![Downloads][downloads-shield]][downloads-url]  

[website-shield]: https://img.shields.io/badge/FastBlenderAddOns-4285F4?style=flat  
[website-url]: https://fast-blender-add-ons.com/fast-animation-studio-tools-2/  
[support-shield]: https://img.shields.io/badge/Support-Email-blue?style=flat  
[support-url]: https://fast-blender-add-ons.com/support/  
[downloads-shield]: https://img.shields.io/badge/Downloads-Available-brightgreen?style=flat  
[downloads-url]: https://fast-blender-add-ons.com/shop


## 🚀 Repository Naming Issue🚀  
**For tonight: You must install the add-on manually and rename the module folder to  'blender_ai_thats_error_proof' before using. We will fix having to do this early tomorrow.**

---

## ⚠️ **One Quick Note**  
We're uploading everything as planned, but we've noticed something interesting during our testing. The **example pulling functionality** works **most of the time**, successfully retrieving references. However, during testing of a **basic Geometry Nodes script**, the assistant didn’t always pull the correct **Geometry Nodes code examples**.

### **Temporary Recommendation:**  
To avoid unnecessary processing costs, **we recommend avoiding Geometry Nodes script generation** if the assistant doesn't pull the correct examples.  

That said, on the **panel, there's a box displaying `.py` files**—one of them is `main_file.py`. You can **manually add small code examples** here if needed, apart from the AI’s example pulling functionality. The system processes a **200,000-line file** that we provide, to locate examples, but manual input allows for more direct control which could help here.

### **Optimization in Progress:**  
- We are currently **improving the vector search functionality** to enhance retrieval accuracy.  
- In the meantime, **manually providing single code examples** (functions, operators, or small scripts) in `main_file.py` is the best approach....(main_file.py is visible in a box on panel...read tooltips...)
- **Keep `main_file.py` limited to one example at a time** for optimal results.  
- You can also use the **instruction set system** to fine-tune the AI’s responses, and circumvent needing code examples, But this is more time consuming and only recommended to do when you have to e.g. AI system can't get past an error or example not being pulled.

---


---

### 🎥 Coming Soon: Special Section & Video Guide  
We’re going to **add a short video** explaining exactly how to use the **instruction set system** to refine the assistant’s output.  

For now, we have a **full-length tutorial video** at the bottom of the page, that includes that information toward the end, and we highly recommend watching it to fully understand how everything works. 

If you have any **questions, issues, video documentation request or feedback**, please use the **GitHub issue reporting section**—you're helping us improve! 🚀




### 📌 FYI: Start Amassing Blender Code Examples to Get the Best Results  

Originally, this feature was part of **our main add-on, FAST Animation Studio Tools**, where it pulled examples from the biggest Blender add-on in the world. That setup made our script generator work **amazingly well** by using real Blender automation examples.

Since this **standalone version** doesn’t include our main add-on’s full codebase, it works a little differently—you’ll need to **supply your own example code or even full add-ons as examples** for the best results. Luckily, this is super easy!

---

### 🧠 How Our AI Generates Perfect Scripts

Our add-on uses **the same AI models as ChatGPT**, and these models generate **better scripts when given real, tested code examples**. That means the more **high-quality Blender add-ons** you provide as references, the **smarter and more accurate** your script generation will be.  

We provide a **large example file of code** with the add-on that works fine in many cases, but if a script **isn't generating correctly**, you may need to provide **relevant code examples** related to the type of script you're trying to create.


1️⃣ **How to Add Your Own Code Examples:**
- You can **add entire Blender add-ons** as code references by simply **adding their file paths** to a special file.
- The system will use those add-ons to generate **high-quality, error-free scripts**.

2️⃣ **Where to Find Free Blender Add-ons:**
- **[Gumroad](https://gumroad.com/)** has **tons of free Blender add-ons** that you can use.
- You can **filter by price** to find **free** ones.
- Look for add-ons that match **the type of scripts you want to generate**.

3️⃣ **Choosing the Right Add-ons for Best Results:**
- **Make sure the add-ons you choose are updated for Blender 4.0+** for maximum compatibility.
- If necessary, you can go down to **Blender 3.6**, but be aware that **major changes happened between 3.6 and 4.0**.
- Using outdated add-ons **may introduce issues** due to API changes.

4️⃣ **Why This Matters:**
- **LLM that generate code perform best with real, up-to-date code.**  
- If you **don’t know how to code**, you’ll get much better results by giving the system **code examples**.  
- **Note: This system uses AI to determine the perfect code examples to use so they are provided without need of user interaction.**  


</div>

## About This Add-on  
**An AI-powered script generator with automatic error fixing—it generates, tests, and fixes Blender scripts for you.**  


### **Introducing the Ultimate Script Generator for Blender 4.3**  
The latest addition to **FAST Animation Studio Tools**—which is the **BIGGEST Blender add-on IN THE WORLD (code-wise)** Provided free here for your enjoyment.!  

## Features  
- **AI-Powered Script Generation**: Uses **GPT-4o**, the same model available in ChatGPT Pro, to generate automation scripts from your detailed commands.  
- **Automatic Error Handling**: Runs the script, detects issues, and automatically fixes errors in a loop.  
- **Smart Code Lookup**: Searches the **Blender API, Blender Manual, and your own database of code examples** for solutions.  
- **Version Compatibility**: Converts older scripts to **Blender 4.3 compatibility** automatically.  
- **Boost User Command Feature**: Optimizes your input to be **Blender Manual-compatible** for better results.  
- **Self-Updating Fixes**: Can locate and retrieve example scripts from our **internal database** or even **external add-ons** you specify.  
- **Interactive Fix System**: In rare cases where auto-fix doesn’t work, an easy-to-follow instruction set system allows even **non-programmers to resolve errors in 5-10 minutes.** 
- **Hail Mary Fix Attempt**: The system performs a final attempt to **automatically solve complex issues**, so manual fixing might not be necessary.  
- **Optimized for Animation & Nodes**: Works especially well for **automation scripts, shader setups, compositor nodes, and geometry nodes.**  
- **World-Class Customer Support**: We will start fixing any issue reported **immediately**  

[More information here!](https://fast-blender-add-ons.com/)  



## Installation  

### Windows Users  

#### 1. Download & Extract  
- **Pre-packaged with dependencies.**  
- **Double-click the ZIP file** to open it.  
- **Drag or Copy & Paste** the folder inside the ZIP to:  
  **Blender's `scripts/addons/` directory**  
- **Rename the folder** to:  


#### 2. Enable the Add-On in Blender  
- Open **Blender**  
- Go to **Edit** → **Preferences** → **Add-ons**  
- Find **Blender AI That's Error Proof** and enable it  

#### 3. Confirm AI Features in the Blender Console  
📢 **Check the Blender console!**  
- The add-on will prompt you to install AI-related files.  
- **Press "Y" in the console to proceed.**  
- **Wait for the PIP libraries to install automatically.**  

#### 4. Enter Your API Key in the Blender AI2 Panel  
- Open Blender’s **N-Panel** by pressing **N**.  
- Navigate to **Blender AI2**.  
- **Enter your OpenAI API key** to unlock full functionality.  

### Mac & Linux Users   
- **Mac & Linux support is coming soon.**  
- Dependencies will **auto-install on the first run.**  

## How to Use  

### 1. Enable the Add-On  
- Open **Blender**  
- Go to **Edit** → **Preferences** → **Add-ons**  
- Find **Blender AI That's Error Proof** and enable it  

### 2. Confirm AI Features in the Blender Console  
📢 **Check the Blender console!**  
- The add-on will prompt you to install AI-related files.  
- **Press "Y" in the console to proceed.**  
- **Wait for the PIP libraries to install automatically.**  

### 3. Enter Your API Key in the Blender AI2 Panel  
- Open Blender’s **N-Panel** by pressing **N**.  
- Navigate to **Blender AI2**.  
- **Enter your OpenAI API key** to unlock full functionality.  

### 4. Generate Scripts  
- Click **"Edit User Command"** and describe the script you need.  
- Click **"Assistant"** to generate the script.  

### 5. Enable **Verbose ToolTips** (Recommended)  
- Provides **detailed, built-in documentation** inside all Blender AI panels.  
- **Highly recommended:** Spend **about 30 minutes** reading tooltips to understand all available features.  
- The add-on is **user-friendly**, but reading the documentation will help **unlock its full potential**.  
- If the script generator encounters an issue, **tooltips will guide you on how to resolve it quickly.**  




## Handling Errors well is our big selling point: It has the Easiest Debugging System Ever

We’ve made fixing errors **so simple that even a kid could do it**—seriously! 🚀  

If the script generator does encounter an error it **can’t get past**, you can resolve it in **just 5-10 minutes** using our **user instruction set system and ChatGPT Plus**. This means **anyone** can keep their script generator running smoothly, without needing deep programming knowledge.  


### **Pro Tip for Coders:**
If you know a function has an issue, **just throw it into the script generator**. Our AI is **explicitly instructed not to change your code structure**, so you can **trust it**. We regularly do this ourselves—just let the AI handle the debugging while you focus on creating scenes!  

🚀 **Bottom line:** This tool is **not just about generating code**—it’s designed to keep you scripting **all the time** with **minimal effort**. **It's designed for coders and non coders** alike making it so everybody can continuously generate error free code regardless.

---
🔹 **How the AI Works**  
- The add-on runs OpenAI models **in a loop**, perfecting code over **5 iterations by default**.  
- Each run **typically takes 1 to 5 minutes** and **costs around 30 to 50 cents**.  
- **We've implemented the GPT-03 Mini model** as a option for some of our **commonly used helper functions** that support the main AI assistant responsible for generating code.  
- **This likely reduces costs**, but we haven't fully tested it yet. If you experience issues, **switch back to GPT-4o in the settings** to ensure stability.  

🚀 **Upcoming AI Enhancements**  
We are actively testing the **GPT-03 Mini model as an alternative for the main assistant**. In our first test, it generated **600 lines of code**, while **GPT-4o maxed out at 358 lines**. This increased output is promising, but we need further testing to ensure all **helper functions work reliably with it** before making it a selectable option.  

Our approach is to **give users flexibility**—whenever we introduce a new model, it will be **tickable in the settings**, allowing you to **choose the AI setup that works best for your needs**. We will always keep **GPT-4o as an option** so users can revert to it at any time if they prefer.  

We are also evaluating **free AI models like DeepSeek and TULU 4.5B** to see if they can match GPT-4o’s capabilities. If they perform well, we’ll integrate them as an **optional setting**, providing users with additional **cost-saving choices**.  

🔹 **Our Approach to AI Optimization**  
- We’ve worked extensively with **GPT-4o since launch** and optimized our workflows to **maximize its accuracy and efficiency**.  
- While some users report varied experiences with GPT-4o, **We feeel it works very well & our prompting methods ensure exceptional results**.  
- We recognize that AI models can fluctuate in performance, so we are committed to **keeping previous models available as backup options**.  


## **Caveat: First Release Update System Notice ⚠️**  
We're pushing to get this to you **as soon as possible**, so while we **are including an add-on update system**, it **has not been fully tested yet**.  

🔹 **What to do?**  
✅ **Manually check for updates** on **GitHub** until you see a console message confirming the update system is working properly, or this is removed.  



## Additional Features  
- **Restart Blender Button**: Restart without losing progress.  
- **Show Console Button**: View script execution in real time.  
- **Auto-Update System**: Checks for updates on startup.  
- **Save/Delete Startup File**: Manage Blender startup configurations easily.  
- **Verbose Tool-tip System**: View comprehensive documentation inside the add-on.


## Get Our Full Add-on!  
This script generator is just one part of **FAST Animation Studio Tools**—the **BIGGEST Blender add-on IN THE WORLD (code-wise)**, featuring **500+ workflow optimizations**!  

🚨 **We Would Be Literally Screwing 23 Million Blender Users If We Didn’t Tell You About This!** 🚨  
We’ve spent **2+ years** developing and **updating this add-on daily**, refining it into the ultimate tool for **streamlining Blender workflows**. There are **23 million Blender users out there** who don’t know this exists—and that means they’re stuck doing things **the slow, hard way** when **they don’t have to**.  

Whenever we're working on our **TV Show**, which is the **reason** why we created this **Blender add-on**, if something is **hard to do**, we **write code**—and the end result is **it benefits you**.  

This isn’t just an add-on—it’s a **game-changer**, removing unnecessary clicks from **every Blender process**, making complex tasks effortless, and **saving you time every single day**.

👉 **Don’t Miss Out—See What You’ve Been Missing!**  
[Check it out here!](https://fast-blender-add-ons.com/fast-animation-studio-tools-2/)  




## Need Help?  
- [Support Email](mailto:support@fast-blender-add-ons.com)  
- Open an issue on GitHub  



## 📺 Should Watch These Videos 

### 🎬 Intro  
[![Intro](https://img.youtube.com/vi/F8UzMOiVUsA/maxresdefault.jpg)](https://youtu.be/F8UzMOiVUsA)

### 🎥 How It Works  
[![How It Works](https://img.youtube.com/vi/_CaFP8KjZz0/maxresdefault.jpg)](https://youtu.be/_CaFP8KjZz0)

---



