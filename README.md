# 🐘 - square-pgadmin4

**square-pgadmin4** is a project made with a focus on making it possible to host a [pgAdmin4 website](https://pgadmin.org/) on the [Square Cloud](https://squarecloud.app/) hosting platform

With this project, you will be able to host a fully functional and accessible pgAdmin4 website anywhere at a cost of just $2.00/month!

## How to install

- ⚠ Firstly, you will need to have an active plan on Square Cloud, you can purchase it [here](https://squarecloud.app/pt-BR/plans)
- Clone the repository with `git clone https://github.com/josejooj/square-pgadmin4`
- Create a `.env` file
  - Add `PGADMIN_SETUP_EMAIL=<YOUR_EMAIL>` on your `.env` file
  - Add `PGADMIN_SETUP_PASSWORD=<YOUR_PASSWORD>` on your `.env` file
- Open the `squarecloud.app` file
  - Edit the line `SUBDOMAIN=pgadmin-nocache-<RANDOM_TEXT_HERE_WITH_MAX_46_CHARACTERS>`
  - Example: `SUBDOMAIN=pgadmin-nocache-fc051a0bb46d438bae5157464ec6c1c8`
