""" Test constraints """

# --- (BOBA_CONFIG)
{
  "graph": ["A->B->C->D"],
  "decisions": [
    {"var": "a", "options": ["if", "else"]},
    {"var": "b", "options": [0, 1] }
  ],
  "constraints": [
    {"variable": "b", "option": 1, "condition": "a.index == 0"},
    {"variable": "b", "option": 0, "condition": "a == else"}
  ]
}
# --- (END)

if __name__ == '__main__':
    # --- (A)
    a = {{a}}

    # --- (B) b1
    b = 1 + {{b}}

    # --- (B) b2
    b = 2 + {{b}}

    # --- (C)
    print(a * b)

    # --- (D)
    print(a + b)
