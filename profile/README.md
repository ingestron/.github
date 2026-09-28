<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ingestron/.github/main/profile/assets/hero-dark.png">
  <img src="https://raw.githubusercontent.com/ingestron/.github/main/profile/assets/hero-light.png" alt="Ingestron: build data pipelines from reviewed contracts. Open source, Apache-2.0." width="100%">
</picture>

<p align="center">
  <a href="https://ingestron.io"><b>Website</b></a>
  &nbsp;·&nbsp;
  <a href="https://docs.ingestron.io"><b>Documentation</b></a>
  &nbsp;·&nbsp;
  <a href="https://docs.ingestron.io/docs/tutorials/retail-files"><b>Tutorial</b></a>
  &nbsp;·&nbsp;
  <a href="https://ingestron.io/security"><b>Security</b></a>
</p>

## Get started

```sh
npm install --global ingestron
```

The [retail files tutorial](https://docs.ingestron.io/docs/tutorials/retail-files) takes you from public sample files to a reviewed run on your machine. Check the [system requirements](https://docs.ingestron.io/docs/start/installation) first.

## How it works

<img src="https://raw.githubusercontent.com/ingestron/.github/main/profile/assets/how-it-works.png" alt="A pipeline drawn as a technical drawing: a source connects to ingest, cleanse, model and present stages. Marker 1 is the connection at the source, marker 2 the contract check on every hand-off, marker 3 the standard on each stage." width="100%">

You describe where the data comes from, what it should look like and how each stage handles it. Ingestron checks those definitions and generates native code for your platform. Nothing runs until a person has reviewed and approved it.

## Repositories

| Repository | What it holds |
| :--- | :--- |
| [cli](https://github.com/ingestron/cli) | Command-line interface and MCP server for coding agents |
| [core](https://github.com/ingestron/core) | Compiler, project schemas and plugin interfaces |
| [connectors](https://github.com/ingestron/connectors) | Source connectors |
| [provider-local](https://github.com/ingestron/provider-local) | Runs flows on your machine, with a receipt for every run |
| [docs](https://github.com/ingestron/docs) | Documentation and tested examples |

Current versions and the list of installable plugins are in the [documentation](https://docs.ingestron.io/docs/guides/plugins).

## Open source

The compiler, CLI, plugin interfaces, connectors and local runner are Apache-2.0. The VS Code extension and Studio are in private preview. Maintained standard packs and team services are planned on top of the open foundation, not in place of it. [What is open and why](https://ingestron.io/open-source).

## Security

Report vulnerabilities privately to [security@ingestron.io](mailto:security@ingestron.io). Please do not include live secrets or customer data.

<sub>Ingestron is an independent, early-stage project in development preview, based in Auckland, New Zealand. Original code is licensed by Otrera Limited under Apache-2.0.</sub>
