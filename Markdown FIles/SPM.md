# Software Project Management – Course Notes

## Table of Contents

- [Lecture 2: Project Management Phases](#lecture-2-project-management-phases)
  - [1. Initiation Phase](#1-initiation-phase)
  - [2. Planning Phase](#2-planning-phase)
  - [3. Execution Phase](#3-execution-phase)
  - [4. Monitoring Phase](#4-monitoring-phase)
  - [5. Closing Phase](#5-closing-phase)
- [Role of a Project Manager](#role-of-a-project-manager)
- [Lecture 3: Software Development Life Cycle (SDLC)](#lecture-3-software-development-life-cycle-sdlc)
  - [Waterfall Model](#waterfall-model)
  - [Agile Model](#agile-model)
  - [Scrum Framework](#scrum-framework)
  - [Iterative Model](#iterative-model)
- [Choosing the Best SDLC Model](#choosing-the-best-sdlc-model)
- [Project Integration Management](#project-integration-management)

---

## Lecture 2: Project Management Phases

A software project typically goes through **five key phases**. Each phase has a defined objective, set of activities, and deliverables.

### 1. Initiation Phase

**Objective:** Problem identification, defining functional & non-functional requirements, and establishing the project scope.

- **Key Activity:** Create a **Project Charter** — a document that formally authorizes the project.
- **Project Charter Components:**
  - Project objectives
  - Scope
  - Stakeholders
  - Authorities
- **Stakeholder Identification** is performed at this stage.

---

### 2. Planning Phase

**Objective:** Define the total scope and refine the course of action for the project.

| Activities | Deliverables |
|:--|:--|
| Develop Project Management Plan | Project Plan |
| Define Scope, Schedule & Budget | Work Breakdown Structure (WBS) |
| Risk Management Planning | Gantt Charts |
| Resource Planning | Risk Register |
| Communication Planning | Project Charter |

> The planning phase lays the foundation for successful execution by creating a roadmap that the team follows.

---

### 3. Execution Phase

**Objective:** Complete the work while meeting project objectives.

| Activities | Deliverables |
|:--|:--|
| Task & Resource Allocation | Deliverables as per project plan |
| Team Development & Leadership | Performance Reports |
| Quality Assurance | |
| Communication with Stakeholders | |

---

### 4. Monitoring Phase

**Objective:** Track, review, and regulate project progress and performance.

| Activities |
|:--|
| Performance Measurement |
| Risk Monitoring |
| Quality Control |

> Monitoring runs **in parallel** with execution — it is not a sequential step. The project manager continuously compares actual progress against the plan.

---

### 5. Closing Phase

**Objective:** Finalize all project activities and formally close the project.

| Activities |
|:--|
| Deliver the Final Product |
| Obtain Stakeholder Acceptance |
| Conduct Post-Implementation Review |
| Document Lessons Learned |
| Release / Re-gather Resources |

---

## Role of a Project Manager

The **Project Manager (PM)** is responsible for planning, executing, and closing projects successfully. Their responsibilities include:

### Key Responsibilities

| Area | Description |
|:--|:--|
| **Project Planning** | Defining and planning the project scope, timeline, and resources |
| **Communication** | Bridging the gap between clients and developers (and vice versa) |
| **Team Leadership** | Leading with quality and fairness — no favoritism |
| **Stakeholder Communication** | Keeping stakeholders informed and aligned |
| **Risk Management** | Identifying and mitigating potential risks |
| **Quality Assurance** | Ensuring deliverables meet quality standards |
| **Budget Management** | Keeping the project within financial constraints |
| **Change Management** | Handling scope changes and their impact |

### Essential Skills

1. **Technical Knowledge** – Understanding of the technology stack
2. **Leadership** – Ability to guide and motivate teams
3. **Communication** – Clear, effective information exchange
4. **Problem-Solving** – Analytical thinking to resolve blockers
5. **Time Management** – Prioritizing tasks and meeting deadlines
6. **Negotiation** – Balancing competing interests and expectations

---

### Discussion Questions

1. How does project management in software development differ from other industries?
2. Can you think of a project where poor project management led to its failure? What could have been done differently?
3. How do different project management methodologies impact the role of a project manager?

---

## Lecture 3: Software Development Life Cycle (SDLC)

### What is SDLC?

The **Software Development Life Cycle (SDLC)** is a structured process used for developing information systems. It:

- Provides a **systematic approach** to software development
- Enhances **quality** and **manageability**
- Enables **clear communication** with stakeholders

---

### Waterfall Model

> **Definition:** A **linear and sequential** approach where each phase must be completed before the next begins.

#### Phases

```
Requirements → System Design → Implementation → Integration & Testing → Deployment → Maintenance
```

| Advantages | Disadvantages |
|:--|:--|
| Simple and easy to understand | Inflexible to change |
| Well-documented with clear tracking | Late detection of defects can be costly |
| Works well with well-defined requirements | Not ideal for complex or long-term projects |

**Best Used When:** Requirements are stable and unlikely to change (e.g., construction, manufacturing).

---

### Agile Model

> **Definition:** An **iterative and incremental** approach focused on adaptability and collaboration.

#### The Four Key Principles of Agile

| Principle | Explanation |
|:--|:--|
| **Individuals & Interactions** over processes and tools | Better communication leads to better performance |
| **Working Software** over comprehensive documentation | Prioritize deliverables over paperwork |
| **Customer Collaboration** over contract negotiation | Ongoing collaboration with customers throughout the project |
| **Responding to Change** over following a plan | Flexibility to adjust phases and meet evolving objectives |

---

### Scrum Framework

> **Definition:** An Agile framework that organizes work into time-boxed iterations called **Sprints**.

#### Roles

| Role | Responsibility |
|:--|:--|
| **Scrum Master** | Facilitates the process, removes impediments |
| **Product Owner** | Defines the product backlog and priorities |
| **Development Team** | Builds the product increment |

#### Scrum Ceremonies (Events)

| Ceremony | Purpose |
|:--|:--|
| **Sprint** | A time-boxed iteration (typically 2–4 weeks) |
| **Sprint Planning** | Plan the work for the upcoming sprint |
| **Daily Standups** | Short daily sync meetings (~15 min) |
| **Sprint Review** | Demo completed work to stakeholders |
| **Sprint Retrospective** | Reflect on what went well and what to improve |

#### Artifacts

- **Product Backlog** – The full list of features/work items
- **Sprint Backlog** – Items selected for the current sprint

| Advantages | Disadvantages |
|:--|:--|
| Highly flexible and adaptable | Requires experienced team members |
| Customer satisfaction through frequent delivery | Budget and timeline can be unpredictable |
| | Less emphasis on documentation |

**Best Used When:** Requirements are evolving — startups and innovative projects.

---

### Iterative Model

> **Definition:** Development is done in **repeated cycles (iterations)**, delivering the system in smaller portions at a time.

#### Phases (per Iteration)

```
Planning → Design → Implementation → Testing → Evaluation
```

| Advantages | Disadvantages |
|:--|:--|
| Incremental improvements over time | Costs and time increase if iterations aren't managed well |
| Early detection of issues | Requires strong project management skills |
| Flexibility to incorporate changes in each iteration | |

**Best Used When:** Large and complex projects where iterative refinement is needed.

---

## Choosing the Best SDLC Model

The right model depends on several factors:

| Factor | Consideration |
|:--|:--|
| **Requirements Stability** | Stable → Waterfall/Iterative · Evolving → Agile |
| **Project Size & Complexity** | Large/Complex → Iterative · Small/Medium → Agile or Waterfall |
| **Customer Involvement** | High → Agile · Low → Waterfall |
| **Risk Level** | High risk needing flexibility → Agile/Iterative · Low risk → Waterfall |
| **Team Expertise** | Skilled Agile teams → Agile · Limited resources → Waterfall/Iterative |
| **Time & Budget** | Constrained → Waterfall · Flexible → Agile |

### Decision-Making Framework

```
Is the requirement stable?
├── Yes → Waterfall or Iterative
└── No  → Agile

Is the project large and complex?
├── Yes → Iterative
└── No  → Agile or Waterfall

Is customer involvement high?
├── Yes → Agile
└── No  → Waterfall

Is the risk level high?
├── Yes → Agile or Iterative
└── No  → Waterfall
```

---

## Project Integration Management

> Every element of a project/product must coordinate with each other for successful delivery.

### Project Charter

A **Project Charter** is a document that **formally authorizes** a project.

#### Components

| Component | Description |
|:--|:--|
| **Project Purpose** | Why the project exists |
| **Measurables** | Success criteria and KPIs |
| **High-Level Requirements** | What the project must deliver |
| **Assumptions & Constraints** | Conditions assumed true and limitations |
| **High-Level Risks** | Major risks identified early |
| **Summary Milestone Schedule** | Key dates and milestones |
| **Assigned Project Manager** | PM name and authority level |
| **Stakeholders List** | All parties with interest in the project |

#### Process Structure

```
Inputs → Tools & Techniques → Outputs
```

> Project Integration Management ensures that all project components are properly coordinated, from initiation through closing.

---

*These notes cover Software Project Management topics from Semester 7 — project phases, the PM role, SDLC models (Waterfall, Agile, Scrum, Iterative), model selection criteria, and project integration management.*
