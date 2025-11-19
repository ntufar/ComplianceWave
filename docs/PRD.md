# Product Requirements Document (PRD)
**Project Name:** Global E-Invoice Compliance Map (The "Compliance Wave")
**Version:** 1.0
**Status:** Draft
**Owner:** Nicolai Tufar

---

## 1. Problem Statement
**The Pain:** Regulatory requirements for e-invoicing are shifting rapidly worldwide. Information is currently fragmented across dry government PDFs, expensive consultant reports, and news articles.
**The Opportunity:** Tax managers and CTOs lack a centralized, visual tool to instantly understand *where* and *when* e-invoicing mandates are coming into effect.
**The Solution:** An interactive, time-based geospatial dashboard that visualizes the global adoption of e-invoicing mandates from 2015 to 2030.

---

## 2. Target Audience (Personas)
1.  **The Global Tax Manager:** Needs to ensure their company complies with upcoming laws in countries where they operate (e.g., "When does France go live?").
2.  **The SaaS Product Strategist:** Needs to decide which country to expand their invoicing software into next based on market maturity.
3.  **The Consultant:** Needs a visual aid to explain the "spread" of Clearance models to clients during presentations.

---

## 3. User Stories
| ID | As a... | I want to... | So that... |
| :--- | :--- | :--- | :--- |
| **3.1** | User | View a world map color-coded by mandate status | I can instantly identify which regions are heavily regulated (e.g., LatAm vs. Europe). |
| **3.2** | User | Drag a timeline slider (Year) | I can watch the evolution of mandates and see what the world will look like in 2026. |
| **3.3** | User | Filter by Scope (B2G vs. B2B) | I can separate government procurement rules from general business mandates. |
| **3.4** | User | Filter by Model (Post-Audit vs. Clearance) | I can identify which countries require real-time government approval of invoices. |
| **3.5** | User | Hover/Click on a specific country | I can see detailed metadata (Platform name, exact launch date, format standard). |

---

## 4. Functional Requirements

### 4.1 The Interactive Map
* **Visualization Type:** Choropleth Map (Mercator projection).
* **Color Logic:**
    * **Grey:** No Mandate / Paper allowed.
    * **Yellow:** Voluntary / Partial (e.g., B2G only).
    * **Orange:** Upcoming Mandate (Announced but not live).
    * **Dark Blue:** Mandatory B2B Live.
* **Interactivity:** Pan and Zoom capabilities.

### 4.2 Time Control
* **Timeline Slider:** A horizontal slider at the bottom ranging from **2015** to **2030**.
* **Animation:** A "Play" button that auto-advances the slider by 1 year every 1.5 seconds.

### 4.3 Country Detail Panel (Sidebar or Tooltip)
When a country is selected, display:
* **Country Name**
* **Status:** (e.g., "Mandatory B2B")
* **Effective Date:** (e.g., "July 1, 2024")
* **Platform Name:** (e.g., *Chorus Pro* for France, *KSeF* for Poland, *SDI* for Italy).
* **Standard/Format:** (e.g., *Peppol BIS*, *FatturaPA*, *UBL*).

### 4.4 Filters
* **Scope Toggle:** [ All | B2G Only | B2B & B2G ]
* **Region Filter:** [ Global | Europe | Asia-Pac | LatAm ]

---

## 5. Data Requirements & Schema
Since this data is not available via a single API, you will build a **static dataset** (CSV or JSON).

**Proposed Schema (`mandate_data.csv`):**

| Country Code (ISO-3) | Country Name | Year | Status_B2B | Status_B2G | Model_Type | Platform_Name | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ITA | Italy | 2019 | Mandatory | Mandatory | Clearance | SDI | First EU country to mandate B2B. |
| FRA | France | 2026 | Mandatory | Mandatory | Hybrid | PPF / PDP | Delayed from 2024. |
| POL | Poland | 2026 | Mandatory | Mandatory | Clearance | KSeF | Delayed. |
| BRA | Brazil | 2008 | Mandatory | Mandatory | Clearance | NF-e | Early adopter. |
| DEU | Germany | 2025 | Optional | Mandatory | Post-Audit | N/A | B2B starting with e-reporting. |

*Note: You will need one row per country, per year where a status change occurs, OR logic in your code to handle "start dates."*

---

## 6. Technical Stack Recommendation
* **Language:** Python 3.9+
* **Framework:** **Streamlit** (Fastest to build, easiest to host).
* **Visualization Library:** **Plotly Express** (`px.choropleth`).
    * *Why Plotly?* It has built-in animation frames (the "Play" button) that link directly to a "Year" column in your dataframe.
* **Data Handling:** Pandas.

---

## 7. User Interface (UI) Wireframe Description



[Image of wireframe dashboard layout]


* **Header:** "Global E-Invoicing Mandate Tracker" + Brief description.
* **Left Sidebar:**
    * Filter: "Select Scope" (Radio button).
    * Filter: "Highlight Model Type" (Checkbox).
    * Info Box: "Data last updated: Nov 2025".
* **Main Content Area:**
    * Large World Map.
    * Timeline Slider (Bottom of map).
* **Right Panel (Dynamic):**
    * "Country Details" (Appears when user clicks a country).

---

## 8. Roadmap / Phasing

### Phase 1: MVP (Minimum Viable Product)
* Static CSV data for top 20 major economies (G20).
* Basic Choropleth map.
* Timeline slider functionality.
* Tooltip with basic status.

### Phase 2: Detail & Depth
* Expand data to 50+ countries.
* Add "Platform Name" and "Format" details.
* Add "Region" filtering (Zoom to Europe button).

### Phase 3: Analytics (The "Value Add")
* Add a summary chart below the map: "Number of Countries with Active Mandates over Time" (Bar chart).

---

## 9. Next Step: Data Collection
To start this project, you need the data. Would you like me to:

1.  Generate a **sample CSV file** with real data for 10 major countries (France, Italy, Poland, Brazil, Saudi Arabia, etc.) so you can start coding immediately?
2.  Write the **Python/Streamlit code** to load that CSV and render the map?