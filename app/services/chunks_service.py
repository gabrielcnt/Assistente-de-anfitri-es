class ChunkService:
    def generate_chunks(self, text: str, size: int = 300, overlap: int = 50):

        word = text.split()
        chunks = []

        step = size - overlap

        for i in range(0, len(word), step):
            chunk = " ".join(word[i : i + size])
            chunks.append(chunk)
        return chunks
