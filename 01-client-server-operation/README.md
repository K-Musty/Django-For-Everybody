# World Simplest Server and Client

This repository contains basic examples of a Python web server and client (browser) that communicate over HTTP using the `socket` library.

## 01-world-simplest-browser

This is a **simple Python web browser** that connects to a web server and fetches a web page.

### Summary:
This script acts as a **basic web browser** that connects to a server, sends an HTTP request, and prints the response. It's a demonstration of how HTTP communication works at a very low level using Python's `socket` library.

---

## 02-world-simplest-server

This is a **basic Python HTTP server** that listens for incoming connections and sends a simple HTML response.

### Summary:
This is a **basic web server** that listens for incoming client requests, processes the request, and sends back a simple HTML page as the response. It demonstrates the basic building blocks of an HTTP server.

---

## 03-world-simplest-client.py

This is another **simple Python client** that connects to a local server, sends an HTTP GET request, and receives the response.

### Summary:
This script acts as a **basic HTTP client** that sends a GET request to the server for a file (`romeo.txt`), receives the response, and prints it. It demonstrates how to interact with a web server at a low level using Python's `socket` library.

---

These three scripts demonstrate the **client-server communication** in Python using **sockets**. The server listens for incoming connections, while the client sends requests and receives responses. It's a simple and fundamental way to understand how HTTP works behind the scenes.

