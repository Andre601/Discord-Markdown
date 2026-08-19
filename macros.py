def define_env(env):
    @env.macro
    def mention(is_message: bool = False, has_server: bool = False):
        parts = ["<span class='mention'>"]

        if has_server:
            parts.append("Server")
        else:
            parts.append(":discord-channel: channel")
        
        if is_message:
            parts.append(" <small>></small> :discord-message:")
        else:
            if has_server:
                parts.append(" <small>></small> :discord-channel: channel")
        
        parts.append("</span>")

        return "".join(parts)
    
    @env.macro
    def message(msg: str, mention: bool = False, silent: bool = False):
        parts = ['<div class="discord-message is-mentioned">'] if mention else ['<div class="discord-message">']

        parts.extend([
            '<img class="discord-avatar" src="/Discord-Markdown/assets/img/android-chrome-512x512.png" alt="discord-avatar">',
            '<div class="discord-message-content">',
            '<div class="discord-message-header">',
            '<span class="discord-username">Discord-Markdown</span>',
            '<span class="discord-timestamp">Today at 00:00</span>'
        ])
        
        if silent:
            parts.append('<span class="discord-silent-message" title="This is a @silent message."></span>')
        
        parts.extend([
            '</div>',
            '<div class="discord-message-body">',
            f'{msg}',
            '</div>',
            '</div>',
            '</div>'
        ])

        return "\n".join(parts)