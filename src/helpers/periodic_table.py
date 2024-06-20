import jq
import requests


def periodic_table():
    try:
        response = requests.get(
            "https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json"
        )
        json = response.json()
    except Exception:
        print("Fetching periodic table data failed. Try again later.")
        exit(1)

    # The program — even though it's quite simple — was written by ChatGPT. See last question in https://chatgpt.com/share/b1e31118-b7c2-411a-a138-db96e54d10ac
    jq_program = jq.compile(
        "reduce .elements[] as $elem ({}; .[$elem.symbol] = $elem.atomic_mass)"
    )

    return jq_program.input_value(json).text()
