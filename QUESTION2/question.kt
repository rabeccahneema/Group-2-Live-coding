
data class Project(val name: String, val skills: Set<String>)
data class Team(
    val name: String,
    val skills: Set<String>,
    val preferences: List<String>,
    var available: Boolean
)

fun main() {
    val projects = listOf(
        Project("AI App", setOf("python", "ml")),
        Project("Web App", setOf("html", "css", "js"))
    )

    val teams = mutableListOf(
        Team("Team A", setOf("python", "ml", "sql"), listOf("AI App"), true),
        Team("Team B", setOf("html", "css", "js"), listOf("Web App"), true)
    )

    val assignments = mutableMapOf<String, String>()

    for (project in projects) {
        var bestTeam: Team? = null
        var bestScore = 0

        for (team in teams) {
            if (team.available && project.skills.all { it in team.skills }) {
                var score = 1
                if (project.name in team.preferences) {
                    score += 1
                }
                if (score > bestScore) {
                    bestScore = score
                    bestTeam = team
                }
            }
        }

        if (bestTeam != null) {
            assignments[project.name] = bestTeam.name
            bestTeam.available = false
        }
    }

    println(assignments)
}

