Sublime Move To Character
===

Move to character command, works just like the "f" command in vim.

It does not come with default key bindings. You can add it by:

```
  { "keys": ["ctrl+j", "<character>"], "command": "move_to_character" },
  { "keys": ["ctrl+shift+j", "<character>"], "command": "move_to_character", "args": {"extend": true} },
  ```

Inspired by [Sublime Text Vintage Mode](https://github.com/sublimehq/Vintage).


## Usage
Clone or download this repo to `~/Library/Application Support/Sublime Text 3/Packages`
