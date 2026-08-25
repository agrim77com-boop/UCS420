import pandas as pd

roll_number = input("Enter your roll number: ")

# Q1
categories = ["billing", "account", "general"]

fixed_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    }
]

last_two_digits = roll_number[-2:]
personalized_entries = []

questions = {
    "billing": [
        "how can i check my payment status",
        "how do i update my billing details"
    ],
    "account": [
        "how do i update my registered mobile number",
        "how can i change my account email"
    ],
    "general": [
        "where can i find more information",
        "how can i contact customer support"
    ]
}

answers = {
    "billing": [
        "You can check your payment status from the billing section.",
        "You can update your billing details from the account settings."
    ],
    "account": [
        "You can update your registered mobile number from account settings.",
        "You can change your account email from your profile settings."
    ],
    "general": [
        "You can find more information in the help section.",
        "You can contact customer support through the support section."
    ]
}

keywords = {
    "billing": [
        "payment status billing",
        "billing details update"
    ],
    "account": [
        "mobile number update",
        "email account change"
    ],
    "general": [
        "information help support",
        "contact support help"
    ]
}

for i, digit in enumerate(last_two_digits):
    category = categories[int(digit) % 3]

    personalized_entries.append({
        "question": questions[category][i],
        "answer": answers[category][i],
        "keywords": keywords[category][i],
        "category": category
    })

faq_data = fixed_entries + personalized_entries
df = pd.DataFrame(faq_data)

print("\nFinal FAQ DataFrame:")
print(df)

# Q2
def score_query(query, df):
    query_words = set(query.lower().split())
    results = []

    for index, row in df.iterrows():
        question_words = set(row["question"].lower().split())
        keyword_words = set(row["keywords"].lower().split())

        score = len(query_words & question_words) + len(query_words & keyword_words)

        if score > 0:
            results.append({
                "index": index,
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "score": score
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    return pd.DataFrame(results)


query = input("\nEnter a query: ")
print("\nMatching Entries:")
print(score_query(query, df))

# Q3
def same_category(category_name, df):
    return df[df["category"] == category_name]

personalized_category = personalized_entries[0]["category"]

print("\nEntries in category:", personalized_category)
print(same_category(personalized_category, df))

# Q4
entry_index = 0
new_keyword = input("\nEnter a new keyword: ")

df.loc[entry_index, "keywords"] = (
    df.loc[entry_index, "keywords"] + " " + new_keyword
)

filename = roll_number + "_faq_data.csv"
df.to_csv(filename, index=False)

print("\nUpdated DataFrame:")
print(df)
print("\nSaved as:", filename)

# Q5
print("\nFAQ Entries Per Category:")
print(df.groupby("category").size())

# Q6
def score_query_with_ties(query, df):
    query_words = set(query.lower().split())
    results = []

    for index, row in df.iterrows():
        question_words = set(row["question"].lower().split())
        keyword_words = set(row["keywords"].lower().split())

        score = len(query_words & question_words) + len(query_words & keyword_words)

        if score > 0:
            results.append({
                "index": index,
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "score": score
            })

    if not results:
        print("No matching entries found.")
        return

    results.sort(key=lambda x: x["score"], reverse=True)

    highest_score = results[0]["score"]
    top_matches = [result for result in results if result["score"] == highest_score]

    print("\nHighest Confidence Matches:")
    print(pd.DataFrame(top_matches))

# Tie demonstration
print("\nTie Demonstration:")
score_query_with_ties("fee", df)

print("\nNon-Tie Demonstration:")
score_query_with_ties("password", df)
