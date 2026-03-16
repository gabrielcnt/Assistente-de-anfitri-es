class ChunkService:
    def generate_chunks(self, text: str, size: int = 300):
        word = text.split()
        chunks = []

        for i in range(0, len(word), size):
            chunk = " ".join(word[i : i + size])
            chunks.append(chunk)
        return chunks
