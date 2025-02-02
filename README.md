# README

Welcome to my experiments with Large Language Models (LLMs)!

## Projects

### 1. RAG Chatbot

A RAG chatbot which fetches the documentation of a GitHub repository and uses that information to answer a user's questions.

## Getting Started
1. Clone the repository:
    ```sh
    $ git clone https://github.com/anirudhs001/NLP.git
    ```
2. Get your github access token. Set it in the `GITHUB_ACCESS_TOKEN` env variable using:
    ```sh
    $ export GITHUB_ACCESS_TOKEN="<your token here>"
    ```

2. Install the required dependencies:
    ```sh
    $ pip install -r requirements.txt
    ```
3. run main.ipynb

## Sample Output

Here's a sample output of the RAG Chatbot:

```
User: How do I create a window using clay?

Chatbot: To create a window using `clay`, you first need to define `CLAY_IMPLEMENTATION` and include `clay.h` in your source file.
Then, you can use `clay.EndLayout` to specify the size of the window you want to create. Here's a step-by-step example of how to create a window with `clay`:

// Define CLAY_IMPLEMENTATION at the beginning of your source file
#define CLAY_IMPLEMENTATION
#include "clay.h"

// ... other code ...

int main() {
    // Set the dimensions for the window (width, height)
    int windowWidth = 800;
    int windowHeight = 600;

    // End the layout with the specified dimensions
    clay.EndLayout(windowWidth, windowHeight);

    // Process the resulting clay.RenderCommandArray in your choice of renderer
    Odin renderCommands: clay.RenderCommandArray() = clay.EndLayout(windowWidth, windowHeight);

    // Your rendering code here

    return 0;
}
```

## License

MIT.
