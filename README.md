# Yard: A Tool for Building Linux Projects

## Introduction
Yard is a tool inspired by Yarn, tailored specifically for building Linux projects in C/C++, Python, JavaScript, and GTK environments. It seamlessly manages workspaces, packages, and builds for diverse language and build system combinations.

## Purpose
Yard serves as a comprehensive platform for building and managing Linux projects. It simplifies the process of creating workspaces, managing packages, and building programs in various languages, including C/C++, Python, and JavaScript. By supporting various build systems, such as Meson, Yard facilitates the creation of packages compatible with popular formats like deb and rpm.

## Origins
Yard's initial focus lies in facilitating the development of packages for Linux Mint. It aims to provide a comfortable and user-friendly environment akin to Yarn, making it easier to build and manage Linux projects. Once this primary goal is accomplished, the development of Yard 2 will commence, incorporating support for the Gnome technology stack.

## Features
* **Workspace Management:** Efficiently organize and manage workspaces for multiple projects.
* **Package Management:** Seamlessly install, update, and remove packages for your projects.
* **Language Support:** Build and manage programs written in C/C++, Python, and JavaScript.
* **Build System Compatibility:** Leverage various build systems, including Meson, for efficient package creation.
* **Popular Package Types:** Generate packages in popular formats like deb and rpm for seamless distribution.

## Usage
Yard's usage can be summarized in the following steps:

1. Install Yard using the provided installation command.
2. Create a Yard workspace for your project.
3. Add your project's source code and package dependencies to the workspace.
4. Use Yard commands to manage your project's packages, builds, and dependencies.

## Installation

To install Yard, execute the following command in a terminal:

```bash
sudo python3 setup.py install
```