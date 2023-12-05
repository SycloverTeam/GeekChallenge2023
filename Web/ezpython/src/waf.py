def waf(data):
    data=str(data)
    if "isvip" in data or "_static_folder" in data or "os" in data or "loader" in data or "defaults" in data or "kwdefaults" in data:
        return True