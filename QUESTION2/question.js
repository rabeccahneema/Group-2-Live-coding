
const programs = [
  { name: "News", duration: 1, reach: 9, revenue: 1000, rights: [0, 24] },
  { name: "Movie", duration: 2, reach: 10, revenue: 5000, rights: [18, 22] },
  { name: "Kids Show", duration: 1, reach: 6, revenue: 800, rights: [8, 18] }
];

const slots = new Array(24).fill(null);
const primeTime = [18, 19, 20, 21];

programs.sort((a, b) => b.reach * b.revenue - a.reach * a.revenue);

for (const program of programs) {
  const [start, end] = program.rights;
  for (let i = start; i <= end - program.duration; i++) {
    let canFit = true;
    for (let j = i; j < i + program.duration; j++) {
      if (slots[j]) {
        canFit = false;
        break;
      }
    }

    if (canFit) {
      const isPrime = primeTime.some(t => t >= i && t < i + program.duration);
      if (isPrime || program.reach >= 8) {
        for (let j = i; j < i + program.duration; j++) {
          slots[j] = program.name;
        }
        break;
      }
    }
  }
}

// print schedule
slots.forEach((program, hour) => {
  console.log(`${hour}:00 - ${hour + 1}:00 => ${program || "Free"}`);
});