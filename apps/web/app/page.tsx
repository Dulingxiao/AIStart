const foundationItems = [
  "Canonical context in .ai/",
  "Bridge files for multiple AI coding tools",
  "Minimal FastAPI + Next.js project structure",
  "Governance scripts for tasks, ADRs, iterations, and drift checks",
];

export default function HomePage() {
  return (
    <main className="page-shell">
      <section className="hero-card">
        <p className="eyebrow">AI-first project scaffold</p>
        <h1>AIStart</h1>
        <p className="hero-copy">
          Launch new fullstack projects with shared context, stable boundaries,
          and lightweight governance from day one.
        </p>
      </section>

      <section className="content-card">
        <h2>What V1 includes</h2>
        <ul>
          {foundationItems.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </section>
    </main>
  );
}
