# Code Compass – AI Safety Risks in Legacy Modernization

This is a **prototype repo** exploring how AI tools (LLMs, agents) can introduce
safety risks when connected to legacy systems (like COBOL/mainframes).

## Contents
- `scripts/demo1_data_leak.py` → Prompt injection revealing sensitive fields.
- `scripts/demo2_audit_bypass.py` → AI bypasses logging; audit trail missing.
- `scripts/demo3_unauthorized_action.py` → AI triggers unsafe action (fund transfer) without authorization.
- `scripts/demo4_policy_override.py` → AI overrides role-based policy to leak restricted info.
- `scripts/demo5_infinite_loop.py` → Malicious prompt induces resource-draining loop (DoS-like).
- `requirements.txt` → Python version requirements.

## How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/VIK102/code-compass-ai-safety.git
   cd code-compass-ai-safety
   ```

## Step 2 Install Python 3.9+

## Step 3 Run any demo, for example:
python scripts/demo1_data_leak.py
python scripts/demo2_audit_bypass.py
python scripts/demo3_unauthorized_action.py
python scripts/demo4_policy_override.py
python scripts/demo5_infinite_loop.py
