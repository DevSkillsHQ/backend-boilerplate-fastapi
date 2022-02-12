# Backend Boilerplate FastAPI/Python

A backbone for your coding challenge.

## Contents

- [Backend service](app) - a FastAPI service with a `/ping` endpoint.
- [E2E test suites](cypress/integration) - a backend and a frontend Cypress test suites. Extend with your tests.
- [Pipeline](.github/workflows/tests.yml) - a test Runner that executes the Cypress tests on push to a branch other than `master`/`main`.

## Tech Stack

### Backend

- [FastAPI](https://fastapi.tiangolo.com)
- [databases](https://pypi.org/project/databases/)
- [SQLite](https://www.sqlite.org/index.html)

### Misc

- Cypress
- GitHub Actions

## Getting started

1. Make sure [`python3`](https://www.python.org/downloads/) and [`pip3`](https://pip.pypa.io/en/stable/installing/) are installed on your local env.

2. Make sure npm & node are configured on your local env. You can download those distributions for your platform [here](https://nodejs.org/en/download/)

3. Build your app.

```bash
npm install
npm run build
```

4. Start your app.

```bash
npm install
npm run start
```

5. Run the Cypress tests.

```bash
npm run test # run project tests under `cypress/integration`
```

---

Made by [DevSkills](https://devskills.co).

Did you find this repo useful? **Give us a shout on [Twitter](https://twitter.com/DevSkillsHQ) / [LinkedIn](https://www.linkedin.com/company/devskills)**.
