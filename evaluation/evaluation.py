def evaluate_response(response):

    score = 10

    feedback = []

    if len(response) < 300:
        score -= 2
        feedback.append("Answer is too short.")

    if "example" not in response.lower():
        score -= 2
        feedback.append("Missing real-world example.")

    if "interview" not in response.lower():
        score -= 2
        feedback.append("Missing interview perspective.")

    if score < 0:
        score = 0

    return score, feedback