# OIDC Oauth2 authentication using Django and mozilla-django-oidc with Okta

> ## [Tutorial Link](https://dev.to/hesbon/oidc-oauth2-authentication-using-django-and-mozilla-django-oidc-with-okta-4jll)

> ## How to set up the project

### Features

- python 3.10
- [poetry](https://python-poetry.org/docs/) as dependency manager

---

### PROJECT SETUP

- clone the repository

```bash
git clone https://github.com/Hesbon5600/oidc-connect.git
```

- cd into the directory

```bash
cd oidc-connect
```

### create environment variables

  On Unix or MacOS, run:

```bash
cp .env.example .env
```

You can edit whatever values you like in there.

Note: There is no space next to '='

### On terminal

```bash
source .env
```

---

> > ### VIRTUAL ENVIRONMENT

---

**To Create:**

```bash
make env
```

---

**To Activate:**

```bash
source ./env/bin/activate
```

---

**Installing dependencies:**

```bash
make install
```

> > ### MIGRATIONS - DATABASE

---

#### Make migrations

```bash
make makemigrations
```

---

> > ### THE APPLICATION

---

#### run application

```bash
make run
```

---
