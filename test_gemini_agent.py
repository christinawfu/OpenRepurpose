from dossier_generator.gemini_agent import run_agent


result = run_agent(
    target="PCSK9",
    drug="evolocumab",
    disease="hypercholesterolemia",
)


print("\n=== GEMINI RESPONSE ===\n")

print(result)