projects = [
    ("Website Development", ["Python", "Django", "HTML", "CSS"]),
  ("Mobile App Development", ["Java", "Android", "UI/UX"]),
    ("Data Analysis", ["Python", "Pandas", "SQL"]),
]

team_members = [
  ("Alice", ["Python", "Django", "HTML", "CSS", "JavaScript"], ["Website Development", "Data Analysis"]),
   ("Bob", ["Java", "Android", "UI/UX", "Kotlin"], ["Mobile App Development"]),
("Charlie", ["Python", "Pandas", "SQL", "Machine Learning"], ["Data Analysis", "Website Development"]),
   ("David", ["Project Management", "Communication"], [])
]

teams = [
 ("Web Team", [team_members[0]]),
   ("Mobile Team", [team_members[1]]),
("Data Team", [team_members[2]]),
("Management Team", [team_members[3]])
]
def assign_projects(projects, teams, team_members):

    
    project_assignments = {}

    for project_name, project_skills in projects:
        assigned_team = None
        for team_name, team_data in teams:
            if all(skill in team_data['skills'] for skill in project_skills):
                assigned_team = team_name
                break

        if assigned_team:
            project_assignments[project_name] = assigned_team
        else:
            project_assignments[project_name] = "No suitable team found"
    return project_assignments