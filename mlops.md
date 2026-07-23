## Evolution of Requirements in Software Development

- **Initial Phase**  
  Companies built software for themselves, with clear and stable requirements.

- **Customer-Centric Phase**  
  Companies started building for customers who did not know requirements well.  
  - Requirements began evolving.  
  - Software had to adapt continuously.

- **Agile Emergence**  
  Agile methodology was introduced to handle evolving requirements.  
  - **Develop smaller chunks**  
  - **Take feedback and improve**
  - **Deploy**

  ## True Agile

True Agile is when the story is deployed within **2 weeks**:

- **Develop**
- **Push to Git**
- **Code Review (CX)**
- **Deploy**

Some steps
- Integration - **roadblocks**
- Quality Gates - testing, reviews, checklists
- Automated deployment
- Dependencies, version mismatch
- Supports
- Build time
- Monitoring deployment

Some tools
- git: version management
- docker: version mismatch

Continous testing
- Development happens across sprints e.g. 20 requirements across 5 sprints
- testing accumulates every sprint i.e. 20, 40, 60,...
- Automated testing is therefore mandatory because the time for testing in every sprint remains same.
- Automated regression testing is typically to be build by **Dev team** and not by QA team

# Agility vs Stability
- **Dev team** targets Agility: deploy as early as possible; fail fast
- **Ops team** targets Stability: avoid defects, complaints from customer

# CI/CD is a culture
- Continuous Integration
- Continuous Deployment
- This is in total: Dev+Ops
- DevOps is not a team, but its a **culture**

# Jenkins and GH Actions

# Software Development vs ML development
| Features          | Software      | ML
|-------------------|---------------|-------------------------------
| Source            | source code   | code + data (parameters)
| source control    | GitHub        | Data version control (DVC)

* KPI of a Generative AI application is **Usability**
* Developer's focus could be **Accuracy**
* Product Owner's KPI would be **Usability**
* Funder's KPI would be the **Impact**

# workflow
- dataset selection: kaggle.com
- feature engineering and model training
- creation of pickle file, load and predict from pickle file
- version the source code
- use DVC and version the data and pickle file
- creation of end point

