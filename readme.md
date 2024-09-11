# Aegir 0.3

## About the project

This is the initial data entry module of the Aegir Student Information System, which also contains user registration and authentication.
Features like more advanced data management and course management (planning and signup, course material management, grading and assessments) are under development.
Start of beta testing is planned within 18 months.

### User stories

1. As an Administrator, I want to register with my own username and password so that I can personalize my credentials.
2. As an Administrator, I want to log in so that the data I enter are safe from outsiders.
3. As an Administrator, I want to get feedback about the data I enter so that I can fix any mistakes early on.
4. As an Administrator, I want to see a list of the saved data so that I can check which students are already entered.


### Data validation

The entered student data are validated.
All fields are required and some of them have extra rules that apply to them.

| Field              | Rule                                                                 |
|--------------------|----------------------------------------------------------------------|
| ID card number     | Six digits, then two capital letters of the English alphabet         |
| Personal ID number | Pattern: `c-yymmdd-sssk` (see explanation below)                     |
| Email              | Must contain one `@` and at least one `.` after that                 |
| Phone number       | May or may not contain a `+` at the beginning, has at least 8 digits |
| Zip code           | Exactly 4 digits and cannot start with 0                             |
| Starting date      | Between 2022 and 2028                                                |

#### Personal identification number

As described in the table, the pattern is `c-yymmdd-sssk`, where all characters stand for digits.

- `c`
  - This digit holds information about the person's time of birth and gender.
  - Can be 1, 2, 3 or 4
  - 1: Male, born before January 1, 2000
  - 2: Female, born before January 1, 2000
  - 3: Male, born after December 31, 1999
  - 4: Female, born after December 31, 1999
- `yymmdd`
  - Date of birth
  - Example: 20040225 for February 25, 2004
- `sss`
  - This 3-digit number identifies the person among those born on the same day
- `k`
  - Check digit to prevent typos, calculated from the rest of the digits
  - Calculation:
    1. We multiply every digit with their serial number and then sum them all
      - Example: 2-19870423-072 -> `2 + 2 * 1 + 3 * 9 + 4 * 8 + 5 * 7 + 6 * 0 + 7 * 4 + 8 * 2 + 9 * 3 + 10 * 0 + 11 * 7 + 12 * 2`
      - Result: 270
    2. We divide the result by 11 and get the remainder
       - 207 mod 11 = 6, so the last digit in this case should be 6

## Instructions to run Aegir

### Prerequisites

Ensure you have the following installed:

- Python 3.6 or later
- pip (Python package installer)

### Installation

1. **Clone the repository**


2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
  - On Windows:
    ```bash
    .\venv\Scripts\activate
    ```
  - On Unix systems (macOS and Linux distros):
    ```bash
    source venv/bin/activate`
    ```

4. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application:**
    ```bash
    python app.py
    ```
**Note:** Steps 1, 2 and 4 need to be executed only once.
Step 3, however, needs to be done every time before starting up the application in a new shell.
