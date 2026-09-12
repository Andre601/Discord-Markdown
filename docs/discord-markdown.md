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

#### Notifications

Mentioning a User or Role in a message will send a Push Notification for the mentioned Users, or for every user having the mentioned role assigned.  
This is not the case for the following cases:

- The mentioned user is not on the server/in the DM they were mentioned in.
- The User has "Do not Disturb" or "Invisible" status set. They still have a mention indicator shown in the app but will not receive a Push Notification.
- The User mentioning the Role doesn't have the `Mention @everyone, @here, and All Roles` permission.
- The role mentioned does not have the `Allow anyone to @mention this role` setting enabled.
- The message is silenced [[More Info](#silent)].

### `@everyone` and `@here`

Writing `@everyone` or `@here` in chat will create a mention that will mention every user on the server, or only users currently online on the server respectively.

/// tip | Funfact
`@everyone` is also a role every user has and shares the same ID as the Server.  
This makes it the only object in Discord that doesn't have a unique snowflake ID.
///

/// example
//// tab | markdown
```
This message mentions @everyone and @here
```
////

//// tab | Result
{{ message('This message mentions <span class="mention">@everyone</span> and <span class="mention">@here</span>', true) }}
////
///

### `@silent`

Starting a message with `@silent` will have any mentions in it be surpresed for everyone that would usually receive a Push Notification. The `@silent` tag will also be removed from the actual message.  
This is effectively the same as if all recipients have "Do not Disturb" or "Invisible" status.

Silenced messages will have a :discord-message-silent:{ title="This is a @silent message." } icon displayed next to the user's time of posting. Hovering over the message will show `This is a @silent message.`

/// example
//// tab | Markdown
```
@silent This is a silenced message
```
////

//// tab | Result
{{ message('This is a silenced message', True, True) }}
////
///

### `@time`

Writing `@time` in the chat will show a selectable option to create a Timestamp with.  
When selected, you can either insert a date and/or time, or simply leave empty to use the moment of when you selected the option.

Discord will show you multiple variants for how the timestamp has to look. Clicking one will automatically insert it into your chat, replacing the `@time` option.

/// tip
The option supports various date and time formats, allowing highly flexible configurations.  
Some examples of valid dates include:

- `dd.mm.yyyy`
- `dd/mm/yyyy`*
- `mm/dd/yyyy`*
- `yyyy-mm-dd`
- `dd month yyyy` (i.e. `31 january 2026`)

*If the provided date is valid in both formats (Day is less than 13) will Discord prioritize the pattern used in your local settings.
///

### User

Starting with an at-symbol, followed by the User's unique username, one can create a mention that will notify the user.

/// example
//// tab | Markdown
```
@user
```
////

//// tab | Result
{{ message('<span class="mention">@User</span>', True) }}
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
{{ message('<span class="mention">@Role</span>', True) }}
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
{{ message('<span class="mention"># channel</span>') }}
////
///

----
## Emojis/Emotes

Unicode Emojis and Emotes - Discord's custom emoji feature - can be used using the same syntax: `:name:`  
Depending on the emote's name will the client append `~<number>` to the name (i.e. if there are two Emotes called `smile`, one will show as `smile~1`).

While Unicode Emojis are used as is (using their Unicode value) do Emotes use a custom syntax in Discord:

|Emoji type | Raw syntax           |
|-----------|----------------------|
| Static    | `<:name:123456789>`  |
| Animated  | `<a:name:123456789>` |

The name in the format can be anything and is only used for emotes the client cannot retrieve the name from.

/// tip
Prefixing the `:name:` pattern with a `+` will add it as a reaction to the last message in chat.
///

/// example
//// tab | Markdown
```
:smile:
```
////

//// tab | Result
{{ message('<img alt="😄" class="twemoji" src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f604.svg" title=":smile:">') }}
////
///

----
## Timestamps

A unique feature in Discord is sharing timestamps, which automatically display in the user's language and with the date and time converted to their timezone.  
This means that a time of UTC 00:00 shows as 00:00 for users with UTC+0 while it shows as 01:00 for users with UTC+1.

The custom [`@time`](#time) mention type can be used to create a timestamp in the client.

The raw format of the timestamp is as follows:

```
<t:123456789:r>
 |     |     |- Optional style definition
 |     |
 |     |- UNIX timestamp (Seconds since January 1st, 1970)
 |
 |- Always t to identify the timestamp format
```

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
{{ message('<span class="spoiler">This is some super secret text!</span>') }}
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
{{ message('This is normal text<br><small>This text is so tiny!</small>')}}
////
///
