import pathway as pw

documents = pw.io.fs.read(
    "./data",
    format="plaintext_by_file",
    mode="streaming"
)

texts = documents.select(
    content=pw.this.data
)

pw.debug.compute_and_print(texts, include_id=False)
pw.run()
