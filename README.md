# StickyNotes-MCP

A simple Python-based MCP (Model Context Protocol) server project – Sticky Notes – that demonstrates the creation of custom tools, resources, and prompts for integration with AI assistants like the Claude Desktop App.

![MCP Logo](https://placeholder.com/wp-content/uploads/2018/10/placeholder.com-logo1.png)

## Overview

Large Language Models (LLMs) such as Claude and GPT-4 are excellent at generating text but struggle when they need to interact with external data or perform real-world actions. The **Model Context Protocol (MCP)** addresses this by defining a standard, modular way for LLM applications to communicate with external tools, data sources, and services. MCP follows a client-host-server pattern and uses stateful, JSON-RPC–based messages to ensure that only the necessary context is exchanged—improving scalability, security, and flexibility.

This project is a starter implementation of an MCP server using the official Python SDK. It is designed as a proof-of-concept that shows how to create and expose simple functionality – in this case, managing sticky notes – which can later be connected to MCP clients (like Claude Desktop).

## About Model Context Protocol (MCP)

MCP is an emerging open standard introduced by Anthropic to streamline the way LLMs interact with external tools and data. Its main advantages include:

# Unified Integration:

Reduces the need for custom integrations by standardizing how applications call external services.

# Modularity & Scalability:

Allows developers to build once and use across many applications – creating a vast ecosystem of plug-and-play components.

# Stateful Sessions & Context Management:

Supports multi-turn dialogues, preserving context over multiple interactions.

# Enhanced Security:

Ensures that each tool receives only the necessary context, protecting sensitive data with sandboxing and capability negotiation.

By leveraging MCP, AI applications can dynamically extend their capabilities, whether it’s to retrieve the latest customer data or to execute specific actions like managing sticky notes.

## Features

- **Tool: `add_note(message: str) -> str`**  
  Appends a new note to a local file (`notes.txt`) and returns a confirmation message.

- **Tool: `read_notes() -> str`**  
  Reads all notes from the sticky note file and returns them as a concatenated string. If no notes are present, it returns a default message.

- **Resource: `get_latest_note() -> str`**  
  Retrieves and returns only the latest note from the file.

- **Prompt: `note_summary_prompt() -> str`**  
  Generates a prompt for the AI to summarize all the current notes.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for improvements. Please ensure that your code follows the established patterns of MCP integration.
