# Basic Markdown

The following Markdown is commonly found in other places that provide Markdown support.

<h2 id="table-of-contents">Table of Contents<a class="headerlink" href="#table-of-contents" title="Permanent Link">¶</a></h2>

[TOC]

----
## Basics

### Headers

Using between 1 and 3 Hashtags (`#`) followed by a space and any text creates a H1, H2 or H3 header based on the number of Hashtags used.

/// example
//// tab | Markdown
```
# H1
## H2
### H3
```
////

//// tab | Result
<h1>H1</h1>
<h2>H2</h2>
<h3>H3</h3>
////
///

### Bold Text

Surrounding text with two asterisk symbols (`**`) will render it bold.

/// example
//// tab | Markdown
```
**Bold Text**
```
////

//// tab | Result
**Bold Text**
////
///

### Italic Text

Surrounding text with one asterisk symbol (`*`) will render it italic (tilted).

/// example
//// tab | Markdown
```
*Italic Text*
```
////

//// tab | Result
*Italic Text*
////
///

### Underline Text

/// warning | This markdown feature may not be available in all markdown variants, or with a different syntax.
///

Surrounding text with 2 underscores (`__`) will render it underlined.

/// example
//// tab | Markdown
```
__Underline Text__
```
////

//// tab | Result
<u>Underline Text</u>
////
///

### Strikethrough Text

/// warning | This markdown feature may not be available in all markdown variants, or with a different syntax.
///

Surrounding text with 2 tildas (`~~`) will render it as strikethrough.

/// example
//// tab | Markdown
```
~~Strikethrough Text~~
```
////

//// tab | Result
~~Strikethrough Text~~
////
///

----
## Code

### Inline Code

Surrounding text with a back tick (`` ` ``) will render it as inline code, with a monospaced font and different background.

/// example
//// tab | Markdown
```
`Inline Code`
```
////

//// tab | Result
`Inline Code`
////
///

### Code Blocks

Starting a line with 3 back ticks (```` ``` ````), followed by text on a new line and another 3 back ticks on another line will render the text in-between as a code block with a monospaced font and different background.

/// example
//// tab | Markdown
````
```
Code Block
```
````
////

//// tab | Result
```
Code Block
```
////
///

/// tip
Discord supports Syntax highlighting using GitHub's Syntax highlighting theme.  
To use Syntax highlighting, add the name of the coding language (i.e. markdown) after the first 3 back ticks. They need to be on the same line!

//// warning | Syntax highlighting is only fully supported on browser/Desktop with mobile having limited support.
////
///

----
## Links

### Normal Links

Pasting any link in Discord makes them clickable.  
Additionally will Discord display an embed containing Information based on the site's Open Graph and/or Twitter Card Metadata, including Thumbnails, Images and Videos [with some special exceptions](#special-links-behaviour).

Display of such an embed can be supressed by wrapping the link in chevrons (`<>`). This also works for [embedded links](#embedded-links).  
Embeds may also not be shown, if the user who posted the link does not have `Embed Links` permissions on the server.

/// example
//// tab | Markdown
```
https://google.com
```
////

//// tab | Result
https://google.com{ target="_blank" rel="nofollow" }
////
///

### Embedded Links

Embedded Links (Text that can be clicked to open a link) can be made using the below listed format.

/// example
//// tab | Markdown
```
[This links to Google](https://google.com)
```
////

//// tab | Result
[This links to Google](https://google.com){ target="_blank" rel="nofollow" }
////
///

/// tip
You can add a title to the link that is shown when hovering over it. Just add the text to display in double quotes after the link, but before the closing bracket.

**Example:** `[Totally not google](https://google.com "Trust me. It's Google!")` -> [Totally not google](https://google.com "Trust me. It's not Google!")

Note that Discord will still include the URL in the hover to combat scams and fraud.
///

### Special Links behaviour

Discord renders certain links differently in the client.  
The following unique behaviours are displayed:

- Links to Channels, threads and messages display as [Mentions](discord-markdown.md#mentions) in the following formats:
    - Channels (Same Server): {{ mention() }}
    - Channels (Different Server): {{ mention(has_server = True) }}
    - Message (Same Server): {{ mention(is_message = True) }}
    - Message (Different Server): {{ mention(is_message = True, has_server = True) }}
    - Threads, News Channels, Voice Channels and Stage channels have the same behaviour, but display their respective icons instead of the Hashtag.
- Links to Music and Playlists on Spotify will render a custom embed that allows you to listen to a snippet of the song or playlist.