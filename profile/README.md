<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ingestron/.github/main/profile/assets/hero-dark.png">
  <img src="https://raw.githubusercontent.com/ingestron/.github/main/profile/assets/hero-light.png" alt="Ingestron: build data pipelines from reviewed contracts. Open source, Apache-2.0." width="100%">
</picture>

<p align="center">
  <a href="https://docs.ingestron.io"><b>Documentation</b></a>
  &nbsp;·&nbsp;
  <a href="https://docs.ingestron.io/docs/start/first-project"><b>First project</b></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/ingestron/ingestron"><b>Source</b></a>
  &nbsp;·&nbsp;
  <a href="https://www.npmjs.com/package/ingestron"><b>npm</b></a>
</p>

## Get started

You need Node.js 22.13 or later.

```sh
npx ingestron init demo --template minimal --yes
cd demo
npx ingestron plan
```

[Generate your first project](https://docs.ingestron.io/docs/start/first-project) walks through it, and [Install a tool](https://docs.ingestron.io/docs/start/install) covers a global install and the VS Code extension.

## What it does

You declare data ingestion in YAML definitions: connections, data contracts, flows and transforms. Your organisation's standard chooses the methods and fixes the policy. Ingestron generates the files your own platform runs, such as Databricks Asset Bundles, Lakeflow pipelines and Azure Data Factory copies, for review in a pull request.

It runs on your machine, never connects to your sources or your cloud, and never overwrites a file someone edited by hand. In CI, `ingestron check` fails when the generated files are out of date.

## Repositories

| Repository | What it holds |
| :--- | :--- |
| [ingestron](https://github.com/ingestron/ingestron) | The CLI, the VS Code extension, the Databricks and Azure Data Factory packs, and the documentation |

## Open source

Ingestron is licensed under Apache-2.0. Services for enterprise platform teams are planned on top of the open core, not in place of it.

## Contact

Questions and feedback: [hello@ingestron.io](mailto:hello@ingestron.io). Report vulnerabilities privately to [security@ingestron.io](mailto:security@ingestron.io); please do not include live secrets or customer data.

<sub>Ingestron is an independent, early-stage project made by IntentLabs in Auckland, New Zealand. Original code is licensed by Otrera Limited, trading as IntentLabs, under Apache-2.0.</sub>
