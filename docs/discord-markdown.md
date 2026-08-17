# Discord Markdown

Discord contains some unique markdown syntaxes that aren't found in your common Markdown parsers.

<h2 id="table-of-contents">Table of Contents<a class="headerlink" href="#table-of-contents" title="Permanent Link">¶</a></h2>

[TOC]

----
## Mentions

Discord has various mentionable objects that a user can use using different formats.

### Basic structure

Despite using different formats in the client, the actual raw syntax used for a mention remains the same across all objects:

```
<#123456789>
 |    |
 |    |- Unique ID of the object
 |
 |- Characters to identify type
```

The client automatically converts the used mention format (i.e. `#channel`) into a raw mention object, if the user has permissions to mention the given object.

Below is a table of the things a User can mention, their raw syntax and their appearance.

| Type    | Raw format      | Appearance                         | Notes                                                                                                                      |
|---------|-----------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| User    | `<@123456789>`  | <span class="mention">@User</span> | Raw format may contain a `!` after the at-symbol.<br>This is a legacy feature.                                             |
| Role    | `<@&123456789>` | <span class="mention">@Role</span> | Mention appears in the color of the role.<br>If the user has no permission to mention the role, will it not mention users. |
| Channel | `<#123456789>`  | {{ mention() }}                    |                                                                                                                            |

### User

Starting with an at-symbol, followed by the User's unique username, one can create a mention that will notify the user, unless one of the following is the case:

- The user is not on the server, if mentioned on one
- The user is not in the group DM or DM, if mentioned in one.
- The user has "Do not Disturb" set as status, which disables notifications and sounds.
- `@silent` was put at the start of the message, which acts as if all mentioned users had "Do not Disturb" set.

/// example
//// tab | Markdown
```
@user
```
////

//// tab | Result
<span class="mention">@User</span>
////
///

### Role

A role is mentioned the same way as a [User](#user) by starting with an at-symbol (`@`) followed by the Role name.  
Roles can only be mentioned if either the user has the permission to mention all roles, or the role has set to be mentionable by everyone. The client also only suggests roles based on these criterias.

A user can mention any role by using the [Raw format](#basic-structure) for a role. However, the role will only mention users if the above mentioned requirement is true. The mention still renders properly tho.

This is the only mention type that actually changes its color based on the color of the role that got mentioned.

/// example
//// tab | Markdown
```
@role
```
////

//// tab | Result
<span class="mention">@Role</span>
////
///

### Channel

Starting with a Hashtag (`#`) followed by a channel name allows a user to mention a channel. Any text-based channel (News, Thread, Forum, Forum Post) can be mentioned using this method.  
Appending an exclamation mark (`!`) after the Hashtag allows you to mention Voice Channels, but also special channels such as the Server-instrcutions, Server customization and similar.

/// example
//// tab | Markdown
```
#channel
```
////

//// tab | Result
{{ mention() }}
////
///

----
## Custom Emojis

Discord allows custom emojis to be displayed on the server.  
The format used in the client to use is the same as unicode emojis, no matter if animated or not.

The actual syntax used by Discord for custom emojis is different depending on the type of Emoji:

|Emoji type | Raw syntax           |
|-----------|----------------------|
| Static    | `<:name:123456789>`  |
| Animated  | `<a:name:123456789>` |

The name can be any and is only used by the client to display in the hover, if the emoji is from a server the client doesn't share.

----
## Timestamps

A unique feature in Discord is sharing timestamps, which automatically display in the user's language and with the date and time converted to their timezone.  
This means that a time of UTC 00:00 shows as 00:00 for users with UTC+0 while it shows as 01:00 for users with UTC+1.

The client allows creating a timestamp by writing `@time` and selecting the non-user option in the suggestions. You can then fill in a date and time to have it be converted to a timestamp on send.  
There's no known syntax used for the `@time` feature.

The raw format of the timestamp is as follows:

```
<t:123456789:r>
 |     |     |- Optional style definition
 |     |
 |     |- Unix Timestamp in seconds (not milliseconds)
 |
 |- Always t to identify the timestamp format
```

### Unix timestamp

The number used after the `<t:` is the unix timestamp (Seconds since January 1st, 1970) and can easily be obtained through various online tools.

### Variants

An optional colon (`:`) followed by a case-sensitive character can be used to have the timestamp appear in different formats:

| Character | Description                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------|
| `t`       | Displays hour and minute as `hh:mm`.                                                                   |
| `T`       | Displays hour, minute and seconds as `hh:mm:ss`.                                                       |
| `d`       | Displays the day, month and year all in numbers.                                                       |
| `D`       | Displays the day, month and year with the month using its localized name.                              |
| `f`       | Displays the date (same as `D`) with time (Same as `t`). This is the default if no variant is defined. |
| `F`       | Displays the date and time (Same as `f`) with the localized weekday added.                             |
| `R`       | Displays a relative timestamp (i.e. `in 1 hour`). Will update itself automatically.                    |

/// warning | Important
How the date appears depends on a user's own system settings.  
As an example, the 1st of december 2025 can appear as `12/01/2025` for one user while appearing as `01.12.2025` for another
///

----
## Text

### Spoiler

Surrounding text with two vertical lines (`||`) creates a Spoiler, where the text is covered by a bar and only shown once clicked.  
Embeds created by spoilered links will also be spoilered, by having the embed blurred and a "SPOILER" text shown.

/// tip
- You can mark images as spoiler when uploading by either clicking the spoiler (eye) icon on the attached image, or edit its filename to start with `SPOILER_`.
- You can change in your preferences whether spoilers should be covered by default, shown if moderating a server or always visible.
///

/// example
//// tab | Markdown
```
||This is some super secret text!||
```
////

//// tab | Result
<span class="spoiler">This is some super secret text!</span>
////
///

### Subtext

Subtext (aka subtitle) can be created by starting a line with a dash, followed by a hashtag (`-#`), space and text.  
It creates text that is smaller and slightly darker than the default text.

/// example
//// tab | Markdown
```
This is normal text

-# This text is so tiny!
```
////

//// tab | Result
This is normal text

<small>This text is so tiny!</small>
////
///