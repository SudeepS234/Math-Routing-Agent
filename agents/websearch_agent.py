def fallback_web_answer(query):
    if "prime" in query.lower():
        return "A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself."
    return "Sorry, I couldn't find an accurate answer to this question."
