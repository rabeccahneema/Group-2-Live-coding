data class Program(
    val name: String,
    val duration: Int,
    val reach: Int,
    val revenue: Int,
    val rights: IntRange
)

fun main() {
    val programs = mutableListOf(
        Program("News", 1, 9, 1000, 0..23),
        Program("Movie", 2, 10, 5000, 18..21),
        Program("Kids Show", 1, 6, 800, 8..17)
    )

    val slots = Array<String?>(24) { null }
    val primeTime = 18..21

    val sortedPrograms = programs.sortedByDescending { it.reach * it.revenue }

    for (program in sortedPrograms) {
        val (name, duration, _, _, rights) = program
        for (i in rights) {
            if (i + duration - 1 > rights.last || i + duration > 24) continue
            if ((i until i + duration).all { slots[it] == null }) {
                val isPrime = (i until i + duration).any { it in primeTime }
                if (isPrime || program.reach >= 8) {
                    for (j in i until i + duration) {
                        slots[j] = name
                    }
                    break
                }
            }
        }
    }

    for (i in slots.indices) {
        println("${i}:00 - ${i + 1}:00 => ${slots[i] ?: "Free"}")
    }
}

