


const projects = [
  { name: "AI App", skills: ["python", "ml"] },
  { name: "Web App", skills: ["html", "css", "js"] }
];

const teams = [
  {
    name: "Team A",
    skills: ["python", "ml", "sql"],
    preferences: ["AI App"],
    available: true
  },
  {
    name: "Team B",
    skills: ["html", "css", "js"],
    preferences: ["Web App"],
    available: true
  }
];

const assignments = {};

projects.forEach(project => {
  let bestTeam = null;
  let bestScore = 0;

  teams.forEach(team => {
    const hasSkills = project.skills.every(skill => team.skills.includes(skill));
    if (team.available && hasSkills) {
      let score = 1;
      if (team.preferences.includes(project.name)) {
        score += 1;
      }
      if (score > bestScore) {
        bestScore = score;
        bestTeam = team;
      }
    }
  });

  if (bestTeam) {
    assignments[project.name] = bestTeam.name;
    bestTeam.available = false;
  }
});

console.log(assignments);

