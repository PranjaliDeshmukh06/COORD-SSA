# COORD-SSA

## Coordinated Space Situational Awareness

COORD-SSA is a simulation-based decision-support prototype for evaluating collision-avoidance strategies in a multi-conjunction orbital environment.

The system is designed to demonstrate how different possible manoeuvres can be simulated, compared, and evaluated before a human operator selects a response.

> **COORD-SSA is a research and simulation prototype. It does not control real spacecraft or issue operational manoeuvre commands.**

---

## 1. Problem Statement

Earth orbit is becoming increasingly crowded with satellites, debris, and other tracked space objects. As the number of objects increases, satellites can experience multiple close approaches, known as conjunctions.

Existing Space Situational Awareness systems can detect and assess conjunction risks and support collision-avoidance operations. However, when several conjunctions interact, selecting a suitable response can become difficult because changing one satellite's trajectory may affect its future encounters with other objects.

For example:

```text
Satellite A ↔ Satellite B
       ↓
   Avoid B
       ↓
New trajectory of A
       ↓
Satellite A ↔ Satellite C
```

Therefore, the prototype focuses on evaluating possible responses and their downstream effects before a final decision is made.

---

## 2. Objective

The objective of COORD-SSA is to build a simulation-based decision-support workflow that can:

1. Analyse multiple conjunctions.
2. Generate hypothetical collision-avoidance strategies.
3. Simulate the effects of each strategy.
4. Check for secondary or downstream conjunctions.
5. Apply operational constraints.
6. Compare and rank feasible strategies.
7. Explain why a strategy is recommended.
8. Re-plan when important conditions change.
9. Keep a human operator in the decision loop.

---

## 3. Research Gap

COORD-SSA does **not** claim to replace existing Space Situational Awareness systems or to invent conjunction detection.

The prototype focuses on the decision-support layer surrounding a conjunction response.

The research direction is to provide an integrated workflow in which:

```text
Conjunction relationships
+
Operational constraints
+
What-if manoeuvre simulation
+
Secondary-risk checking
+
Strategy comparison
+
Explainable recommendation
+
Dynamic re-planning
```

are considered together in a single simulation workflow.

The prototype therefore investigates how candidate responses can be evaluated based on both their immediate and downstream effects.

---

## 4. Proposed Solution

COORD-SSA represents the orbital environment as a set of interacting objects and conjunctions.

For a detected conjunction, the system can evaluate multiple hypothetical strategies.

Example:

```text
A ↔ B   = primary conjunction

Strategy 1
    ↓
A avoids B
    ↓
A ↔ C appears
    ↓
Rejected

Strategy 2
    ↓
A avoids B
    ↓
No secondary conjunction
    ↓
Within constraints
    ↓
Recommended
```

The recommendation is intended to support a human operator rather than autonomously control a spacecraft.

---

## 5. Core Features

### 5.1 Multiple-Conjunction Analysis

The system can evaluate multiple object pairs rather than being restricted to a single A-B conjunction.

For example:

```text
A ↔ B
A ↔ C
B ↔ D
```

These relationships form the basis for evaluating interacting risks.

---

### 5.2 Mission and Manoeuvre Constraints

Candidate strategies can be evaluated using configurable prototype constraints such as:

* Maximum Δv
* Manoeuvre window
* Mission-sensitive time window
* Propulsion limitations
* Operator-defined restrictions

A manoeuvre that is mathematically possible may still be rejected if it violates configured constraints.

---

### 5.3 What-If Manoeuvre Simulation

The system generates hypothetical manoeuvre options and simulates the resulting trajectory.

The purpose is to answer:

> What happens if this manoeuvre is performed?

The manoeuvres used in the prototype are simulation inputs and are not spacecraft commands.

---

### 5.4 Secondary and Cascade Conjunction Checking

After a candidate manoeuvre is simulated, the new trajectory is propagated and checked against other objects.

This allows the system to detect cases such as:

```text
Before manoeuvre:

A ↔ B  ⚠️
A ↔ C  ✅

After manoeuvre:

A ↔ B  ✅
A ↔ C  ⚠️
```

A strategy that resolves the original conjunction but creates an unacceptable downstream risk can therefore be rejected.

---

### 5.5 Strategy Ranking

Candidate strategies are compared using configurable prototype criteria such as:

* Primary conjunction risk
* Secondary conjunction risk
* Δv requirement
* Mission impact
* Constraint violations

The final ranking is intended to be transparent and explainable.

---

### 5.6 Explainable Recommendation

Instead of only displaying a numerical score, the system provides reasons for its recommendation.

Example:

```text
Recommended Strategy: B

✓ Primary conjunction resolved
✓ No secondary conjunction detected
✓ Within Δv limit
✓ Mission window preserved
```

---

### 5.7 Dynamic Re-Planning

The prototype can simulate changes in conditions.

For example:

```text
Initial recommendation
        ↓
Propulsion constraint changes
        ↓
Previous strategy becomes infeasible
        ↓
System recalculates
        ↓
New strategy recommended
```

This demonstrates that a recommendation is dependent on the current scenario and constraints.

---

### 5.8 Data Freshness / Confidence

The prototype can display a simple indication of the freshness or confidence of the orbital input data.

This is intended to make the decision context visible to the operator.

---

## 6. Prototype Workflow

```text
Public / Simulated Orbital Data
             ↓
      Data Input Module
             ↓
      Orbit Propagation
             ↓
   Multiple Conjunction Analysis
             ↓
   Mission / Manoeuvre Constraints
             ↓
   Candidate Strategy Generation
             ↓
      What-If Simulation
             ↓
 Secondary / Cascade Risk Checking
             ↓
      Strategy Evaluation
             ↓
       Strategy Ranking
             ↓
 Explainable Recommendation
             ↓
       Human Approval
             ↓
     Condition Changes
             ↓
        Re-Planning
```

---

## 7. Architecture

```text
                    ┌─────────────────────────┐
                    │ Public / Simulated Data │
                    └────────────┬────────────┘
                                 ↓
                    ┌─────────────────────────┐
                    │   Person 1: Orbital     │
                    │   & Conjunction Engine  │
                    └────────────┬────────────┘
                                 ↓
                    ┌─────────────────────────┐
                    │ Person 2: Manoeuvre &    │
                    │ Decision Engine          │
                    └────────────┬────────────┘
                                 ↓
                    ┌─────────────────────────┐
                    │ Person 3: Dashboard &    │
                    │ Visualization            │
                    └────────────┬────────────┘
                                 ↓
                    ┌─────────────────────────┐
                    │ Human Operator Decision  │
                    └─────────────────────────┘
```

---

## 8. Team Responsibilities

### Person 1 — Orbital and Conjunction Module

Responsible for:

* Loading public orbital data
* TLE handling
* SGP4 propagation
* Satellite position and velocity calculation
* Distance calculation
* Closest approach calculation
* Pairwise conjunction screening
* Providing structured conjunction results to Person 2

Main directory:

```text
src/person1_orbit/
```

---

### Person 2 — Manoeuvre and Decision Module

Responsible for:

* Candidate manoeuvre generation
* Hypothetical manoeuvre simulation
* Constraint evaluation
* Secondary/cascade conjunction checking
* Strategy scoring
* Strategy ranking
* Explainable recommendation
* Dynamic re-planning

Main directory:

```text
src/person2_maneuver/
```

---

### Person 3 — Dashboard and Visualization Module

Responsible for:

* Streamlit dashboard
* Orbital/result visualization
* Conjunction alerts
* Candidate strategy display
* Comparison tables
* Recommendation display
* Scenario controls
* Final prototype demonstration interface

Main directory:

```text
src/person3_dashboard/
```

---

## 9. Project Structure

```text
COORD-SSA/
│
├── config/
│   └── settings.yaml
│
├── data/
│   ├── raw/
│   │   └── orbital_data/
│   ├── processed/
│   └── scenarios/
│
├── src/
│   ├── person1_orbit/
│   │   ├── __init__.py
│   │   ├── tle_loader.py
│   │   ├── propagator.py
│   │   ├── distance.py
│   │   └── conjunction_detector.py
│   │
│   ├── person2_maneuver/
│   │   ├── __init__.py
│   │   ├── maneuver_generator.py
│   │   ├── maneuver_simulator.py
│   │   ├── constraints.py
│   │   ├── cascade_checker.py
│   │   └── decision_engine.py
│   │
│   └── person3_dashboard/
│       ├── __init__.py
│       └── dashboard.py
│
├── tests/
│   ├── test_orbit.py
│   ├── test_conjunction.py
│   ├── test_maneuver.py
│   └── test_dashboard.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 10. Technology Stack

### Programming Language

* Python

### Orbital Mechanics

* SGP4

### Numerical Processing

* NumPy
* SciPy

### Data Handling

* Pandas

### Visualization

* Plotly

### User Interface

* Streamlit

### Configuration

* YAML

### Version Control

* Git
* GitHub

---

## 11. Data Sources

The prototype uses:

### Public orbital data

Publicly available orbital element data such as TLE or other supported orbital-element formats can be used for the simulation.

### Simulated scenarios

Controlled scenarios are created to demonstrate:

* Close approaches
* Multiple interacting conjunctions
* Candidate manoeuvres
* Secondary conjunctions
* Constraint conflicts
* Dynamic re-planning

The final demonstration does not require access to restricted operational SSA data.

---

## 12. Important Prototype Limitations

COORD-SSA is a **simulation and research prototype**.

It is not intended to:

* Control real spacecraft
* Issue real manoeuvre commands
* Replace operational SSA systems
* Claim operational collision-probability accuracy
* Represent official ISRO manoeuvre-planning criteria

Prototype values such as screening thresholds, scoring weights, manoeuvre limits, and scenario constraints are configurable assumptions for demonstration purposes.

---

## 13. Running the Project

### Clone the repository

```bash
git clone <repository-url>
cd COORD-SSA
```

### Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add orbital data

Place required public orbital-element files in:

```text
data/raw/orbital_data/
```

### Run tests

```bash
python -m tests.test_orbit
```

```bash
python -m tests.test_conjunction
```

Additional module-specific tests can be run as they are implemented.

### Run the prototype dashboard

```bash
streamlit run app.py
```

---

## 14. Development Workflow

The project uses separate Git branches for the three major modules.

```text
main
│
├── person1-orbit
├── person2-maneuver
└── person3-dashboard
```

Each team member works primarily within their assigned module and its tests.

Changes are reviewed and merged into `main` after testing.

---

## 15. Example Demonstration Scenario

A typical prototype demonstration can follow this sequence:

```text
1. Multiple conjunctions are loaded.

2. A primary conjunction is identified.

3. The system generates several hypothetical responses.

4. Strategy A resolves the primary conjunction
   but creates a secondary conjunction.

5. Strategy A is rejected.

6. Strategy B resolves the primary conjunction
   without creating an unacceptable secondary risk.

7. Strategy B satisfies the configured constraints.

8. Strategy B is recommended with an explanation.

9. One scenario condition is changed.

10. The previous strategy becomes infeasible.

11. COORD-SSA re-plans and produces a new recommendation.
```

---

## 16. Example Output

```text
CONJUNCTION ANALYSIS
--------------------

Object A: Satellite-A
Object B: Satellite-B

Closest Approach: 0.72 km
Status: CONJUNCTION CANDIDATE
```

Candidate strategies:

```text
Strategy A
Primary Risk: Resolved
Secondary Risk: HIGH
Δv: 0.20 m/s
Status: REJECTED
Reason: Creates secondary conjunction

Strategy B
Primary Risk: Resolved
Secondary Risk: LOW
Δv: 0.27 m/s
Mission Impact: LOW
Status: RECOMMENDED
```

---

## 17. Expected Prototype Demonstration

The final prototype should clearly demonstrate:

```text
Multiple conjunctions
        ↓
Candidate responses
        ↓
What-if simulation
        ↓
Downstream risk checking
        ↓
Constraint evaluation
        ↓
Strategy ranking
        ↓
Explainable recommendation
        ↓
Dynamic re-planning
```

The purpose is to demonstrate the **decision-support concept**, not operational spacecraft control.

---

## 18. Project Status

COORD-SSA is currently under development as a simulation-based prototype.

The development priority is:

1. Build and validate the orbital/conjunction engine.
2. Implement candidate manoeuvre simulation.
3. Add downstream/cascade checking.
4. Add operational constraints.
5. Implement strategy ranking and explanation.
6. Integrate dynamic re-planning.
7. Connect the dashboard.
8. Validate the complete demonstration scenario.

---

## 19. Disclaimer

This project is an academic/research prototype developed for demonstration purposes.

Results generated by the prototype should not be used for real spacecraft operations, collision-avoidance decisions, or mission-critical planning.

Operational spaceflight decisions require validated flight-dynamics data, operational software, mission-specific constraints, uncertainty modelling, and appropriate human/operator authorization.
