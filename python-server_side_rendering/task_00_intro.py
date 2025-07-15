def generate_invitations(template, attendees):
    if not isinstance(template, str):
        return "Invalid template type: expected string"
    if not isinstance(attendees, list):
        return "Invalid attendees type: expected list of dictionaries"
    if not template.strip():
        return "Template is empty, no output files generated"
    if not attendees:
        return "No data provided"

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, 1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))
        filename = f"output_{i}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
