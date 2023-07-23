---
title: Render vs. Preview
---

Making quarto websites involves terminology that might be unfamiliar. This is a light explainer to help you get going.

As you work locally, you will save your files as you normally do. Saving writes your work to disk.

## Render

Rendering is when Quarto formats your document into something different (e.g. .html or .docx).

## Preview

Preview is when Quarto displays the rendered files. It's like saying "show me".

## When do I want Render vs Preview?

From the RStudio IDE, the "Render" button does both Render + Preview together.

From Jupyter, you'll need to do these in two steps, render to make the formatted document, and preview to view it.

From GitHub.com, Quarto will only be able to render when published (through a GitHub Action). This means you cannot preview before publishing online.
