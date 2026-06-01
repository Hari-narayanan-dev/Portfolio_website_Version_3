import { createFileRoute } from "@tanstack/react-router";
import { BackgroundFX } from "@/components/portfolio/BackgroundFX";
import { CursorGlow } from "@/components/portfolio/CursorGlow";
import { ScrollProgress } from "@/components/portfolio/ScrollProgress";
import { Nav } from "@/components/portfolio/Nav";
import { Hero } from "@/components/portfolio/Hero";
import { About } from "@/components/portfolio/About";
import { Skills } from "@/components/portfolio/Skills";
import { Experience } from "@/components/portfolio/Experience";
import { Projects } from "@/components/portfolio/Projects";
import { WhyHire } from "@/components/portfolio/WhyHire";
import { Contact } from "@/components/portfolio/Contact";
import { Footer } from "@/components/portfolio/Footer";
export const Route = createFileRoute("/")({
    component: Index,
    head: () => ({
        meta: [
            { title: "Harinarayanan Pari — Full-Stack & AI Systems Engineer" },
            { name: "description", content: "Backend & AI engineer in Bengaluru. Building scalable LLM-powered SaaS, fintech reconciliation systems, and intelligent search infrastructure." },
            { property: "og:title", content: "Harinarayanan Pari — Full-Stack & AI Systems Engineer" },
            { property: "og:description", content: "Scalable AI systems, LLM integration, production-grade backend architecture." },
            { property: "og:type", content: "website" },
        ],
        links: [{ rel: "canonical", href: "/" }],
        scripts: [
            {
                type: "application/ld+json",
                children: JSON.stringify({
                    "@context": "https://schema.org",
                    "@type": "Person",
                    name: "Harinarayanan Pari",
                    jobTitle: "Full-Stack & AI Systems Engineer",
                    address: { "@type": "PostalAddress", addressLocality: "Bengaluru", addressCountry: "IN" },
                    email: "harinarayananpari@gmail.com",
                    sameAs: [
                        "https://www.linkedin.com/in/harinarayanan-pari",
                        "https://hari-narayanan-portfolio.web.app/",
                    ],
                }),
            },
        ],
    }),
});
function Index() {
    return (<div className="relative min-h-screen overflow-x-hidden">
      <BackgroundFX />
      <CursorGlow />
      <ScrollProgress />
      <Nav />
      <main>
        <Hero />
        <About />
        <Skills />
        <Experience />
        <Projects />
        <WhyHire />
        <Contact />
      </main>
      <Footer />
    </div>);
}
