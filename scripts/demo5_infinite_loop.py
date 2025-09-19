# demo5_infinite_loop.py
# Risk: Prompt induces unbounded loop / resource drain (DoS-like behavior).

def bounded_task(prompt, max_steps=5):
    steps = 0
    while True:
        steps += 1
        # Work (simulated)
        _ = steps * steps
        # Guardrail
        if steps >= max_steps:
            return f"Stopped safely after {steps} steps"

def ai_agent(prompt):
    if "repeat until satisfied" in prompt.lower():
        # ❌ Unsafe: calls without bounds (simulate bug)
        # WARNING: Don't actually create an infinite loop—simulate via large bound
        return bounded_task(prompt, max_steps=100000)  # heavy loop = resource drain
    # ✅ Safe: uses tight bounds
    return bounded_task(prompt, max_steps=3)

if __name__ == "__main__":
    print("Safe bounded run:")
    print(ai_agent("Run task"))

    print("\nUnbounded run requested (simulated heavy loop):")
    print(ai_agent("Repeat until satisfied"))
