## Flask Application Design for Spend Based Commitment Cost Calculation

### HTML Files

**1. Main HTML Page (index.html)**

**Purpose:** serves as the main user interface for inputting spending data and calculating costs.

**Content:**

- Header
- Form containing input fields for:
  - Total spend
  - Commitment percentage
- Submit button
- Display area for results

**2. Results HTML Page (results.html)**

**Purpose:** displays the calculated commitment cost based on input values.

**Content:**

- Header
- Displayed results:
  - Total spend
  - Commitment percentage
  - Commitment cost

### Routes

**1. Main Route (`/`)**

**Purpose:** handles the main page, processing user input and displaying the results page.

**Method:** GET and POST

**Functionality:**
- GET: Renders the main HTML page (index.html)
- POST: Collects user input from the form, calculates the commitment cost, and redirects to the results page with the results.

**2. Results Route (`/results`)**

**Purpose:** displays the calculated commitment cost.

**Method:** GET

**Functionality:**
- GET: Renders the results HTML page (results.html) with the commitment cost data.