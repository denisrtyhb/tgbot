def int_to_list(i):
    l = []
    for _ in range(4):
        l.append(i % 10)
        i //= 10
    return l


def similarity(ans, guess):
    l1 = int_to_list(ans)
    l2 = int_to_list(guess)
    ans = [0, 0]
    for i in range(4):
        if l1[i] == l2[i]:
            ans[0] += 1
            l1[i] = 10
            l2[i] = 11
    for i in range(4):
        for j in range(4):
            if l1[i] == l2[j]:
                ans[1] += 1
                l1[i] = 10
                l2[j] = 11
    return ans


def bulls_and_cows_impl(text, state):
    try:
        guess = int(text)
        if guess < 0 or 9999 < guess:
            return "expected 4 digit number"
        state[2] += 1
        t = similarity(state[1], guess)
        if t[0] == 4:
            state[0] = 0
            return f"You won in {state[2]} guesses, congrats"
        else:
            return f"you got {t[0]} bulls and {t[1]} cows"
    except:
        return "expected 4 digit number"
    
    