from groq import Groq
import os
from pathlib import Path
from dotenv import load_dotenv
# Go up from backend/services -> backend -> portfolio_v3
env_path = Path(__file__).resolve().parents[1] / ".env"

load_dotenv(env_path)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
SYSTEM_PROMPT = """
You are a helpful AI assistant embedded in Hari Narayanan's developer portfolio.
Use the reference data provided below to answer questions about Hari accurately.
Always be concise, friendly, and professional.

REFERENCE DATA:
/**
 * Reference data injected into the Groq system prompt for portfolio Q&A.
 */
export const PORTFOLIO_CONTEXT = {
  personal: {
    name: "Harinarayanan Pari",
    title: "Full-Stack & AI Systems Engineer",
    location: "Bengaluru, India",
    email: "harinarayananpari@gmail.com",
    linkedin: "https://www.linkedin.com/in/harinarayanan-pari",
    portfolio: "https://hari-narayanan-portfolio.web.app/",
    github: "https://github.com/harinarayananpari",
    experience_years: "2+",
    availability: "Open to senior backend & AI engineering roles",
  },
  summary:
    "Backend & AI engineer building scalable LLM-powered SaaS, fintech reconciliation systems, and intelligent search infrastructure. Focus on production-grade pipelines, search, and distributed backends.",
  skills: {
    backend: ["Python", "Flask", "Django", "REST APIs", "System Design"],
    frontend: ["React.js", "Next.js", "TypeScript", "Tailwind CSS"],
    ai_search: [
      "OpenAI APIs",
      "Gemini APIs",
      "LLM Integration",
      "Prompt Engineering",
      "RAG",
      "Elasticsearch",
      "Fuzzy Matching",
    ],
    databases_cloud: ["MongoDB", "PostgreSQL", "AWS S3", "Azure Blob"],
    architecture: ["ETL Pipelines", "Data Validation", "Batch Processing", "Scalable Systems"],
  },
  experience: {
    company: "Finkraft.ai",
    role: "Software Developer",
    focus: "Backend & AI Systems",
    period: "Jul 2024 — Present",
    highlights: [
      "Architected AI-powered invoice processing pipeline from scratch",
      "Built Elasticsearch fuzzy matching for vendor & invoice reconciliation",
      "Integrated OpenAI and Gemini APIs with cost-aware fallback logic",
      "Designed scalable backend batch processing services",
      "Led AWS S3 → Azure Blob migration with zero downtime",
    ],
    stats: {
      invoices_processed: "200,000+",
      gst_reconciled: "₹13+ crore",
      accuracy_uplift: "~30%",
      manual_effort_removed: "~40%",
    },
  },
  projects: [
    {
      name: "AI Invoice Processing Engine",
      problem: "Manual invoice validation bottlenecking finance ops",
      impact: "40% reduction in manual validation; 200,000+ invoices processed",
      tech: ["Python", "Flask", "OpenAI", "Gemini", "MongoDB", "Azure Blob"],
    },
    {
      name: "GST Reconciliation Platform",
      problem: "Error-prone matching of invoices against GSTN filings",
      impact: "₹13+ crore GST value reconciled; ~30% accuracy improvement",
      tech: ["Python", "Elasticsearch", "PostgreSQL", "Flask"],
    },
    {
      name: "Intelligent Document Parser",
      problem: "Heterogeneous PDFs/scans needed unified structured output",
      impact: "Cut new vendor template onboarding from days to hours",
      tech: ["Python", "OpenAI", "Pydantic", "MongoDB"],
    },
    {
      name: "AI-Powered Search & Matching",
      problem: "Fragmented vendor master data across names, GSTINs, aliases",
      impact: "Sub-100ms p95 across millions of vendor records",
      tech: ["Elasticsearch", "Python", "RAG", "PostgreSQL"],
    },
  ],
  contact:
    "Reach via email harinarayananpari@gmail.com or the contact section on this portfolio.",
};

"""

def get_groq_reply(message):
    if not os.getenv("GROQ_API_KEY"):
        raise Exception("GROQ_API_KEY is not configured")

    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ],
        max_tokens=256,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
