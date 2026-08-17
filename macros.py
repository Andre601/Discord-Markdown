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