# Checkmk extension for Aare Guru

![build](https://github.com/ellr/checkmk_aare_guru/workflows/build/badge.svg)
![flake8](https://github.com/ellr/checkmk_aare_guru/workflows/Lint/badge.svg)
![pytest](https://github.com/ellr/checkmk_aare_guru/workflows/pytest/badge.svg)

## Description

CheckMK 2.0 compatible custom plugin to monitor the API of the Aare Guru Website.
It was created for training purposes. And to see on which days one needs to get the bath shorts ready of course.


## Authors

- Roger Ellenberger <roger.ellenberger@wagner.ch> migrated the plugin to CheckMK 2.0


## Development

For Developing this plugin, the excellent [boilerplate](https://github.com/jiuka/checkmk_template) by [jjuka](https://github.com/jiuka) was used.

For the best development experience use [VSCode](https://code.visualstudio.com/) with the [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension. This maps your workspace into a checkmk docker container giving you access to the python environment and libraries the installed extension has.

Directories are mapped into the Checkmk site using symlinks.


### Continuous integration - GitHub Actions

There is GitHub workflows to test, lint and build in this repository.
