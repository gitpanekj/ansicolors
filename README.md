# ANSI Text Formatter

This repository contains Python, Ocaml, C/C++ libraries for text formatting
using ANSI escape sequences.
It supports basic color, 8-bit and RGB color models as well as various font effects.

## Overview and Usage

### Color models

#### Reset escape sequence

- `\033[m`

#### Basic colors

<table>
    <!-- header -->
    <tr>
        <td style="font-size: 20px; font-weight: bold">  Code </td>
        <td style="font-size: 20px; font-weight: bold">  Color </td>
        <td style="font-size: 20px; font-weight: bold">  Python / C </td>
        <td style="font-size: 20px; font-weight: bold">  Ocaml </td>
    </tr>
    <!-- foreground -->
    <tr>
        <td>\033[30m</td>
        <td style="color: rgb(  0,  0,  0)">  black   foreground  </td>
        <td><code>fg_black("text")</code></td>
        <td><code>fg_black "text"</code></td>
        </tr>
    <tr>
        <td>\033[31m</td>
        <td style="color: rgb(204,  0,  0)">  red     foreground  </td>
        <td><code>fg_red("text")</code></td>
        <td><code>fg_red "text"</code></td>
        </tr>
    <tr>
        <td>\033[32m</td>
        <td style="color: rgb(  0,204,  0)">  green   foreground  </td>
        <td><code>fg_green("text")</code></td>
        <td><code>fg_green "text"</code></td>
        </tr>
    <tr>
        <td>\033[33m</td>
        <td style="color: rgb(204,204,  0)">  yellow  foreground  </td>
        <td><code>fg_yellow("text")</code></td>
        <td><code>fg_yellow "text"</code></td>
        </tr>
    <tr>
        <td>\033[34m</td>
        <td style="color: rgb(  0,  0,204)">  blue    foreground  </td>
        <td><code>fg_blue("text")</code></td>
        <td><code>fg_blue "text"</code></td>
        </tr>
    <tr>
        <td>\033[35m</td>
        <td style="color: rgb(204,  0,204)">  magenta foreground  </td>
        <td><code>fg_magenta("text")</code></td>
        <td><code>fg_magenta "text"</code></td>
        </tr>
    <tr>
        <td>\033[36m</td>
        <td style="color: rgb(  0,204,204)">  cyan    foreground  </td>
        <td><code>fg_cyan("text")</code></td>
        <td><code>fg_cyan "text"</code></td>
        </tr>
    <tr>
        <td>\033[37m</td>
        <td style="color: rgb(255,255,255)">  white   foreground  </td>
        <td><code>fg_white("text")</code></td>
        <td><code>fg_white "text"</code></td>
        </tr>
    <!-- background -->
    <tr>
        <td>\033[40m</td>
        <td style="background-color:rgb(  0,  0,  0);color: rgb(255,255,255)">  black   background  </td>
        <td><code>bg_black("text")</code></td>
        <td><code>bg_black "text"</code></td>
    </tr>
    <tr>
        <td>\033[41m</td>
        <td style="background-color:rgb(204,  0,  0);color: rgb(  0,255,255)">  red     background  </td>
        <td><code>bg_red("text")</code></td>
        <td><code>bg_red "text"</code></td>
    </tr>
    <tr>
        <td>\033[42m</td>
        <td style="background-color:rgb(  0,204,  0);color: rgb(255,  0,255)">  green   background  </td>
        <td><code>bg_green("text")</code></td>
        <td><code>bg_green "text"</code></td>
    </tr>
    <tr>
        <td>\033[43m</td>
        <td style="background-color:rgb(204,204,  0);color: rgb(  0,  0,255)">  yellow  background  </td>
        <td><code>bg_yellow("text")</code></td>
        <td><code>bg_yellow "text"</code></td>
    </tr>
    <tr>
        <td>\033[44m</td>
        <td style="background-color:rgb(  0,  0,204);color: rgb(255,255,  0)">  blue    background  </td>
        <td><code>bg_blue("text")</code></td>
        <td><code>bg_blue "text"</code></td>
    </tr>
    <tr>
        <td>\033[45m</td>
        <td style="background-color:rgb(204,  0,204);color: rgb(  0,255,  0)">  magenta background  </td>
        <td><code>bg_magenta("text")</code></td>
        <td><code>bg_magenta "text"</code></td>
    </tr>
    <tr>
        <td>\033[46m</td>
        <td style="background-color:rgb(  0,204,204);color: rgb(255,  0,  0)">  cyan    background  </td>
        <td><code>bg_cyan("text")</code></td>
        <td><code>bg_cyan "text"</code></td>
    </tr>
    <tr>
        <td>\033[47m</td>
        <td style="background-color:rgb(255,255,255);color: rgb(  0,  0,  0)">  white   background  </td>
        <td><code>bg_white("text")</code></td>
        <td><code>bg_white "text"</code></td>
    </tr>
</table>

#### 8-bit color model

- **Base format**
  - **Foreground**: \033[38;5<color_code>m
  - **Background**: \033[48;5<color_code>m
- **Color codes**
  | Code range | Meaning | Python / C | Ocaml |
  |------------|------------------|-------|-------|
  | 0 - 15 | Basic colors | `(fg / bg)_basic_color(\<color>, "text")` | `(fg / bg)_basic_color \<color> "text"`
  | 16 - 231 | 6 x 6 x 6 RGB cube | `(fg / bg)_rgb6(<0-5>, <0-5>, <0-5>)` | `(fg / bg)_rgb6 <0-5> <0-5> <0-5>`
  | 232 - 255 | Gray scale | `(fg / bg)_gray_scale(<0-23>, "text")` | `(fg / bg)_gray_scale <0-23> "text"`

#### RGB color model

- **Base format**

  | FG / BF      |  Code            | Python / C                    | Ocaml                           |
  |--------------|------------------|-------------------------------------|---------------------------------|
  | Foreground   |  \033[38;r;g;b;m | `fg_rgb(<0-255>, <0-255>, <0-255>)` | `fg_rgb <0-255> <0-255> <0-255>`|
  | Background   |  \033[48;r;g;bm  | `bg_rgb(<0-255>, <0-255>, <0-255>)` | `bg_rgb <0-255> <0-255> <0-255>`| 



### Supported Font effect

<table>
     <tr>
        <td style="font-size: 20px; font-weight: bold">  ANSI CODE </td>
        <td style="font-size: 20px; font-weight: bold">  MEANING </td>
        <td style="font-size: 20px; font-weight: bold">  Python / C </td>
        <td style="font-size: 20px; font-weight: bold">  Ocaml </td>
    </tr>
    <tr>
        <td>0</td>
        <td>reset</td>
        <td><code>reset("text")</code></td>
        <td><code>reset "text"</code></td>
    </tr>
    <tr>
        <td>1</td>
        <td>bold</td>
        <td><code>bold("text")</code></td>
        <td><code>bold "text"</code></td>
    </tr>
    <tr>
        <td>2</td>
        <td>faint</td>
        <td><code>faint("text")</code></td>
        <td><code>faint "text"</code></td>
    </tr>
    <tr>
        <td>3</td>
        <td>italic</td>
        <td><code>italic("text")</code></td>
        <td><code>italic "text"</code></td>
    </tr>
    <tr>
        <td>4</td>
        <td>underline</td>
        <td><code>underline("text")</code></td>
        <td><code>underline "text"</code></td>
    </tr>
    <tr>
        <td>5</td>
        <td>slow blink</td>
        <td><code>slow_blink("text")</code></td>
        <td><code>slow_blink "text"</code></td>
    </tr>

</table>


### General formatter
<!-- #TODO -->
```python
fmt = ANSI_format(fg_color, bg_color, bold, faint, italic, underline, slow_blink);
formatted_text  = ansi_format(fmt);
```


### Combining formatters
<!-- #TODO -->
```python
fmt_text = bg_red(fg_blue("text"))
```

## Contact

For any questions or issues, please contact [panekjan.j@seznam.cz](mailto:panekjan.j@seznam.cz).
