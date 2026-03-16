from agno.agent import Agent

from app.services.retrieval_service import RetrievalService


class PropertyAgent:
    def __init__(self, retrieval_service: RetrievalService):
        self.retrieval_service = retrieval_service

        self.agent = Agent(
            model="gpt-4o-mini",
            instructions="""
            Você é um concierge digital de um imóvel.

            Responda perguntas dos hóspedes usando
            apenas as informações fornecidas.
        """,
        )

    def to_ask(self, question: str):

        chunks = self.retrieval_service.search_context(question)

        context = "\n\n".join([c.content for c in chunks])

        prompt = f"""
            Contexto do imovel:
            {context}

            Pergunta do hóspede:
            {question}
        """

        response = self.agent.run(prompt)

        return response
