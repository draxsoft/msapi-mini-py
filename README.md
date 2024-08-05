# Macsploit Python Mini API

## Overview

Macsploit's Python Mini API is an open-source API designed for interacting with Roblox exploits. It enables developers to send custom scripts to a local server, simplifying the creation and management of custom user interfaces for Roblox exploits.

## Features

- **Send Scripts**: Send custom Roblox scripts to a local server.
- **Timeout Handling**: Includes timeout management for reliable execution.
- **Default Port**: Uses port 5553 by default.

## Installation

1. Ensure you have Python installed.
2. Clone the repository or save the script file locally.

## Usage

1. **Define Your Script**: Update the `script` variable with your desired Roblox script.

```python
script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/EdgeIY/infiniteyield/master/source"))()'
```
