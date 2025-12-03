from pyscript import display, document # pyright: ignore[reportMissingImports]

chess_club = {
    'name': "Chess Club",
    'advisor': "Mr. Santos",
    'meeting_time': "Monday 3:00 PM - 4:30 PM",
    'Location': "Room 405",
    'Category': "Academic",
    'Description': "A club for chess enthusiasts of all skill levels",
    'mem_count': 25
}
dance_club = {
    'name': "High School Monarchs Dance Club",
    'advisor': "Mr. Marutani",
    'meeting_day': "Friday",
    'meeting_time': "3:00 PM - 5:00 PM",
    'Location': "Auditorium",
    'Category': "Cultural",
    'Description': "A club for students interested in various dance styles",
    'mem_count': 30
}
socsci_club = {
    'name': "Social Sciences Club",
    'advisor': "Ms. Libramonte",
    'meeting_day': "Thursday",
    'meeting_time': "2:30 PM - 3:30 PM",
    'Location': "Room 411",
    'Category': "Academic",
    'Description': "A club that explores social science topics and current events",
    'mem_count': 20
}
bball_varsity = {
    'name': "Basketball Varsity Team",
    'advisor': "Coach Amargo",
    'meeting_day': "Monday, Wednesday, Friday",
    'meeting_time': "3:00 PM - 5:00 PM",
    'Location': "Court",
    'Category': "Sports",
    'Description': "The school's competitive basketball team",
    'mem_count': 15
}
commarts_club = {
    'name': "Communications Arts Club",
    'advisor': "Mr. Loreto",
    'meeting_day': "Tuesday",
    'meeting_time': "2:00 PM - 3:30PM",
    'Location': "Room 408",
    'Category': "Academic",
    'Description': "A club for students interested in media, journalism, and public speaking",
    'mem_count': 23
}

clubs_map = {
    "Chess Club": chess_club,
    "Monarchs Dance Club": dance_club,
    "Social Sciences Club": socsci_club,
    "Basketball Varsity": bball_varsity,
    "Communication Arts": commarts_club
}

def display_club_info(e):

    e.preventDefault() # don't refresh the page
    club_selection = document.getElementById("club-selection").value
    club = clubs_map.get(club_selection, {})
    # club outputs
    info = f"""
    <h2>{club.get('name', 'Club not found')}</h2>
    <p><strong>Advisor:</strong> {club.get('advisor')}</p>
    <p><strong>Meeting Day:</strong> {club.get('meeting_day', club.get('meeting_time'))}</p>
    <p><strong>Meeting Time:</strong> {club.get('meeting_time')}</p>
    <p><strong>Location:</strong> {club.get('Location')}</p>
    <p><strong>Category:</strong> {club.get('Category')}</p>
    <p><strong>Description:</strong> {club.get('Description')}</p>
    <p><strong>Number of Members:</strong> {club.get('mem_count')}</p>
    """
    document.getElementById("club-outputs").innerHTML = info
