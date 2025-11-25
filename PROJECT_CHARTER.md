# PROJECT_CHARTER.md

## Project Title
AI-Powered Leftover Recipe Generator for Reducing Food Waste

## Team Members & Roles
- Solo Developer: Jiashu Hu - Handling all roles including Project Manager, AI Integrator, Front-End Developer, Back-End Developer, and Data & Testing Specialist.

## Problem Statement
It is estimated that about 1.3 billion tons of the food wasted yearly are related to environmental degradation, resource inefficiency, and aggravate hunger among the low-income communities worldwide. Leftovers are not reused creatively even though many households, particularly students and cost-efficient families, find it difficult to creatively use leftovers, which results in discarding them unnecessarily, incurring additional expenses in acquiring grocery products. Current solutions do not take into consideration individual nutritional requirements and preferences towards cultural options, so available ingredients are often underutilized, and waste remains constant.

## Proposed Solution & Core Features
- **User Input Interface**: Simple form to input 3-5 leftover ingredients and user preferences (e.g., vegetarian, low-calorie).
- **AI-Generated Recipes**: Produces 1-2 easy-to-follow recipes with step-by-step instructions (limited to 5 steps), nutritional breakdowns, and zero-waste tips.
- **History Tracking**: Saves past recipes locally for quick reference, promoting repeated use.
- **Ethical Safeguards**: Includes disclaimers for dietary advice and ensures outputs are culturally neutral.

## Novelty Statement
This app is unique compared to generic ChatGPT apps or recipe apps because it takes advantage of generative AI by creating highly-designed prompts that enforce nutritional balance, affordability (with everyday household tools), and a zero-waste philosophy that is specifically optimized to support under-served users. The integration also uses broader suggestions, unlike standard chatbots that impersonate broader advice to low-income contexts, including the fact that it includes an in-depth filter on relevance to low-income contexts, like consideration of affordable staples and metrics of environmental impact, which creates a closed-loop system and not only generates recipes but also educates the user about sustainable habits. By turning a widespread issue into a practical, emphatic instrument, this new solution will promote the creation of long-lasting behavior change without demanding the knowledge of either cooking or AI among users.

## Tech Stack
- **Front-End**: Streamlit (Python-based UI for rapid prototyping)
- **Back-End & AI Integration**: Python with OpenAI GPT-3.5-turbo API (for text generation via prompt engineering)
- **Data Handling**: JSON for local storage of recipe history (no external database needed)
- **Development Tools**: GitHub for version control; requirements.txt for dependencies (e.g., streamlit, openai)
