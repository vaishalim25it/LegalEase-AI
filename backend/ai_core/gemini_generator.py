import os
from dotenv import load_dotenv

load_dotenv()


class GeminiDocumentGenerator:

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY", "").strip()
        self.model_name = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash"
        ).strip()

        self.demo_mode = (
            os.getenv("DEMO_MODE", "true").lower() == "true"
        )

        self.client = None

        if self.api_key and not self.demo_mode:
            from google import genai

            self.client = genai.Client(
                api_key=self.api_key
            )

    def build_prompt(
        self,
        document_type,
        parties,
        terms,
        effective_date
    ):
        return f"""
You are a professional legal document drafting assistant.

Create a structured draft for the following document:

Document Type:
{document_type}

Parties:
{parties}

Effective Date:
{effective_date}

Terms:
{terms}

Instructions:

1. Use only the information supplied by the user.
2. Do not invent names, addresses, amounts, dates, laws, or jurisdictions.
3. If important information is missing, use a clear placeholder.
4. Use professional and clear legal language.
5. Give the document a clear title.
6. Include the parties and effective date.
7. Organize the document into suitable sections.
8. Include rights and responsibilities where relevant.
9. Include termination or confidentiality clauses where relevant.
10. Include signature sections.
11. Do not use Markdown code fences.
12. Do not claim that the document is guaranteed to be legally valid.
13. End with a short notice recommending review by a qualified legal professional.

Return only the document draft.
"""

    def create_demo_document(
        self,
        document_type,
        parties,
        terms,
        effective_date
    ):
        term_list = [
            term.strip()
            for term in terms.split(";")
            if term.strip()
        ]

        lines = [
            document_type.upper(),
            "",
            "1. PARTIES",
            parties,
            "",
            "2. EFFECTIVE DATE",
            effective_date,
            "",
            "3. TERMS AND CONDITIONS",
        ]

        for index, term in enumerate(term_list, start=1):
            lines.append(f"{index}. {term}")

        lines.extend([
            "",
            "4. GENERAL PROVISIONS",
            "The parties agree to comply with the terms stated in this document.",
            "",
            "5. SIGNATURES",
            "",
            "Party 1 Signature: __________________________",
            "",
            "Party 2 Signature: __________________________",
            "",
            "Date: __________________________",
            "",
            "Drafting Notice: This document is an AI-generated drafting aid "
            "and should be reviewed by a qualified legal professional before use."
        ])

        return "\n".join(lines)

    def generate_document(
        self,
        document_type,
        parties,
        terms,
        effective_date
    ):
        if self.demo_mode:
            return self.create_demo_document(
                document_type=document_type,
                parties=parties,
                terms=terms,
                effective_date=effective_date,
            )

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY is missing. "
                "Add your Gemini API key to the .env file."
            )

        if self.client is None:
            raise ValueError(
                "Gemini client could not be initialized."
            )

        prompt = self.build_prompt(
            document_type=document_type,
            parties=parties,
            terms=terms,
            effective_date=effective_date,
        )

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )

        content = getattr(response, "text", None)

        if not content:
            raise ValueError(
                "Gemini returned an empty response."
            )

        return content.strip()