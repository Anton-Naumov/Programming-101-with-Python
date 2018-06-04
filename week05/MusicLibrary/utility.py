def format_length(hours, minutes, seconds):
    result_minutes = minutes + seconds // 60
    result_seconds = seconds % 60
    result_hours = hours + result_minutes // 60
    result_minutes %= 60
    return result_hours, result_minutes, result_seconds
